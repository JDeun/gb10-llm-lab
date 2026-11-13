# 2026-11-13 · vllm · vllm-kr-hyperclovax-seed-think-32b-transformers-impl (자동 실행)

**상태:** 실패 (`server_exited`)  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | naver-hyperclovax/HyperCLOVAX-SEED-Think-32B |
| 받은 파일 | 전체/엔진 기본 (예상 67 GB) |
| 엔진 옵션 | `--max-model-len 131072 --max-num-seqs 4 --gpu-memory-utilization 0.8 --trust-remote-code --reasoning-parser deepseek_r1 --model-impl transformers` |
| API 별칭 | None |
| 측정 프로필 | full |
| 공간 확보로 지운 모델 | - |

## 결과

(측정 결과 없음)


## 실패 정보

- 종류: `server_exited`
- 내용: server process ended before answering

엔진 로그 끝부분:

```
ast one request with the model's max seq len (131072), (36.0 GiB KV cache is needed, which is larger than the available KV cache memory (34.66 GiB). Based on the available memory, the estimated maximum model length is 126176. Try increasing `gpu_memory_utilization` (which also controls CPU memory on the CPU backend) or decreasing `max_model_len` when initializing the engine. See https://docs.vllm.ai/en/latest/configuration/conserving_memory/ for more details.
    raise RuntimeError(
RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
--- last lines ---
           ^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 175, in sync_wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core_client.py", line 1120, in __init__
    super().__init__(
  File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core_client.py", line 682, in __init__
    with launch_core_engines(
  File "/usr/lib/python3.12/contextlib.py", line 144, in __exit__
    next(self.gen)
  File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/utils.py", line 1351, in launch_core_engines
    wait_for_engine_startup(
  File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/utils.py", line 1431, in wait_for_engine_startup
    raise RuntimeError(
RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
```

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
