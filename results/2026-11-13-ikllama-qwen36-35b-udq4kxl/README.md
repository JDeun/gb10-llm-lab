# 2026-11-13 · ikllama · ikllama-qwen36-35b-udq4kxl (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | unsloth/Qwen3.6-35B-A3B-GGUF |
| 받은 파일 | Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf (예상 22 GB) |
| 엔진 옵션 | `-c 65536` |
| API 별칭 | ikllama-qwen36-35b-udq4kxl |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 0.29 | 0.29 | 666.36 | 1000000.0 | 3.45 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.07 | None | 140.87 | 67.45 | 52.11 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.07 | None | 131.97 | 66.18 | 64.96 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.07 | None | 135.62 | 67.1 | 62.44 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 168 | 9.77 | None | 135.8 | 66.77 | 19.21 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 168 | 7.84 | None | 136.62 | 66.74 | 24.66 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 168 | 5.89 | None | 136.27 | 66.73 | 41.0 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 168 | 11.71 | None | 139.84 | 66.76 | 16.47 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2864 | 0.49 | 1.44 | 1848.94 | 65.12 | 56.72 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44903 | 1.25 | 23.27 | 1638.89 | 50.11 | 40.18 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 763 | 0.46 | 0.49 | 1782.17 | 66.12 | 54.25 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11269 | 0.6 | 5.35 | 1887.93 | 60.88 | 53.34 | - |
| sanity-512 | 12/12 | 10 | 10/10 | 2 | 44 | 0.16 | 0.19 | 438.67 | 66.64 | 64.34 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 168 | 0.72 | 0.72 | 786.57 | 66.75 | 56.19 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 168 | 0.07 | None | 135.53 | 66.72 | 65.57 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 168 | 0.07 | None | 139.21 | 66.72 | 65.59 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 31.12, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 65.81, "per_request_e2e_tokens_per_s_median": 16.484549145425376, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
