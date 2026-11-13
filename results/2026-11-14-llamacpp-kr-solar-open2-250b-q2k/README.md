# 2026-11-14 · llamacpp · llamacpp-kr-solar-open2-250b-q2k (자동 실행)

**상태:** 실패 (`server_exited`)  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | prometheusAIR/Solar-Open2-250B-GGUF |
| 받은 파일 | Q2_K/* (예상 95 GB) |
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
sity = 3 (adjust with the `-lv N` CLI arg)
0.00.288.180 W srv  server_setup: security: no API key is set and CORS allows all origins (see https://github.com/ggml-org/llama.cpp/pull/25655)
0.00.290.272 I srv    load_model: loading model '<user-home>/.cache/huggingface/hub/models--prometheusAIR--Solar-Open2-250B-GGUF/snapshots/9b867c45474d13b73d927cdcee412b0ff6459feb/Q2_K/Solar-Open2-250B-Q2_K-00001-of-00003.gguf'
0.00.333.732 E llama_model_load: error loading model: unknown model architecture: 'solar-open2'
0.00.333.740 E llama_model_load_from_file_impl: failed to load model
0.00.333.769 E common_fit_params: encountered an error while trying to fit params to free device memory: failed to load model
0.00.367.125 E llama_model_load: error loading model: unknown model architecture: 'solar-open2'
0.00.367.142 E llama_model_load_from_file_impl: failed to load model
0.00.367.146 E cmn  common_init_: failed to load model '<user-home>/.cache/huggingface/hub/models--prometheusAIR--Solar-Open2-250B-GGUF/snapshots/9b867c45474d13b73d927cdcee412b0ff6459feb/Q2_K/Solar-Open2-250B-Q2_K-00001-of-00003.gguf'
0.00.367.150 E srv    load_model: failed to load model, '<user-home>/.cache/huggingface/hub/models--prometheusAIR--Solar-Open2-250B-GGUF/snapshots/9b867c45474d13b73d927cdcee412b0ff6459feb/Q2_K/Solar-Open2-250B-Q2_K-00001-of-00003.gguf'
0.00.367.151 I srv    operator(): operator(): cleaning up before exit...
0.00.370.287 E srv  server_run_i: exiting due to model loading error

```

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
