#!/usr/bin/env bash
# Run every minute by net-watchdog.timer (root). Escalates while the network stays down:
# 3 min: reconnect the Wi-Fi profile, 6 min: toggle the Wi-Fi radio, 9 min: restart NetworkManager,
# then repeats every 9 min. Restarts tailscaled when the LAN works but Tailscale reports offline.
set -u
STATE=/run/net-watchdog.fails
log() { logger -t net-watchdog "$*"; }
online() {
  local gw; gw=$(ip route show default | awk '{print $3; exit}')
  { [ -n "$gw" ] && ping -c 1 -W 3 "$gw" >/dev/null 2>&1; } || ping -c 1 -W 3 1.1.1.1 >/dev/null 2>&1
}
wifi_profile() {
  nmcli -t -f NAME,TYPE connection show | awk -F: '$2=="802-11-wireless"{print $1; exit}'
}
fails=$(cat "$STATE" 2>/dev/null || echo 0)
if online; then
  [ "$fails" -gt 0 ] && log "network back after ${fails} min"
  echo 0 > "$STATE"
  if ! tailscale status --peers=false >/dev/null 2>&1; then
    log "LAN up but tailscale not running; restarting tailscaled"; systemctl restart tailscaled
  fi
  exit 0
fi
fails=$((fails + 1)); echo "$fails" > "$STATE"
case $((fails % 9)) in
  3) p=$(wifi_profile); log "down ${fails} min: reconnecting '${p}'"; [ -n "$p" ] && nmcli connection up "$p" >/dev/null 2>&1 ;;
  6) log "down ${fails} min: toggling Wi-Fi radio"; nmcli radio wifi off; sleep 5; nmcli radio wifi on ;;
  0) log "down ${fails} min: restarting NetworkManager"; systemctl restart NetworkManager ;;
esac
