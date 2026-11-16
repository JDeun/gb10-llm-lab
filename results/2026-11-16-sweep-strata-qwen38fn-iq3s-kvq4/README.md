# 2026-11-17 · strata · sweep-strata-qwen38fn-iq3s-kvq4 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF (IQ3_S) |
| 받은 파일 | 전체/엔진 기본 (예상 84 GB) |
| 엔진 옵션 | `--family qwen --model iq3_s --context 64k --tune skip --vision off --drafting mtp --kv q4_0` |
| API 별칭 | qwen3.8-flash-next-iq3_s |
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
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 1.75 | 1.75 | 124.0 | 25.6 | 0.57 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 83.2 | 57.0 | 44.5 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.15 | None | 56.0 | 52.1 | 50.94 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.16 | None | 54.9 | 41.5 | 38.52 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.22 | None | 68.6 | 20.25 | 19.92 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.44 | None | 68.2 | 20.5 | 19.85 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.34 | None | 74.3 | 20.35 | 19.9 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.14 | None | 73.6 | 20.15 | 19.98 | - |
| quality-gsm8k | 100/100 | 100 | 96/100 | 0 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 97/100 | 0 | 140 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 163 | 157/163 | 1 | 194 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 100 | 76/100 | 0 | 177 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 139 | 127/139 | 1 | 227 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 11 | - | 1 | 94 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 740 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.62 | 0.67 | 149.0 | 65.3 | 45.88 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.74 | 0.74 | 301.9 | 53.8 | 46.82 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 73.9 | 53.8 | 52.81 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 69.2 | 53.5 | 52.53 | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 96/100, 잘림 0, 평균 출력 287.7 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 97/100, 잘림 0, 평균 출력 415.0 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 157/164, 잘림 1, 평균 출력 875.1 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 76/100, 잘림 0, 평균 출력 1995.7 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 127/140, 잘림 1, 평균 출력 1240.4 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 1, 평균 출력 1046.4 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 80.8 토큰
- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 25.83, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 79.3, "per_request_e2e_tokens_per_s_median": 19.921880853096923, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
