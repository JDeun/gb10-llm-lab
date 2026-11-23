# 2026-11-23 · ikllama · ikllama-inkling2mini-udq4kxl (자동 실행)

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
plate str              = {%- set effort_map = {"none": 0.0, "m...
llama_model_loader: - kv  56:                           general.basename str              = Inkling-2-Mini
llama_model_loader: - kv  57:            tokenizer.ggml.padding_token_id u32              = 199999
llama_model_loader: - kv  58:                      general.sampling.temp f32              = 1.000000
llama_model_loader: - kv  59:                     general.sampling.top_k i32              = 0
llama_model_loader: - kv  60:                     general.sampling.top_p f32              = 1.000000
llama_model_loader: - kv  61:                     general.sampling.min_p f32              = 0.000000
llama_model_loader: - type  f32:  468 tensors
llama_model_loader: - type q8_0:  154 tensors
llama_model_loader: - type bf16:   32 tensors
llama_model_loader: - type nvfp4_ks:   40 tensors
llama_model_load: error loading model: error loading model architecture: unknown model architecture: 'inkling2'
llama_model_load_from_file: failed to load model
llama_init_from_gpt_params: error: failed to load model '<user-home>/.cache/huggingface/hub/models--unsloth--Inkling-2-Mini-GGUF/snapshots/45fd08764f2b0bf16b03a5483a80e5c7aaec8772/Inkling-2-Mini-UD-Q4_K_XL.gguf'
 ERR [              load_model] unable to load model | tid="270821054003392" timestamp=1795398174 model="<user-home>/.cache/huggingface/hub/models--unsloth--Inkling-2-Mini-GGUF/snapshots/45fd08764f2b0bf16b03a5483a80e5c7aaec8772/Inkling-2-Mini-UD-Q4_K_XL.gguf"

```

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
