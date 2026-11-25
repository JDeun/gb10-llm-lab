#!/usr/bin/env bash
# One-time install on the GB10:  sudo bash ~/llm/netwatch/install.sh
set -euo pipefail
[ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
D=$(cd "$(dirname "$0")" && pwd)
install -m 755 "$D/net-watchdog.sh" /usr/local/sbin/net-watchdog.sh
install -m 644 "$D/net-watchdog.service" "$D/net-watchdog.timer" /etc/systemd/system/
systemctl daemon-reload
systemctl enable --now net-watchdog.timer
systemctl list-timers net-watchdog.timer --no-pager
echo "installed; logs: journalctl -t net-watchdog"
