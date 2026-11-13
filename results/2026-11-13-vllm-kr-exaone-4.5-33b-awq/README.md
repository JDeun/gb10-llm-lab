# 2026-11-13 · vllm · vllm-kr-exaone-4.5-33b-awq (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | LGAI-EXAONE/EXAONE-4.5-33B-AWQ |
| 받은 파일 | 전체/엔진 기본 (예상 23 GB) |
| 엔진 옵션 | `--max-model-len 131072 --max-num-seqs 4 --gpu-memory-utilization 0.6 --trust-remote-code --reasoning-parser deepseek_r1` |
| API 별칭 | vllm-kr-exaone-4.5-33b-awq |
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
 "context-60k": "ok",
 "throughput-1": "ok",
 "throughput-2": "ok",
 "throughput-3": "ok",
 "concurrency4": "ok",
 "vision-check": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 123 | 0.21 | None | None | None | 4.67 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 123 | 0.12 | None | None | None | 12.05 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 123 | 0.11 | None | None | None | 12.33 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 123 | 0.11 | None | None | None | 12.31 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 123 | 0.25 | None | None | None | 12.52 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 123 | 0.25 | None | None | None | 12.51 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 123 | 0.21 | None | None | None | 12.54 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 123 | 0.17 | None | None | None | 12.56 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2778 | 0.18 | None | None | None | 11.66 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 43551 | 52.7 | None | None | None | 5.8 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 733 | 0.17 | None | None | None | 12.3 | - |
| context-60k | 3/3 | 2 | 0/2 | 1 | 79493 | 102.89 | None | None | None | 4.78 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 10901 | 12.4 | None | None | None | 9.42 | - |
| sanity-2048 | 12/12 | 11 | 11/11 | 1 | 39 | 0.16 | None | None | None | 12.27 | - |
| sanity-512 | 12/12 | 6 | 6/6 | 6 | 39 | 0.13 | None | None | None | 12.26 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 123 | 0.11 | None | None | None | 12.54 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 123 | 0.11 | None | None | None | 12.55 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 123 | 0.12 | None | None | None | 12.53 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 40.92, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 50.05, "per_request_e2e_tokens_per_s_median": 12.547859191666037, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`
- `vision-check.json`: `{"cases": 3, "passed": 0, "errors": 0}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
