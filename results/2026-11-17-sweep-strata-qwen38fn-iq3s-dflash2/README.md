# 2026-11-17 · strata · sweep-strata-qwen38fn-iq3s-dflash2 (자동 실행)

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
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 1.62 | 1.62 | 133.2 | 34.4 | 0.62 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.17 | None | 45.2 | 59.3 | 40.25 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.15 | None | 46.1 | 49.0 | 47.88 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.15 | None | 50.6 | 50.2 | 46.05 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 2.99 | None | 47.9 | 48.6 | 34.88 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 13.66 | None | 44.9 | 48.85 | 16.79 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 10.9 | None | 43.4 | 47.9 | 17.46 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 16.36 | None | 43.9 | 48.7 | 11.86 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.69 | 0.73 | 134.6 | 82.95 | 48.67 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.97 | 0.97 | 227.0 | 48.3 | 41.04 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.15 | None | 47.8 | 49.7 | 48.59 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.15 | None | 48.1 | 49.9 | 48.7 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 43.19, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 47.42, "per_request_e2e_tokens_per_s_median": 22.86847827178789, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
