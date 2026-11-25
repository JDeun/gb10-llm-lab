import json, os, sys
P = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/llm/queue.json")
q = json.load(open(P))
by = {e["id"]: e for e in q["entries"]}
NOTE = ["NVIDIA Qwen3.8-27B NVFP4-QAD (2026-11-04, NVIDIA Open Model Agreement — not the base Apache-2.0).",
        "Quantization-aware distillation: the BF16 teacher supplies token targets while the NVFP4 weights train, so the vendor reports BF16-level scores (GPQA 87.9 vs 88.2, Terminal-Bench 76.7 vs 77.3).",
        "19.9 GB vs 24.7 GB for RedHatAI/Qwen3.8-27B-NVFP4 (the delivery pin). Needs --quantization modelopt.",
        "Vendor tested on vLLM nightly; our vLLM is v0.32.0, so the entry may fail on this engine version."]
pairs = [("vllm-qwen38-27b-nvfp4-mtp-refpin", "vllm-qwen38-27b-qad-mtp-refpin",
          "Same engine settings as the delivery pin (util 0.45, 8 seqs, 128K, thinking on), for a direct QAD vs RedHatAI comparison."),
         ("vllm-qwen38-27b-nvfp4-mtp-nothink-matched", "vllm-qwen38-27b-qad-mtp-nothink-matched",
          "Same settings as the Qwen3.6 confirm run with thinking off (the best setting found for this model family).")]
added = []
for src, nid, why in pairs:
    if nid in by: continue
    e = json.loads(json.dumps(by[src]))
    e.pop("keep_for", None)
    e.update({"id": nid, "repository": "nvidia/Qwen3.8-27B-NVFP4-QAD", "size_bytes": 19900000000})
    e["vllm_args"] = [*e["vllm_args"], "--quantization", "modelopt"]
    e["notes"] = NOTE + [why]
    if "refpin" in nid:
        e["keep_for"] = ["vllm"]
    added.append(e)
q["entries"] += added
t = P + ".tmp"; json.dump(q, open(t, "w"), indent=1, ensure_ascii=False); os.replace(t, P)
print([e["id"] for e in added], "->", len(q["entries"]))
