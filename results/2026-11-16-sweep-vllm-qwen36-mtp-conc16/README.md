# 2026-11-16 · vllm · sweep-vllm-qwen36-mtp-conc16 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | nvidia/Qwen3.6-35B-A3B-NVFP4 |
| 받은 파일 | 전체/엔진 기본 (예상 23 GB) |
| 엔진 옵션 | `--max-model-len 65536 --trust-remote-code --kv-cache-dtype fp8 --attention-backend flashinfer --moe-backend marlin --gpu-memory-utilization 0.6 --max-num-seqs 16 --max-num-batched-tokens 8192 --enable-chunked-prefill --async-scheduling --enable-prefix-caching --reasoning-parser qwen3 --speculative-config {"method":"mtp","num_speculative_tokens":3,"moe_backend":"triton"} --enable-auto-tool-choice --tool-call-parser qwen3_xml` |
| API 별칭 | sweep-vllm-qwen36-mtp-conc16 |
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
 "concurrency16": "ok",
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 0.42 | None | None | None | 2.35 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.47 | None | None | None | 29.45 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.1 | None | None | None | 109.29 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.1 | None | None | None | 97.57 | - |
| concurrency1-client1 | 2/2 | 0 | - | 2 | 168 | 0.09 | None | None | None | 113.44 | - |
| concurrency16-client1 | 2/2 | 0 | - | 2 | 168 | 0.2 | None | None | None | 35.26 | - |
| concurrency16-client10 | 2/2 | 0 | - | 2 | 168 | 0.35 | None | None | None | 36.34 | - |
| concurrency16-client11 | 2/2 | 0 | - | 2 | 168 | 0.38 | None | None | None | 35.87 | - |
| concurrency16-client12 | 2/2 | 0 | - | 2 | 168 | 0.4 | None | None | None | 35.39 | - |
| concurrency16-client13 | 2/2 | 0 | - | 2 | 168 | 0.39 | None | None | None | 34.96 | - |
| concurrency16-client14 | 2/2 | 0 | - | 2 | 168 | 0.37 | None | None | None | 35.53 | - |
| concurrency16-client15 | 2/2 | 0 | - | 2 | 168 | 0.41 | None | None | None | 36.08 | - |
| concurrency16-client16 | 2/2 | 0 | - | 2 | 168 | 0.35 | None | None | None | 36.43 | - |
| concurrency16-client2 | 2/2 | 0 | - | 2 | 168 | 0.37 | None | None | None | 36.83 | - |
| concurrency16-client3 | 2/2 | 0 | - | 2 | 168 | 0.4 | None | None | None | 34.39 | - |
| concurrency16-client4 | 2/2 | 0 | - | 2 | 168 | 0.36 | None | None | None | 35.88 | - |
| concurrency16-client5 | 2/2 | 0 | - | 2 | 168 | 0.46 | None | None | None | 35.85 | - |
| concurrency16-client6 | 2/2 | 0 | - | 2 | 168 | 0.45 | None | None | None | 35.6 | - |
| concurrency16-client7 | 2/2 | 0 | - | 2 | 168 | 0.37 | None | None | None | 36.01 | - |
| concurrency16-client8 | 2/2 | 0 | - | 2 | 168 | 0.41 | None | None | None | 37.08 | - |
| concurrency16-client9 | 2/2 | 0 | - | 2 | 168 | 0.38 | None | None | None | 36.98 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 168 | 0.17 | None | None | None | 67.45 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 168 | 0.21 | None | None | None | 67.05 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 168 | 0.19 | None | None | None | 68.62 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 168 | 0.22 | None | None | None | 67.23 | - |
| concurrency8-client1 | 2/2 | 0 | - | 2 | 168 | 0.28 | None | None | None | 49.92 | - |
| concurrency8-client2 | 2/2 | 0 | - | 2 | 168 | 0.29 | None | None | None | 48.91 | - |
| concurrency8-client3 | 2/2 | 0 | - | 2 | 168 | 0.3 | None | None | None | 50.19 | - |
| concurrency8-client4 | 2/2 | 0 | - | 2 | 168 | 0.3 | None | None | None | 51.41 | - |
| concurrency8-client5 | 2/2 | 0 | - | 2 | 168 | 0.29 | None | None | None | 48.75 | - |
| concurrency8-client6 | 2/2 | 0 | - | 2 | 168 | 0.24 | None | None | None | 51.7 | - |
| concurrency8-client7 | 2/2 | 0 | - | 2 | 168 | 0.27 | None | None | None | 49.19 | - |
| concurrency8-client8 | 2/2 | 0 | - | 2 | 168 | 0.25 | None | None | None | 50.41 | - |
| quality-gsm8k | 100/100 | 99 | 95/99 | 1 | 82 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 94 | 90/94 | 6 | 98 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 142 | 136/142 | 22 | 152 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 81 | 61/81 | 19 | 135 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 78 | 73/78 | 62 | 185 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 52 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 756 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 11 | 11/11 | 1 | 44 | 0.07 | None | None | None | 134.28 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 111.76 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 117.91 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 114.19 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 95/100, 잘림 1, 평균 출력 1263.0 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 90/100, 잘림 6, 평균 출력 1241.6 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 136/164, 잘림 22, 평균 출력 2441.8 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 61/100, 잘림 19, 평균 출력 2473.6 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 73/140, 잘림 62, 평균 출력 3112.8 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 0, 평균 출력 1789.4 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 200.6 토큰
- `concurrency1-summary.json`: `{"clients": 1, "requests": 2, "errors": 0, "wall_s": 4.52, "completion_tokens_total": 512, "aggregate_completion_tokens_per_s": 113.28, "per_request_e2e_tokens_per_s_median": 117.57681597026108, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `concurrency16-summary.json`: `{"clients": 16, "requests": 32, "errors": 0, "wall_s": 15.04, "completion_tokens_total": 8192, "aggregate_completion_tokens_per_s": 544.61, "per_request_e2e_tokens_per_s_median": 36.040216751798745, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 7.69, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 266.34, "per_request_e2e_tokens_per_s_median": 67.33829312090388, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `concurrency8-summary.json`: `{"clients": 8, "requests": 16, "errors": 0, "wall_s": 10.52, "completion_tokens_total": 4096, "aggregate_completion_tokens_per_s": 389.2, "per_request_e2e_tokens_per_s_median": 50.32922439472478, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
