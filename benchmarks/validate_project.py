#!/usr/bin/env python3
"""Validate small, versioned benchmark inputs without downloading or running models."""
import json
import py_compile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def positive_bytes(value):
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def main():
    configs = {}
    for path in sorted((ROOT / "configs").glob("*.json")):
        configs[path.name] = json.loads(path.read_text(encoding="utf-8"))
    catalog = configs["models.json"]
    if catalog["constraints"]["device_count"] != 1:
        raise ValueError("This protocol is scoped to one GB10")
    limit = catalog["constraints"]["storage_nominal_bytes"]
    if not positive_bytes(limit):
        raise ValueError("Nominal storage must be positive bytes")
    seen = set()
    for case in catalog["candidates"]:
        name = case["id"]
        if not isinstance(name, str) or not name or name in seen:
            raise ValueError("Candidate IDs must be unique nonempty strings")
        seen.add(name)
        size = case["checkpoint_bytes_estimate"]
        if size is not None and not positive_bytes(size):
            raise ValueError("Checkpoint estimates must be positive bytes or null")
        if size is not None and size > limit and not case["excluded_from_current_scope"]:
            raise ValueError("Oversized candidates must be excluded from the current scope")
        if not isinstance(case["sources"], list):
            raise ValueError("Candidate sources must be a list")
        for url in case["sources"]:
            if not isinstance(url, str) or not url.startswith("https://"):
                raise ValueError("Source references must be HTTPS URLs")
    policy = configs["policy.json"]
    if policy["scope"]["storage_nominal_bytes"] != limit:
        raise ValueError("Policy and model catalog storage scope disagree")
    if policy["reporting"]["sanity_is_general_capability_benchmark"]:
        raise ValueError("Sanity checks must not be labelled a capability benchmark")
    cases = [json.loads(line) for line in (ROOT / "prompts/sanity.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    case_ids = set()
    for case in cases:
        if not case.get("id") or case["id"] in case_ids:
            raise ValueError("Sanity IDs must be nonempty and unique")
        case_ids.add(case["id"])
        if not isinstance(case.get("prompt"), str) or not case["prompt"]:
            raise ValueError("Sanity prompt missing")
        if not isinstance(case.get("category"), str):
            raise ValueError("Sanity category missing")
        if ("expected_text" in case) == ("expected_json" in case):
            raise ValueError("Sanity cases need exactly one expected answer")
    if not cases:
        raise ValueError("Sanity set must not be empty")
    for folder in ("benchmarks", "tests"):
        for path in sorted((ROOT / folder).glob("*.py")):
            py_compile.compile(str(path), doraise=True)
    print(json.dumps({"status": "valid", "model_candidates": len(seen), "sanity_cases": len(cases), "models_run": 0}))


if __name__ == "__main__":
    main()
