# 2026-11-19 · llamacpp · quality-llamacpp-kr-solar-open-100b-q4km-nothink (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | mradermacher/Solar-Open-100B-GGUF |
| 받은 파일 | Solar-Open-100B.Q4_K_M.gguf (예상 62 GB) |
| 엔진 옵션 | `-c 32768 --reasoning-budget 0` |
| API 별칭 | quality-llamacpp-kr-solar-open-100b-q4km-nothink |
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
 "throughput-1": "ok",
 "throughput-2": "ok",
 "throughput-3": "ok",
 "concurrency4": "ok",
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 182 | None | None | 275.52 | 0.0 | 1.02 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 182 | 0.12 | None | 20.74 | 24.17 | 22.96 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 182 | 0.11 | None | 24.48 | 24.37 | 24.3 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 182 | 0.1 | None | 23.65 | 24.4 | 24.22 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 182 | 0.35 | None | 22.5 | 15.5 | 15.41 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 182 | 0.33 | None | 360.24 | 15.61 | 15.43 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 182 | 0.32 | None | 359.32 | 15.61 | 15.43 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 182 | 0.33 | None | 22.35 | 15.61 | 15.42 | - |
| context-2k | 3/3 | 3 | 0/3 | 0 | 2805 | 0.19 | None | 116.47 | 22.79 | 22.47 | - |
| context-512 | 3/3 | 3 | 0/3 | 0 | 791 | 0.19 | None | 117.2 | 23.76 | 23.2 | - |
| context-8k | 3/3 | 1 | 0/1 | 2 | 10829 | 0.23 | None | 113.34 | 19.96 | 19.88 | - |
| quality-gsm8k | 100/100 | 100 | 94/100 | 0 | 139 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 99 | 94/99 | 1 | 138 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 84 | 89/84 | 80 | 208 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 64 | 50/64 | 36 | 163 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 113 | 107/113 | 27 | 230 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 9 | - | 3 | 99 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 0 | 0/0 | 0 | None | None | None | None | None | None | HTTPError: HTTP Error 500: Internal Server Error |
| sanity-512 | 12/12 | 12 | 0/12 | 0 | 99 | 0.25 | None | 199.32 | 24.2 | 23.45 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 182 | 0.47 | None | 23.35 | 24.29 | 23.44 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 182 | 0.12 | None | 23.21 | 24.2 | 24.12 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 182 | 0.1 | None | 23.16 | 24.27 | 24.22 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 94/100, 잘림 0, 평균 출력 569.0 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 94/100, 잘림 1, 평균 출력 786.6 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 89/164, 잘림 80, 평균 출력 2830.1 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 50/100, 잘림 36, 평균 출력 2356.5 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 107/140, 잘림 27, 평균 출력 1743.1 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 3, 평균 출력 1930.8 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 0/12, 잘림 0, 평균 출력 0.0 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 33.36, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 61.4, "per_request_e2e_tokens_per_s_median": 16.360747305922473, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
