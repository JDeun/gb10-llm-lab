# 2026-11-19 · llamacpp · llamacpp-gpt-oss-120b-mxfp4 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | ggml-org/gpt-oss-120b-GGUF |
| 받은 파일 | gpt-oss-120b-MXFP4.gguf (예상 63 GB) |
| 엔진 옵션 | `-c 65536` |
| API 별칭 | llamacpp-gpt-oss-120b-mxfp4 |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 245 | None | None | 371.63 | 0.0 | 1.45 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 245 | 0.13 | None | 20.33 | 52.59 | 44.26 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 245 | 0.1 | None | 48.38 | 54.0 | 53.74 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 245 | 0.1 | None | 45.23 | 53.57 | 52.52 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 245 | 0.31 | None | 49.64 | 26.87 | 26.79 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 245 | 0.32 | None | 61.03 | 27.0 | 26.77 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 245 | 0.33 | None | 38.85 | 27.0 | 26.74 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 245 | 0.4 | None | 610.0 | 27.34 | 26.63 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2400 | 0.21 | None | 131.76 | 55.19 | 49.15 | - |
| context-32k | 3/3 | 3 | 1/3 | 0 | 36704 | 0.3 | None | 122.26 | 42.46 | 40.0 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 682 | 0.24 | None | 100.73 | 56.11 | 49.18 | - |
| context-60k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'http_error', 'status': 400, 'detail': '{"error":{" |
| context-8k | 3/3 | 3 | 3/3 | 0 | 9254 | 0.28 | None | 131.57 | 52.03 | 45.24 | - |
| quality-gsm8k | 100/100 | 100 | 96/100 | 0 | 133 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 94/100 | 0 | 161 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 163 | 159/163 | 1 | 201 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 99 | 57/99 | 1 | 200 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 137 | 104/137 | 3 | 222 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 115 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 339 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 99 | 0.27 | None | 225.15 | 55.32 | 48.68 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 245 | 0.15 | None | 35.28 | 55.18 | 54.36 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 245 | 0.13 | None | 21.39 | 55.02 | 54.39 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 245 | 0.13 | None | 20.2 | 55.23 | 54.56 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 96/100, 잘림 0, 평균 출력 293.1 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 94/100, 잘림 0, 평균 출력 389.7 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 159/164, 잘림 1, 평균 출력 557.7 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 57/100, 잘림 1, 평균 출력 1055.4 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 104/140, 잘림 3, 평균 출력 790.4 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 0, 평균 출력 1081.9 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 69.5 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 19.25, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 106.38, "per_request_e2e_tokens_per_s_median": 26.83237425050953, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
