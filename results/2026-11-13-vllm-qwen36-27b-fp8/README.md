# 2026-11-13 · vllm · vllm-qwen36-27b-fp8 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | Qwen/Qwen3.6-27B-FP8 |
| 받은 파일 | 전체/엔진 기본 (예상 31 GB) |
| 엔진 옵션 | `--max-model-len 131072 --max-num-seqs 4 --gpu-memory-utilization 0.6 --reasoning-parser qwen3` |
| API 별칭 | vllm-qwen36-27b-fp8 |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 0.2 | None | None | None | 5.09 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.19 | None | None | None | 7.8 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.19 | None | None | None | 8.03 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.19 | None | None | None | 7.99 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 168 | 0.4 | None | None | None | 7.8 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 168 | 0.43 | None | None | None | 7.79 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 168 | 0.42 | None | None | None | 7.8 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 168 | 0.33 | None | None | None | 7.81 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2864 | 0.38 | None | None | None | 7.86 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44903 | 0.4 | None | None | None | 7.23 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 763 | 0.44 | None | None | None | 7.87 | - |
| context-60k | 3/3 | 3 | 3/3 | 0 | 82029 | 0.68 | None | None | None | 6.68 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11269 | 0.35 | None | None | None | 7.64 | - |
| sanity-2048 | 12/12 | 12 | 12/12 | 0 | 44 | 0.27 | None | None | None | 7.98 | - |
| sanity-512 | 12/12 | 10 | 10/10 | 2 | 44 | 0.27 | None | None | None | 8.0 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 168 | 0.19 | None | None | None | 7.99 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 168 | 0.19 | None | None | None | 7.99 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 168 | 0.19 | None | None | None | 7.99 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 65.71, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 31.17, "per_request_e2e_tokens_per_s_median": 7.79575041199785, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `vision-check.json`: `{"cases": 3, "passed": 3, "errors": 0}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
