import json, os, sys
P = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/llm/queue.json")
q = json.load(open(P))
common = {"engine": "vllm", "repository": "RedHatAI/Qwen3.8-27B-NVFP4", "vision": False, "size_bytes": 24710000000,
          "quality": True, "quality_max_tokens": 16384}
pin = ["--max-model-len", "131072", "--gpu-memory-utilization", "0.45", "--max-num-seqs", "8", "--enable-prefix-caching",
       "--tool-call-parser", "qwen3_xml", "--enable-auto-tool-choice", "--reasoning-parser", "qwen3",
       "--speculative-config", "{\"method\":\"mtp\",\"num_speculative_tokens\":3}"]
matched = ["--max-model-len", "65536", "--kv-cache-dtype", "fp8", "--gpu-memory-utilization", "0.6", "--max-num-seqs", "16",
           "--max-num-batched-tokens", "8192", "--enable-chunked-prefill", "--async-scheduling", "--enable-prefix-caching",
           "--reasoning-parser", "qwen3", "--speculative-config", "{\"method\":\"mtp\",\"num_speculative_tokens\":3}",
           "--enable-auto-tool-choice", "--tool-call-parser", "qwen3_xml"]
new = [
    {"id": "vllm-qwen38-27b-nvfp4-mtp-refpin", **common, "profile": "standard", "context": ["512", "2k", "8k", "32k", "60k"],
     "vllm_args": pin, "concurrency_levels": [1, 4, 8], "keep_for": ["vllm"],
     "notes": ["Reference production setting: 27B dense NVFP4 + MTP-3, util 0.45, 8 seqs, 128K context, thinking on (engine default).",
               "Compare with Qwen3.6-35B-A3B NVFP4 (vLLM, thinking off) and the earlier Qwen3.8-27B FP8 run without MTP."]},
    {"id": "vllm-qwen38-27b-nvfp4-mtp-nothink-matched", **common, "profile": "standard", "context": [],
     "vllm_args": matched, "concurrency_levels": [1, 4, 8, 16], "extra_body": {"chat_template_kwargs": {"enable_thinking": False}},
     "notes": ["Same engine settings and thinking off as sweep/confirm-vllm-qwen36-nothink, for a like-for-like 27B vs 35B-A3B comparison."]},
]
ids = {e["id"] for e in q["entries"]}
q["entries"] += [e for e in new if e["id"] not in ids]
t = P + ".tmp"; json.dump(q, open(t, "w"), indent=1, ensure_ascii=False); os.replace(t, P)
print("queue entries:", len(q["entries"]))
