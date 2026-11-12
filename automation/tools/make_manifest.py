"""Fill the lab manifest template with this machine's hardware facts plus a per-model spec."""
import argparse
import json
import platform
import shutil
import subprocess
from pathlib import Path

TEMPLATE = Path.home() / "gb10-llm-lab/configs/manifest.example.json"


def run(cmd: list[str]) -> str:
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=20, check=False).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def hardware(storage_path: str) -> dict:
    mem_kib = int(next(l.split()[1] for l in Path("/proc/meminfo").read_text().splitlines() if l.startswith("MemTotal")))
    os_name = next((l.split("=", 1)[1].strip().strip('"') for l in Path("/etc/os-release").read_text().splitlines()
                    if l.startswith("PRETTY_NAME")), None)
    driver = run(["nvidia-smi", "--query-gpu=driver_version", "--format=csv,noheader"]) or None
    fs = run(["findmnt", "-n", "-o", "FSTYPE", "--target", storage_path]) or None
    return {
        "memory_bytes": mem_kib * 1024,
        "os": os_name,
        "kernel": platform.release(),
        "driver": driver,
        "cuda": "13.0 (driver-reported runtime family; engine bundles its own CUDA libraries)",
        "storage_model": run(["cat", "/sys/block/nvme0n1/device/model"]) or None,
        "storage_path": "<user-home>/" + Path(storage_path).relative_to(Path.home()).as_posix()
        if storage_path.startswith(str(Path.home())) else storage_path,
        "filesystem": fs,
        "available_storage_bytes": shutil.disk_usage(storage_path).free,
        "power_profile": "default (not changed)",
    }


def deep_merge(base: dict, extra: dict) -> dict:
    merged = dict(base)
    for key, value in extra.items():
        merged[key] = deep_merge(base[key], value) if isinstance(value, dict) and isinstance(base.get(key), dict) else value
    return merged


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", required=True, help="JSON file with experiment_id/model/engine/workload/runtime")
    parser.add_argument("--storage-path", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    manifest = deep_merge(template, {"hardware": hardware(args.storage_path), **spec})
    manifest["status"] = "actual_machine_measurement"
    Path(args.out).write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", args.out)


if __name__ == "__main__":
    main()
