# 2026-11-23 · llamacpp · llamacpp-inkling2mini-udq4kxl (자동 실행)

**상태:** 실패 (`server_exited`)  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | unsloth/Inkling-2-Mini-GGUF |
| 받은 파일 | Inkling-2-Mini-UD-Q4_K_XL.gguf (예상 18 GB) |
| 엔진 옵션 | `-c 65536` |
| API 별칭 | None |
| 측정 프로필 | standard |
| 공간 확보로 지운 모델 | - |

## 결과

(측정 결과 없음)


## 실패 정보

- 종류: `server_exited`
- 내용: server process ended before answering

엔진 로그 끝부분:

```
erver_setup: security: no API key is set and CORS allows all origins (see https://github.com/ggml-org/llama.cpp/pull/25655)
0.00.308.329 I srv    load_model: loading model '<user-home>/.cache/huggingface/hub/models--unsloth--Inkling-2-Mini-GGUF/snapshots/45fd08764f2b0bf16b03a5483a80e5c7aaec8772/Inkling-2-Mini-UD-Q4_K_XL.gguf'
0.00.563.508 E llama_model_load: error loading model: check_tensor_dims: tensor 'blk.24.attn_q.weight' not found
0.00.563.520 E llama_model_load_from_file_impl: failed to load model
0.00.563.551 E common_fit_params: encountered an error while trying to fit params to free device memory: failed to load model
0.00.725.466 W load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
0.00.796.311 E llama_model_load: error loading model: check_tensor_dims: tensor 'blk.24.attn_q.weight' not found
0.00.796.317 E llama_model_load_from_file_impl: failed to load model
0.00.796.324 E cmn  common_init_: failed to load model '<user-home>/.cache/huggingface/hub/models--unsloth--Inkling-2-Mini-GGUF/snapshots/45fd08764f2b0bf16b03a5483a80e5c7aaec8772/Inkling-2-Mini-UD-Q4_K_XL.gguf'
0.00.796.328 E srv    load_model: failed to load model, '<user-home>/.cache/huggingface/hub/models--unsloth--Inkling-2-Mini-GGUF/snapshots/45fd08764f2b0bf16b03a5483a80e5c7aaec8772/Inkling-2-Mini-UD-Q4_K_XL.gguf'
0.00.796.330 I srv    operator(): operator(): cleaning up before exit...
0.00.799.551 E srv  server_run_i: exiting due to model loading error

```

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
