# 2026-11-17 · ikllama · ikllama-gemma4-26b-udq4kxl (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | unsloth/gemma-4-26B-A4B-it-GGUF |
| 받은 파일 | gemma-4-26B-A4B-it-UD-Q4_K_XL.gguf (예상 16 GB) |
| 엔진 옵션 | `-c 65536` |
| API 별칭 | ikllama-gemma4-26b-udq4kxl |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 180 | None | None | 1096.11 | 1000000.0 | 5.46 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 180 | 0.09 | None | 46.16 | 58.03 | 50.91 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 180 | 0.09 | None | 53.98 | 54.09 | 53.69 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 180 | 0.09 | None | 53.78 | 55.55 | 53.89 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 180 | 7.17 | None | 45.1 | 54.44 | 33.75 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 180 | 14.24 | None | 46.38 | 54.46 | 13.56 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 180 | 9.53 | None | 46.31 | 54.45 | 20.32 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 180 | 11.88 | None | 46.24 | 54.45 | 15.81 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2900 | 0.13 | None | 360.82 | 51.37 | 49.52 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 45253 | 0.22 | None | 255.82 | 41.72 | 39.28 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 776 | 0.12 | None | 361.16 | 52.63 | 51.92 | - |
| context-60k | 3/3 | 3 | 2/3 | 0 | 49810 | 30.06 | None | 1687.65 | 42.57 | 0.47 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11330 | 0.15 | None | 326.37 | 49.21 | 46.61 | - |
| quality-gsm8k | 100/100 | 55 | 54/55 | 45 | 89 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 97 | 92/97 | 3 | 107 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 134 | 134/134 | 30 | 163 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 73 | 64/73 | 27 | 154 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 36 | 34/36 | 104 | 195 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 65 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 494 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 51 | 0.15 | None | 705.07 | 55.07 | 53.75 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 180 | 2.88 | None | 1798.98 | 54.35 | 33.99 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 180 | 0.72 | None | 43.79 | 54.39 | 47.71 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 180 | 0.11 | None | 46.14 | 54.43 | 53.78 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 54/100, 잘림 45, 평균 출력 2406.3 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 92/100, 잘림 3, 평균 출력 954.2 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 134/164, 잘림 30, 평균 출력 2257.8 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 64/100, 잘림 27, 평균 출력 2160.7 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 34/140, 잘림 104, 평균 출력 3494.4 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 0, 평균 출력 1434.4 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 129.9 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 37.81, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 54.17, "per_request_e2e_tokens_per_s_median": 13.565612815253557, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
