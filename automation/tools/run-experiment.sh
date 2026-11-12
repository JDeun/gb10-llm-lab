#!/usr/bin/env bash
# Full stage suite for one served model: capacity caps, sanity (two budgets),
# context retrieval, throughput repeats and 4-client concurrency.
# Usage: run-experiment.sh <prefix> <base-url> <alias> <manifest> <ctx-labels> [api-key-env]
#   ctx-labels: space-separated subset of "512 2k 8k 32k 60k 120k"
set -uo pipefail
P="$1"; B="$2"; M="$3"; MAN="$4"; CTX="$5"; K="${6:-}"
LAB=~/gb10-llm-lab; OUT="$LAB/local/$P"; mkdir -p "$OUT"
KEYARG=(); [ -n "$K" ] && KEYARG=(--api-key-env "$K")
bench() { python3 "$LAB/benchmarks/bench.py" run --base-url "$B" --model "$M" "${KEYARG[@]}" --manifest "$MAN" --timeout 1800 "$@"; }
log() { echo "[$(date +%H:%M:%S)] $*"; }
alive() { local h=(); [ -n "$K" ] && h=(-H "Authorization: Bearer ${!K}");
  [ "$(curl -s -m 10 -o /dev/null -w %{http_code} "${h[@]}" "$B/v1/models")" = 200 ] || { log "SERVER_DOWN before: $1"; exit 2; }; }
cd "$LAB"
for cap in 1 16 64 256; do
  alive step; log "capacity cap=$cap"; bench --prompt-file prompts/throughput_ko.txt --max-tokens "$cap" --repeats 1 --telemetry \
    --case-label "capacity-cap$cap" --output-dir "$OUT/capacity-cap$cap" >/dev/null 2>&1
done
alive step; log "sanity 512"; bench --cases-file prompts/sanity.jsonl --max-tokens 512 --repeats 1 --case-label integration-sanity-v1 --output-dir "$OUT/sanity-512" >/dev/null 2>&1
alive step; log "sanity 2048"; bench --cases-file prompts/sanity.jsonl --max-tokens 2048 --repeats 1 --case-label integration-sanity-v1-budget2048 --output-dir "$OUT/sanity-2048" >/dev/null 2>&1
for c in $CTX; do
  alive step; log "context $c"; bench --cases-file ~/llm/prompts/ctx-$c.jsonl --max-tokens 1024 --repeats 1 --telemetry \
    --case-label "context-retrieval-$c" --output-dir "$OUT/context-$c" >/dev/null 2>&1
done
for i in 1 2 3; do
  alive step; log "throughput $i"; bench --prompt-file prompts/throughput_ko.txt --max-tokens 256 --repeats 1 --telemetry \
    --case-label "throughput-256" --output-dir "$OUT/throughput-$i" >/dev/null 2>&1
done
alive step; log "concurrency 4"
for c in 1 2 3 4; do
  bench --prompt-file prompts/throughput_ko.txt --max-tokens 256 --repeats 2 --case-label "concurrency4-client$c" \
    --output-dir "$OUT/concurrency4-client$c" >/dev/null 2>&1 &
done
wait
python3 ~/llm/tools/concurrency.py --out "$OUT/concurrency4-summary.json" "$OUT"/concurrency4-client{1,2,3,4}
log "SUITE_DONE"
