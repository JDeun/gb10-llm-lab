# 2026-11-15 · llamacpp · llamacpp-kr-ax-k2-iq4xs (자동 실행)

**상태:** 실패 (`server_exited`)  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | skt/A.X-K2-GGUF |
| 받은 파일 | A.X-K2-IQ4_XS.gguf (예상 370 GB) |
| 엔진 옵션 | `-c 8192 --cpu-moe` |
| API 별칭 | None |
| 측정 프로필 | capacity |
| 공간 확보로 지운 모델 | - |

## 결과

(측정 결과 없음)


## 실패 정보

- 종류: `server_exited`
- 내용: server process ended before answering

엔진 로그 끝부분:

```
0.00.344.167 I srv  llama_server: initializing ...
0.00.344.187 I cmn  common_param: common_params_print_info: verbosity = 3 (adjust with the `-lv N` CLI arg)
0.00.347.969 W srv  server_setup: security: no API key is set and CORS allows all origins (see https://github.com/ggml-org/llama.cpp/pull/25655)
0.00.350.883 I srv    load_model: loading model '<user-home>/.cache/huggingface/hub/models--skt--A.X-K2-GGUF/snapshots/712a9f2aa123a54964a18e418fd8ab0b39f7759e/A.X-K2-IQ4_XS.gguf'
0.00.405.851 E llama_model_load: error loading model: unknown model architecture: 'axk2'
0.00.405.861 E llama_model_load_from_file_impl: failed to load model
0.00.406.491 E common_fit_params: encountered an error while trying to fit params to free device memory: failed to load model
0.00.440.007 E llama_model_load: error loading model: unknown model architecture: 'axk2'
0.00.440.012 E llama_model_load_from_file_impl: failed to load model
0.00.440.018 E cmn  common_init_: failed to load model '<user-home>/.cache/huggingface/hub/models--skt--A.X-K2-GGUF/snapshots/712a9f2aa123a54964a18e418fd8ab0b39f7759e/A.X-K2-IQ4_XS.gguf'
0.00.440.022 E srv    load_model: failed to load model, '<user-home>/.cache/huggingface/hub/models--skt--A.X-K2-GGUF/snapshots/712a9f2aa123a54964a18e418fd8ab0b39f7759e/A.X-K2-IQ4_XS.gguf'
0.00.440.023 I srv    operator(): operator(): cleaning up before exit...
0.00.442.832 E srv  server_run_i: exiting due to model loading error

```

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
