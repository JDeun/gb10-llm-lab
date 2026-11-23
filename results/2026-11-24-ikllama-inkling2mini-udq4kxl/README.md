# 2026-11-24 · ikllama · ikllama-inkling2mini-udq4kxl (자동 실행)

**상태:** 실패 (`server_exited`)  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | ggml-org/Inkling-2-Mini-GGUF |
| 받은 파일 | Inkling-2-Mini-IQ4_NL.gguf (예상 18 GB) |
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
, "m...
llama_model_loader: - kv  56:                tokenizer.ggml.clean_spaces bool             = false
llama_model_loader: - kv  57:               general.quantization_version u32              = 2
llama_model_loader: - kv  58:                          general.file_type u32              = 25
llama_model_loader: - kv  59:                      quantize.imatrix.file str              = imatrix.gguf
llama_model_loader: - kv  60:                   quantize.imatrix.dataset str              = inkling2-loop-calibration-v6.txt
llama_model_loader: - kv  61:             quantize.imatrix.entries_count u32              = 392
llama_model_loader: - kv  62:              quantize.imatrix.chunks_count u32              = 1770
llama_model_loader: - type  f32:  478 tensors
llama_model_loader: - type q8_0:  186 tensors
llama_model_loader: - type iq4_nl:   40 tensors
llama_model_load: error loading model: error loading model architecture: unknown model architecture: 'inkling2_loop'
llama_model_load_from_file: failed to load model
llama_init_from_gpt_params: error: failed to load model '<user-home>/.cache/huggingface/hub/models--ggml-org--Inkling-2-Mini-GGUF/snapshots/e8a2cecf0e78914f07cc27b9be711a9b2c7561d9/Inkling-2-Mini-IQ4_NL.gguf'
 ERR [              load_model] unable to load model | tid="268459597478080" timestamp=1795458782 model="<user-home>/.cache/huggingface/hub/models--ggml-org--Inkling-2-Mini-GGUF/snapshots/e8a2cecf0e78914f07cc27b9be711a9b2c7561d9/Inkling-2-Mini-IQ4_NL.gguf"

```

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
