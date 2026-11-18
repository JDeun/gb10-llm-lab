# 2026-11-18 · vllm · quality-vllm-qwen36-27b-fp8 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | Qwen/Qwen3.6-27B-FP8 |
| 받은 파일 | 전체/엔진 기본 (예상 31 GB) |
| 엔진 옵션 | `--max-model-len 131072 --max-num-seqs 4 --gpu-memory-utilization 0.6 --reasoning-parser qwen3` |
| API 별칭 | quality-vllm-qwen36-27b-fp8 |
| 측정 프로필 | quality |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "quality": "step_timeout_28800s"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| quality-gsm8k | 100/100 | 93 | 91/93 | 7 | 82 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 92 | 88/92 | 8 | 98 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 86 | 76/86 | 54 | 185 | None | None | None | None | None | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 91/100, 잘림 7, 평균 출력 1527.4 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 88/100, 잘림 8, 평균 출력 1579.0 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 76/140, 잘림 54, 평균 출력 2953.9 토큰

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
