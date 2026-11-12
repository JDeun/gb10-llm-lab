# 2026-11-13 · vllm · vllm-ornith-1.0-35b (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | ornith-ai/Ornith-1.0-35B |
| 받은 파일 | 전체/엔진 기본 (예상 70 GB) |
| 엔진 옵션 | `--max-model-len 131072 --max-num-seqs 4 --gpu-memory-utilization 0.8 --trust-remote-code` |
| API 별칭 | vllm-ornith-1.0-35b |
| 측정 프로필 | full |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "capacity-cap1": "ok",
 "capacity-cap16": "ok",
 "capacity-cap64": "ok",
 "capacity-cap256": "ok",
 "sanity-512": "ok",
 "sanity-2048": "ok",
 "context-512": "ok",
 "context-2k": "ok",
 "context-8k": "ok",
 "context-32k": "ok",
 "context-60k": "ok",
 "throughput-1": "ok",
 "throughput-2": "ok",
 "throughput-3": "ok",
 "concurrency4": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 0.41 | None | None | None | 2.46 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.34 | None | None | None | 19.51 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.2 | None | None | None | 30.48 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.2 | None | None | None | 28.79 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 168 | 0.4 | None | None | None | 26.2 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 168 | 0.27 | None | None | None | 26.21 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 168 | 0.41 | None | None | None | 26.17 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 168 | 0.4 | None | None | None | 26.19 | - |
| context-2k | 3/3 | 3 | 0/3 | 0 | 2864 | 0.41 | None | None | None | 28.03 | - |
| context-32k | 3/3 | 3 | 0/3 | 0 | 44903 | 0.63 | None | None | None | 25.2 | - |
| context-512 | 3/3 | 3 | 0/3 | 0 | 763 | 0.38 | None | None | None | 29.16 | - |
| context-60k | 3/3 | 3 | 0/3 | 0 | 82029 | 0.71 | None | None | None | 22.66 | - |
| context-8k | 3/3 | 3 | 0/3 | 0 | 11269 | 0.54 | None | None | None | 27.27 | - |
| sanity-2048 | 12/12 | 12 | 0/12 | 0 | 44 | 0.16 | None | None | None | 30.83 | - |
| sanity-512 | 12/12 | 9 | 0/9 | 3 | 44 | 0.17 | None | None | None | 30.87 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 168 | 0.21 | None | None | None | 30.41 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 168 | 0.2 | None | None | None | 30.24 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 168 | 0.2 | None | None | None | 30.3 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 19.57, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 104.68, "per_request_e2e_tokens_per_s_median": 26.223309355679415, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
