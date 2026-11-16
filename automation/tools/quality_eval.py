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
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROWS_API = "https://datasets-server.huggingface.co/rows"
LOCAL = Path.home() / "llm/quality"
LETTERS = "ABCDEFGHIJ"
SEED = 20261116
REQUEST_GAP_S = 1.5
SETS = {
    "mmlu-pro": {"dataset": "TIGER-Lab/MMLU-Pro", "config": "default", "split": "test", "n": 140, "max_tokens": 4096},
    "kmmlu": {"dataset": "HAERAE-HUB/KMMLU", "split": "test", "n": 100, "max_tokens": 4096},
    "gsm8k": {"dataset": "openai/gsm8k", "config": "main", "split": "test", "n": 100, "max_tokens": 4096},
    "hrm8k-gsm8k": {"dataset": "HAERAE-HUB/HRM8K", "config": "GSM8K", "split": "test", "n": 100, "max_tokens": 4096},
}
KMMLU_SUBJECTS = ["Accounting", "Biology", "Chemistry", "Civil-Engineering", "Computer-Science", "Criminal-Law",
                  "Economics", "Education", "Electrical-Engineering", "Health", "Korean-History", "Law",
                  "Management", "Math", "Mechanical-Engineering", "Patent", "Political-Science-and-Sociology",
                  "Psychology", "Real-Estate", "Taxation"]


def fetch_rows(dataset: str, config: str, split: str, offset: int, length: int) -> list[dict]:
    query = urllib.parse.urlencode({"dataset": dataset, "config": config, "split": split, "offset": offset, "length": length})
    for attempt in range(8):  # the public rows API rate-limits bursts (HTTP 429): pace and back off
        try:
            time.sleep(REQUEST_GAP_S)
            with urllib.request.urlopen(f"{ROWS_API}?{query}", timeout=60) as resp:
                data = json.load(resp)
            return [{"row_idx": r["row_idx"], **r["row"]} for r in data["rows"]], data.get("num_rows_total")
        except urllib.error.HTTPError as exc:
            if exc.code != 429 or attempt == 7:
                raise
            time.sleep(min(300, 15 * 2 ** attempt))
    raise RuntimeError("unreachable")


def mc_prompt(question: str, options: list[str], korean: bool) -> str:
    opts = "\n".join(f"({LETTERS[i]}) {o}" for i, o in enumerate(options))
    tail = ("풀이 후 마지막 줄에 '정답: (X)' 형식으로 답하세요." if korean
            else "Think step by step, then finish with 'The answer is (X)'.")
    return f"{question}\n\n{opts}\n\n{tail}"


def math_prompt(question: str, korean: bool) -> str:
    tail = "풀이 후 마지막 줄에 '정답: 숫자' 형식으로 답하세요." if korean else "Solve it, then finish with 'The answer is <number>'."
    return f"{question}\n\n{tail}"


def build_items(name: str) -> tuple[list[dict], dict]:
    spec = SETS[name]
    rng = random.Random(f"{SEED}-{name}")
    items, revision = [], {}
    if name == "kmmlu":
        per = spec["n"] // len(KMMLU_SUBJECTS)
        for subject in KMMLU_SUBJECTS:
            _, total = fetch_rows(spec["dataset"], subject, spec["split"], 0, 1)
            for idx in sorted(rng.sample(range(total), per)):
                row = fetch_rows(spec["dataset"], subject, spec["split"], idx, 1)[0][0]
                items.append({"id": f"kmmlu/{subject}/{idx}", "prompt": mc_prompt(row["question"], [row[c] for c in "ABCD"], True),
                              "answer": LETTERS[int(row["answer"]) - 1], "kind": "mc"})
        return items, revision
    _, total = fetch_rows(spec["dataset"], spec["config"], spec["split"], 0, 1)
    for idx in sorted(rng.sample(range(total), spec["n"])):
        row = fetch_rows(spec["dataset"], spec["config"], spec["split"], idx, 1)[0][0]
        if name == "mmlu-pro":
            items.append({"id": f"mmlu-pro/{row['question_id']}", "category": row["category"],
                          "prompt": mc_prompt(row["question"], row["options"], False), "answer": row["answer"], "kind": "mc"})
        elif name == "gsm8k":
            items.append({"id": f"gsm8k/{idx}", "prompt": math_prompt(row["question"], False),
                          "answer": row["answer"].split("####")[-1].strip().replace(",", ""), "kind": "num"})
        else:
            items.append({"id": f"hrm8k-gsm8k/{idx}", "prompt": math_prompt(row["question"], True),
                          "answer": str(row["answer"]).replace(",", ""), "kind": "num"})
    return items, revision


def extract(kind: str, text: str) -> str | None:
    if kind == "mc":
        found = re.findall(r"(?:answer is|정답\s*[:：]?)\s*\(?([A-J])\)?", text, re.IGNORECASE)
        return found[-1].upper() if found else None
    found = re.findall(r"(?:answer is|정답\s*[:：]?)\s*\$?\s*(-?[\d,]*\.?\d+)", text, re.IGNORECASE)
    return found[-1].replace(",", "") if found else None


def same_number(a: str, b: str) -> bool:
    try:
        return abs(float(a) - float(b)) < 1e-6
    except ValueError:
        return False


def ask(base: str, model: str, prompt: str, max_tokens: int, extra: dict) -> dict:
    body = {"model": model, "messages": [{"role": "user", "content": prompt}], "temperature": 0, "max_tokens": max_tokens, **extra}
    req = urllib.request.Request(base.rstrip("/") + "/v1/chat/completions", json.dumps(body).encode(), {"Content-Type": "application/json"})
    start = time.time()
    with urllib.request.urlopen(req, timeout=3600) as resp:
        data = json.load(resp)
    choice = data["choices"][0]
    msg = choice["message"]
    return {"content": msg.get("content") or "", "reasoning": msg.get("reasoning_content") or msg.get("reasoning") or "",
            "finish_reason": choice.get("finish_reason"), "usage": data.get("usage"), "elapsed_s": round(time.time() - start, 2)}


def grade(item: dict, base: str, model: str, max_tokens: int, extra: dict) -> dict:
    try:
        out = ask(base, model, item["prompt"], max_tokens, extra)
    except (OSError, ValueError, KeyError, IndexError) as exc:
        return {"id": item["id"], "error": f"{type(exc).__name__}: {exc}"[:300], "correct": False, "complete": False}
    truncated = out["finish_reason"] == "length"
    pred = None if item.get("answer") is None else extract(item["kind"], out["content"])
    correct = None if item.get("answer") is None else bool(
        pred is not None and (pred == item["answer"] if item["kind"] == "mc" else same_number(pred, item["answer"])))
    return {"id": item["id"], "category": item.get("category"), "answer": item.get("answer"), "pred": pred, "correct": correct,
            "complete": not truncated and bool(out["content"].strip()), "truncated": truncated, **out, "error": None}


def summarize(name: str, rows: list[dict], wall: float) -> dict:
    graded = [r for r in rows if r.get("answer") is not None]
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
    manifest = {"seed": SEED, "sets": {}}
    for name in args.sets:
        items, _ = build_items(name)
        (LOCAL / f"{name}.jsonl").write_text("".join(json.dumps(i, ensure_ascii=False) + "\n" for i in items), encoding="utf-8")
        manifest["sets"][name] = {**{k: v for k, v in SETS[name].items()}, "ids": [i["id"] for i in items]}
        print(name, len(items))
    Path(args.manifest_out).write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")


def cmd_run(args) -> None:
    extra = json.loads(Path(args.extra_body).read_text()) if args.extra_body else {}
    for name in args.sets:
        src = Path(args.items_dir) / f"{name}.jsonl"
        items = [json.loads(line) for line in src.read_text(encoding="utf-8").splitlines() if line.strip()]
        max_tokens = args.max_tokens or SETS.get(name, {}).get("max_tokens", 2048)
        start = time.time()
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            rows = list(pool.map(grade, items, *[[v] * len(items) for v in (args.base_url, args.model, max_tokens, extra)]))
        out = Path(args.out_dir) / f"quality-{name}"
        out.mkdir(parents=True, exist_ok=True)
        (out / "results.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
        summary = summarize(name, rows, time.time() - start)
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
    args = parser.parse_args()
    {"prepare": cmd_prepare, "run": cmd_run}[args.cmd](args)


if __name__ == "__main__":
    main()
