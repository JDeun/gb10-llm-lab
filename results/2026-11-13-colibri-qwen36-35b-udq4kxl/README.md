# 2026-11-13 · colibri · colibri-qwen36-35b-udq4kxl (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | unsloth/Qwen3.6-35B-A3B-GGUF |
| 받은 파일 | Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf (예상 22 GB) |
| 엔진 옵션 | `` |
| API 별칭 | colibri-qwen36-35b-udq4kxl |
| 측정 프로필 | standard |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "capacity-cap1": "ok",
 "capacity-cap16": "ok",
 "capacity-cap64": "ok",
 "capacity-cap256": "ok",
 "sanity-512": "ok",
 "context-512": "ok",
 "context-2k": "ok",
 "context-8k": "ok",
 "context-32k": "ok",
 "throughput-1": "ok",
 "throughput-2": "ok",
 "throughput-3": "ok",
 "concurrency4": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 170 | 0.22 | None | None | None | 4.5 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 170 | 0.17 | None | None | None | 20.25 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 170 | 0.23 | None | None | None | 26.57 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 170 | 0.21 | None | None | None | 24.56 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 170 | 19.32 | None | None | None | 9.93 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 170 | 15.76 | None | None | None | 12.5 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 170 | 22.79 | None | None | None | 8.79 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 170 | 12.22 | None | None | None | 20.26 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2866 | 4.27 | None | None | None | 1.34 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44905 | 91.17 | None | None | None | 0.07 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 765 | 1.22 | None | None | None | 4.71 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11271 | 16.14 | None | None | None | 0.43 | - |
| sanity-512 | 12/12 | 12 | 11/12 | 0 | 46 | 0.19 | None | None | None | 9.43 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 170 | 0.62 | None | None | None | 28.73 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 170 | 0.57 | None | None | None | 29.12 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 170 | 0.64 | None | None | None | 30.47 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 58.53, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 34.99, "per_request_e2e_tokens_per_s_median": 9.364941214497739, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
