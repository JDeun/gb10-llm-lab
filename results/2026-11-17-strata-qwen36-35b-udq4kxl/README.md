# 2026-11-17 · strata · strata-qwen36-35b-udq4kxl (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | unsloth/Qwen3.6-35B-A3B-GGUF (UD-Q4_K_XL via Strata) |
| 받은 파일 | 전체/엔진 기본 (예상 22 GB) |
| 엔진 옵션 | `--family qwen36 --model ud-q4_k_xl --context 64k --vision off --tune skip` |
| API 별칭 | qwen3.6-35b-a3b-ud-q4_k_xl |
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
 "context-32k": "ok",
 "throughput-1": "ok",
 "throughput-2": "ok",
 "throughput-3": "ok",
 "concurrency4": "ok",
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 0.15 | 0.15 | 1266.0 | 10000.0 | 6.56 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.15 | 0.15 | 1305.4 | 68.5 | 42.09 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.14 | 0.14 | 1374.8 | 66.1 | 63.77 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.14 | 0.14 | 1375.9 | 66.9 | 58.36 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 168 | 0.16 | 0.17 | 1373.7 | 39.2 | 38.25 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 168 | 0.49 | 0.57 | 1365.9 | 41.15 | 38.14 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 168 | 0.24 | 0.31 | 1357.0 | 39.5 | 38.14 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 168 | 0.36 | 0.42 | 1361.4 | 40.3 | 38.18 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2864 | 1.06 | 1.06 | 2762.1 | 60.9 | 43.38 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44903 | 36.03 | 36.11 | 1247.6 | 9.5 | 4.72 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 763 | 0.31 | 0.32 | 2631.0 | 64.7 | 56.73 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11269 | 4.71 | 4.72 | 2408.1 | 48.4 | 25.55 | - |
| quality-gsm8k | 100/100 | 100 | 95/100 | 0 | 82 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 92/100 | 0 | 98 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 164 | 162/164 | 0 | 152 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 100 | 66/100 | 0 | 135 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 134 | 113/134 | 6 | 185 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 52 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 11/12 | 0 | 702 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 9 | 9/9 | 3 | 44 | 0.1 | 0.11 | 537.0 | 66.5 | 64.96 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 168 | 0.14 | 0.14 | 1353.7 | 65.5 | 63.26 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 168 | 0.15 | 0.15 | 1338.6 | 65.5 | 63.07 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 168 | 0.14 | 0.14 | 1360.3 | 65.5 | 63.26 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 95/100, 잘림 0, 평균 출력 1217.9 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 92/100, 잘림 0, 평균 출력 1300.0 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 162/164, 잘림 0, 평균 출력 2346.1 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 66/100, 잘림 0, 평균 출력 2327.7 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 113/140, 잘림 6, 평균 출력 2955.6 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 0, 평균 출력 1781.5 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 11/12, 잘림 0, 평균 출력 277.6 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 13.49, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 151.83, "per_request_e2e_tokens_per_s_median": 38.302895355953254, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
