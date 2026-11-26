#!/usr/bin/env bash
# Serve one model for an external evaluation (lm-eval-harness KMMLU cross-check), then restore the runner.
# Usage: crosscheck_serve.sh start | stop
# It waits for the entry that is running now to finish, so no measurement is cut short.
set -u
LOG=~/llm/logs/lab-runner.log
STATE=~/llm/queue-state.json
MODEL=nvidia/Qwen3.6-35B-A3B-NVFP4
ALIAS=crosscheck
case "${1:-start}" in
start)
  current=$(python3 -c "import json;s=json.load(open('$STATE'));r=[(v.get('started',''),k) for k,v in s.items() if v.get('status')=='running'];print(max(r)[1] if r else '')")
  if [ -n "$current" ]; then
    echo "[crosscheck] waiting for $current" >> "$LOG"
    while [ "$(python3 -c "import json;print(json.load(open('$STATE'))['$current'].get('status'))")" = running ]; do sleep 60; done
  fi
  systemctl --user stop lab-runner
  sleep 5
  docker rm -f lab-vllm 2>/dev/null
  "$HOME/.local/bin/uvx" --from "huggingface_hub[hf_xet]" hf download "$MODEL" >/dev/null 2>&1
  docker run -d --name lab-vllm --gpus all --ipc=host --memory 108g --memory-swap 112g \
    -v "$HOME/.cache/huggingface:/root/.cache/huggingface" -p 127.0.0.1:8001:8000 \
    vllm/vllm-openai:v0.32.0 "$MODEL" --served-model-name "$ALIAS" --host 0.0.0.0 --port 8000 \
    --max-model-len 65536 --trust-remote-code --kv-cache-dtype fp8 --attention-backend flashinfer \
    --moe-backend marlin --gpu-memory-utilization 0.6 --max-num-seqs 16 --max-num-batched-tokens 8192 \
    --enable-chunked-prefill --async-scheduling --enable-prefix-caching --reasoning-parser qwen3 \
    --speculative-config '{"method":"mtp","num_speculative_tokens":3,"moe_backend":"triton"}' \
    --enable-auto-tool-choice --tool-call-parser qwen3_xml >/dev/null
  for _ in $(seq 1 120); do
    curl -sf http://127.0.0.1:8001/health >/dev/null && { echo "[crosscheck] serving $MODEL on 8001" >> "$LOG"; echo READY; exit 0; }
    sleep 15
  done
  echo "[crosscheck] server did not become ready" >> "$LOG"; echo NOTREADY; exit 1 ;;
stop)
  docker rm -f lab-vllm >/dev/null 2>&1
  systemctl --user start lab-runner
  echo "[crosscheck] server stopped, runner resumed" >> "$LOG"; echo RESUMED ;;
esac
