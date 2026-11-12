#!/usr/bin/env bash
# Sustained-load test: N parallel clients loop the 256-token throughput prompt for DURATION seconds,
# while GPU temperature/power/clock and memory are sampled every 10 s.
# Usage: soak.sh <prefix> <base-url> <alias> <manifest> <duration-s> <clients> [api-key-env]
set -uo pipefail
P="$1"; B="$2"; M="$3"; MAN="$4"; DUR="$5"; N="$6"; K="${7:-}"
LAB=~/gb10-llm-lab; OUT="$LAB/local/$P"; mkdir -p "$OUT"
KEYARG=(); [ -n "$K" ] && KEYARG=(--api-key-env "$K")
END=$(( $(date +%s) + DUR ))
sample() {
  echo "utc,gpu_temp_c,power_w,sm_clock_mhz,util_pct,mem_available_kib" > "$OUT/hw.csv"
  while [ "$(date +%s)" -lt "$END" ]; do
    g=$(nvidia-smi --query-gpu=temperature.gpu,power.draw,clocks.sm,utilization.gpu --format=csv,noheader,nounits | tr -d " ")
    m=$(awk '/MemAvailable/{print $2}' /proc/meminfo)
    echo "$(date -u +%FT%TZ),$g,$m" >> "$OUT/hw.csv"; sleep 10
  done
}
client() {
  local c=$1 i=0
  while [ "$(date +%s)" -lt "$END" ]; do
    i=$((i+1))
    python3 "$LAB/benchmarks/bench.py" run --base-url "$B" --model "$M" "${KEYARG[@]}" --manifest "$MAN" \
      --prompt-file "$LAB/prompts/throughput_ko.txt" --max-tokens 256 --repeats 1 --timeout 600 \
      --case-label "soak-c$c" --output-dir "$OUT/c$c-$(printf %04d $i)" >/dev/null 2>&1
  done
}
sample & SP=$!
for c in $(seq 1 "$N"); do client "$c" & done
wait
echo SOAK_DONE
