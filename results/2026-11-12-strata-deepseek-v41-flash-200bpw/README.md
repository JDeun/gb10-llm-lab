# 2026-11-12 · strata · strata-deepseek-v41-flash-200bpw (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF (IST-DAS 2.00bpw) |
| 받은 파일 | 전체/엔진 기본 (예상 257 GB) |
| 엔진 옵션 | `--family deepseek41 --model ist-das-2.00bpw --context 128k --vision on --speed full --tune skip` |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 224 | 3.32 | 3.32 | 68.1 | 1666.7 | 0.3 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 224 | 0.11 | None | 12.5 | 9.7 | 8.55 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 224 | 2.89 | 2.89 | 65.9 | 15.6 | 13.64 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 224 | 0.1 | None | 0.3 | 13.5 | 8.57 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 224 | 33.24 | 39.24 | 76.9 | 19.65 | 5.63 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 224 | 19.71 | None | 2.2 | 19.15 | 8.09 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 224 | 13.15 | None | 2.3 | 19.35 | 12.39 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 224 | 40.81 | 16.44 | 72.3 | 21.2 | 6.06 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2369 | 3.0 | 8.81 | 175.5 | 31.6 | 7.37 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 36750 | 3.1 | 56.76 | 172.3 | 29.8 | 10.99 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 646 | 3.86 | 3.87 | 172.7 | 31.0 | 6.42 | - |
| context-60k | 3/3 | 3 | 3/3 | 0 | 67104 | 3.13 | 94.29 | 185.7 | 31.4 | 10.7 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 9231 | 3.03 | 19.76 | 175.2 | 28.8 | 11.01 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 65 | 1.97 | 2.34 | 36.4 | 22.5 | 11.84 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 224 | 2.64 | 2.64 | 62.2 | 12.8 | 11.45 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 224 | 0.26 | None | 0.9 | 15.3 | 15.17 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 224 | 0.26 | None | 1.4 | 16.1 | 16.32 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 106.9, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 19.16, "per_request_e2e_tokens_per_s_median": 6.745246744301234, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `vision-check.json`: `{"cases": 3, "passed": 3, "errors": 0}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.

## 해석 (2026-11-12 추가)

- **정상 동작:** sanity 12/12, 합성 이미지 3/3, 실제 646~67,104 토큰 입력 검색 전부 3/3.
- **속도:** 짧은 대화 엔진 decode 13~16 tok/s, 긴 입력 처리 후 decode 29~31 tok/s (Strata 문서의 GB10 수치 13~23 tok/s와 같은 범위). prefill 약 172~186 tok/s로 느려, 캐시 없는 첫 처리 TTFT는 9K 19.8초 · 37K 56.8초 · **67K 94.3초**.
- **동시성:** Strata DeepSeek은 이 설정에서 요청을 하나씩 처리(parallel 꺼짐)하므로 4동시 합계 19.2 tok/s, 대기 때문에 TTFT가 13~41초로 늘어납니다.
- **해석:** 이 장비에서 돌아가는 가장 큰 축의 모델이고 검색·정상 동작은 통과했지만, 첫 응답 지연과 동시성 때문에 대화형 상시 서빙보다는 **배치·장문 단발 작업**에 맞습니다.
- 측정 시작 전 모델 파일은 수동 실행으로 받은 것이고, 측정 후 258 GB를 삭제했습니다.
