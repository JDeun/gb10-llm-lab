#!/usr/bin/env bash
# Bring up the default LLM server chosen in ~/llm/serve-mode (vllm | strata | none).
# Usage: serve-default.sh start   -> boot-time start (waits for the Tailscale IP)
#        serve-default.sh check   -> health check; restarts the server if it stopped answering
set -uo pipefail
MODE_FILE="$HOME/llm/serve-mode"
# host-specific values (TS_IP=...) live in ~/llm/host.env, which is not committed
[ -f "$HOME/llm/host.env" ] && . "$HOME/llm/host.env"
TS_IP="${TS_IP:?set TS_IP in ~/llm/host.env}"
STRATA_PRESET="gb10-default"
export PATH="$HOME/.local/bin:/usr/bin:/bin"

mode() { tr -d '[:space:]' < "$MODE_FILE" 2>/dev/null || echo none; }
log() { echo "[serve-default] $*"; }

wait_for_tailscale() {
  for _ in $(seq 1 60); do
    ip -4 addr show tailscale0 2>/dev/null | grep -q "$TS_IP" && return 0
    sleep 5
  done
  log "Tailscale IP $TS_IP not up after 5 min"; return 1
}

vllm_ok() {
  local key; key=$(sed -n 's/^VLLM_API_KEY=//p' "$HOME/llm/vllm.env")
  [ "$(curl -s -m 10 -o /dev/null -w '%{http_code}' -H "Authorization: Bearer $key" "http://$TS_IP:8000/v1/models")" = 200 ]
}
strata_ok() { [ "$(curl -s -m 10 -o /dev/null -w '%{http_code}' "http://$TS_IP:8080/v1/models")" = 200 ]; }

start_vllm() {
  if docker inspect vllm-qwen36 >/dev/null 2>&1; then docker start vllm-qwen36 >/dev/null; else "$HOME/llm/run-vllm.sh" >/dev/null; fi
  log "vllm container started"
}
start_strata() { strata launch --preset "$STRATA_PRESET" --no-tui --yes >/dev/null 2>&1 && log "strata preset $STRATA_PRESET started"; }

case "${1:-start}:$(mode)" in
  *:none) log "mode none (experiments) - nothing to do" ;;
  start:vllm) wait_for_tailscale && start_vllm ;;
  start:strata) wait_for_tailscale && start_strata ;;
  check:vllm) vllm_ok || { log "vllm not answering - restarting"; wait_for_tailscale && docker restart vllm-qwen36 >/dev/null; } ;;
  check:strata) strata_ok || { log "strata not answering - restarting"; wait_for_tailscale && start_strata; } ;;
  *) log "unknown mode '$(mode)' or action '${1:-}'"; exit 1 ;;
esac
