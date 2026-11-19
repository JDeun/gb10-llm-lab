# 2026-11-19 · strata · issue14-strata-qwen38fn-iq3s-tune-quick (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF (IQ3_S) |
| 받은 파일 | 전체/엔진 기본 (예상 84 GB) |
| 엔진 옵션 | `--family qwen --model iq3_s --vision off --drafting mtp --context 64k --tune quick` |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 1.83 | 1.83 | 119.7 | 23.4 | 0.55 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 83.3 | 75.9 | 55.31 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 77.2 | 50.7 | 49.88 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.14 | None | 57.8 | 56.9 | 52.09 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.5 | None | 72.6 | 20.05 | 19.35 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.41 | None | 71.9 | 19.9 | 19.36 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.15 | None | 75.3 | 19.65 | 19.43 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.24 | None | 73.1 | 19.7 | 19.39 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 1.75 | 1.75 | 1715.6 | 61.2 | 22.03 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 1.19 | 1.22 | 703.3 | 66.3 | 24.02 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 5.9 | 5.92 | 1935.4 | 72.7 | 12.94 | - |
| quality-gsm8k | 100/100 | 100 | 96/100 | 0 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 97/100 | 0 | 140 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 162 | 158/162 | 2 | 194 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 100 | 74/100 | 0 | 177 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 140 | 125/140 | 0 | 227 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 11 | - | 1 | 94 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 740 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.64 | 0.82 | 148.7 | 71.05 | 46.41 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.82 | 0.82 | 280.0 | 47.6 | 41.55 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 76.8 | 50.9 | 50.05 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 74.2 | 50.8 | 49.91 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 96/100, 잘림 0, 평균 출력 272.8 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 97/100, 잘림 0, 평균 출력 395.5 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 158/164, 잘림 2, 평균 출력 835.2 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 74/100, 잘림 0, 평균 출력 2034.8 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 125/140, 잘림 0, 평균 출력 1259.7 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 1, 평균 출력 1178.4 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 80.2 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 26.55, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 77.13, "per_request_e2e_tokens_per_s_median": 19.811441217034165, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
