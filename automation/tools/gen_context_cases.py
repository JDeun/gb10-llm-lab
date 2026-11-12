"""Generate deterministic long-context retrieval cases (needle in a record list).

Each output file holds three cases whose needle sits at 10%, 50% and 90% of the
record list. The expected answer is an exact code string, so bench.py can grade
it with its exact-match rule.
"""
import argparse
import json
import random
import string
from pathlib import Path

CHARS_PER_TOKEN = 3.4  # rough estimate for this record format; real counts come from server usage
REGIONS = ("north", "south", "east", "west", "central")
STATUSES = ("active", "paused", "archived", "pending")


def make_code(rng: random.Random) -> str:
    alphabet = string.ascii_uppercase + string.digits
    return "".join(rng.choices(alphabet, k=4)) + "-" + "".join(rng.choices(alphabet, k=4))


def make_records(target_tokens: int, seed: int) -> list[tuple[str, str]]:
    rng = random.Random(seed)
    records, chars, index = [], 0, 0
    while chars / CHARS_PER_TOKEN < target_tokens:
        code = make_code(rng)
        line = (f"Record {index:05d}: code {code}; region {rng.choice(REGIONS)}; "
                f"status {rng.choice(STATUSES)}; owner team-{rng.randint(1, 99):02d}.")
        records.append((f"{index:05d}", line))
        chars += len(line) + 1
        index += 1
    return records


def build_cases(label: str, target_tokens: int, seed: int) -> list[dict]:
    records = make_records(target_tokens, seed)
    body = "\n".join(line for _, line in records)
    cases = []
    for fraction in (0.1, 0.5, 0.9):
        record_id, line = records[int(len(records) * fraction)]
        code = line.split("code ", 1)[1].split(";", 1)[0]
        prompt = (f"Below is a list of {len(records)} records.\n\n{body}\n\n"
                  f"What is the code of Record {record_id}? Reply with only the code, nothing else.")
        cases.append({"id": f"ctx-{label}-p{int(fraction * 100):02d}", "category": "context_retrieval",
                      "target_tokens": target_tokens, "prompt": prompt, "expected_text": code})
    return cases


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--seed", type=int, default=20261112)
    args = parser.parse_args()
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    targets = {"512": 512, "2k": 2048, "8k": 8192, "32k": 32768, "60k": 60000, "120k": 120000}
    for label, tokens in targets.items():
        path = out / f"ctx-{label}.jsonl"
        cases = build_cases(label, tokens, args.seed + tokens)
        path.write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in cases), encoding="utf-8")
        print(path, len(cases[0]["prompt"]), "chars")


if __name__ == "__main__":
    main()
