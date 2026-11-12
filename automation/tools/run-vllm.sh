#!/usr/bin/env bash
# Qwen3.6-35B-A3B NVFP4 on vLLM, exposed only on the Tailscale IP.
set -euo pipefail
# host-specific values (TS_IP=...) live in ~/llm/host.env, which is not committed
[ -f "$HOME/llm/host.env" ] && . "$HOME/llm/host.env"
TS_IP="${TS_IP:?set TS_IP in ~/llm/host.env}"
IMAGE="${IMAGE:-vllm/vllm-openai:v0.32.0}"
NAME=vllm-qwen36

docker rm -f "$NAME" >/dev/null 2>&1 || true
docker run -d --name "$NAME" \
  --restart no \
  --gpus all --ipc=host \
  --env-file "$HOME/llm/vllm.env" \
  -v "$HOME/.cache/huggingface:/root/.cache/huggingface" \
  -p "${TS_IP}:8000:8000" \
  "$IMAGE" \
  nvidia/Qwen3.6-35B-A3B-NVFP4 \
  --served-model-name qwen3.6-35b-a3b \
  --host 0.0.0.0 --port 8000 \
  --tensor-parallel-size 1 \
  --trust-remote-code \
  --kv-cache-dtype fp8 \
  --attention-backend flashinfer \
  --moe-backend marlin \
  --gpu-memory-utilization 0.4 \
  --max-model-len 262144 \
  --max-num-seqs 4 \
  --max-num-batched-tokens 8192 \
  --enable-chunked-prefill \
  --async-scheduling \
  --enable-prefix-caching \
  --speculative-config '{"method":"mtp","num_speculative_tokens":3,"moe_backend":"triton"}' \
  --reasoning-parser qwen3 \
  --tool-call-parser qwen3_xml \
  --enable-auto-tool-choice
