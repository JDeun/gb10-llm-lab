# 2026-11-16 · vllm · sweep-vllm-qwen36-nothink (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | nvidia/Qwen3.6-35B-A3B-NVFP4 |
| 받은 파일 | 전체/엔진 기본 (예상 23 GB) |
| 엔진 옵션 | `--max-model-len 65536 --trust-remote-code --kv-cache-dtype fp8 --attention-backend flashinfer --moe-backend marlin --gpu-memory-utilization 0.6 --max-num-seqs 16 --max-num-batched-tokens 8192 --enable-chunked-prefill --async-scheduling --enable-prefix-caching --reasoning-parser qwen3 --speculative-config {"method":"mtp","num_speculative_tokens":3,"moe_backend":"triton"} --enable-auto-tool-choice --tool-call-parser qwen3_xml` |
| API 별칭 | sweep-vllm-qwen36-nothink |
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
 "concurrency4": "ok",
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 170 | 0.41 | None | None | None | 2.46 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 170 | 0.48 | None | None | None | 25.6 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 170 | 0.09 | None | None | None | 98.78 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 170 | 0.09 | None | None | None | 91.09 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 170 | 0.19 | None | None | None | 59.85 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 170 | 0.17 | None | None | None | 63.74 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 170 | 0.18 | None | None | None | 64.11 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 170 | 0.2 | None | None | None | 61.78 | - |
| quality-gsm8k | 100/100 | 100 | 95/100 | 0 | 84 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 94/100 | 0 | 100 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 164 | 156/164 | 0 | 154 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 98 | 68/98 | 2 | 137 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 130 | 114/130 | 10 | 187 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 54 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 758 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 46 | 0.08 | None | None | None | 39.12 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 170 | 0.09 | None | None | None | 90.62 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 170 | 0.1 | None | None | None | 95.87 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 170 | 0.09 | None | None | None | 98.84 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 95/100, 잘림 0, 평균 출력 320.4 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 94/100, 잘림 0, 평균 출력 296.6 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 156/164, 잘림 0, 평균 출력 274.6 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 68/100, 잘림 2, 평균 출력 813.7 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 114/140, 잘림 10, 평균 출력 1228.2 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 0, 평균 출력 565.3 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 48.2 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 8.56, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 239.22, "per_request_e2e_tokens_per_s_median": 63.024994682858974, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
