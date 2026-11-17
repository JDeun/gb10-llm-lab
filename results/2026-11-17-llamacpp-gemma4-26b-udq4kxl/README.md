# 2026-11-17 · llamacpp · llamacpp-gemma4-26b-udq4kxl (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | unsloth/gemma-4-26B-A4B-it-GGUF |
| 받은 파일 | gemma-4-26B-A4B-it-UD-Q4_K_XL.gguf (예상 16 GB) |
| 엔진 옵션 | `-c 65536` |
| API 별칭 | llamacpp-gemma4-26b-udq4kxl |
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
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 180 | None | None | 416.28 | 0.0 | 2.22 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 180 | 0.15 | None | 73.59 | 51.45 | 42.6 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 180 | 0.14 | None | 77.17 | 52.71 | 52.04 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 180 | 0.14 | None | 77.75 | 52.09 | 49.59 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 180 | 0.33 | 0.38 | 644.09 | 33.29 | 32.36 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 180 | 0.33 | 0.39 | 646.27 | 33.29 | 32.36 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 180 | 0.36 | None | 59.31 | 33.13 | 32.41 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 180 | 0.37 | None | 54.84 | 32.91 | 32.41 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2900 | 0.28 | 1.12 | 103.44 | 52.04 | 46.89 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 45253 | 0.3 | 17.77 | 117.48 | 43.35 | 39.66 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 776 | 0.33 | 0.46 | 2041.65 | 52.98 | 50.34 | - |
| context-60k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'http_error', 'status': 400, 'detail': '{"error":{" |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11330 | 0.25 | 3.82 | 115.86 | 49.97 | 44.83 | - |
| quality-gsm8k | 100/100 | 53 | 52/53 | 47 | 89 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 97 | 93/97 | 3 | 107 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 127 | 127/127 | 37 | 163 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 72 | 61/72 | 28 | 154 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 42 | 42/42 | 98 | 195 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 65 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 494 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 51 | 0.19 | None | 445.96 | 54.25 | 52.59 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 180 | 0.15 | None | 80.64 | 54.34 | 53.57 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 180 | 0.16 | None | 85.64 | 54.37 | 53.39 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 180 | 0.14 | None | 81.52 | 54.36 | 53.68 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 52/100, 잘림 47, 평균 출력 2510.8 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 93/100, 잘림 3, 평균 출력 950.4 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 127/164, 잘림 37, 평균 출력 2298.5 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 61/100, 잘림 28, 평균 출력 2164.5 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 42/140, 잘림 98, 평균 출력 3432.0 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 0, 평균 출력 1476.2 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 120.6 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 15.85, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 129.24, "per_request_e2e_tokens_per_s_median": 32.44379791676209, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
