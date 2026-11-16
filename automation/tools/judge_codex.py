"""Pairwise LLM-as-judge for the open Korean prompts, run on the Mac with the local Codex CLI.

For every open-ko prompt the candidate's answer is compared with the reference model's answer twice,
with the A/B positions swapped, and model names are never shown to the judge. Output goes to
results/_shared/judgments/<candidate>__vs__<reference>.json with per-item verdicts and a summary.

Only non-confidential benchmark prompts and public-model answers are sent to the judge service.
"""
import argparse
import hashlib
import json
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

SCHEMA = {"type": "object", "additionalProperties": False, "required": ["winner", "score_a", "score_b", "reason"],
          "properties": {"winner": {"type": "string", "enum": ["A", "B", "tie"]},
                         "score_a": {"type": "integer", "minimum": 1, "maximum": 10},
                         "score_b": {"type": "integer", "minimum": 1, "maximum": 10},
                         "reason": {"type": "string"}}}
TEMPLATE = """You are an impartial judge. Compare two answers to the same Korean user request.
Judge helpfulness, factual correctness, Korean fluency, honesty about uncertainty and how well the request is followed.
A safe refusal of a harmful request is correct. Ignore length unless it hurts quality. Do not use tools or read files.

[Request]
{prompt}

[Answer A]
{a}

[Answer B]
{b}

Return the verdict as JSON."""
TEMPLATE_SHA = hashlib.sha256(TEMPLATE.encode()).hexdigest()[:12]


def codex_default_model() -> str:
    """The model `codex exec` uses when -m is not given (recorded so verdicts stay attributable)."""
    cfg = Path.home() / ".codex/config.toml"
    for line in cfg.read_text().splitlines() if cfg.exists() else []:
        if line.split("=")[0].strip() == "model":
            return line.split("=", 1)[1].strip().strip('"') + " (codex config)"
    return "codex default"


def load_answers(result_dir: Path) -> dict[str, dict]:
    path = result_dir / "runs" / "quality-open-ko" / "results.jsonl"
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return {r["id"]: r for r in rows}


def judge_once(prompt: str, a: str, b: str, model: str | None) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        schema, out = Path(tmp) / "schema.json", Path(tmp) / "out.json"
        schema.write_text(json.dumps(SCHEMA))
        cmd = ["codex", "exec", "--ephemeral", "--skip-git-repo-check", "-s", "read-only",
               "--output-schema", str(schema), "-o", str(out), *(["-m", model] if model else []), "-"]
        proc = subprocess.run(cmd, input=TEMPLATE.format(prompt=prompt, a=a or "(빈 응답)", b=b or "(빈 응답)"),
                              capture_output=True, text=True, timeout=600, check=False)
        if proc.returncode != 0 or not out.exists():
            return {"error": (proc.stderr or proc.stdout)[-300:]}
        return json.loads(out.read_text())


def cand_outcome(verdict: dict, cand_pos: str) -> str | None:
    if "winner" not in verdict:
        return None
    return "tie" if verdict["winner"] == "tie" else ("win" if verdict["winner"] == cand_pos else "loss")


def judge_item(item_id: str, prompt: str, cand: str, ref: str, model: str | None) -> dict:
    first = judge_once(prompt, cand, ref, model)   # candidate in position A
    second = judge_once(prompt, ref, cand, model)  # candidate in position B
    return {"id": item_id, "cand_first": cand_outcome(first, "A"), "cand_second": cand_outcome(second, "B"),
            "cand_scores": [first.get("score_a"), second.get("score_b")], "ref_scores": [first.get("score_b"), second.get("score_a")],
            "verdicts": [first, second]}


def summarize(rows: list[dict]) -> dict:
    outcomes = [o for r in rows for o in (r["cand_first"], r["cand_second"]) if o]
    def scores(key: str) -> list[int]:
        return [s for r in rows for s in r[key] if isinstance(s, int)]

    def mean(xs: list[int]) -> float | None:
        return round(sum(xs) / len(xs), 2) if xs else None

    consistent = sum(1 for r in rows if r["cand_first"] and r["cand_first"] == r["cand_second"])
    return {"judgments": len(outcomes), "win": outcomes.count("win"), "tie": outcomes.count("tie"), "loss": outcomes.count("loss"),
            "win_rate_ties_half": round((outcomes.count("win") + 0.5 * outcomes.count("tie")) / len(outcomes), 3) if outcomes else None,
            "candidate_score_mean": mean(scores("cand_scores")), "reference_score_mean": mean(scores("ref_scores")),
            "position_consistent_items": consistent, "items": len(rows)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", required=True, help="result folder of the model to judge")
    parser.add_argument("--reference", required=True, help="result folder of the reference model")
    parser.add_argument("--out-dir", default="results/_shared/judgments")
    parser.add_argument("--model", help="Codex model (default: Codex config)")
    parser.add_argument("--workers", type=int, default=3)
    args = parser.parse_args()
    cand, ref = load_answers(Path(args.candidate)), load_answers(Path(args.reference))
    ids = sorted(cand.keys() & ref.keys())
    open_items = Path("results/_shared/quality/open-ko.jsonl").read_text(encoding="utf-8").splitlines()
    prompts = {row["id"]: row["prompt"] for row in map(json.loads, filter(str.strip, open_items))}
    jobs = [(i, prompts[i], cand[i]["content"], ref[i]["content"], args.model) for i in ids]
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        rows = list(pool.map(lambda job: judge_item(*job), jobs))
    name = f"{Path(args.candidate).name}__vs__{Path(args.reference).name}"
    report = {"judge": {"tool": "codex exec", "model": args.model or codex_default_model(), "template_sha": TEMPLATE_SHA,
                        "method": "pairwise, positions swapped, model names hidden"},
              "candidate": Path(args.candidate).name, "reference": Path(args.reference).name,
              "summary": summarize(rows), "items": rows}
    out = Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)
    (out / f"{name}.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(report["summary"], ensure_ascii=False))


if __name__ == "__main__":
    main()
