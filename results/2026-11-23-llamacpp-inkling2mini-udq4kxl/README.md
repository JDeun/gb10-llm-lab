# 2026-11-24 · llamacpp · llamacpp-inkling2mini-udq4kxl (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | ggml-org/Inkling-2-Mini-GGUF |
| 받은 파일 | Inkling-2-Mini-IQ4_NL.gguf (예상 18 GB) |
| 엔진 옵션 | `-c 65536` |
| API 별칭 | llamacpp-inkling2mini-udq4kxl |
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
 "quality": "step_timeout_28800s"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 262 | None | None | 500.2 | 0.0 | 1.84 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 262 | 0.15 | None | 61.31 | 35.7 | 31.75 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 262 | 0.15 | None | 56.12 | 37.24 | 36.9 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 262 | 0.15 | None | 56.96 | 37.02 | 35.78 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 262 | 1.03 | 1.7 | 173.07 | 20.03 | 18.8 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 262 | 0.88 | None | 55.02 | 19.01 | 18.88 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 262 | 1.03 | 1.69 | 173.14 | 20.03 | 18.81 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 262 | 1.02 | 1.68 | 173.12 | 20.03 | 18.81 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2523 | 1.19 | 4.97 | 466.72 | 35.52 | 22.07 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 39544 | 2.92 | 182.25 | 188.08 | 28.67 | 13.44 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 676 | 0.9 | 1.23 | 630.85 | 37.37 | 27.08 | - |
| context-60k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'http_error', 'status': 400, 'detail': '{"error":{" |
| context-8k | 3/3 | 3 | 3/3 | 0 | 9914 | 1.56 | 30.61 | 356.88 | 33.56 | 19.92 | - |
| quality-gsm8k | 100/100 | 100 | 96/100 | 0 | 89 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 97 | 92/97 | 3 | 138 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 111 | 99/111 | 29 | 193 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 53 | 0.28 | None | 211.05 | 37.42 | 35.08 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 262 | 0.16 | None | 55.97 | 36.87 | 36.49 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 262 | 0.15 | None | 55.81 | 36.92 | 36.59 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 262 | 0.15 | None | 55.47 | 36.95 | 36.63 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 96/100, 잘림 0, 평균 출력 431.7 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 92/100, 잘림 3, 평균 출력 1237.0 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 99/140, 잘림 29, 평균 출력 4840.5 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 27.33, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 74.93, "per_request_e2e_tokens_per_s_median": 19.718393765122382, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
