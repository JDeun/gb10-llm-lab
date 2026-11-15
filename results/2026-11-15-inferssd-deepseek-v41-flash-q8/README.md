# 2026-11-16 · inferssd · inferssd-deepseek-v41-flash-q8 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | mrfakename/DeepSeek-V4.1-Flash-1017-GGUF |
| 받은 파일 | 전체/엔진 기본 (예상 505 GB) |
| 엔진 옵션 | `` |
| API 별칭 | DeepSeek-V4.1-Flash-1017-Q8_0-00001-of-00010.gguf |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 224 | 22.87 | 22.87 | 9.8 | 1000000.0 | 0.04 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 224 | 2.16 | None | 1.87 | 2.52 | 1.88 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 224 | 1.26 | None | 3.22 | 5.97 | 5.34 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2369 | 32.84 | 33.14 | 72.2 | 8.4 | 0.87 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 646 | 26.33 | 26.49 | 24.56 | 8.97 | 1.05 | - |
| context-8k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'http_error', 'status': 400, 'detail': '{"error":{" |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 65 | 13.85 | 15.25 | 4.45 | 8.57 | 2.39 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 224 | 0.83 | None | 5.06 | 8.02 | 7.82 | - |


측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
