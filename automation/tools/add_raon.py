import json, os, sys
P = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/llm/queue.json")
q = json.load(open(P))
NOTE = ["Raon-1 mini (KRAFTON, 2026-11-24, Apache 2.0): 28.8B total / 4.3B active MoE trained from scratch, hybrid Raon Delta Attention, 262K context.",
        "Vendor benchmarks put it far ahead on internal Korean chat (92.7 vs Qwen3.6-35B 74.5) and ahead on MultiChallenge, while trailing on MMLU-Pro.",
        "reasoning_effort has six levels (none/low/medium/high/xhigh/max); 'none' or enable_thinking=false turns thinking off."]
HOLD_LCPP = "llama.cpp build after 2026-11-25 (PR #32176 adds the Raon architecture); current build 44c20b1 (11-21)"
HOLD_VLLM = "needs KRAFTON's vLLM fork (github.com/krafton-ai/vllm); stock vLLM v0.32.0 cannot load raon1_mini"
base = {"vision": False, "quality": True, "quality_max_tokens": 16384, "license_class": "free"}
new = [
    {"id": "llamacpp-raon1-mini-q4km", "engine": "llamacpp", "profile": "standard", **base,
     "repository": "KRAFTON/Raon-1-mini-gguf", "hf_include": ["raon-1-mini-Q4_K_M.gguf"], "size_bytes": 19700000000,
     "context": ["512", "2k", "8k", "32k", "60k"], "llama_args": ["-c", "65536"],
     "keep_for": ["ikllama", "inferssd"], "hold": HOLD_LCPP,
     "notes": NOTE + ["Q4_K_M (19.7 GB). Korean-first candidate for the in-house chatbot use case."]},
    {"id": "quality-llamacpp-raon1-mini-q4km-nothink", "engine": "llamacpp", "profile": "quality", **base,
     "repository": "KRAFTON/Raon-1-mini-gguf", "hf_include": ["raon-1-mini-Q4_K_M.gguf"], "size_bytes": 19700000000,
     "context": [], "llama_args": ["-c", "65536"], "extra_body": {"reasoning_effort": "none"},
     "hold": HOLD_LCPP, "notes": NOTE + ["Thinking off, to pair with the other nothink runs."]},
    {"id": "quality-llamacpp-raon1-mini-q4km-effort-medium", "engine": "llamacpp", "profile": "quality", **base,
     "repository": "KRAFTON/Raon-1-mini-gguf", "hf_include": ["raon-1-mini-Q4_K_M.gguf"], "size_bytes": 19700000000,
     "context": [], "llama_args": ["-c", "65536"], "extra_body": {"reasoning_effort": "medium"},
     "hold": HOLD_LCPP, "notes": NOTE + ["Middle reasoning effort; Bonsai showed the middle setting can beat both extremes."]},
    {"id": "vllm-raon1-mini-nvfp4", "engine": "vllm", "profile": "full", **base,
     "repository": "KRAFTON/Raon-1-mini-nvfp4", "size_bytes": 17600000000,
     "context": ["512", "2k", "8k", "32k", "60k"],
     "vllm_args": ["--max-model-len", "65536", "--trust-remote-code", "--gpu-memory-utilization", "0.6", "--max-num-seqs", "16"],
     "concurrency_levels": [1, 4, 8, 16], "hold": HOLD_VLLM,
     "notes": NOTE + ["Native NVFP4 (17.6 GB). Needs the KRAFTON vLLM fork, so this stays on hold until that engine is built."]},
]
ids = {e["id"] for e in q["entries"]}
q["entries"] += [e for e in new if e["id"] not in ids]
t = P + ".tmp"; json.dump(q, open(t, "w"), indent=1, ensure_ascii=False); os.replace(t, P)
print("queue entries:", len(q["entries"]))
