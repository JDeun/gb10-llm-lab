# 2026-11-13 · vllm · vllm-ornith-1.0-35b-reasoning-parser (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | ornith-ai/Ornith-1.0-35B |
| 받은 파일 | 전체/엔진 기본 (예상 70 GB) |
| 엔진 옵션 | `--max-model-len 131072 --max-num-seqs 4 --gpu-memory-utilization 0.8 --trust-remote-code --reasoning-parser qwen3` |
| API 별칭 | vllm-ornith-1.0-35b-reasoning-parser |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 0.36 | None | None | None | 2.77 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.3 | None | None | None | 20.26 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.2 | None | None | None | 30.26 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.2 | None | None | None | 28.68 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 168 | 0.4 | None | None | None | 26.11 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 168 | 0.41 | None | None | None | 26.09 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 168 | 0.4 | None | None | None | 26.12 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 168 | 0.27 | None | None | None | 26.12 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2864 | 0.35 | None | None | None | 28.21 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44903 | 0.62 | None | None | None | 25.07 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 763 | 0.38 | None | None | None | 28.96 | - |
| context-60k | 3/3 | 3 | 3/3 | 0 | 82029 | 0.74 | None | None | None | 22.51 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11269 | 0.51 | None | None | None | 27.3 | - |
| sanity-2048 | 12/12 | 12 | 12/12 | 0 | 44 | 0.17 | None | None | None | 30.63 | - |
| sanity-512 | 12/12 | 9 | 9/9 | 3 | 44 | 0.18 | None | None | None | 30.67 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 168 | 0.21 | None | None | None | 30.13 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 168 | 0.21 | None | None | None | 30.2 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 168 | 0.21 | None | None | None | 30.21 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 19.63, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 104.34, "per_request_e2e_tokens_per_s_median": 26.13594313237985, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
