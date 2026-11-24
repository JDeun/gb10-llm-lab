# 2026-11-24 · vllm · vllm-qwen38-27b-nvfp4-mtp-refpin (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | RedHatAI/Qwen3.8-27B-NVFP4 |
| 받은 파일 | 전체/엔진 기본 (예상 25 GB) |
| 엔진 옵션 | `--max-model-len 131072 --gpu-memory-utilization 0.45 --max-num-seqs 8 --enable-prefix-caching --tool-call-parser qwen3_xml --enable-auto-tool-choice --reasoning-parser qwen3 --speculative-config {"method":"mtp","num_speculative_tokens":3}` |
| API 별칭 | vllm-qwen38-27b-nvfp4-mtp-refpin |
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
 "context-60k": "ok",
 "throughput-1": "ok",
 "throughput-2": "ok",
 "throughput-3": "ok",
 "concurrency1": "ok",
 "concurrency4": "ok",
 "concurrency8": "ok",
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 0.19 | None | None | None | 5.31 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.58 | None | None | None | 13.49 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.16 | None | None | None | 16.87 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.16 | None | None | None | 19.28 | - |
| concurrency1-client1 | 2/2 | 0 | - | 2 | 210 | 0.18 | None | None | None | 16.76 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.6 | None | None | None | 15.76 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.5 | None | None | None | 16.71 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.59 | None | None | None | 16.67 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.59 | None | None | None | 16.13 | - |
| concurrency8-client1 | 2/2 | 0 | - | 2 | 210 | 0.74 | None | None | None | 14.79 | - |
| concurrency8-client2 | 2/2 | 0 | - | 2 | 210 | 0.7 | None | None | None | 14.68 | - |
| concurrency8-client3 | 2/2 | 0 | - | 2 | 210 | 0.72 | None | None | None | 14.8 | - |
| concurrency8-client4 | 2/2 | 0 | - | 2 | 210 | 0.7 | None | None | None | 14.49 | - |
| concurrency8-client5 | 2/2 | 0 | - | 2 | 210 | 0.71 | None | None | None | 14.59 | - |
| concurrency8-client6 | 2/2 | 0 | - | 2 | 210 | 0.69 | None | None | None | 14.83 | - |
| concurrency8-client7 | 2/2 | 0 | - | 2 | 210 | 0.53 | None | None | None | 17.02 | - |
| concurrency8-client8 | 2/2 | 0 | - | 2 | 210 | 0.69 | None | None | None | 14.73 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 1.27 | None | None | None | 16.04 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44945 | 1.36 | None | None | None | 15.87 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 0.49 | None | None | None | 19.12 | - |
| context-60k | 3/3 | 3 | 3/3 | 0 | 82071 | 2.36 | None | None | None | 14.45 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 0.91 | None | None | None | 19.33 | - |
| quality-gsm8k | 100/100 | 100 | 95/100 | 0 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 96/100 | 0 | 140 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 159 | 149/159 | 5 | 194 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 67 | 52/67 | 33 | 177 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 127 | 112/127 | 13 | 227 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 94 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 794 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.32 | None | None | None | 21.53 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.17 | None | None | None | 16.71 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.16 | None | None | None | 16.77 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.17 | None | None | None | 16.76 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 95/100, 잘림 0, 평균 출력 561.7 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 96/100, 잘림 0, 평균 출력 484.3 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 149/164, 잘림 5, 평균 출력 1690.3 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 52/100, 잘림 33, 평균 출력 7319.4 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 112/140, 잘림 13, 평균 출력 3368.8 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 0, 평균 출력 2118.6 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 92.4 토큰
- `concurrency1-summary.json`: `{"clients": 1, "requests": 2, "errors": 0, "wall_s": 30.55, "completion_tokens_total": 512, "aggregate_completion_tokens_per_s": 16.76, "per_request_e2e_tokens_per_s_median": 16.76602722181904, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 32.53, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 62.96, "per_request_e2e_tokens_per_s_median": 16.181103881175368, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `concurrency8-summary.json`: `{"clients": 8, "requests": 16, "errors": 0, "wall_s": 35.4, "completion_tokens_total": 4096, "aggregate_completion_tokens_per_s": 115.7, "per_request_e2e_tokens_per_s_median": 14.720939887199648, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
