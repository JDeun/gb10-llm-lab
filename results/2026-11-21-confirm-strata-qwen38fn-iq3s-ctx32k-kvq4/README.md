# 2026-11-22 · strata · confirm-strata-qwen38fn-iq3s-ctx32k-kvq4 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF (IQ3_S) |
| 받은 파일 | 전체/엔진 기본 (예상 84 GB) |
| 엔진 옵션 | `--family qwen --model iq3_s --vision off --drafting mtp --context 32k --kv q4_0 --tune skip` |
| API 별칭 | qwen3.8-flash-next-iq3_s |
| 측정 프로필 | confirm |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "sanity-2048": "ok",
 "context-512": "ok",
 "context-2k": "ok",
 "context-8k": "ok",
 "throughput-1": "ok",
 "throughput-2": "ok",
 "throughput-3": "ok",
 "throughput-4": "ok",
 "throughput-5": "ok",
 "concurrency1": "ok",
 "concurrency4": "ok",
 "concurrency8": "ok",
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| concurrency1-client1 | 2/2 | 0 | - | 2 | 210 | 0.12 | None | 75.0 | 54.25 | 53.2 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.43 | None | 73.0 | 21.45 | 20.74 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.22 | None | 75.5 | 21.1 | 20.79 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.49 | None | 71.1 | 21.5 | 20.69 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.17 | None | 73.5 | 21.1 | 20.85 | - |
| concurrency8-client1 | 2/2 | 0 | - | 2 | 210 | 6.4 | None | 69.6 | 20.55 | 14.78 | - |
| concurrency8-client2 | 2/2 | 0 | - | 2 | 210 | 12.85 | None | 70.7 | 21.25 | 10.32 | - |
| concurrency8-client3 | 2/2 | 0 | - | 2 | 210 | 12.97 | None | 70.7 | 21.4 | 10.29 | - |
| concurrency8-client4 | 2/2 | 0 | - | 2 | 210 | 6.58 | None | 67.9 | 20.65 | 14.66 | - |
| concurrency8-client5 | 2/2 | 0 | - | 2 | 210 | 12.9 | None | 71.8 | 21.3 | 10.29 | - |
| concurrency8-client6 | 2/2 | 0 | - | 2 | 210 | 0.41 | None | 68.5 | 20.4 | 19.8 | - |
| concurrency8-client7 | 2/2 | 0 | - | 2 | 210 | 13.1 | None | 72.6 | 21.65 | 13.79 | - |
| concurrency8-client8 | 2/2 | 0 | - | 2 | 210 | 6.42 | None | 71.8 | 20.55 | 14.79 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 5.07 | 5.08 | 579.9 | 59.3 | 12.51 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 1.76 | 1.76 | 472.2 | 60.5 | 18.53 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 19.38 | 19.4 | 585.3 | 69.3 | 4.95 | - |
| quality-gsm8k-l | 300/300 | 300 | 294/300 | 0 | 122 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k-l | 300/300 | 300 | 286/300 | 0 | 138 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 163 | 157/163 | 1 | 194 | None | None | None | None | None | - |
| quality-kmmlu-l | 300/300 | 300 | 233/300 | 0 | 171 | None | None | None | None | None | - |
| quality-mmlu-pro-l | 420/420 | 420 | 355/420 | 0 | 224 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 11 | - | 1 | 94 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 740 | None | None | None | None | None | - |
| sanity-2048 | 12/12 | 12 | 12/12 | 0 | 86 | 0.64 | 1.27 | 142.8 | 63.8 | 43.11 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.88 | 0.88 | 254.7 | 50.4 | 43.21 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 75.1 | 54.4 | 53.4 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 75.1 | 54.3 | 53.35 | - |
| throughput-4 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 74.7 | 54.2 | 53.23 | - |
| throughput-5 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 72.8 | 54.3 | 53.33 | - |

- 품질 `gsm8k-l-subset-zeroshot`: 정답 294/300, 잘림 0, 평균 출력 302.6 토큰
- 품질 `hrm8k-gsm8k-l-subset-zeroshot`: 정답 286/300, 잘림 0, 평균 출력 496.9 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 157/164, 잘림 1, 평균 출력 875.4 토큰
- 품질 `kmmlu-l-subset-zeroshot`: 정답 233/300, 잘림 0, 평균 출력 1767.4 토큰
- 품질 `mmlu-pro-l-subset-zeroshot`: 정답 355/420, 잘림 0, 평균 출력 1250.3 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 1, 평균 출력 1046.4 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 76.2 토큰
- `concurrency1-summary.json`: `{"clients": 1, "requests": 2, "errors": 0, "wall_s": 9.62, "completion_tokens_total": 512, "aggregate_completion_tokens_per_s": 53.2, "per_request_e2e_tokens_per_s_median": 53.20557315105283, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 24.8, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 82.59, "per_request_e2e_tokens_per_s_median": 20.941264479172442, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `concurrency8-summary.json`: `{"clients": 8, "requests": 16, "errors": 0, "wall_s": 49.91, "completion_tokens_total": 4096, "aggregate_completion_tokens_per_s": 82.07, "per_request_e2e_tokens_per_s_median": 10.580956474768971, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
