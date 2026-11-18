# 2026-11-18 · vllm · quality-vllm-qwen38-27b-fp8 (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | Qwen/Qwen3.8-27B-FP8 |
| 받은 파일 | 전체/엔진 기본 (예상 31 GB) |
| 엔진 옵션 | `--max-model-len 131072 --gpu-memory-utilization 0.6 --max-num-seqs 4 --reasoning-parser qwen3` |
| API 별칭 | quality-vllm-qwen38-27b-fp8 |
| 측정 프로필 | quality |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| quality-gsm8k | 100/100 | 99 | 96/99 | 1 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 98 | 94/98 | 2 | 140 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 152 | 138/152 | 12 | 194 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 51 | 48/51 | 49 | 177 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 108 | 100/108 | 32 | 227 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 10 | - | 2 | 94 | None | None | None | None | None | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 96/100, 잘림 1, 평균 출력 371.9 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 94/100, 잘림 2, 평균 출력 524.2 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 138/164, 잘림 12, 평균 출력 1044.1 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 48/100, 잘림 49, 평균 출력 2631.1 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 100/140, 잘림 32, 평균 출력 1627.8 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 2, 평균 출력 1445.0 토큰

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
