# 2026-11-12 · vllm · vllm-gpt-oss-120b (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | openai/gpt-oss-120b |
| 받은 파일 | 전체/엔진 기본 (예상 65 GB) |
| 엔진 옵션 | `--max-model-len 131072 --gpu-memory-utilization 0.7 --max-num-seqs 4` |
| API 별칭 | vllm-gpt-oss-120b |
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
 "concurrency4": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 245 | 0.58 | None | None | None | 1.72 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 245 | 0.15 | None | None | None | 32.64 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 245 | 0.15 | None | None | None | 34.17 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 245 | 0.15 | None | None | None | 34.8 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 245 | 0.19 | None | None | None | 31.7 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 245 | 0.22 | None | None | None | 31.62 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 245 | 0.19 | None | None | None | 31.7 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 245 | 0.22 | None | None | None | 31.63 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2400 | 0.21 | None | None | None | 32.11 | - |
| context-32k | 3/3 | 3 | 1/3 | 0 | 36704 | 0.26 | None | None | None | 28.41 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 682 | 0.36 | None | None | None | 31.69 | - |
| context-60k | 3/3 | 3 | 1/3 | 0 | 66979 | 22.96 | None | None | None | 11.95 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 9254 | 2.34 | None | None | None | 16.16 | - |
| sanity-2048 | 12/12 | 12 | 12/12 | 0 | 99 | 0.16 | None | None | None | 34.52 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 99 | 0.22 | None | None | None | 33.61 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 245 | 0.15 | None | None | None | 35.07 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 245 | 0.15 | None | None | None | 35.04 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 245 | 0.16 | None | None | None | 35.08 | - |

- `concurrency4-summary.json`: `{"clients": 4, "requests": 8, "errors": 0, "wall_s": 16.21, "completion_tokens_total": 2048, "aggregate_completion_tokens_per_s": 126.34, "per_request_e2e_tokens_per_s_median": 32.4848503601086, "note": "Aggregate = all completion tokens / wall time from first start to last end; includes prefill."}`

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.

## 해석 (2026-11-12 추가)

- **정상 동작:** sanity 512·2048 모두 12/12.
- **속도:** 단일 요청 e2e 약 **35 tok/s** (커뮤니티 수치 33.5 tok/s와 일치), 4동시 합계 **126 tok/s**(요청당 약 32).
- **긴 입력 검색 실패:** 682~9,254 토큰은 3/3이지만 **36,704 토큰 1/3, 66,979 토큰 1/3**. 오답은 형식 문제가 아니라 다른 레코드의 코드를 답한 실제 오답입니다(예: 기대 `EFNA-N3ZC` → 응답 `9B8J-2HJ3`). 같은 문제에서 Qwen3.6·Qwen3.8·DeepSeek은 모두 3/3이었습니다.
- **해석:** 짧은 대화·툴 호출 용도로는 안정적이지만 **30K 토큰 이상 긴 문맥 근거 찾기에는 이 측정에서 신뢰도가 낮습니다.**
- `artifact.sha256`은 자동 실행 직후 잘못된 해시(캐시 내용 저장소 이름)로 기록되어 같은 날 LFS sha256으로 정정했습니다.
