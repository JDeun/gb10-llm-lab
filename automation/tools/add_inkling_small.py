import json, os, sys
P = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/llm/queue.json")
q = json.load(open(P))
base = {"vision": False, "repository": "bartowski/Inkling-2-Small-GGUF", "hf_include": ["Inkling-2-Small-IQ1_S/*"],
        "size_bytes": 127500000000, "context": ["512", "2k"], "may_evict": ["strata-qwen38fn-iq3s"],
        "notes": ["Inkling 2 Small (Thinking Machines, Apache 2.0): MoE 594B total / 17B active, 8 of 384 experts, 1M context.",
                  "Smallest GGUF (IQ1_S, 127.5 GB) is larger than the 108 GB runner limit: experts stream from SSD (capacity test, not a serving candidate).",
                  "Needs llama.cpp with #32217 + #32657 (inkling2, per-expert scales)."]}
new = [
    {"id": "llamacpp-inkling2small-iq1s", "engine": "llamacpp", "profile": "capacity", **base,
     "llama_args": ["-c", "8192", "--cpu-moe"], "keep_for": ["colibri"]},
    {"id": "colibri-inkling2small-iq1s", "engine": "colibri", "profile": "capacity", **base,
     "colibri_args": ["--ctx", "8192"], "start_timeout_s": 21600,
     "notes": base["notes"] + ["colibri support for inkling2 unconfirmed; same GGUF files as the llama.cpp entry."]},
]
ids = {e["id"] for e in q["entries"]}
q["entries"] += [e for e in new if e["id"] not in ids]
t = P + ".tmp"; json.dump(q, open(t, "w"), indent=1, ensure_ascii=False); os.replace(t, P)
print("queue entries:", len(q["entries"]))
