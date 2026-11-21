# 2026-11-21 · prism · prism-bonsai2-27b-ternary-ptq1_0 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | prism-ml/Ternary-Bonsai-2-27B-gguf |
| 받은 파일 | Ternary-Bonsai-2-27B-PTQ1_0.gguf (예상 6 GB) |
| 엔진 옵션 | `-c 65536` |
| API 별칭 | prism-bonsai2-27b-ternary-ptq1_0 |
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
 "throughput-1": "ok",
 "throughput-2": "ok",
 "throughput-3": "ok",
 "concurrency4": "ok",
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 0.45 | 0.45 | 482.99 | 0.0 | 2.21 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 49.06 | 36.46 | 31.3 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 49.93 | 37.36 | 36.97 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 49.08 | 37.21 | 35.72 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.69 | 1.01 | 265.73 | 23.18 | 21.94 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.38 | None | 25.77 | 22.6 | 21.94 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.65 | None | 232.05 | 23.11 | 21.94 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.38 | None | 36.88 | 22.6 | 21.94 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 0.65 | None | 830.62 | 36.15 | 23.75 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44945 | 0.86 | None | 638.43 | 24.49 | 20.85 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 0.63 | None | 850.01 | 37.04 | 24.69 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 0.69 | None | 798.79 | 32.78 | 22.31 | - |
| quality-gsm8k | 100/100 | 100 | 93/100 | 0 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 95/100 | 0 | 140 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 155 | 145/155 | 9 | 194 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 53 | 42/53 | 46 | 177 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 118 | 103/118 | 22 | 227 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 11 | - | 1 | 94 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 794 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.29 | None | 249.9 | 37.41 | 33.77 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 1.15 | None | 541.18 | 32.76 | 28.65 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.23 | None | 47.58 | 32.79 | 31.98 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 48.7 | 32.81 | 32.53 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 93/100, 잘림 0, 평균 출력 539.4 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 95/100, 잘림 0, 평균 출력 603.7 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 145/164, 잘림 9, 평균 출력 2185.7 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 42/100, 잘림 46, 평균 출력 9489.2 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 103/140, 잘림 22, 평균 출력 4040.1 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 1, 평균 출력 2486.5 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 92.5 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 23.41, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 87.48, "per_request_e2e_tokens_per_s_median": 21.96328562972616, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
