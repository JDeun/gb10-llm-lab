# 2026-11-16 · vllm · sweep-vllm-qwen36-nomtp-conc16 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | nvidia/Qwen3.6-35B-A3B-NVFP4 |
| 받은 파일 | 전체/엔진 기본 (예상 23 GB) |
| 엔진 옵션 | `--max-model-len 65536 --trust-remote-code --kv-cache-dtype fp8 --attention-backend flashinfer --moe-backend marlin --gpu-memory-utilization 0.6 --max-num-seqs 16 --max-num-batched-tokens 8192 --enable-chunked-prefill --async-scheduling --enable-prefix-caching --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser qwen3_xml` |
| API 별칭 | sweep-vllm-qwen36-nomtp-conc16 |
| 측정 프로필 | standard |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "capacity-cap1": "ok",
 "capacity-cap16": "ok",
 "capacity-cap64": "ok",
 "capacity-cap256": "ok",
 "sanity-512": "ok",
 "throughput-1": "ok",
 "throughput-2": "ok",
 "throughput-3": "ok",
 "concurrency4": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 0.11 | None | None | None | 9.35 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 55.59 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 75.45 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 70.47 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 168 | 0.17 | None | None | None | 49.08 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 168 | 0.14 | None | None | None | 49.02 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 168 | 0.17 | None | None | None | 49.09 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 168 | 0.18 | None | None | None | 49.03 | - |
| sanity-512 | 12/12 | 10 | 10/10 | 2 | 44 | 0.07 | None | None | None | 77.34 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 76.46 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 76.58 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 75.4 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 10.46, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 195.79, "per_request_e2e_tokens_per_s_median": 49.02964603037313, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
