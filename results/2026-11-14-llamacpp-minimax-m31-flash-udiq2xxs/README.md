# 2026-11-14 · llamacpp · llamacpp-minimax-m31-flash-udiq2xxs (자동 실행)

**상태:** 실패 (`server_exited`)  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | unsloth/MiniMax-M3.1-Flash-GGUF |
| 받은 파일 | UD-IQ2_XXS/* (예상 135 GB) |
| 엔진 옵션 | `-c 32768 --cpu-moe` |
| API 별칭 | None |
| 측정 프로필 | slow |
| 공간 확보로 지운 모델 | - |

## 결과

(측정 결과 없음)


## 실패 정보

- 종류: `server_exited`
- 내용: server process ended before answering

엔진 로그 끝부분:

```
o API key is set and CORS allows all origins (see https://github.com/ggml-org/llama.cpp/pull/25655)
0.00.299.476 I srv    load_model: loading model '<user-home>/.cache/huggingface/hub/models--unsloth--MiniMax-M3.1-Flash-GGUF/snapshots/b17b7f5459c0b8f127ea12ee774409b282521d6a/UD-IQ2_XXS/MiniMax-M3.1-Flash-UD-IQ2_XXS-00001-of-00004.gguf'
0.00.492.317 E llama_model_load: error loading model: done_getting_tensors: wrong number of tensors; expected 1188, got 1176
0.00.492.330 E llama_model_load_from_file_impl: failed to load model
0.00.492.423 E common_fit_params: encountered an error while trying to fit params to free device memory: failed to load model
0.00.663.627 E llama_model_load: error loading model: done_getting_tensors: wrong number of tensors; expected 1188, got 1176
0.00.663.634 E llama_model_load_from_file_impl: failed to load model
0.00.663.641 E cmn  common_init_: failed to load model '<user-home>/.cache/huggingface/hub/models--unsloth--MiniMax-M3.1-Flash-GGUF/snapshots/b17b7f5459c0b8f127ea12ee774409b282521d6a/UD-IQ2_XXS/MiniMax-M3.1-Flash-UD-IQ2_XXS-00001-of-00004.gguf'
0.00.663.645 E srv    load_model: failed to load model, '<user-home>/.cache/huggingface/hub/models--unsloth--MiniMax-M3.1-Flash-GGUF/snapshots/b17b7f5459c0b8f127ea12ee774409b282521d6a/UD-IQ2_XXS/MiniMax-M3.1-Flash-UD-IQ2_XXS-00001-of-00004.gguf'
0.00.663.647 I srv    operator(): operator(): cleaning up before exit...
0.00.665.667 E srv  server_run_i: exiting due to model loading error

```

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
