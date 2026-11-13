# 2026-11-14 · llamacpp · llamacpp-ling-3.0-flash-q4km (자동 실행)

**상태:** 실패 (`server_exited`)  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | AtomicChat/Ling-3.0-flash-GGUF |
| 받은 파일 | Q4_K_M_STOCK/* (예상 75 GB) |
| 엔진 옵션 | `-c 32768` |
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
rg/llama.cpp/pull/25655)
0.00.299.248 I srv    load_model: loading model '<user-home>/.cache/huggingface/hub/models--AtomicChat--Ling-3.0-flash-GGUF/snapshots/b0d27aaa5c1bfbc97f353fcb740b286d1de4754e/Q4_K_M_STOCK/Ling-3.0-flash-Q4_K_M_STOCK-00001-of-00002.gguf'
0.00.437.161 E llama_model_load: error loading model: check_tensor_dims: tensor 'blk.0.ssm_f_a.weight' not found
0.00.437.174 E llama_model_load_from_file_impl: failed to load model
0.00.437.202 E common_fit_params: encountered an error while trying to fit params to free device memory: failed to load model
0.00.532.860 W load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
0.00.565.155 E llama_model_load: error loading model: check_tensor_dims: tensor 'blk.0.ssm_f_a.weight' not found
0.00.565.161 E llama_model_load_from_file_impl: failed to load model
0.00.565.168 E cmn  common_init_: failed to load model '<user-home>/.cache/huggingface/hub/models--AtomicChat--Ling-3.0-flash-GGUF/snapshots/b0d27aaa5c1bfbc97f353fcb740b286d1de4754e/Q4_K_M_STOCK/Ling-3.0-flash-Q4_K_M_STOCK-00001-of-00002.gguf'
0.00.565.173 E srv    load_model: failed to load model, '<user-home>/.cache/huggingface/hub/models--AtomicChat--Ling-3.0-flash-GGUF/snapshots/b0d27aaa5c1bfbc97f353fcb740b286d1de4754e/Q4_K_M_STOCK/Ling-3.0-flash-Q4_K_M_STOCK-00001-of-00002.gguf'
0.00.565.175 I srv    operator(): operator(): cleaning up before exit...
0.00.568.338 E srv  server_run_i: exiting due to model loading error

```

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
