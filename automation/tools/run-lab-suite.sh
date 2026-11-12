#!/usr/bin/env bash
# Run the gb10-llm-lab stage-1 suite against one OpenAI-compatible server.
# Usage: run-lab-suite.sh <base-url> <model-alias> <label-prefix> [model-dir] [api-key-env]
set -uo pipefail
B="$1"; M="$2"; P="$3"; D="${4:-}"; K="${5:-}"
cd ~/gb10-llm-lab
KEYARG=(); [ -n "$K" ] && KEYARG=(--api-key-env "$K")
DIRARG=(); [ -n "$D" ] && DIRARG=(--model-dir "$D")
python3 benchmarks/bench.py run --base-url "$B" --model "$M" "${KEYARG[@]}" "${DIRARG[@]}" \
  --cases-file prompts/sanity.jsonl --max-tokens 512 --repeats 1 --manifest local/manifest.json \
  --case-label integration-sanity-v1 --output-dir "local/$P-sanity"
for i in 1 2 3; do
  python3 benchmarks/bench.py run --base-url "$B" --model "$M" "${KEYARG[@]}" \
    --prompt-file prompts/throughput_ko.txt --max-tokens 256 --repeats 1 --manifest local/manifest.json \
    --telemetry --case-label "$P-throughput-$i" --output-dir "local/$P-throughput-$i"
done
echo SUITE_DONE
