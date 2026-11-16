# 2026-11-16 · vllm · sweep-vllm-qwen36-kvauto (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | nvidia/Qwen3.6-35B-A3B-NVFP4 |
| 받은 파일 | 전체/엔진 기본 (예상 23 GB) |
| 엔진 옵션 | `--max-model-len 65536 --trust-remote-code --kv-cache-dtype auto --attention-backend flashinfer --moe-backend marlin --gpu-memory-utilization 0.6 --max-num-seqs 16 --max-num-batched-tokens 8192 --enable-chunked-prefill --async-scheduling --enable-prefix-caching --reasoning-parser qwen3 --speculative-config {"method":"mtp","num_speculative_tokens":3,"moe_backend":"triton"} --enable-auto-tool-choice --tool-call-parser qwen3_xml` |
| API 별칭 | sweep-vllm-qwen36-kvauto |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 0.43 | None | None | None | 2.31 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.5 | None | None | None | 27.83 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.1 | None | None | None | 107.49 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.1 | None | None | None | 101.21 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 168 | 0.21 | None | None | None | 66.56 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 168 | 0.24 | None | None | None | 63.98 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 168 | 0.21 | None | None | None | 65.46 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 168 | 0.22 | None | None | None | 64.87 | - |
| sanity-512 | 12/12 | 10 | 10/10 | 2 | 44 | 0.08 | None | None | None | 135.85 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 168 | 0.1 | None | None | None | 108.56 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 109.48 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 106.35 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 8.03, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 255.2, "per_request_e2e_tokens_per_s_median": 64.92168265990736, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
