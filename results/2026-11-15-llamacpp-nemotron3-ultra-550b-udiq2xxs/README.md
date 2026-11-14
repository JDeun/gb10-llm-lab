# 2026-11-15 · llamacpp · llamacpp-nemotron3-ultra-550b-udiq2xxs (자동 실행)

**상태:** 실패 (`server_exited`)  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | unsloth/NVIDIA-Nemotron-3-Ultra-550B-A55B-GGUF |
| 받은 파일 | UD-IQ2_XXS/* (예상 194 GB) |
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
0.00.327.957 I srv  llama_server: initializing ...
0.00.327.969 I cmn  common_param: common_params_print_info: verbosity = 3 (adjust with the `-lv N` CLI arg)
0.00.329.718 W srv  server_setup: security: no API key is set and CORS allows all origins (see https://github.com/ggml-org/llama.cpp/pull/25655)
0.00.332.076 I srv    load_model: loading model '<user-home>/.cache/huggingface/hub/models--unsloth--NVIDIA-Nemotron-3-Ultra-550B-A55B-GGUF/snapshots/2fb7d5b3f4eae7aedb18b4839b6a6300111e46f6/UD-IQ2_XXS/NVIDIA-Nemotron-3-Ultra-550B-A55B-UD-IQ2_XXS-00001-of-00005.gguf'

```

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
