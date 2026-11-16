"""Answer-quality evaluation on fixed public subsets (zero-shot, generate-only) plus open Korean prompts.

prepare: fetch fixed rows from the HF datasets-server into ~/llm/quality/<set>.jsonl (not committed:
         KMMLU is CC-BY-ND) and write the id manifest committed to the repo.
run:     ask every item over an OpenAI-compatible API, extract the final answer, grade it and write
         results.jsonl + summary.json with the protocol denominators (planned/attempted/complete/graded/correct).

Scores are named "<set>-subset-zeroshot" and are not comparable with official benchmark numbers.
"""
import argparse
import json
import random
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

PARQUET_API = "https://datasets-server.huggingface.co/parquet"
LOCAL = Path.home() / "llm/quality"
LETTERS = "ABCDEFGHIJ"
SEED = 20261116
MC_TOKENS = 4096
BASE = {
    "mmlu-pro": {"dataset": "TIGER-Lab/MMLU-Pro", "config": "default", "split": "test"},
    "kmmlu": {"dataset": "HAERAE-HUB/KMMLU", "split": "test"},
    "gsm8k": {"dataset": "openai/gsm8k", "config": "main", "split": "test"},
    "hrm8k-gsm8k": {"dataset": "HAERAE-HUB/HRM8K", "config": "GSM8K", "split": "test"},
    "humaneval": {"dataset": "openai/openai_humaneval", "config": "openai_humaneval", "split": "test"},
}
# "-l" sets are the larger confirmation subsets used for the final candidates
SETS = {"mmlu-pro": ("mmlu-pro", 140), "mmlu-pro-l": ("mmlu-pro", 420), "kmmlu": ("kmmlu", 100), "kmmlu-l": ("kmmlu", 300),
        "gsm8k": ("gsm8k", 100), "gsm8k-l": ("gsm8k", 300), "hrm8k-gsm8k": ("hrm8k-gsm8k", 100),
        "hrm8k-gsm8k-l": ("hrm8k-gsm8k", 300), "humaneval": ("humaneval", 164)}
KMMLU_SUBJECTS = ["Accounting", "Biology", "Chemistry", "Civil-Engineering", "Computer-Science", "Criminal-Law",
                  "Economics", "Education", "Electrical-Engineering", "Health", "Korean-History", "Law",
                  "Management", "Math", "Mechanical-Engineering", "Patent", "Political-Science-and-Sociology",
                  "Psychology", "Real-Estate", "Taxation"]


def http_get(url: str) -> bytes:
    for attempt in range(8):  # the public endpoints rate-limit (429) and sometimes fail (5xx): back off and retry
        try:
            with urllib.request.urlopen(url, timeout=120) as resp:
                return resp.read()
        except urllib.error.HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 7:
                raise
            time.sleep(min(300, 15 * 2 ** attempt))
        except urllib.error.URLError:  # DNS or connection drop on a flaky network
            if attempt == 7:
                raise
            time.sleep(min(300, 15 * 2 ** attempt))
    raise RuntimeError("unreachable")


def split_rows(dataset: str, config: str, split: str) -> list[dict]:
    """All rows of one split from the dataset's converted parquet files (a few MB, fetched once)."""
    import pyarrow.parquet as pq  # run prepare with: uvx --with pyarrow python quality_eval.py prepare ...
    listing = json.loads(http_get(f"{PARQUET_API}?{urllib.parse.urlencode({'dataset': dataset})}"))
    urls = [f["url"] for f in listing["parquet_files"] if f["config"] == config and f["split"] == split]
    cache = LOCAL / "_parquet"
    cache.mkdir(parents=True, exist_ok=True)
    rows = []
    for url in urls:
        path = cache / (dataset.replace("/", "__") + "__" + config + "__" + url.rsplit("/", 1)[-1])
        if not path.exists():
            path.write_bytes(http_get(url))
        rows += pq.read_table(path).to_pylist()
    return rows


def mc_prompt(question: str, options: list[str], korean: bool) -> str:
    opts = "\n".join(f"({LETTERS[i]}) {o}" for i, o in enumerate(options))
    tail = ("풀이 후 마지막 줄에 '정답: (X)' 형식으로 답하세요." if korean
            else "Think step by step, then finish with 'The answer is (X)'.")
    return f"{question}\n\n{opts}\n\n{tail}"


def math_prompt(question: str, korean: bool) -> str:
    tail = "풀이 후 마지막 줄에 '정답: 숫자' 형식으로 답하세요." if korean else "Solve it, then finish with 'The answer is <number>'."
    return f"{question}\n\n{tail}"


def to_item(base: str, idx: int, row: dict, subject: str = "") -> dict:
    if base == "mmlu-pro":
        return {"id": f"mmlu-pro/{row['question_id']}", "category": row["category"], "kind": "mc",
                "prompt": mc_prompt(row["question"], row["options"], False), "answer": row["answer"]}
    if base == "kmmlu":
        return {"id": f"kmmlu/{subject}/{idx}", "category": subject, "kind": "mc",
                "prompt": mc_prompt(row["question"], [row[c] for c in "ABCD"], True), "answer": LETTERS[int(row["answer"]) - 1]}
    if base == "gsm8k":
        return {"id": f"gsm8k/{idx}", "kind": "num", "prompt": math_prompt(row["question"], False),
                "answer": row["answer"].split("####")[-1].strip().replace(",", "")}
    if base == "hrm8k-gsm8k":
        return {"id": f"hrm8k-gsm8k/{idx}", "kind": "num", "prompt": math_prompt(row["question"], True),
                "answer": str(row["answer"]).replace(",", "")}
    return {"id": row["task_id"], "kind": "code", "entry_point": row["entry_point"], "test": row["test"], "answer": "pass",
            "prompt": "Complete the following Python function. Reply with the full function in one ```python code block.\n\n"
                      + row["prompt"]}


def build_items(name: str) -> list[dict]:
    base, n = SETS[name]
    spec = BASE[base]
    rng = random.Random(f"{SEED}-{name}")
    if base == "kmmlu":
        items = []
        for subject in KMMLU_SUBJECTS:
            rows = split_rows(spec["dataset"], subject, spec["split"])
            items += [to_item(base, i, rows[i], subject) for i in sorted(rng.sample(range(len(rows)), n // len(KMMLU_SUBJECTS)))]
        return items
    rows = split_rows(spec["dataset"], spec["config"], spec["split"])
    picks = range(len(rows)) if n >= len(rows) else sorted(rng.sample(range(len(rows)), n))
    return [to_item(base, i, rows[i]) for i in picks]


def extract(kind: str, text: str) -> str | None:
    if kind == "mc":
        found = re.findall(r"(?:answer is|정답\s*[:：]?)\s*\(?([A-J])\)?", text, re.IGNORECASE)
        return found[-1].upper() if found else None
    found = re.findall(r"(?:answer is|정답\s*[:：]?)\s*\$?\s*(-?[\d,]*\.?\d+)", text, re.IGNORECASE)
    return found[-1].replace(",", "") if found else None


SANDBOX = ["docker", "run", "--rm", "-i", "--network", "none", "--memory", "512m", "--cpus", "1", "--pids-limit", "64",
           "--read-only", "--tmpfs", "/tmp:size=16m", "--user", "65534:65534", "python:3.12-slim", "timeout", "15", "python", "-"]


def code_block(text: str) -> str | None:
    blocks = re.findall(r"```(?:python|py)?\s*\n(.*?)```", text, re.DOTALL)
    return blocks[-1] if blocks else None


def sandbox_pass(code: str, test: str, entry_point: str) -> bool:
    """Run model code + the hidden tests in a throwaway container: no network, read-only, 512 MB, 15 s."""
    program = f"{code}\n\n{test}\n\ncheck({entry_point})\n"
    try:
        return subprocess.run(SANDBOX, input=program, capture_output=True, text=True, timeout=60, check=False).returncode == 0
    except subprocess.TimeoutExpired:
        return False


def tool_match(call: dict | None, expect: dict) -> bool:
    if not call or call.get("name") != expect["name"]:
        return False
    try:
        args = json.loads(call.get("arguments") or "{}")
    except ValueError:
        return False
    def norm(value) -> str:  # ignore case, spaces and punctuation; 100 == 100.0
        text = str(value).strip().lower()
        text = text.removesuffix(".0")
        return re.sub(r"[\s'\".,!?]", "", text)

    def accepts(got, want) -> bool:
        return any(norm(got) == norm(w) for w in (want if isinstance(want, list) else [want]))

    return all(accepts(args.get(k), v) for k, v in expect.get("args", {}).items())


def same_number(a: str, b: str) -> bool:
    try:
        return abs(float(a) - float(b)) < 1e-6
    except ValueError:
        return False


def ask(base: str, model: str, prompt: str, max_tokens: int, extra: dict, tools: list | None = None) -> dict:
    body = {"model": model, "messages": [{"role": "user", "content": prompt}], "temperature": 0, "max_tokens": max_tokens, **extra}
    if tools:
        body["tools"] = tools
    req = urllib.request.Request(base.rstrip("/") + "/v1/chat/completions", json.dumps(body).encode(), {"Content-Type": "application/json"})
    start = time.time()
    with urllib.request.urlopen(req, timeout=3600) as resp:
        data = json.load(resp)
    choice = data["choices"][0]
    msg = choice["message"]
    calls = msg.get("tool_calls") or []
    return {"content": msg.get("content") or "", "reasoning": msg.get("reasoning_content") or msg.get("reasoning") or "",
            "tool_call": (calls[0].get("function") if calls else None),
            "finish_reason": choice.get("finish_reason"), "usage": data.get("usage"), "elapsed_s": round(time.time() - start, 2)}


def grade(item: dict, base: str, model: str, max_tokens: int, extra: dict) -> dict:
    try:
        out = ask(base, model, item["prompt"], max_tokens, extra, item.get("tools"))
    except (OSError, ValueError, KeyError, IndexError) as exc:
        return {"id": item["id"], "error": f"{type(exc).__name__}: {exc}"[:300], "correct": False, "complete": False}
    truncated = out["finish_reason"] == "length"
    pred, correct = judge_answer(item, out)
    answered = bool(out["content"].strip()) or out.get("tool_call") is not None
    return {"id": item["id"], "category": item.get("category"), "answer": item.get("answer"), "pred": pred, "correct": correct,
            "complete": not truncated and answered, "truncated": truncated, **out, "error": None}


def judge_answer(item: dict, out: dict) -> tuple:
    kind = item["kind"]
    if kind == "open":
        return None, None
    if kind == "tool":
        call = out.get("tool_call")
        return (call or {}).get("name"), tool_match(call, item["expect"])
    if kind == "code":
        code = code_block(out["content"])
        return ("code" if code else None), bool(code and sandbox_pass(code, item["test"], item["entry_point"]))
    pred = extract(kind, out["content"])
    ok = pred is not None and (pred == item["answer"] if kind == "mc" else same_number(pred, item["answer"]))
    return pred, ok


def summarize(name: str, rows: list[dict], wall: float) -> dict:
    graded = [r for r in rows if r.get("correct") is not None]
    complete = [r for r in rows if r.get("complete")]
    correct = sum(1 for r in graded if r.get("correct"))
    toks = [(r.get("usage") or {}).get("completion_tokens", 0) for r in rows]
    return {"set": name, "label": f"{name}-subset-zeroshot", "planned_requests": len(rows), "attempted_requests": len(rows),
            "final_text_complete_requests": len(complete), "truncated_outputs": sum(1 for r in rows if r.get("truncated")),
            "transport_failures": sum(1 for r in rows if r.get("error")), "planned_correctness_requests": len(graded),
            "correctness_evaluated": sum(1 for r in graded if r.get("complete")), "correctness_passed": correct,
            "accuracy_on_attempted": round(correct / len(graded), 4) if graded else None,
            "accuracy_on_completed": round(correct / max(1, sum(1 for r in graded if r.get("complete"))), 4) if graded else None,
            "completion_tokens_mean": round(sum(toks) / max(1, len(toks)), 1), "wall_s": round(wall, 1), "metrics": {}}


def cmd_prepare(args) -> None:
    LOCAL.mkdir(parents=True, exist_ok=True)
    out = Path(args.manifest_out)
    manifest = json.loads(out.read_text()) if out.exists() else {"seed": SEED, "sets": {}}
    for name in args.sets:
        items = build_items(name)
        (LOCAL / f"{name}.jsonl").write_text("".join(json.dumps(i, ensure_ascii=False) + "\n" for i in items), encoding="utf-8")
        manifest["sets"][name] = {**BASE[SETS[name][0]], "n": len(items), "ids": [i["id"] for i in items]}
        print(name, len(items))
        out.write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")  # save after every set


def cmd_run(args) -> None:
    extra = json.loads(Path(args.extra_body).read_text()) if args.extra_body else {}
    for name in args.sets:
        src = Path(args.items_dir) / f"{name}.jsonl"
        items = [json.loads(line) for line in src.read_text(encoding="utf-8").splitlines() if line.strip()]
        if args.limit:  # slow models: the first N items of each set, reported as a separate "-firstN" label
            items = items[:args.limit]
        max_tokens = args.max_tokens or MC_TOKENS
        start = time.time()
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            rows = list(pool.map(grade, items, *[[v] * len(items) for v in (args.base_url, args.model, max_tokens, extra)]))
        out = Path(args.out_dir) / f"quality-{name}"
        out.mkdir(parents=True, exist_ok=True)
        (out / "results.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
        summary = summarize(name, rows, time.time() - start)
        if args.limit and args.limit < len(items) + 1:
            summary["label"] += f"-first{len(items)}"
        (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
        print(json.dumps({k: summary[k] for k in ("set", "correctness_passed", "planned_correctness_requests", "truncated_outputs", "wall_s")}))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prepare")
    p.add_argument("--sets", nargs="+", default=list(SETS))
    p.add_argument("--manifest-out", required=True)
    r = sub.add_parser("run")
    r.add_argument("--base-url", required=True)
    r.add_argument("--model", required=True)
    r.add_argument("--sets", nargs="+", required=True)
    r.add_argument("--items-dir", default=str(LOCAL))
    r.add_argument("--out-dir", required=True)
    r.add_argument("--workers", type=int, default=4)
    r.add_argument("--max-tokens", type=int)
    r.add_argument("--extra-body")
    r.add_argument("--limit", type=int, help="first N items per set (slow models)")
    args = parser.parse_args()
    {"prepare": cmd_prepare, "run": cmd_run}[args.cmd](args)


if __name__ == "__main__":
    main()
