# 2026-11-22 · vllm · confirm-vllm-qwen36-nothink (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | nvidia/Qwen3.6-35B-A3B-NVFP4 |
| 받은 파일 | 전체/엔진 기본 (예상 23 GB) |
| 엔진 옵션 | `--max-model-len 65536 --trust-remote-code --kv-cache-dtype fp8 --attention-backend flashinfer --moe-backend marlin --gpu-memory-utilization 0.6 --max-num-seqs 16 --max-num-batched-tokens 8192 --enable-chunked-prefill --async-scheduling --enable-prefix-caching --reasoning-parser qwen3 --speculative-config {"method":"mtp","num_speculative_tokens":3,"moe_backend":"triton"} --enable-auto-tool-choice --tool-call-parser qwen3_xml` |
| API 별칭 | confirm-vllm-qwen36-nothink |
| 측정 프로필 | confirm |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "sanity-2048": "ok",
 "context-512": "ok",
 "context-2k": "ok",
 "context-8k": "ok",
 "context-32k": "ok",
 "throughput-1": "ok",
 "throughput-2": "ok",
 "throughput-3": "ok",
 "throughput-4": "ok",
 "throughput-5": "ok",
 "concurrency1": "ok",
 "concurrency4": "ok",
 "concurrency8": "ok",
 "concurrency16": "ok",
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| concurrency1-client1 | 2/2 | 0 | - | 2 | 170 | 0.1 | None | None | None | 97.78 | - |
| concurrency16-client1 | 2/2 | 0 | - | 2 | 170 | 0.31 | None | None | None | 30.71 | - |
| concurrency16-client10 | 2/2 | 0 | - | 2 | 170 | 0.37 | None | None | None | 30.85 | - |
| concurrency16-client11 | 2/2 | 0 | - | 2 | 170 | 0.34 | None | None | None | 30.95 | - |
| concurrency16-client12 | 2/2 | 0 | - | 2 | 170 | 0.28 | None | None | None | 32.04 | - |
| concurrency16-client13 | 2/2 | 0 | - | 2 | 170 | 0.3 | None | None | None | 32.52 | - |
| concurrency16-client14 | 2/2 | 0 | - | 2 | 170 | 0.33 | None | None | None | 30.76 | - |
| concurrency16-client15 | 2/2 | 0 | - | 2 | 170 | 0.39 | None | None | None | 32.37 | - |
| concurrency16-client16 | 2/2 | 0 | - | 2 | 170 | 0.34 | None | None | None | 31.45 | - |
| concurrency16-client2 | 2/2 | 0 | - | 2 | 170 | 0.39 | None | None | None | 32.19 | - |
| concurrency16-client3 | 2/2 | 0 | - | 2 | 170 | 0.4 | None | None | None | 31.85 | - |
| concurrency16-client4 | 2/2 | 0 | - | 2 | 170 | 0.37 | None | None | None | 31.04 | - |
| concurrency16-client5 | 2/2 | 0 | - | 2 | 170 | 0.31 | None | None | None | 31.48 | - |
| concurrency16-client6 | 2/2 | 0 | - | 2 | 170 | 0.28 | None | None | None | 31.43 | - |
| concurrency16-client7 | 2/2 | 0 | - | 2 | 170 | 0.3 | None | None | None | 30.85 | - |
| concurrency16-client8 | 2/2 | 0 | - | 2 | 170 | 0.36 | None | None | None | 31.38 | - |
| concurrency16-client9 | 2/2 | 0 | - | 2 | 170 | 0.38 | None | None | None | 31.49 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 170 | 0.2 | None | None | None | 62.26 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 170 | 0.22 | None | None | None | 59.8 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 170 | 0.19 | None | None | None | 59.92 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 170 | 0.22 | None | None | None | 61.08 | - |
| concurrency8-client1 | 2/2 | 0 | - | 2 | 170 | 0.2 | None | None | None | 46.29 | - |
| concurrency8-client2 | 2/2 | 0 | - | 2 | 170 | 0.24 | None | None | None | 45.23 | - |
| concurrency8-client3 | 2/2 | 0 | - | 2 | 170 | 0.23 | None | None | None | 42.78 | - |
| concurrency8-client4 | 2/2 | 0 | - | 2 | 170 | 0.23 | None | None | None | 43.52 | - |
| concurrency8-client5 | 2/2 | 0 | - | 2 | 170 | 0.23 | None | None | None | 43.55 | - |
| concurrency8-client6 | 2/2 | 0 | - | 2 | 170 | 0.23 | None | None | None | 43.84 | - |
| concurrency8-client7 | 2/2 | 0 | - | 2 | 170 | 0.24 | None | None | None | 43.0 | - |
| concurrency8-client8 | 2/2 | 0 | - | 2 | 170 | 0.22 | None | None | None | 43.37 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2866 | 0.39 | None | None | None | 15.34 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44905 | 1.1 | None | None | None | 5.79 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 765 | 0.16 | None | None | None | 36.38 | - |
| context-8k | 3/3 | 3 | 2/3 | 0 | 11271 | 0.45 | None | None | None | 12.76 | - |
| quality-gsm8k-l | 300/300 | 299 | 290/299 | 1 | 82 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k-l | 300/300 | 299 | 275/299 | 1 | 98 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 164 | 157/164 | 0 | 154 | None | None | None | None | None | - |
| quality-kmmlu-l | 300/300 | 294 | 213/294 | 6 | 131 | None | None | None | None | None | - |
| quality-mmlu-pro-l | 420/420 | 392 | 329/392 | 28 | 184 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 54 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 758 | None | None | None | None | None | - |
| sanity-2048 | 12/12 | 12 | 12/12 | 0 | 46 | 0.08 | None | None | None | 37.95 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 170 | 0.39 | None | None | None | 86.63 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 170 | 0.09 | None | None | None | 95.24 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 170 | 0.09 | None | None | None | 101.66 | - |
| throughput-4 | 1/1 | 0 | - | 1 | 170 | 0.1 | None | None | None | 100.5 | - |
| throughput-5 | 1/1 | 0 | - | 1 | 170 | 0.1 | None | None | None | 91.64 | - |

- 품질 `gsm8k-l-subset-zeroshot`: 정답 290/300, 잘림 1, 평균 출력 346.0 토큰
- 품질 `hrm8k-gsm8k-l-subset-zeroshot`: 정답 275/300, 잘림 1, 평균 출력 323.9 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 157/164, 잘림 0, 평균 출력 271.4 토큰
- 품질 `kmmlu-l-subset-zeroshot`: 정답 213/300, 잘림 6, 평균 출력 711.1 토큰
- 품질 `mmlu-pro-l-subset-zeroshot`: 정답 329/420, 잘림 28, 평균 출력 1264.5 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 0, 평균 출력 550.0 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 44.7 토큰
- `concurrency1-summary.json`: `{"clients": 1, "requests": 2, "errors": 0, "wall_s": 5.24, "completion_tokens_total": 512, "aggregate_completion_tokens_per_s": 97.7, "per_request_e2e_tokens_per_s_median": 100.50072156351018, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `concurrency16-summary.json`: `{"clients": 16, "requests": 32, "errors": 0, "wall_s": 16.94, "completion_tokens_total": 8192, "aggregate_completion_tokens_per_s": 483.57, "per_request_e2e_tokens_per_s_median": 31.822499139588707, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 8.62, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 237.57, "per_request_e2e_tokens_per_s_median": 61.06637819941139, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `concurrency8-summary.json`: `{"clients": 8, "requests": 16, "errors": 0, "wall_s": 12.11, "completion_tokens_total": 4096, "aggregate_completion_tokens_per_s": 338.31, "per_request_e2e_tokens_per_s_median": 44.202562779595766, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
