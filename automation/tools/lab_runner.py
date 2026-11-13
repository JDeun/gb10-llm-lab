"""Run the experiment queue (~/llm/queue.json) unattended, one model at a time.

Per entry: download -> start server -> measurement suite -> sanitized export ->
local git commit -> stop server -> delete this entry's new model files.
Progress is kept in ~/llm/queue-state.json so a reboot resumes at the next
unfinished entry. Failures are recorded and committed, then the queue moves on.
When every entry is done or failed, the default server is restored and the
runner service disables itself.
"""
import json
import os
import shutil
import subprocess
import time
import traceback
import urllib.request
from datetime import date, datetime
from pathlib import Path

import lab_suite
from lab_suite import EntryFailed

HOME = Path.home()
LLM = HOME / "llm"
LAB = HOME / "gb10-llm-lab"
QUEUE = LLM / "queue.json"
STATE = LLM / "queue-state.json"
HF_HUB = HOME / ".cache/huggingface/hub"
STRATA_MODELS = HOME / ".local/share/strata/Strata-data/models"
INFERSSD_MODELS = HOME / ".local/share/inferssd/models"
COLI_MODELS = HOME / "llm/colibri-models"  # small per-entry model dirs made by `coli import` (point at the GGUF)
DELETE_ROOTS = (HF_HUB, STRATA_MODELS, INFERSSD_MODELS, COLI_MODELS)
HF_ENGINES = ("vllm", "llamacpp", "ikllama", "colibri")  # engines whose weights the runner downloads into the HF cache
TRANSIENT = {"timeout", "command_failed", "server_down", "server_exited", "start_timeout"}
MAX_ATTEMPTS = 2
KEEP_DIRS = {HF_HUB / "models--nvidia--Qwen3.6-35B-A3B-NVFP4"}
EVICTABLE = {"strata-qwen38fn-iq3s": [STRATA_MODELS / "IQ3_S"]}
RESERVE_BYTES = 64 * 2**30
PORTS = {"vllm": 8001, "strata": 8080, "llamacpp": 8002, "ikllama": 8003, "inferssd": 8080, "colibri": 8005}
VLLM_IMAGE = "vllm/vllm-openai:v0.32.0"
LLAMA_SERVER = LLM / "src/llama.cpp/build/bin/llama-server"
STRATA = HOME / ".local/bin/strata"
IK_SERVER = LLM / "src/ik_llama.cpp/build/bin/llama-server"
INFERSSD = HOME / ".local/bin/inferssd"
COLI = LLM / "src/colibri/c/coli"
CUDA_ENV = {**os.environ, "PATH": f"/usr/local/cuda/bin:{os.environ.get('PATH', '/usr/bin:/bin')}"}


def uses_hf(entry: dict) -> bool:
    """Weights come from the shared HF cache (downloaded by the runner) rather than an engine's own store."""
    return entry["engine"] in HF_ENGINES or (entry["engine"] == "inferssd" and bool(entry.get("hf_include")))


def log(msg: str) -> None:
    print(f"[{datetime.now():%m-%d %H:%M:%S}] {msg}", flush=True)


def run(cmd: list[str], timeout: float | None = None, check: bool = True, env: dict | None = None) -> subprocess.CompletedProcess:
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, env=env, check=False)
    except subprocess.TimeoutExpired as exc:
        raise EntryFailed("timeout", f"{' '.join(cmd[:3])} after {timeout}s") from exc
    if check and proc.returncode != 0:
        tail = (proc.stderr or proc.stdout)[-400:]
        raise EntryFailed("command_failed", f"{' '.join(cmd[:4])} rc={proc.returncode} {tail}")
    return proc


def load_json(path: Path, default: dict) -> dict:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


RESET_FILE = LLM / "queue-reset.txt"  # entry ids to run again, one per line (consumed by the runner)


def write_state(state: dict) -> None:
    tmp = STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(STATE)


def save_record(eid: str, record: dict) -> None:
    """Merge one entry's record into the file so edits made to other entries meanwhile are kept."""
    state = load_json(STATE, {})
    state[eid] = record
    write_state(state)


def apply_resets() -> None:
    if not RESET_FILE.exists():
        return
    ids = {line.strip() for line in RESET_FILE.read_text().splitlines() if line.strip()}
    state = load_json(STATE, {})
    for eid in ids & state.keys():
        log(f"reset {eid} (was {state.pop(eid).get('status')})")
    write_state(state)
    RESET_FILE.unlink()


# ---------- files and disk ----------

SHARED_DIRS = {HF_HUB / "blobs", HF_HUB / ".locks"}


def snapshot_dirs() -> set[Path]:
    """Per-model directories under the model roots (the shared HF blob store is never one of them)."""
    return {p for root in DELETE_ROOTS if root.exists() for p in root.iterdir()
            if p.is_dir() and p not in SHARED_DIRS}


def free_bytes() -> int:
    return shutil.disk_usage(HOME).free


def link_targets(repo_dir: Path) -> set[Path]:
    """Final files behind an HF repo's symlinks (repo blobs link on to the shared hub/blobs store)."""
    return {f.resolve() for f in repo_dir.rglob("*") if f.is_symlink()} if repo_dir.exists() else set()


def kept_paths() -> set[Path]:
    return set(KEEP_DIRS) | SHARED_DIRS | {t for d in KEEP_DIRS for t in link_targets(d)}


def delete_paths(paths: set[Path]) -> list[str]:
    """Delete files/dirs inside the model roots only; never the kept serving model, its blobs or shared dirs."""
    keep, removed = kept_paths(), []
    for p in sorted(paths):
        if not any(root in p.parents for root in DELETE_ROOTS) or p in keep or not p.exists():
            continue
        try:
            if p.is_dir() and not p.is_symlink():
                shutil.rmtree(p)
            else:
                p.unlink()
        except PermissionError:
            remove_as_container_root(p)
        removed.append(p.name)
    return removed


def remove_as_container_root(path: Path) -> None:
    """vLLM runs as root in docker and leaves root-owned files in the HF cache; remove them the same way."""
    if HF_HUB not in path.parents:
        log(f"cannot delete {path}: permission denied outside HF cache")
        return
    rel = path.relative_to(HF_HUB)
    proc = run(["docker", "run", "--rm", "--entrypoint", "rm", "-v", f"{HF_HUB}:/hub", VLLM_IMAGE,
                "-rf", f"/hub/{rel}"], check=False, timeout=600)
    if proc.returncode != 0 or path.exists():
        log(f"could not delete {path}: {proc.stderr[-200:]}")


def entry_files(entry: dict, new_dirs: set[Path]) -> set[Path]:
    """Everything this entry downloaded: HF repo dir + its shared blobs, explicit paths, new strata dirs."""
    paths = set(new_dirs) | {HOME / p for p in entry.get("delete_paths", [])}
    if uses_hf(entry):
        repo_dir = HF_HUB / ("models--" + entry["repository"].replace("/", "--"))
        paths |= link_targets(repo_dir) | {repo_dir}
    return paths


def ensure_disk(entry: dict) -> list[str]:
    need = entry.get("size_bytes", 0) + RESERVE_BYTES
    evicted = []
    for key in entry.get("may_evict", []):
        if free_bytes() >= need:
            break
        evicted += delete_paths({p for p in EVICTABLE.get(key, []) if p.exists()})
    if free_bytes() < need:
        raise EntryFailed("storage_insufficient", f"free {free_bytes() / 1e9:.0f} GB < need {need / 1e9:.0f} GB")
    return evicted


def hf_download(entry: dict) -> None:
    cmd = [str(HOME / ".local/bin/uvx"), "--from", "huggingface_hub[hf_xet]", "hf", "download", entry["repository"]]
    for pat in entry.get("hf_include", []):
        cmd += ["--include", pat]
    for pat in entry.get("hf_exclude", []):
        cmd += ["--exclude", pat]
    log(f"download {entry['repository']}")
    run(cmd, timeout=48 * 3600)


def hf_snapshot(repo: str) -> Path:
    snaps = sorted((HF_HUB / ("models--" + repo.replace("/", "--")) / "snapshots").glob("*"))
    if not snaps:
        raise EntryFailed("download_missing", repo)
    return snaps[-1]


def digests(entry: dict, new_dirs: set[Path]) -> str:
    if uses_hf(entry):
        snap = hf_snapshot(entry["repository"])
        # first link hop is the repo blob named by the LFS sha256; the final hop is a content-store name
        return "".join(f"{Path(os.readlink(f)).name}  {f.relative_to(snap)}\n" for f in sorted(snap.rglob("*"))
                       if f.is_symlink() and f.suffix in {".gguf", ".safetensors"})
    files = sorted(f for d in new_dirs for f in d.rglob("*.gguf"))
    out = run(["sha256sum", *map(str, files)], timeout=6 * 3600).stdout if files else ""
    for root in (STRATA_MODELS, INFERSSD_MODELS):
        out = out.replace(str(root) + "/", "")
    return out


# ---------- servers ----------

def http_ok(port: int) -> bool:
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/v1/models", timeout=10) as resp:
            return resp.status == 200
    except OSError:
        return False


def served_alias(port: int) -> str:
    with urllib.request.urlopen(f"http://127.0.0.1:{port}/v1/models", timeout=10) as resp:
        return json.load(resp)["data"][0]["id"]


def wait_until_up(port: int, timeout_s: int, alive) -> None:
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        if http_ok(port):
            return
        if not alive():
            raise EntryFailed("server_exited", "server process ended before answering")
        time.sleep(15)
    raise EntryFailed("start_timeout", f"no answer on port {port} after {timeout_s}s")


def wait_for_manual_strata() -> None:
    while run(["pgrep", "-f", "strata/terminal/.*setup.py"], check=False).returncode == 0:
        log("an earlier strata setup is still running; waiting")
        time.sleep(60)


def start_vllm(entry: dict):
    run(["docker", "rm", "-f", "lab-vllm"], check=False)
    run(["docker", "run", "-d", "--name", "lab-vllm", "--gpus", "all", "--ipc=host",
         "-v", f"{HOME}/.cache/huggingface:/root/.cache/huggingface",
         "-p", f"127.0.0.1:{PORTS['vllm']}:8000", VLLM_IMAGE, entry["repository"],
         "--served-model-name", entry["id"], "--host", "0.0.0.0", "--port", "8000", *entry.get("vllm_args", [])])
    inspect = ["docker", "inspect", "-f", "{{.State.Running}}", "lab-vllm"]
    return lambda: run(inspect, check=False).stdout.strip() == "true"


def start_strata(entry: dict):
    wait_for_manual_strata()
    if not http_ok(PORTS["strata"]):
        run([str(STRATA), "launch", *entry["launch"], "--access", "local", "--port", str(PORTS["strata"]),
             "--restart", "--no-tui", "--yes"], timeout=48 * 3600)
    return lambda: run(["pgrep", "-f", "strata --serve"], check=False).returncode == 0


def first_shard(entry: dict) -> Path:
    snap = hf_snapshot(entry["repository"])
    shards = sorted(snap.rglob("*-00001-of-*.gguf")) or sorted(f for f in snap.rglob("*.gguf") if "mmproj" not in f.name)
    if not shards:
        raise EntryFailed("download_missing", "no gguf file")
    return shards[0]


def server_log(entry: dict):
    return open(LLM / "logs" / f"{entry['id']}.server.log", "w")


def require(binary: Path) -> None:
    if not binary.exists():
        raise EntryFailed("engine_not_installed", str(binary.relative_to(HOME)))


def start_gguf_server(entry: dict, binary: Path, port: int):
    """llama.cpp-compatible server (mainline or ik_llama.cpp) on the entry's first GGUF shard."""
    require(binary)
    shard = first_shard(entry)
    proc = subprocess.Popen([str(binary), "-m", str(shard), "--host", "127.0.0.1", "--port", str(port),
                             "-ngl", "999", "-fa", "on", "--jinja", "--alias", entry["id"], *entry.get("llama_args", [])],
                            stdout=server_log(entry), stderr=subprocess.STDOUT)
    return lambda: proc.poll() is None


def start_inferssd(entry: dict):
    """With hf_include InferSSD reads the shared HF-cache GGUF (-m); otherwise it downloads its own copy (-hf)."""
    require(INFERSSD)
    source = ["-m", str(first_shard(entry))] if uses_hf(entry) else ["-hf", entry["repository"]]
    proc = subprocess.Popen([str(INFERSSD), "serve", *source, *entry.get("inferssd_args", [])],
                            stdout=server_log(entry), stderr=subprocess.STDOUT)
    return lambda: proc.poll() is None


def start_colibri(entry: dict):
    """colibri: import the GGUF in place (a small model dir), build the engine for this machine, then serve."""
    require(COLI)
    shard = first_shard(entry)
    model_dir = COLI_MODELS / entry["id"]
    COLI_MODELS.mkdir(parents=True, exist_ok=True)
    if not model_dir.exists():
        run(["python3", str(COLI), "import", str(shard), "--out", str(model_dir)], timeout=4 * 3600, env=CUDA_ENV)
    # coli build runs make with the Makefile default CUDA=0; force a CUDA rebuild (-B) for this family
    run(["python3", str(COLI), "build", "--model", str(model_dir)], timeout=4 * 3600,
        env={**CUDA_ENV, "CUDA": "1", "MAKEFLAGS": "-B"})
    proc = subprocess.Popen(["python3", str(COLI), "serve", "--model", str(model_dir), "--host", "127.0.0.1",
                             "--port", str(PORTS["colibri"]), "--model-id", entry["id"], "--gpu", "auto",
                             "--auto-tier", *entry.get("colibri_args", [])],
                            stdout=server_log(entry), stderr=subprocess.STDOUT, env=CUDA_ENV)
    return lambda: proc.poll() is None


STARTERS = {
    "vllm": start_vllm,
    "strata": start_strata,
    "llamacpp": lambda e: start_gguf_server(e, LLAMA_SERVER, PORTS["llamacpp"]),
    "ikllama": lambda e: start_gguf_server(e, IK_SERVER, PORTS["ikllama"]),
    "inferssd": start_inferssd,
    "colibri": start_colibri,
}


def stop_servers() -> None:
    run(["docker", "rm", "-f", "lab-vllm"], check=False)
    run(["docker", "stop", "vllm-qwen36"], check=False)
    run([str(STRATA), "launch", "--stop"], check=False, timeout=300)
    if COLI.exists():
        run(["python3", str(COLI), "stop"], check=False, timeout=120)
    for binary in (LLAMA_SERVER, IK_SERVER, INFERSSD, COLI.parent):
        run(["pkill", "-f", str(binary)], check=False)
    time.sleep(10)


def engine_log_tail(entry: dict) -> str:
    if entry["engine"] == "vllm":
        logs = run(["docker", "logs", "--tail", "400", "lab-vllm"], check=False)
        lines = (logs.stdout + logs.stderr).splitlines()
        # keep the root-cause lines (vLLM prints the real error long before the final RuntimeError)
        errors = [ln for ln in lines if any(k in ln for k in ("Error", "error", "not supported", "Exception"))]
        return "\n".join(errors[-25:] + ["--- last lines ---"] + lines[-15:])[-4000:]
    if entry["engine"] != "strata":
        path = LLM / "logs" / f"{entry['id']}.server.log"
        return path.read_text(errors="ignore")[-3000:] if path.exists() else ""
    logs = sorted((HOME / ".local/state/strata/launch").glob("*.engine.log"), key=lambda p: p.stat().st_mtime)
    return logs[-1].read_text(errors="ignore")[-3000:] if logs else ""


# ---------- one entry ----------

def run_entry(entry: dict, defaults: dict, state: dict) -> None:
    eid = entry["id"]
    record = state.setdefault(eid, {})
    record.update(status="running", started=datetime.now().isoformat(timespec="seconds"))
    save_record(eid, record)
    before = snapshot_dirs()
    result_dir = LAB / "results" / f"{date.today():%Y-%m-%d}-{eid}"
    failure, alias, evicted = None, None, []
    try:
        wait_for_manual_strata()
        stop_servers()
        evicted = ensure_disk(entry)
        if uses_hf(entry):
            hf_download(entry)
        alive = STARTERS[entry["engine"]](entry)
        wait_until_up(PORTS[entry["engine"]], entry.get("start_timeout_s", defaults["start_timeout_s"]), alive)
        alias = served_alias(PORTS[entry["engine"]])
        lab_suite.run_suite(entry, alias, PORTS[entry["engine"]], defaults["step_timeout_s"])
    except EntryFailed as exc:
        failure = {"kind": exc.kind, "detail": exc.detail[:600], "engine_log_tail": engine_log_tail(entry)}
        log(f"{eid} FAILED {exc}")
    except Exception as exc:  # noqa: BLE001 - a runner bug must fail this entry, not crash-loop the whole queue
        failure = {"kind": "runner_error", "detail": f"{type(exc).__name__}: {exc}"[:600],
                   "engine_log_tail": traceback.format_exc()[-3000:]}
        log(f"{eid} RUNNER ERROR {failure['detail']}")
    new_dirs = snapshot_dirs() - before
    try:
        digest_text = digests(entry, new_dirs)
    except EntryFailed:
        digest_text = ""
    stop_servers()
    lab_suite.export_and_commit(entry, alias, result_dir, failure, digest_text, evicted)
    attempts = record.get("attempts", 0) + 1
    retry = bool(failure) and failure["kind"] in TRANSIENT and attempts < MAX_ATTEMPTS
    # keep files for a retry, or for a following entry that reuses them on another engine (if installed)
    keep_for = entry.get("keep_for") or []
    keep_for = [keep_for] if isinstance(keep_for, str) else keep_for
    reuse = any(ENGINE_BINARIES[name].exists() for name in keep_for)
    removed = [] if entry.get("keep") or retry or reuse else delete_paths(entry_files(entry, new_dirs))
    status = "retry" if retry else ("failed" if failure else "done")
    record.update(status=status, attempts=attempts, failure=failure, removed=removed, evicted=evicted,
                  finished=datetime.now().isoformat(timespec="seconds"), result_dir=result_dir.name)
    save_record(eid, record)


def finish_queue() -> None:
    log("queue complete: restoring default server and disabling runner")
    (LLM / "serve-mode").write_text("vllm\n")
    run(["systemctl", "--user", "start", "llm-serve.service"], check=False)
    run(["systemctl", "--user", "restart", "llm-serve.service"], check=False)
    run(["systemctl", "--user", "disable", "lab-runner.service"], check=False)


ENGINE_BINARIES = {"strata": STRATA, "llamacpp": LLAMA_SERVER, "ikllama": IK_SERVER, "inferssd": INFERSSD,
                   "colibri": COLI}


def engine_ready(entry: dict) -> bool:
    binary = ENGINE_BINARIES.get(entry["engine"])
    return binary is None or binary.exists()


def pending_entries(queue: dict, state: dict) -> list[dict]:
    return [e for e in queue["entries"] if state.get(e["id"], {}).get("status") not in ("done", "failed", "skipped")]


def main() -> None:
    (LLM / "serve-mode").write_text("none\n")
    while True:
        # re-read both files every entry so queue edits take effect without restarting the runner
        apply_resets()
        queue, state = load_json(QUEUE, {"entries": []}), load_json(STATE, {})
        pending = pending_entries(queue, state)
        if not pending:
            break
        entry = next((e for e in pending if engine_ready(e)), None)
        if entry is None:
            # only entries whose engine is not installed yet remain: wait instead of finishing
            log(f"waiting for engines: {sorted({e['engine'] for e in pending})}")
            time.sleep(3600)
            continue
        log(f"=== {entry['id']} ({entry['engine']}) ===")
        run_entry(entry, queue["defaults"], state)
    finish_queue()


if __name__ == "__main__":
    main()
