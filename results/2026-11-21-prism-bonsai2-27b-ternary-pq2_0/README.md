# 2026-11-21 · prism · prism-bonsai2-27b-ternary-pq2_0 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | prism-ml/Ternary-Bonsai-2-27B-gguf |
| 받은 파일 | Ternary-Bonsai-2-27B-PQ2_0.gguf (예상 7 GB) |
| 엔진 옵션 | `-c 65536` |
| API 별칭 | prism-bonsai2-27b-ternary-pq2_0 |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 0.47 | 0.47 | 467.85 | 0.0 | 2.14 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 46.82 | 30.05 | 26.54 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 47.25 | 30.73 | 30.48 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 47.39 | 30.71 | 29.72 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.35 | None | 42.55 | 20.22 | 19.76 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.74 | None | 220.01 | 20.83 | 19.73 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.77 | 1.03 | 249.7 | 20.89 | 19.74 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.56 | None | 28.83 | 20.57 | 19.76 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 0.61 | None | 871.48 | 29.68 | 21.21 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44945 | 0.85 | None | 653.77 | 21.04 | 18.32 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 0.6 | None | 888.17 | 30.36 | 21.85 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 0.66 | None | 821.65 | 27.33 | 19.97 | - |
| quality-gsm8k | 100/100 | 100 | 94/100 | 0 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 95/100 | 0 | 140 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 47 | 38/47 | 53 | 177 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 117 | 106/117 | 23 | 227 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.3 | None | 238.51 | 30.74 | 28.26 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 1.16 | None | 544.37 | 27.34 | 24.41 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.24 | None | 43.91 | 27.33 | 26.75 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 44.81 | 27.35 | 27.14 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 94/100, 잘림 0, 평균 출력 526.0 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 95/100, 잘림 0, 평균 출력 542.4 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 38/100, 잘림 53, 평균 출력 10055.4 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 106/140, 잘림 23, 평균 출력 4238.2 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 26.01, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 78.75, "per_request_e2e_tokens_per_s_median": 19.861220486936013, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
