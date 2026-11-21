#!/usr/bin/env bash
# Build latest llama.cpp master in llama.cpp-next ($ORIGIN rpath), swap it in when no llama-server runs,
# keep the old tree as llama.cpp-9fba51d, then release the Inkling GGUF entries from hold.
set -u
export PATH=/usr/local/cuda/bin:$PATH CUDACXX=/usr/local/cuda/bin/nvcc
SRC=~/llm/src; LOG=~/llm/logs/lab-runner.log; BUILD=~/llm/logs/llamacpp-next-build.log
cd "$SRC" && rm -rf llama.cpp-next
{ git clone -q --local llama.cpp llama.cpp-next && cd llama.cpp-next \
  && git remote set-url origin https://github.com/ggml-org/llama.cpp.git && git fetch -q origin master \
  && git checkout -q -B master origin/master && git log --oneline -1 \
  && grep -rqi inkling src/ && echo "inkling support present" \
  && cmake -B build -DGGML_CUDA=ON -DGGML_NATIVE=ON -DCMAKE_BUILD_TYPE=Release -DLLAMA_CURL=OFF \
       -DCMAKE_BUILD_RPATH='$ORIGIN' -DCMAKE_SKIP_INSTALL_RPATH=ON >/dev/null \
  && cmake --build build -j 10 --target llama-server llama-cli llama-bench >/dev/null \
  && ldd build/bin/llama-server | grep -q "llama.cpp-next/build/bin/libllama" && echo BUILD_OK; } >"$BUILD" 2>&1 \
  || { echo BUILD_FAIL >>"$BUILD"; echo "[llama.cpp update] build failed; kept 9fba51d (see $BUILD)" >>"$LOG"; exit 1; }
grep -q BUILD_OK "$BUILD" || { echo "[llama.cpp update] build check failed; kept 9fba51d" >>"$LOG"; exit 1; }
while pgrep -f "[l]lama.cpp/build/bin/llama-server|[l]lama.cpp-new/build/bin/llama-server" >/dev/null; do sleep 60; done
cd "$SRC" && mv llama.cpp llama.cpp-9fba51d && mv llama.cpp-next llama.cpp
python3 - <<'PY'
import json, os
p = os.path.expanduser("~/llm/queue.json"); q = json.load(open(p))
for e in q["entries"]:
    if e["id"] in ("llamacpp-inkling2mini-udq4kxl", "ikllama-inkling2mini-udq4kxl", "inferssd-inkling2mini-udq4kxl"):
        e.pop("hold", None)
t = p + ".tmp"; json.dump(q, open(t, "w"), indent=1, ensure_ascii=False); os.replace(t, p)
PY
echo "[llama.cpp update] now $(git -C "$SRC/llama.cpp" log --oneline -1); Inkling GGUF entries released at $(date +%T)" >>"$LOG"
