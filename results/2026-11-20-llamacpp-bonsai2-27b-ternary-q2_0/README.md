# 2026-11-21 · llamacpp · llamacpp-bonsai2-27b-ternary-q2_0 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | prism-ml/Ternary-Bonsai-2-27B-gguf |
| 받은 파일 | Ternary-Bonsai-2-27B-Q2_0.gguf (예상 8 GB) |
| 엔진 옵션 | `-c 65536` |
| API 별칭 | llamacpp-bonsai2-27b-ternary-q2_0 |
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
 "quality": "step_timeout_28800s"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 0.61 | 0.61 | 357.05 | 0.0 | 1.63 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 39.09 | 25.29 | 22.15 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 40.4 | 25.79 | 25.57 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 39.22 | 25.83 | 24.93 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.22 | None | 40.69 | 19.99 | 19.72 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.61 | None | 231.71 | 20.56 | 19.7 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.64 | 0.99 | 260.29 | 20.62 | 19.71 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.42 | None | 27.06 | 20.31 | 19.74 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 0.74 | None | 740.49 | 25.07 | 17.83 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44945 | 0.94 | None | 583.96 | 19.23 | 16.66 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 0.74 | None | 737.89 | 25.6 | 18.21 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 0.78 | None | 695.65 | 23.6 | 17.14 | - |
| quality-gsm8k | 100/100 | 100 | 94/100 | 0 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 95/100 | 0 | 140 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 47 | 38/47 | 51 | 177 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 119 | 105/119 | 21 | 227 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.25 | None | 227.24 | 25.79 | 24.37 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 1.13 | None | 555.66 | 26.6 | 23.88 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.17 | None | 45.8 | 26.58 | 26.22 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 40.95 | 26.69 | 26.48 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 94/100, 잘림 0, 평균 출력 470.1 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 95/100, 잘림 0, 평균 출력 678.4 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 38/100, 잘림 51, 평균 출력 10086.3 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 105/140, 잘림 21, 평균 출력 4210.1 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 26.05, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 78.6, "per_request_e2e_tokens_per_s_median": 20.005855646671865, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
