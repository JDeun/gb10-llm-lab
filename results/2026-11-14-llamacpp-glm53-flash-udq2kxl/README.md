# 2026-11-14 · llamacpp · llamacpp-glm53-flash-udq2kxl (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | unsloth/GLM-5.3-Flash-GGUF |
| 받은 파일 | UD-Q2_K_XL/* (예상 109 GB) |
| 엔진 옵션 | `-c 32768 --cpu-moe` |
| API 별칭 | llamacpp-glm53-flash-udq2kxl |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 271 | 3.65 | 3.65 | 74.56 | 0.0 | 0.27 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 271 | 0.41 | None | 10.13 | 3.87 | 3.73 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 271 | 0.39 | None | 10.57 | 3.88 | 3.85 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2355 | 3.62 | 16.24 | 143.58 | 3.86 | 3.1 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 632 | 3.56 | None | 145.78 | 3.89 | 2.99 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 9348 | 4.08 | 59.92 | 135.73 | 3.84 | 3.08 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 46 | 1.6 | None | 24.58 | 3.84 | 3.53 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 271 | 0.63 | None | 10.13 | 3.85 | 3.83 | - |


측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
