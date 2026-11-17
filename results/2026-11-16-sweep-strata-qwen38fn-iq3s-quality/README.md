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
 "concurrency4": "ok",
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 2.04 | 2.04 | 123.9 | 23.3 | 0.49 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 90.7 | 71.5 | 53.43 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 75.1 | 50.4 | 49.45 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 74.9 | 57.5 | 53.4 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.44 | None | 71.5 | 20.0 | 19.37 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.13 | None | 73.1 | 19.6 | 19.46 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.45 | None | 72.0 | 20.0 | 19.34 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.22 | None | 76.5 | 19.7 | 19.39 | - |
| quality-gsm8k | 100/100 | 100 | 96/100 | 0 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 97/100 | 0 | 140 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 162 | 158/162 | 2 | 194 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 100 | 74/100 | 0 | 177 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 140 | 125/140 | 0 | 227 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 11 | - | 1 | 94 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 740 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.64 | 0.89 | 149.3 | 69.7 | 41.97 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.75 | 0.75 | 298.6 | 49.3 | 43.3 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 76.2 | 49.9 | 49.13 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 77.4 | 50.5 | 49.71 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 96/100, 잘림 0, 평균 출력 272.8 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 97/100, 잘림 0, 평균 출력 395.5 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 158/164, 잘림 2, 평균 출력 835.2 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 74/100, 잘림 0, 평균 출력 2034.8 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 125/140, 잘림 0, 평균 출력 1259.7 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 1, 평균 출력 1178.4 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 80.2 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 26.49, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 77.32, "per_request_e2e_tokens_per_s_median": 19.386605037351327, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
