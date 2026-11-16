# 2026-11-16 · strata · sweep-strata-qwen38fn-iq3s-quality (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF (IQ3_S) |
| 받은 파일 | 전체/엔진 기본 (예상 84 GB) |
| 엔진 옵션 | `--family qwen --model iq3_s --context 64k --tune skip --vision off --drafting mtp` |
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
 "concurrency4": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 1.49 | 1.49 | 180.1 | 33.4 | 0.67 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 93.8 | 51.8 | 41.41 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 79.4 | 50.8 | 49.94 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 76.9 | 59.0 | 54.78 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.13 | None | 75.1 | 19.9 | 19.75 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.48 | None | 57.7 | 20.35 | 19.67 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.37 | None | 75.3 | 20.2 | 19.68 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.22 | None | 73.6 | 20.0 | 19.7 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.64 | 0.82 | 149.3 | 72.15 | 43.67 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.75 | 0.75 | 299.8 | 51.2 | 44.74 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 75.5 | 52.0 | 51.08 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 76.1 | 52.4 | 51.5 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 26.1, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 78.48, "per_request_e2e_tokens_per_s_median": 20.091756286788307, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
