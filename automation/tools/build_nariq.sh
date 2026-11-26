#!/usr/bin/env bash
# Build the Nari Labs llama.cpp fork (NariQ trellis tensor types) into ~/llm/src/nari-llama.cpp,
# then release the NariQ queue entries from hold. Nothing else is touched; a failure leaves them on hold.
set -u
export PATH=/usr/local/cuda/bin:$PATH CUDACXX=/usr/local/cuda/bin/nvcc
SRC=~/llm/src; LOG=~/llm/logs/lab-runner.log; BUILD=~/llm/logs/nari-build.log
cd "$SRC" && rm -rf nari-llama.cpp
{ git clone -q --depth 1 --branch b12431-nariv0 https://github.com/nari-labs/nari-llama.cpp.git nari-llama.cpp \
    || git clone -q --depth 1 https://github.com/nari-labs/nari-llama.cpp.git nari-llama.cpp; } >"$BUILD" 2>&1 \
  || { echo BUILD_FAIL >>"$BUILD"; echo "[nariq] clone failed (see $BUILD)" >>"$LOG"; exit 1; }
{ cd nari-llama.cpp && git log --oneline -1 \
  && cmake -B build -DGGML_CUDA=ON -DGGML_NATIVE=ON -DCMAKE_BUILD_TYPE=Release -DLLAMA_CURL=OFF \
       -DCMAKE_CUDA_ARCHITECTURES=121 -DLLAMA_BUILD_UI=OFF -DLLAMA_USE_PREBUILT_UI=OFF \
       -DCMAKE_BUILD_RPATH='$ORIGIN' -DCMAKE_SKIP_INSTALL_RPATH=ON \
  && nice -n 19 cmake --build build -j 8 --target llama-server llama-cli \
  && ./build/bin/llama-server --version 2>&1 | head -3 && echo BUILD_OK; } >>"$BUILD" 2>&1
grep -q BUILD_OK "$BUILD" || { echo "[nariq] build failed; entries stay on hold (see $BUILD)" >>"$LOG"; exit 1; }
python3 - <<'PY'
import json, os
p = os.path.expanduser("~/llm/queue.json"); q = json.load(open(p))
for e in q["entries"]:
    if e["engine"] == "nariq":
        e.pop("hold", None)
t = p + ".tmp"; json.dump(q, open(t, "w"), indent=1, ensure_ascii=False); os.replace(t, p)
PY
echo "[nariq] built $(git -C "$SRC/nari-llama.cpp" log --oneline -1); entries released at $(date +%T)" >>"$LOG"
