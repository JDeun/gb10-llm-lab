# 2026-11-16 · strata · sweep-strata-qwen38fn-iq3s-dflash2 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF (IQ3_S) |
| 받은 파일 | 전체/엔진 기본 (예상 84 GB) |
| 엔진 옵션 | `--family qwen --model iq3_s --context 64k --tune skip --vision off --drafting dflash2` |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 2.9 | 2.9 | 73.8 | 34.2 | 0.35 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 57.1 | 54.0 | 39.95 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.14 | None | 51.3 | 50.2 | 49.09 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.15 | None | 52.3 | 59.9 | 53.7 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 10.58 | None | 49.9 | 50.0 | 18.36 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 13.18 | None | 49.9 | 50.05 | 17.16 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 15.79 | None | 50.4 | 50.0 | 12.26 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 2.75 | None | 50.4 | 50.0 | 36.68 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.7 | 0.87 | 130.7 | 81.8 | 43.29 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.81 | 0.81 | 274.2 | 49.9 | 43.32 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.15 | None | 50.3 | 50.1 | 48.97 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.14 | None | 51.0 | 50.1 | 48.99 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 41.79, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 49.01, "per_request_e2e_tokens_per_s_median": 24.462501138604406, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
