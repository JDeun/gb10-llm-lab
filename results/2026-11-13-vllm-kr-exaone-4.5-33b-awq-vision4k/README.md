# 2026-11-13 · vllm · vllm-kr-exaone-4.5-33b-awq-vision4k (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | LGAI-EXAONE/EXAONE-4.5-33B-AWQ |
| 받은 파일 | 전체/엔진 기본 (예상 23 GB) |
| 엔진 옵션 | `--max-model-len 131072 --max-num-seqs 4 --gpu-memory-utilization 0.6 --trust-remote-code --reasoning-parser deepseek_r1` |
| API 별칭 | vllm-kr-exaone-4.5-33b-awq-vision4k |
| 측정 프로필 | capacity |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "capacity-cap1": "ok",
 "capacity-cap16": "ok",
 "capacity-cap64": "ok",
 "sanity-mini-512": "ok",
 "context-512": "ok",
 "throughput-1": "ok",
 "vision-check": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 123 | 0.21 | None | None | None | 4.74 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 123 | 0.11 | None | None | None | 12.28 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 123 | 0.12 | None | None | None | 12.42 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 733 | 0.17 | None | None | None | 12.21 | - |
| sanity-mini-512 | 4/4 | 2 | 2/2 | 2 | 25 | 0.12 | None | None | None | 12.46 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 123 | 0.12 | None | None | None | 12.39 | - |

- `vision-check.json`: `{"cases": 3, "passed": 0, "errors": 0}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
