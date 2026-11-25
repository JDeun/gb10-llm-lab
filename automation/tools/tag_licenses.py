"""Tag every queue entry with license_class, from the HF licence of its repository.

free         Apache-2.0 / MIT: no commercial restriction beyond notices.
conditional  commercial use allowed under conditions (scale thresholds, branding, MaaS carve-outs, NVIDIA indemnity).
non_commercial  research and education only: cannot ship.
unknown      no licence recorded: treat as conditional until checked.

docs/licenses.md holds the per-model detail and the source URLs.
"""
import json, os, re, sys, urllib.request

FREE = {"apache-2.0", "mit", "bsd-3-clause", "cc0-1.0"}
NON_COMMERCIAL = {"exaone"}
RANK = {"free": 0, "conditional": 1, "unknown": 1, "non_commercial": 2}

# A redistributor cannot grant more than the original model allows, so the base model's licence wins.
OVERRIDE = {
    # tagged apache-2.0 on the Hub, but the base Qwen3.8-Flash-Next is Qwen Community 1.0 (MaaS carve-out)
    "ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF": "conditional",
    # no licence field; the base thinkingmachines/Inkling-2-Mini is Apache-2.0
    "ggml-org/Inkling-2-Mini-GGUF": "free",
}


def fetch(repo: str) -> dict:
    with urllib.request.urlopen(f"https://huggingface.co/api/models/{repo}", timeout=20) as r:
        return (json.load(r).get("cardData") or {})


def normalise(repo: str) -> str:
    """Queue repositories sometimes carry a trailing note, e.g. "owner/name (IQ3_S)"."""
    return re.sub(r"\s*\(.*?\)\s*$", "", repo).strip()


def classify(license_id, license_name) -> str:
    if (license_name or "") in NON_COMMERCIAL:
        return "non_commercial"
    if (license_id or "") in FREE:
        return "free"
    if not license_id:
        return "unknown"
    return "conditional"


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/llm/queue.json")
    queue = json.load(open(path))
    cache = {}
    here = os.path.dirname(os.path.abspath(__file__))
    for rec in json.load(open(os.path.join(here, "license-data.json"))):
        repo = rec.get("resolved") or rec["repo"]
        if not rec.get("error"):
            cache[repo] = (rec.get("license"), rec.get("license_name"))
    changed = 0
    for entry in queue["entries"]:
        repo = normalise(entry["repository"])
        if repo not in cache:
            try:
                card = fetch(repo)
                cache[repo] = (card.get("license"), card.get("license_name"))
            except Exception:
                cache[repo] = (None, None)
        cls = OVERRIDE.get(repo) or classify(*cache[repo])
        if entry.get("license_class") != cls:
            entry["license_class"] = cls
            changed += 1
    tmp = path + ".tmp"
    json.dump(queue, open(tmp, "w"), indent=1, ensure_ascii=False)
    os.replace(tmp, path)
    from collections import Counter
    print(changed, "tagged;", Counter(e["license_class"] for e in queue["entries"]))


if __name__ == "__main__":
    main()
