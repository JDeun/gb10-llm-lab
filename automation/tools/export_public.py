"""Export one experiment's local runs as a sanitized, reviewable bundle for the public repo.

Copies summary/results/manifest/inventory per run part, strips long prompt bodies
from request echoes (replaced by sha256 + length), redacts host-identifying strings
and writes a markdown table of the per-part metrics.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

# Host-specific words (user name, hostname) are read from ~/llm/redact-terms.txt, one per line, not committed.
TERMS_FILE = Path.home() / "llm/redact-terms.txt"
HOST_TERMS = [t.strip() for t in TERMS_FILE.read_text().splitlines() if t.strip()] if TERMS_FILE.exists() else []
REDACTIONS = [
    (re.compile(r"/home/[A-Za-z0-9._-]+"), "<user-home>"),
    *[(re.compile(r"\b" + re.escape(t) + r"[0-9a-z-]*\b"), "<host>") for t in HOST_TERMS],
    (re.compile(r"\b100\.(6[4-9]|[7-9]\d|1[01]\d|12[0-7])\.\d{1,3}\.\d{1,3}\b"), "<tailscale-ip>"),
    (re.compile(r"\b192\.168\.\d{1,3}\.\d{1,3}\b"), "<lan-ip>"),
]
PROMPT_KEEP_CHARS = 400


def leaks(text: str) -> bool:
    """True when a host term, home path or private IP is still present after redaction."""
    return bool(re.search(r"/home/|\b100\.(6[4-9]|[7-9]\d|1[01]\d|12[0-7])\.|192\.168\.", text)
                or any(t in text for t in HOST_TERMS))


def redact(text: str) -> str:
    for pattern, repl in REDACTIONS:
        text = pattern.sub(repl, text)
    return text


def shrink_record(record: dict) -> dict:
    request = record.get("request") or {}
    messages = [
        {**m, "content": m["content"]} if len(str(m.get("content", ""))) <= PROMPT_KEEP_CHARS else
        {"role": m.get("role"), "content_sha256": hashlib.sha256(str(m["content"]).encode()).hexdigest(),
         "content_chars": len(str(m["content"])), "content_head": str(m["content"])[:200]}
        for m in request.get("messages", [])
    ]
    return {**record, "request": {**request, "messages": messages}}


def median(values: list) -> float | None:
    vals = sorted(v for v in values if isinstance(v, (int, float)))
    return round(vals[len(vals) // 2], 2) if vals else None


def part_row(name: str, summary: dict, records: list[dict]) -> str:
    m = summary.get("metrics", {})
    pick = lambda k: round(m[k]["median"], 2) if m.get(k, {}).get("n") else None
    prompt_tokens = median([(r.get("usage") or {}).get("prompt_tokens") for r in records])
    prefill = median([(r.get("engine_timings") or {}).get("prompt_per_second") for r in records])
    def no_cache(r: dict) -> bool:
        engine = (r.get("engine_timings") or {}).get("cache_n")
        usage = ((r.get("usage") or {}).get("prompt_tokens_details") or {}).get("cached_tokens")
        return (engine if engine is not None else usage) == 0
    cold = [r for r in records if no_cache(r) and r.get("ttft_semantic_s")]
    cold_ttft = round(max(r["ttft_semantic_s"] for r in cold), 2) if cold else None
    errors = sorted({str(r.get("error"))[:60] for r in records if r.get("error")})
    k, g = summary.get("correctness_passed"), summary.get("correctness_evaluated")
    graded = f"{k}/{g}" if summary.get("planned_correctness_requests") else "-"
    return (f"| {name} | {summary.get('attempted_requests')}/{summary.get('planned_requests')} | "
            f"{summary.get('final_text_complete_requests')} | {graded} | {summary.get('truncated_outputs')} | "
            f"{prompt_tokens} | {pick('ttft_semantic_s')} | {cold_ttft} | {prefill} | {pick('engine_reported_decode_tokens_per_s')} | "
            f"{pick('end_to_end_completion_tokens_per_s')} | {'; '.join(errors) or '-'} |")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--src", required=True, help="local/<prefix> directory")
    parser.add_argument("--dst", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--digests", help="sha256sum output for the model artifacts")
    args = parser.parse_args()
    src, dst = Path(args.src), Path(args.dst)
    (dst / "runs").mkdir(parents=True, exist_ok=True)
    (dst / "manifest.json").write_text(redact(Path(args.manifest).read_text(encoding="utf-8")), encoding="utf-8")
    if args.digests:
        (dst / "artifact.sha256").write_text(redact(Path(args.digests).read_text(encoding="utf-8")), encoding="utf-8")
    rows = []
    for part in sorted(p for p in src.iterdir() if p.is_dir()):
        out = dst / "runs" / part.name
        out.mkdir(exist_ok=True)
        records = [json.loads(l) for l in (part / "results.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()] \
            if (part / "results.jsonl").exists() else []
        (out / "results.jsonl").write_text(
            "".join(redact(json.dumps(shrink_record(r), ensure_ascii=False)) + "\n" for r in records), encoding="utf-8")
        for name in ("summary.json", "inventory.json"):
            if (part / name).exists():
                (out / name).write_text(redact((part / name).read_text(encoding="utf-8")), encoding="utf-8")
        if (part / "summary.json").exists():
            rows.append(part_row(part.name, json.loads((part / "summary.json").read_text(encoding="utf-8")), records))
    for extra in src.glob("*.json"):
        (dst / extra.name).write_text(redact(extra.read_text(encoding="utf-8")), encoding="utf-8")
    header = ("| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | "
              "TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |\n"
              "|---|---|---|---|---|---|---|---|---|---|---|---|")
    (dst / "TABLE.md").write_text(header + "\n" + "\n".join(rows) + "\n", encoding="utf-8")
    leftovers = [p for p in dst.rglob("*") if p.is_file() and leaks(p.read_text(errors="ignore"))]
    print("exported", dst, "rows", len(rows), "unredacted files:", leftovers)


if __name__ == "__main__":
    main()
