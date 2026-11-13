# 2026-11-13 · llamacpp · llamacpp-qwen36-35b-udq4kxl-ctx64k (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | unsloth/Qwen3.6-35B-A3B-GGUF |
| 받은 파일 | Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf (예상 22 GB) |
| 엔진 옵션 | `-c 65536` |
| API 별칭 | llamacpp-qwen36-35b-udq4kxl-ctx64k |
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
 "concurrency4": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 0.31 | 0.31 | 580.43 | 0.0 | 3.26 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.06 | None | 90.75 | 59.71 | 51.35 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.06 | None | 86.26 | 63.59 | 62.84 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.07 | None | 88.53 | 62.28 | 59.1 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 168 | 0.26 | 0.36 | 513.11 | 39.6 | 38.29 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 168 | 0.23 | None | 56.02 | 39.48 | 38.29 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 168 | 0.13 | None | 87.58 | 38.87 | 38.23 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 168 | 0.26 | 0.37 | 514.26 | 39.59 | 38.28 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2864 | 0.27 | 1.14 | 2143.63 | 64.63 | 59.51 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44903 | 0.37 | 19.03 | 1654.06 | 51.14 | 47.56 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 763 | 0.25 | 0.4 | 2178.8 | 65.37 | 58.59 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11269 | 0.28 | 4.3 | 1991.41 | 61.63 | 57.93 | - |
| sanity-512 | 12/12 | 10 | 10/10 | 2 | 44 | 0.14 | 0.15 | 493.91 | 63.71 | 62.4 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 168 | 0.33 | None | 86.3 | 64.26 | 59.61 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | 87.34 | 65.87 | 64.57 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 168 | 0.06 | None | 88.25 | 65.94 | 65.15 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 13.45, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 152.24, "per_request_e2e_tokens_per_s_median": 39.6042153174731, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
