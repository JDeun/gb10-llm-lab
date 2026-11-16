# 2026-11-16 · strata · sweep-strata-qwen38fn-iq3s-kvq4 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF (IQ3_S) |
| 받은 파일 | 전체/엔진 기본 (예상 84 GB) |
| 엔진 옵션 | `--family qwen --model iq3_s --context 64k --tune skip --vision off --drafting mtp --kv q4_0` |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 1.47 | 1.47 | 150.0 | 23.2 | 0.68 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 62.8 | 76.6 | 50.71 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 75.4 | 53.6 | 52.63 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 76.3 | 45.8 | 43.22 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.13 | None | 78.4 | 20.3 | 20.12 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.39 | None | 74.6 | 20.65 | 20.03 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.24 | None | 74.2 | 20.4 | 20.07 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.47 | None | 71.5 | 20.7 | 20.01 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.63 | 0.82 | 146.0 | 66.9 | 45.05 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.74 | 0.74 | 302.9 | 54.4 | 47.23 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 70.9 | 53.8 | 52.83 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 76.9 | 53.7 | 52.79 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 25.62, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 79.95, "per_request_e2e_tokens_per_s_median": 20.080701427300905, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
