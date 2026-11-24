import json, os, sys
P = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/llm/queue.json")
q = json.load(open(P))
HOLD = "nari-llama.cpp fork not built yet (no arm64 release; build from source, untested on GB10)"
NOTE = ["NariQ (Nari Labs, 2026-11-20, Apache 2.0): trellis-coded PTQ of Qwen3.8-27B calibrated on coding-agent traces.",
        "Vendor claims 3.0/2.5bpw match BF16 on long-horizon agent tasks, math and image understanding.",
        "Needs the nari-llama.cpp fork (b12431-nariv0); stock llama.cpp cannot load the tensor types.",
        "Vision (mmproj) not measured: the runner's GGUF server does not pass --mmproj yet."]
base = {"engine": "nariq", "vision": False, "repository": "nari-labs/Qwen3.8-27B-NariQ-GGUF",
        "profile": "standard", "context": ["512", "2k", "8k", "32k", "60k"], "quality": True,
        "quality_max_tokens": 16384, "llama_args": ["-c", "65536", "--temp", "1.0", "--top-p", "0.95",
                                                    "--top-k", "20", "--min-p", "0"], "hold": HOLD}
new = [
    {"id": "nariq-qwen38-27b-3.0bpw", **base, "hf_include": ["Qwen3.8-27B-NariQ-3.0bpw.gguf", "Qwen3.8-27B-NariQ-mmproj-BF16.gguf"],
     "size_bytes": 11050000000, "keep_for": ["nariq"],
     "notes": NOTE + ["Default file (10.12 GB). Sampling flags are the vendor's thinking-mode settings."]},
    {"id": "nariq-qwen38-27b-2.5bpw", **base, "hf_include": ["Qwen3.8-27B-NariQ-2.5bpw.gguf"],
     "size_bytes": 8440000000, "keep_for": ["nariq"],
     "notes": NOTE + ["8.44 GB; vendor reports BF16-level agent scores at this size."]},
    {"id": "nariq-qwen38-27b-2.0bpw", **base, "hf_include": ["Qwen3.8-27B-NariQ-2.0bpw.gguf"],
     "size_bytes": 6750000000,
     "notes": NOTE + ["6.75 GB; vendor reports it is weaker on math and agent tasks."]},
]
ids = {e["id"] for e in q["entries"]}
q["entries"] += [e for e in new if e["id"] not in ids]
t = P + ".tmp"; json.dump(q, open(t, "w"), indent=1, ensure_ascii=False); os.replace(t, P)
print("queue entries:", len(q["entries"]))
