# 2026-11-14 · ikllama · ikllama-glm53-flash-udq2kxl (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | unsloth/GLM-5.3-Flash-GGUF |
| 받은 파일 | UD-Q2_K_XL/* (예상 109 GB) |
| 엔진 옵션 | `-c 32768 -ot exps=CPU` |
| API 별칭 | ikllama-glm53-flash-udq2kxl |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 271 | 4.06 | 4.06 | 73.3 | 1000000.0 | 0.25 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 271 | 0.35 | None | 17.71 | 6.84 | 5.96 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 271 | 0.35 | None | 16.08 | 6.62 | 6.39 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2355 | 4.11 | 24.28 | 75.53 | 6.66 | 3.99 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 632 | 7.5 | 7.66 | 84.74 | 6.66 | 3.18 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 9348 | 12.83 | 91.38 | 90.66 | 6.59 | 2.59 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 46 | 1.38 | 1.72 | 35.37 | 6.64 | 5.7 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 271 | 0.65 | None | 16.17 | 6.58 | 6.48 | - |


측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
