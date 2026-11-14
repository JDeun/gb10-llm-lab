# 2026-11-14 · vllm · vllm-mistral-medium-3.5-128b-nvfp4 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | nvidia/Mistral-Medium-3.5-128B-NVFP4 |
| 받은 파일 | 전체/엔진 기본 (예상 95 GB) |
| 엔진 옵션 | `--max-model-len 32768 --max-num-seqs 2 --gpu-memory-utilization 0.92` |
| API 별칭 | vllm-mistral-medium-3.5-128b-nvfp4 |
| 측정 프로필 | slow |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "capacity-cap1": "ok",
 "capacity-cap16": "ok",
 "capacity-cap64": "ok",
 "sanity-512": "ok",
 "context-512": "ok",
 "context-2k": "ok",
 "context-8k": "ok",
 "throughput-1": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 176 | 0.7 | None | None | None | 1.43 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 176 | 0.57 | None | None | None | 2.47 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 176 | 0.43 | None | None | None | 2.54 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2832 | 0.81 | None | None | None | 2.19 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 754 | 1.02 | None | None | None | 2.11 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11088 | 0.84 | None | None | None | 2.18 | - |
| sanity-512 | 12/12 | 12 | 11/12 | 0 | 50 | 0.82 | None | None | None | 2.18 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 176 | 0.6 | None | None | None | 2.52 | - |


측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
