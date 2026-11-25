# 2026-11-25 · nariq · nariq-qwen38-27b-2.5bpw (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | nari-labs/Qwen3.8-27B-NariQ-GGUF |
| 받은 파일 | Qwen3.8-27B-NariQ-2.5bpw.gguf (예상 8 GB) |
| 엔진 옵션 | `-c 65536 --temp 1.0 --top-p 0.95 --top-k 20 --min-p 0` |
| API 별칭 | nariq-qwen38-27b-2.0bpw |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 1.24 | None | 523.79 | 0.0 | 0.8 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 41.8 | 19.47 | 18.11 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 39.04 | 19.33 | 19.23 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 38.86 | 19.35 | 18.96 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.53 | None | 23.74 | 15.48 | 15.06 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.66 | None | 221.57 | 15.55 | 15.01 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.23 | None | 39.37 | 15.2 | 15.05 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.65 | None | 198.41 | 15.55 | 15.02 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 0.73 | None | 727.4 | 18.96 | 15.96 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44945 | 0.96 | None | 570.78 | 15.34 | 13.2 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 0.72 | None | 740.8 | 19.24 | 15.56 | - |
| context-60k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'http_error', 'status': 400, 'detail': '{"error":{" |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 0.79 | None | 679.65 | 18.09 | 15.77 | - |
| quality-gsm8k | 100/100 | 99 | 90/99 | 1 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 95/100 | 0 | 140 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 119 | 105/119 | 21 | 227 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.26 | None | 210.25 | 19.34 | 18.34 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.38 | None | 525.23 | 19.3 | 18.82 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.17 | None | 43.06 | 19.39 | 19.22 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 38.49 | 19.19 | 19.09 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 90/100, 잘림 1, 평균 출력 788.9 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 95/100, 잘림 0, 평균 출력 385.6 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 105/140, 잘림 21, 평균 출력 4281.8 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 34.15, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 59.97, "per_request_e2e_tokens_per_s_median": 15.24117041177569, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
