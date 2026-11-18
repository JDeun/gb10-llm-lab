# 2026-11-19 · ikllama · ikllama-gpt-oss-120b-mxfp4 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | ggml-org/gpt-oss-120b-GGUF |
| 받은 파일 | gpt-oss-120b-MXFP4.gguf (예상 63 GB) |
| 엔진 옵션 | `-c 65536` |
| API 별칭 | ikllama-gpt-oss-120b-mxfp4 |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 245 | None | None | 556.66 | 1000000.0 | 2.15 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 245 | 0.1 | None | 47.73 | 57.66 | 50.06 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 245 | 0.1 | None | 49.04 | 55.68 | 55.18 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 245 | 0.1 | None | 48.91 | 55.8 | 53.84 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 245 | 11.55 | None | 51.48 | 56.19 | 16.27 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 245 | 6.96 | None | 51.74 | 55.98 | 34.6 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 245 | 9.25 | None | 51.15 | 56.17 | 20.9 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 245 | 13.82 | None | 51.55 | 56.04 | 13.96 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2400 | 0.19 | None | 151.03 | 54.92 | 49.26 | - |
| context-32k | 3/3 | 3 | 1/3 | 0 | 36704 | 0.29 | None | 145.66 | 39.22 | 37.54 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 682 | 0.17 | None | 152.88 | 56.03 | 51.2 | - |
| context-60k | 3/3 | 3 | 2/3 | 0 | 34211 | 25.35 | 25.92 | 1360.51 | 40.39 | 2.67 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 9254 | 0.21 | None | 152.92 | 50.48 | 45.29 | - |
| quality-gsm8k | 100/100 | 100 | 96/100 | 0 | 133 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 93/100 | 0 | 161 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 164 | 158/164 | 0 | 201 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 100 | 63/100 | 0 | 200 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 136 | 106/136 | 4 | 222 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 115 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 339 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 99 | 0.22 | None | 266.0 | 56.45 | 51.42 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 245 | 0.91 | 0.91 | 700.77 | 55.5 | 46.84 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 245 | 0.1 | None | 50.69 | 56.17 | 55.57 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 245 | 0.1 | None | 50.22 | 56.15 | 55.62 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 96/100, 잘림 0, 평균 출력 290.0 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 93/100, 잘림 0, 평균 출력 388.0 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 158/164, 잘림 0, 평균 출력 554.1 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 63/100, 잘림 0, 평균 출력 1108.3 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 106/140, 잘림 4, 평균 출력 829.2 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 0, 평균 출력 1181.8 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 66.3 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 36.71, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 55.79, "per_request_e2e_tokens_per_s_median": 13.979407749651324, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
