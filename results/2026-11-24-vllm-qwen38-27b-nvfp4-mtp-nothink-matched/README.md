# 2026-11-24 · vllm · vllm-qwen38-27b-nvfp4-mtp-nothink-matched (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | RedHatAI/Qwen3.8-27B-NVFP4 |
| 받은 파일 | 전체/엔진 기본 (예상 25 GB) |
| 엔진 옵션 | `--max-model-len 65536 --kv-cache-dtype fp8 --gpu-memory-utilization 0.6 --max-num-seqs 16 --max-num-batched-tokens 8192 --enable-chunked-prefill --async-scheduling --enable-prefix-caching --reasoning-parser qwen3 --speculative-config {"method":"mtp","num_speculative_tokens":3} --enable-auto-tool-choice --tool-call-parser qwen3_xml` |
| API 별칭 | vllm-qwen38-27b-nvfp4-mtp-nothink-matched |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 170 | 0.17 | None | None | None | 6.01 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 170 | 0.56 | None | None | None | 9.82 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 170 | 0.16 | None | None | None | 15.88 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 170 | 0.16 | None | None | None | 14.0 | - |
| concurrency1-client1 | 2/2 | 0 | - | 2 | 170 | 0.25 | None | None | None | 15.79 | - |
| concurrency16-client1 | 2/2 | 0 | - | 2 | 170 | 1.23 | None | None | None | 11.62 | - |
| concurrency16-client10 | 2/2 | 0 | - | 2 | 170 | 1.22 | None | None | None | 11.63 | - |
| concurrency16-client11 | 2/2 | 0 | - | 2 | 170 | 1.32 | None | None | None | 11.57 | - |
| concurrency16-client12 | 2/2 | 0 | - | 2 | 170 | 1.01 | None | None | None | 11.46 | - |
| concurrency16-client13 | 2/2 | 0 | - | 2 | 170 | 1.04 | None | None | None | 11.29 | - |
| concurrency16-client14 | 2/2 | 0 | - | 2 | 170 | 1.24 | None | None | None | 11.62 | - |
| concurrency16-client15 | 2/2 | 0 | - | 2 | 170 | 1.24 | None | None | None | 11.62 | - |
| concurrency16-client16 | 2/2 | 0 | - | 2 | 170 | 0.78 | None | None | None | 11.16 | - |
| concurrency16-client2 | 2/2 | 0 | - | 2 | 170 | 1.25 | None | None | None | 11.61 | - |
| concurrency16-client3 | 2/2 | 0 | - | 2 | 170 | 1.23 | None | None | None | 11.62 | - |
| concurrency16-client4 | 2/2 | 0 | - | 2 | 170 | 1.32 | None | None | None | 11.58 | - |
| concurrency16-client5 | 2/2 | 0 | - | 2 | 170 | 0.51 | None | None | None | 11.5 | - |
| concurrency16-client6 | 2/2 | 0 | - | 2 | 170 | 1.25 | None | None | None | 11.61 | - |
| concurrency16-client7 | 2/2 | 0 | - | 2 | 170 | 1.24 | None | None | None | 11.62 | - |
| concurrency16-client8 | 2/2 | 0 | - | 2 | 170 | 1.24 | None | None | None | 11.62 | - |
| concurrency16-client9 | 2/2 | 0 | - | 2 | 170 | 1.26 | None | None | None | 11.61 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 170 | 0.37 | None | None | None | 15.58 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 170 | 0.46 | None | None | None | 15.05 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 170 | 0.51 | None | None | None | 15.46 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 170 | 0.48 | None | None | None | 15.38 | - |
| concurrency8-client1 | 2/2 | 0 | - | 2 | 170 | 0.59 | None | None | None | 14.24 | - |
| concurrency8-client2 | 2/2 | 0 | - | 2 | 170 | 0.65 | None | None | None | 13.82 | - |
| concurrency8-client3 | 2/2 | 0 | - | 2 | 170 | 0.68 | None | None | None | 13.89 | - |
| concurrency8-client4 | 2/2 | 0 | - | 2 | 170 | 0.69 | None | None | None | 14.31 | - |
| concurrency8-client5 | 2/2 | 0 | - | 2 | 170 | 0.64 | None | None | None | 13.83 | - |
| concurrency8-client6 | 2/2 | 0 | - | 2 | 170 | 0.68 | None | None | None | 14.31 | - |
| concurrency8-client7 | 2/2 | 0 | - | 2 | 170 | 0.64 | None | None | None | 13.95 | - |
| concurrency8-client8 | 2/2 | 0 | - | 2 | 170 | 0.7 | None | None | None | 13.88 | - |
| quality-gsm8k | 100/100 | 100 | 95/100 | 0 | 84 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 94/100 | 0 | 100 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 164 | 158/164 | 0 | 154 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 100 | 65/100 | 0 | 137 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 140 | 117/140 | 0 | 187 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 54 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 758 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 46 | 0.33 | None | None | None | 8.33 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 170 | 0.16 | None | None | None | 15.88 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 170 | 0.16 | None | None | None | 15.88 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 170 | 0.16 | None | None | None | 15.88 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 95/100, 잘림 0, 평균 출력 398.6 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 94/100, 잘림 0, 평균 출력 267.4 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 158/164, 잘림 0, 평균 출력 247.0 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 65/100, 잘림 0, 평균 출력 788.9 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 117/140, 잘림 0, 평균 출력 1373.6 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 0, 평균 출력 586.1 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 42.2 토큰
- `concurrency1-summary.json`: `{"clients": 1, "requests": 2, "errors": 0, "wall_s": 32.42, "completion_tokens_total": 512, "aggregate_completion_tokens_per_s": 15.79, "per_request_e2e_tokens_per_s_median": 15.879506702093073, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `concurrency16-summary.json`: `{"clients": 16, "requests": 32, "errors": 0, "wall_s": 46.02, "completion_tokens_total": 8192, "aggregate_completion_tokens_per_s": 178.0, "per_request_e2e_tokens_per_s_median": 11.531965246641931, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 34.04, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 60.17, "per_request_e2e_tokens_per_s_median": 15.245725450546178, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `concurrency8-summary.json`: `{"clients": 8, "requests": 16, "errors": 0, "wall_s": 37.06, "completion_tokens_total": 4096, "aggregate_completion_tokens_per_s": 110.52, "per_request_e2e_tokens_per_s_median": 14.223411807550228, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
