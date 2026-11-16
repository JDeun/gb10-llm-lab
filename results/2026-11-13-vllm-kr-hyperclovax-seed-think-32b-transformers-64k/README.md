# 2026-11-14 · vllm · vllm-kr-hyperclovax-seed-think-32b-transformers-64k (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | naver-hyperclovax/HyperCLOVAX-SEED-Think-32B |
| 받은 파일 | 전체/엔진 기본 (예상 67 GB) |
| 엔진 옵션 | `--max-model-len 65536 --max-num-seqs 4 --gpu-memory-utilization 0.85 --trust-remote-code --reasoning-parser deepseek_r1 --model-impl transformers` |
| API 별칭 | vllm-kr-hyperclovax-seed-think-32b-transformers-64k |
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
 "throughput-1": "ok",
 "throughput-2": "ok",
 "throughput-3": "ok",
 "concurrency4": "ok",
 "vision-check": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 165 | 0.53 | None | None | None | 1.87 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 165 | 0.43 | None | None | None | 3.57 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 165 | 0.3 | None | None | None | 3.69 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 165 | 0.31 | None | None | None | 3.69 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 165 | 0.84 | None | None | None | 3.59 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 165 | 0.84 | None | None | None | 3.59 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 165 | 0.83 | None | None | None | 3.59 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 165 | 0.57 | None | None | None | 3.61 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2911 | 0.59 | None | None | None | 3.61 | - |
| context-32k | 3/3 | 3 | 1/3 | 0 | 45648 | 0.8 | None | None | None | 2.93 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 778 | 0.58 | None | None | None | 3.64 | - |
| context-8k | 3/3 | 3 | 2/3 | 0 | 11436 | 0.63 | None | None | None | 3.46 | - |
| sanity-2048 | 12/12 | 11 | 10/11 | 1 | 45 | 0.56 | None | None | None | 3.66 | - |
| sanity-512 | 12/12 | 11 | 10/11 | 1 | 45 | 0.59 | None | None | None | 3.67 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 165 | 0.41 | None | None | None | 3.68 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 165 | 0.31 | None | None | None | 3.68 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 165 | 0.31 | None | None | None | 3.68 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 142.47, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 14.38, "per_request_e2e_tokens_per_s_median": 3.5955458876370843, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `vision-check.json`: `{"cases": 3, "passed": 3, "errors": 0}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
