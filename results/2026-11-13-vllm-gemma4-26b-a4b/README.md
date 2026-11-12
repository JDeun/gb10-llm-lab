# 2026-11-13 · vllm · vllm-gemma4-26b-a4b (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | google/gemma-4-26B-A4B-it |
| 받은 파일 | 전체/엔진 기본 (예상 52 GB) |
| 엔진 옵션 | `--max-model-len 131072 --max-num-seqs 4 --gpu-memory-utilization 0.7` |
| API 별칭 | vllm-gemma4-26b-a4b |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 177 | 0.88 | None | None | None | 1.14 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 177 | 0.11 | None | None | None | 22.18 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 177 | 0.11 | None | None | None | 24.45 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 177 | 0.11 | None | None | None | 24.06 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 177 | 0.2 | None | None | None | 22.71 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 177 | 0.2 | None | None | None | 22.71 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 177 | 0.22 | None | None | None | 22.67 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 177 | 0.15 | None | None | None | 22.75 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2897 | 0.85 | None | None | None | 6.88 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 45250 | 19.03 | None | None | None | 0.46 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 773 | 0.16 | None | None | None | 18.07 | - |
| context-60k | 3/3 | 3 | 3/3 | 0 | 82574 | 48.44 | None | None | None | 0.2 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11327 | 0.17 | None | None | None | 17.53 | - |
| sanity-2048 | 12/12 | 12 | 11/12 | 0 | 48 | 0.13 | None | None | None | 16.01 | - |
| sanity-512 | 12/12 | 12 | 11/12 | 0 | 48 | 0.17 | None | None | None | 14.43 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 177 | 0.11 | None | None | None | 24.2 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 177 | 0.11 | None | None | None | 24.25 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 177 | 0.11 | None | None | None | 24.27 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 22.6, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 90.61, "per_request_e2e_tokens_per_s_median": 22.685759664142022, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `vision-check.json`: `{"cases": 3, "passed": 3, "errors": 0}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
