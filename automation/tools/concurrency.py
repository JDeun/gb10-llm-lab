"""Aggregate N parallel bench.py run directories into one concurrency summary."""
import argparse
import json
from datetime import datetime, timedelta
from pathlib import Path


def load_records(run_dir: Path) -> list[dict]:
    lines = (run_dir / "results.jsonl").read_text(encoding="utf-8").splitlines()
    return [json.loads(line) for line in lines if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True)
    parser.add_argument("run_dirs", nargs="+")
    args = parser.parse_args()
    records = [r for d in args.run_dirs for r in load_records(Path(d))]
    starts = [datetime.fromisoformat(r["started_utc"]) for r in records]
    ends = [s + timedelta(seconds=r["elapsed_s"]) for s, r in zip(starts, records)]
    wall = (max(ends) - min(starts)).total_seconds()
    tokens = sum((r.get("usage") or {}).get("completion_tokens", 0) for r in records)
    per_request = sorted(r["end_to_end_completion_tokens_per_s"] for r in records
                         if r.get("end_to_end_completion_tokens_per_s"))
    summary = {
        "clients": len(args.run_dirs),
        "requests": len(records),
        "errors": sum(1 for r in records if r.get("error")),
        "wall_s": round(wall, 2),
        "completion_tokens_total": tokens,
        "aggregate_completion_tokens_per_s": round(tokens / wall, 2) if wall else None,
        "per_request_e2e_tokens_per_s_median": per_request[len(per_request) // 2] if per_request else None,
        "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill.",
    }
    Path(args.out).write_text(json.dumps(summary, indent=1), encoding="utf-8")
    print(json.dumps(summary))


if __name__ == "__main__":
    main()
