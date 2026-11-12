#!/usr/bin/env bash
# One-time admin settings for running GB10 as an always-on LLM server.
# Run on the GB10:  sudo bash ~/llm/admin-setup.sh
# Every change is printed; nothing is removed or installed.
set -euo pipefail
[ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }

echo "1) Wi-Fi power save off for the active Wi-Fi connection (reduces SSH/API drops)"
WIFI=$(nmcli -t -f NAME,TYPE connection show --active | awk -F: '$2=="802-11-wireless"{print $1; exit}')
if [ -n "$WIFI" ]; then
  nmcli connection modify "$WIFI" 802-11-wireless.powersave 2
  echo "   set powersave=disable on '$WIFI' (applies on next reconnect; 'nmcli connection up \"$WIFI\"' applies now but drops the link briefly)"
fi

echo "2) Snap refresh only in a weekly window: Sunday 04:00-05:00"
snap set system refresh.timer=sun,04:00-05:00
snap get system refresh.timer

echo "3) apt: keep downloading package lists, never install or reboot automatically"
cat > /etc/apt/apt.conf.d/99-gb10-llm-server <<'CONF'
// GB10 LLM server: updates are applied by hand (DGX Dashboard or apt) in a chosen window.
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Unattended-Upgrade "0";
Unattended-Upgrade::Automatic-Reboot "false";
CONF
echo "   wrote /etc/apt/apt.conf.d/99-gb10-llm-server"

echo "Done. Recommended: apply DGX Dashboard / apt updates by hand on Sunday 04:00-05:00;"
echo "the llm-serve user service starts the default server again after the reboot."
