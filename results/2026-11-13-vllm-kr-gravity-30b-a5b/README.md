# 2026-11-13 · vllm · vllm-kr-gravity-30b-a5b (자동 실행)

**상태:** 실패 (`server_exited`)  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | trillionlabs/Gravity-30B-A5B-Preview |
| 받은 파일 | 전체/엔진 기본 (예상 59 GB) |
| 엔진 옵션 | `--max-model-len 131072 --max-num-seqs 4 --gpu-memory-utilization 0.75 --trust-remote-code` |
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
nc_llm.py", line 255, in from_vllm_config
    return cls(
           ^^^^
  File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/async_llm.py", line 184, in __init__
    self.engine_core = EngineCoreClient.make_async_mp_client(
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 175, in sync_wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core_client.py", line 167, in make_async_mp_client
    return AsyncMPClient(
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
