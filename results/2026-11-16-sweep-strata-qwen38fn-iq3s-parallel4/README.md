# 2026-11-16 · strata · sweep-strata-qwen38fn-iq3s-parallel4 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF (IQ3_S) |
| 받은 파일 | 전체/엔진 기본 (예상 84 GB) |
| 엔진 옵션 | `--family qwen --model iq3_s --context 64k --tune skip --vision off --drafting mtp --parallel 4` |
| API 별칭 | qwen3.8-flash-next-iq3_s |
| 측정 프로필 | standard |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "capacity-cap1": "ok",
 "capacity-cap16": "ok",
 "capacity-cap64": "ok",
 "capacity-cap256": "ok",
 "sanity-512": "ok",
 "throughput-1": "ok",
 "throughput-2": "ok",
 "throughput-3": "ok",
 "concurrency1": "ok",
 "concurrency4": "ok",
 "concurrency8": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 1.55 | 1.55 | 141.4 | 22.8 | 0.65 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 91.2 | 74.0 | 55.29 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 76.5 | 48.3 | 47.57 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 68.4 | 51.9 | 48.31 | - |
| concurrency1-client1 | 2/2 | 0 | - | 2 | 210 | 0.11 | None | 74.4 | 48.9 | 48.13 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.14 | None | 72.8 | 19.1 | 18.94 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.22 | None | 71.8 | 19.2 | 18.91 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.35 | None | 75.6 | 19.35 | 18.9 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.54 | None | 69.5 | 19.55 | 18.91 | - |
| concurrency8-client1 | 2/2 | 0 | - | 2 | 210 | 12.99 | None | 72.2 | 20.1 | 9.96 | - |
| concurrency8-client2 | 2/2 | 0 | - | 2 | 210 | 0.31 | None | 70.6 | 20.15 | 19.73 | - |
| concurrency8-client3 | 2/2 | 0 | - | 2 | 210 | 6.72 | None | 72.2 | 20.15 | 14.77 | - |
| concurrency8-client4 | 2/2 | 0 | - | 2 | 210 | 6.75 | None | 70.2 | 20.15 | 14.79 | - |
| concurrency8-client5 | 2/2 | 0 | - | 2 | 210 | 13.24 | None | 70.4 | 20.35 | 9.93 | - |
| concurrency8-client6 | 2/2 | 0 | - | 2 | 210 | 13.14 | None | 74.3 | 20.25 | 13.22 | - |
| concurrency8-client7 | 2/2 | 0 | - | 2 | 210 | 6.86 | None | 73.6 | 20.2 | 14.66 | - |
| concurrency8-client8 | 2/2 | 0 | - | 2 | 210 | 13.13 | None | 71.3 | 20.3 | 9.96 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.63 | 0.83 | 150.6 | 70.55 | 46.45 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.76 | 0.76 | 295.0 | 49.1 | 43.09 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 74.9 | 49.1 | 48.29 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 70.0 | 48.8 | 47.93 | - |

- `concurrency1-summary.json`: `{"clients": 1, "requests": 2, "errors": 0, "wall_s": 10.64, "completion_tokens_total": 512, "aggregate_completion_tokens_per_s": 48.13, "per_request_e2e_tokens_per_s_median": 48.151624324329674, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 27.27, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 75.09, "per_request_e2e_tokens_per_s_median": 19.954620587776745, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `concurrency8-summary.json`: `{"clients": 8, "requests": 16, "errors": 0, "wall_s": 51.58, "completion_tokens_total": 4096, "aggregate_completion_tokens_per_s": 79.41, "per_request_e2e_tokens_per_s_median": 10.037741841109211, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
