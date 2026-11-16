# 2026-11-14 · strata · strata-deepseek-v41-flash-225bpw (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF (IST-DAS 2.25bpw) |
| 받은 파일 | 전체/엔진 기본 (예상 274 GB) |
| 엔진 옵션 | `--family deepseek41 --model ist-das-2.25bpw --context 128k --vision on --speed full --tune skip` |
| API 별칭 | deepseek-v4.1-flash |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 224 | 5.55 | 5.55 | 43.0 | 5000.0 | 0.18 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 224 | 0.12 | None | 10.2 | 6.1 | 5.05 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 224 | 5.02 | 5.02 | 31.8 | 10.4 | 8.46 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 224 | 0.1 | None | 0.4 | 6.7 | 6.52 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 224 | 72.09 | 45.27 | 48.5 | 13.85 | 3.1 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 224 | 49.81 | None | 0.7 | 13.15 | 4.44 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 224 | 17.47 | 30.0 | 39.9 | 12.25 | 6.95 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 224 | 60.56 | 88.05 | 41.3 | 13.7 | 3.53 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2369 | 4.88 | 13.73 | 123.4 | 21.0 | 5.49 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 36750 | 5.05 | 63.48 | 122.1 | 20.3 | 6.07 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 646 | 5.8 | 8.51 | 111.8 | 19.4 | 4.79 | - |
| context-60k | 3/3 | 3 | 3/3 | 0 | 67104 | 4.81 | 114.84 | 124.3 | 24.0 | 7.15 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 9231 | 6.13 | 23.5 | 124.0 | 20.4 | 6.07 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 65 | 3.63 | 4.84 | 17.9 | 14.65 | 7.37 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 224 | 4.07 | 4.07 | 37.9 | 7.6 | 6.81 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 224 | 0.52 | None | 0.4 | 10.7 | 10.18 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 224 | 0.41 | None | 0.2 | 11.5 | 10.04 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 182.19, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 11.24, "per_request_e2e_tokens_per_s_median": 4.649197499230017, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `vision-check.json`: `{"cases": 3, "passed": 3, "errors": 0}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
