# 2026-11-19 · strata · issue14-strata-qwen38fn-iq3s-ctx32k-kvq4 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF (IQ3_S) |
| 받은 파일 | 전체/엔진 기본 (예상 84 GB) |
| 엔진 옵션 | `--family qwen --model iq3_s --vision off --drafting mtp --context 32k --kv q4_0 --tune skip` |
| API 별칭 | qwen3.8-flash-next-iq3_s |
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
 "throughput-1": "ok",
 "throughput-2": "ok",
 "throughput-3": "ok",
 "concurrency4": "ok",
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 2.09 | 2.09 | 103.2 | 32.8 | 0.48 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.14 | None | 62.6 | 59.7 | 43.75 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.14 | None | 55.8 | 53.3 | 52.12 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 63.9 | 53.0 | 49.07 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.15 | None | 70.1 | 20.6 | 20.39 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.42 | None | 73.0 | 20.95 | 20.32 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.27 | None | 72.2 | 20.75 | 20.35 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.56 | None | 62.5 | 21.15 | 20.32 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 5.16 | 5.19 | 568.3 | 58.2 | 12.51 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 1.76 | 1.77 | 468.4 | 65.6 | 18.88 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 19.67 | 19.68 | 576.8 | 69.7 | 4.89 | - |
| quality-gsm8k | 100/100 | 100 | 96/100 | 0 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 97/100 | 0 | 140 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 163 | 157/163 | 1 | 194 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 100 | 76/100 | 0 | 177 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 140 | 128/140 | 0 | 227 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 11 | - | 1 | 94 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 740 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.64 | 0.87 | 146.4 | 64.85 | 45.04 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.87 | 0.87 | 255.0 | 54.0 | 45.85 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 73.1 | 54.8 | 53.86 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 75.1 | 53.7 | 52.73 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 96/100, 잘림 0, 평균 출력 287.8 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 97/100, 잘림 0, 평균 출력 415.0 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 157/164, 잘림 1, 평균 출력 875.4 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 76/100, 잘림 0, 평균 출력 1992.7 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 128/140, 잘림 0, 평균 출력 1217.6 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 1, 평균 출력 1046.4 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 76.2 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 25.29, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 80.99, "per_request_e2e_tokens_per_s_median": 20.747203423774458, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
