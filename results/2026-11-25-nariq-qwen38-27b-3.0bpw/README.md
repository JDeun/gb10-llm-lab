# 2026-11-26 · nariq · nariq-qwen38-27b-3.0bpw (자동 실행)

> ⚠️ **이 결과는 무효입니다 (2026-11-26 확인).** 이전 측정의 NariQ 서버가 종료되지 않고 남아 있어, 이 항목의 질문이 그 서버로 갔습니다. 즉 여기 수치는 이 파일이 아니라 **2.0bpw 파일**의 것입니다. 원인은 `stop_servers()`에 NariQ 실행 파일이 빠져 있던 것이고, 고친 뒤 재측정을 큐에 넣었습니다.

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | nari-labs/Qwen3.8-27B-NariQ-GGUF |
| 받은 파일 | Qwen3.8-27B-NariQ-3.0bpw.gguf, Qwen3.8-27B-NariQ-mmproj-BF16.gguf (예상 11 GB) |
| 엔진 옵션 | `-c 262144 --temp 1.0 --top-p 0.95 --top-k 20 --min-p 0` |
| API 별칭 | quality-nariq-qwen38-27b-2.0bpw-rest |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 1.21 | None | 521.32 | 0.0 | 0.83 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 40.59 | 19.14 | 17.8 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 39.85 | 19.28 | 19.18 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 39.08 | 19.32 | 18.93 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.65 | None | 197.37 | 15.57 | 15.04 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.23 | None | 39.35 | 15.21 | 15.07 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.66 | None | 219.01 | 15.57 | 15.03 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.54 | None | 23.43 | 15.5 | 15.07 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 0.74 | None | 721.17 | 18.77 | 15.73 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44945 | 0.97 | None | 563.4 | 15.24 | 13.09 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 0.72 | None | 739.77 | 18.94 | 15.26 | - |
| context-60k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'http_error', 'status': 400, 'detail': '{"error":{" |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 0.79 | None | 687.48 | 17.94 | 15.62 | - |
| quality-gsm8k | 100/100 | 99 | 90/99 | 1 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 95/100 | 0 | 140 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 118 | 105/118 | 21 | 227 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.28 | None | 206.44 | 19.24 | 18.08 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.4 | None | 511.44 | 19.12 | 18.64 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.18 | None | 41.7 | 19.13 | 18.95 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 38.8 | 19.21 | 19.12 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 90/100, 잘림 1, 평균 출력 722.4 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 95/100, 잘림 0, 평균 출력 385.9 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 105/140, 잘림 21, 평균 출력 4152.1 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 34.11, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 60.04, "per_request_e2e_tokens_per_s_median": 15.235909782014541, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
