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
 "concurrency1": "ok",
 "concurrency4": "ok",
 "concurrency8": "ok",
 "concurrency16": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 0.11 | None | None | None | 9.15 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 55.95 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 76.06 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 70.8 | - |
| concurrency1-client1 | 2/2 | 0 | - | 2 | 168 | 0.1 | None | None | None | 75.69 | - |
| concurrency16-client1 | 2/2 | 0 | - | 2 | 168 | 0.36 | None | None | None | 27.88 | - |
| concurrency16-client10 | 2/2 | 0 | - | 2 | 168 | 0.36 | None | None | None | 27.84 | - |
| concurrency16-client11 | 2/2 | 0 | - | 2 | 168 | 0.22 | None | None | None | 27.67 | - |
| concurrency16-client12 | 2/2 | 0 | - | 2 | 168 | 0.37 | None | None | None | 27.8 | - |
| concurrency16-client13 | 2/2 | 0 | - | 2 | 168 | 0.38 | None | None | None | 27.78 | - |
| concurrency16-client14 | 2/2 | 0 | - | 2 | 168 | 0.14 | None | None | None | 27.68 | - |
| concurrency16-client15 | 2/2 | 0 | - | 2 | 168 | 0.36 | None | None | None | 27.88 | - |
| concurrency16-client16 | 2/2 | 0 | - | 2 | 168 | 0.26 | None | None | None | 27.77 | - |
| concurrency16-client2 | 2/2 | 0 | - | 2 | 168 | 0.35 | None | None | None | 27.86 | - |
| concurrency16-client3 | 2/2 | 0 | - | 2 | 168 | 0.39 | None | None | None | 27.75 | - |
| concurrency16-client4 | 2/2 | 0 | - | 2 | 168 | 0.39 | None | None | None | 27.75 | - |
| concurrency16-client5 | 2/2 | 0 | - | 2 | 168 | 0.28 | None | None | None | 27.72 | - |
| concurrency16-client6 | 2/2 | 0 | - | 2 | 168 | 0.19 | None | None | None | 27.65 | - |
| concurrency16-client7 | 2/2 | 0 | - | 2 | 168 | 0.35 | None | None | None | 27.86 | - |
| concurrency16-client8 | 2/2 | 0 | - | 2 | 168 | 0.35 | None | None | None | 27.86 | - |
| concurrency16-client9 | 2/2 | 0 | - | 2 | 168 | 0.38 | None | None | None | 27.77 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 168 | 0.2 | None | None | None | 49.82 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 168 | 0.19 | None | None | None | 49.86 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 168 | 0.2 | None | None | None | 49.8 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 168 | 0.15 | None | None | None | 49.87 | - |
| concurrency8-client1 | 2/2 | 0 | - | 2 | 168 | 0.26 | None | None | None | 38.37 | - |
| concurrency8-client2 | 2/2 | 0 | - | 2 | 168 | 0.26 | None | None | None | 38.57 | - |
| concurrency8-client3 | 2/2 | 0 | - | 2 | 168 | 0.27 | None | None | None | 38.5 | - |
| concurrency8-client4 | 2/2 | 0 | - | 2 | 168 | 0.26 | None | None | None | 38.37 | - |
| concurrency8-client5 | 2/2 | 0 | - | 2 | 168 | 0.17 | None | None | None | 38.42 | - |
| concurrency8-client6 | 2/2 | 0 | - | 2 | 168 | 0.26 | None | None | None | 38.53 | - |
| concurrency8-client7 | 2/2 | 0 | - | 2 | 168 | 0.27 | None | None | None | 38.49 | - |
| concurrency8-client8 | 2/2 | 0 | - | 2 | 168 | 0.26 | None | None | None | 38.54 | - |
| sanity-512 | 12/12 | 10 | 10/10 | 2 | 44 | 0.07 | None | None | None | 77.13 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 75.56 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 168 | 0.12 | None | None | None | 75.79 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 75.64 | - |

- `concurrency1-summary.json`: `{"clients": 1, "requests": 2, "errors": 0, "wall_s": 6.77, "completion_tokens_total": 512, "aggregate_completion_tokens_per_s": 75.68, "per_request_e2e_tokens_per_s_median": 76.3415520551066, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `concurrency16-summary.json`: `{"clients": 16, "requests": 32, "errors": 0, "wall_s": 18.64, "completion_tokens_total": 8192, "aggregate_completion_tokens_per_s": 439.44, "per_request_e2e_tokens_per_s_median": 27.793906675859194, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 10.29, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 199.09, "per_request_e2e_tokens_per_s_median": 50.8252424029093, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `concurrency8-summary.json`: `{"clients": 8, "requests": 16, "errors": 0, "wall_s": 13.35, "completion_tokens_total": 4096, "aggregate_completion_tokens_per_s": 306.79, "per_request_e2e_tokens_per_s_median": 38.60579948896346, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
