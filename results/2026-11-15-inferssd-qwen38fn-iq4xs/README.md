# 2026-11-15 · inferssd · inferssd-qwen38fn-iq4xs (자동 실행)

**상태:** 실패 (`server_exited`)  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | bartowski/Qwen3.8-Flash-Next-GGUF |
| 받은 파일 | 전체/엔진 기본 (예상 100 GB) |
| 엔진 옵션 | `` |
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
b8 in ggml_backend_cpu_graph_compute(ggml_backend*, ggml_cgraph*) () from <user-home>/.local/share/inferssd/releases/source.ws3vVcGZ/source/build-linux-cuda/bin/libggml-cpu.so.0
#7  0x0000ed8e358d7e78 in ggml_backend_sched_graph_compute_async () from <user-home>/.local/share/inferssd/releases/source.ws3vVcGZ/source/build-linux-cuda/bin/libggml-base.so.0
#8  0x0000ed8e35a602ac in llama_context::graph_compute(ggml_cgraph*, bool, llama_memory_context_i*) () from <user-home>/.local/share/inferssd/releases/source.ws3vVcGZ/source/build-linux-cuda/bin/libllama.so.0
#9  0x0000ed8e35a6aec8 in llama_context::process_ubatch(llama_ubatch const&, llm_graph_type, llama_memory_context_i*, ggml_status&) () from <user-home>/.local/share/inferssd/releases/source.ws3vVcGZ/source/build-linux-cuda/bin/libllama.so.0
#10 0x0000ed8e35a6c3f0 in llama_context::decode(llama_batch const&) () from <user-home>/.local/share/inferssd/releases/source.ws3vVcGZ/source/build-linux-cuda/bin/libllama.so.0
#11 0x0000ed8e35a6e6b4 in llama_decode () from <user-home>/.local/share/inferssd/releases/source.ws3vVcGZ/source/build-linux-cuda/bin/libllama.so.0
#12 0x0000ed8e35f789b0 in common_context_can_seq_rm(llama_context*) () from <user-home>/.local/share/inferssd/releases/source.ws3vVcGZ/source/build-linux-cuda/bin/libllama-common.so.0
#13 0x0000c7ac29605608 in server_context_impl::load_model(common_params&) ()
#14 0x0000c7ac2954a604 in main ()
[Inferior 1 (process 914047) detached]

```

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
