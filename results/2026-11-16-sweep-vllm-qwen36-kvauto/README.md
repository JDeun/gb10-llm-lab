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
 "concurrency4": "ok",
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 0.41 | None | None | None | 2.43 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.5 | None | None | None | 27.66 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 108.92 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 102.13 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 168 | 0.23 | None | None | None | 68.26 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 168 | 0.21 | None | None | None | 69.09 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 168 | 0.25 | None | None | None | 69.92 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 168 | 0.25 | None | None | None | 69.05 | - |
| quality-gsm8k | 100/100 | 99 | 95/99 | 1 | 82 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 91 | 86/91 | 9 | 98 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 142 | 137/142 | 22 | 152 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 80 | 61/80 | 20 | 135 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 82 | 74/82 | 58 | 185 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 52 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 756 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 10 | 10/10 | 2 | 44 | 0.08 | None | None | None | 136.16 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 110.02 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 109.38 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 102.19 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 95/100, 잘림 1, 평균 출력 1251.3 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 86/100, 잘림 9, 평균 출력 1380.5 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 137/164, 잘림 22, 평균 출력 2470.2 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 61/100, 잘림 20, 평균 출력 2496.2 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 74/140, 잘림 58, 평균 출력 3096.3 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 0, 평균 출력 1818.8 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 251.7 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 7.51, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 272.81, "per_request_e2e_tokens_per_s_median": 68.91530353146099, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
