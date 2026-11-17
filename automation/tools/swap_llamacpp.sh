#!/usr/bin/env bash
# Swap in ~/llm/src/llama.cpp-new once its build succeeded and no llama.cpp server is running,
# keep the old tree as llama.cpp-v0.9.0, then queue the entries that needed a newer llama.cpp.
set -u
SRC=~/llm/src; LOG=~/llm/logs/lab-runner.log; BUILD=~/llm/logs/llamacpp-new-build.log
until grep -qE "BUILD_OK|BUILD_FAIL" "$BUILD"; do sleep 60; done
grep -q BUILD_OK "$BUILD" || { echo "[llama.cpp swap] new build failed; kept v0.9.0" >> "$LOG"; exit 1; }
while pgrep -f "$SRC/llama.cpp/build/bin/llama-server" >/dev/null; do sleep 60; done
mv "$SRC/llama.cpp" "$SRC/llama.cpp-v0.9.0" && mv "$SRC/llama.cpp-new" "$SRC/llama.cpp"
# the binaries keep the build tree in RUNPATH (.../llama.cpp-new/build/bin): keep that path resolvable
ln -sfn "$SRC/llama.cpp" "$SRC/llama.cpp-new"
printf "llamacpp-ling-3.0-flash-q4km\nllamacpp-minimax-m31-flash-udiq2xxs\n" >> ~/llm/queue-reset.txt
echo "[llama.cpp swap] now $(git -C "$SRC/llama.cpp" log --oneline -1); Ling and MiniMax re-queued at $(date +%T)" >> "$LOG"
