#!/usr/bin/env bash
# Install ~/llm/tools/lab_runner.next.py once the entry that is running now has finished.
# Usage: nohup ~/llm/tools/swap_runner.sh >/dev/null 2>&1 &
set -u
STATE=~/llm/queue-state.json
LOG=~/llm/logs/lab-runner.log
current=$(python3 -c "import json;s=json.load(open('$STATE'));print(next((k for k,v in s.items() if v.get('status')=='running'),''))")
if [ -n "$current" ]; then
  while [ "$(python3 -c "import json;print(json.load(open('$STATE'))['$current'].get('status'))")" = running ]; do sleep 30; done
fi
python3 -m py_compile ~/llm/tools/lab_runner.next.py || { echo "[swap] next runner does not compile; kept old" >> "$LOG"; exit 1; }
mv ~/llm/tools/lab_runner.next.py ~/llm/tools/lab_runner.py
systemctl --user restart lab-runner
echo "[swap] runner updated after ${current:-idle} at $(date +%T)" >> "$LOG"
