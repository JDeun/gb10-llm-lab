# 2026-11-19 · strata · issue14-strata-qwen38fn-iq3s-tune-thorough (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF (IQ3_S) |
| 받은 파일 | 전체/엔진 기본 (예상 84 GB) |
| 엔진 옵션 | `--family qwen --model iq3_s --vision off --drafting mtp --context 64k --tune thorough` |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 1.56 | 1.56 | 139.2 | 31.6 | 0.64 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 74.1 | 51.5 | 40.3 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.15 | None | 53.5 | 35.0 | 34.49 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.15 | None | 54.5 | 52.6 | 48.2 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.14 | None | 72.2 | 17.2 | 17.09 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.44 | None | 52.2 | 17.5 | 17.03 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.25 | None | 72.2 | 17.3 | 17.05 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.61 | None | 51.1 | 17.7 | 17.04 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 1.75 | 8.71 | 1710.1 | 61.0 | 18.09 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 1.2 | 2.4 | 698.0 | 62.5 | 24.18 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 5.92 | 5.93 | 1929.6 | 70.0 | 12.78 | - |
| quality-gsm8k | 100/100 | 100 | 96/100 | 0 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 97/100 | 0 | 140 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 162 | 158/162 | 2 | 194 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 100 | 74/100 | 0 | 177 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 140 | 125/140 | 0 | 227 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 11 | - | 1 | 94 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 740 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.66 | 0.95 | 144.2 | 68.0 | 41.69 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 1.1 | 1.1 | 200.0 | 37.8 | 32.68 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 74.2 | 47.6 | 46.81 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 72.5 | 47.6 | 46.8 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 96/100, 잘림 0, 평균 출력 272.8 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 97/100, 잘림 0, 평균 출력 395.5 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 158/164, 잘림 2, 평균 출력 835.2 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 74/100, 잘림 0, 평균 출력 2034.8 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 125/140, 잘림 0, 평균 출력 1259.7 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 1, 평균 출력 1178.4 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 80.2 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 30.16, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 67.9, "per_request_e2e_tokens_per_s_median": 17.57281074632852, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
