# 2026-11-12 · vllm · vllm-qwen38-27b-fp8 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | Qwen/Qwen3.8-27B-FP8 |
| 받은 파일 | 전체/엔진 기본 (예상 31 GB) |
| 엔진 옵션 | `--max-model-len 131072 --gpu-memory-utilization 0.6 --max-num-seqs 4 --reasoning-parser qwen3` |
| API 별칭 | vllm-qwen38-27b-fp8 |
| 측정 프로필 | full |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "capacity-cap1": "ok",
 "capacity-cap16": "ok",
 "capacity-cap64": "ok",
 "capacity-cap256": "ok",
 "sanity-512": "ok",
 "sanity-2048": "ok",
 "context-512": "ok",
 "context-2k": "ok",
 "context-8k": "ok",
 "context-32k": "ok",
 "context-60k": "ok",
 "throughput-1": "ok",
 "throughput-2": "ok",
 "throughput-3": "ok",
 "concurrency4": "ok",
 "vision-check": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 0.22 | None | None | None | 4.61 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.22 | None | None | None | 7.42 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.22 | None | None | None | 7.72 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.22 | None | None | None | 7.64 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.48 | None | None | None | 7.78 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.35 | None | None | None | 7.79 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.47 | None | None | None | 7.78 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.47 | None | None | None | 7.78 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 0.43 | None | None | None | 7.32 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44945 | 0.48 | None | None | None | 6.9 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 0.28 | None | None | None | 7.56 | - |
| context-60k | 3/3 | 3 | 3/3 | 0 | 82071 | 0.76 | None | None | None | 6.51 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 0.38 | None | None | None | 7.41 | - |
| sanity-2048 | 12/12 | 12 | 12/12 | 0 | 86 | 0.29 | None | None | None | 7.62 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.29 | None | None | None | 7.64 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.2 | None | None | None | 7.98 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.2 | None | None | None | 7.99 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.2 | None | None | None | 7.98 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 65.82, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 31.12, "per_request_e2e_tokens_per_s_median": 7.782758239028905, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `vision-check.json`: `{"cases": 3, "passed": 3, "errors": 0}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
