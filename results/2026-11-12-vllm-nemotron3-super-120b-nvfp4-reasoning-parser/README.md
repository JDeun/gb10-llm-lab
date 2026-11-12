# 2026-11-13 · vllm · vllm-nemotron3-super-120b-nvfp4-reasoning-parser (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 |
| 받은 파일 | 전체/엔진 기본 (예상 80 GB) |
| 엔진 옵션 | `--max-model-len 131072 --gpu-memory-utilization 0.85 --max-num-seqs 4 --trust-remote-code --reasoning-parser deepseek_r1` |
| API 별칭 | vllm-nemotron3-super-120b-nvfp4-reasoning-parser |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 177 | 0.53 | None | None | None | 1.87 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 177 | 0.46 | None | None | None | 11.52 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 177 | 0.35 | None | None | None | 15.81 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 177 | 0.35 | None | None | None | 15.03 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 177 | 0.54 | None | None | None | 10.86 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 177 | 0.76 | None | None | None | 10.84 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 177 | 0.75 | None | None | None | 10.84 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 177 | 0.75 | None | None | None | 10.84 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2833 | 1.47 | None | None | None | 11.99 | - |
| context-32k | 3/3 | 0 | 0/0 | 3 | 44120 | 1.63 | None | None | None | 15.47 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 755 | 0.59 | None | None | None | 14.33 | - |
| context-60k | 3/3 | 0 | 0/0 | 2 | 80633 | 3.42 | None | None | None | 14.86 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11089 | 1.49 | None | None | None | 14.27 | - |
| sanity-2048 | 12/12 | 12 | 12/12 | 0 | 51 | 0.29 | None | None | None | 15.02 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 51 | 0.29 | None | None | None | 14.98 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 177 | 0.36 | None | None | None | 15.69 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 177 | 0.35 | None | None | None | 15.71 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 177 | 0.35 | None | None | None | 15.71 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 47.23, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 43.36, "per_request_e2e_tokens_per_s_median": 10.921906262932199, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
