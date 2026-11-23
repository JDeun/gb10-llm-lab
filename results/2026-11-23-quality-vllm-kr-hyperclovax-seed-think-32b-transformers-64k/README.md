# 2026-11-23 · vllm · quality-vllm-kr-hyperclovax-seed-think-32b-transformers-64k (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | naver-hyperclovax/HyperCLOVAX-SEED-Think-32B |
| 받은 파일 | 전체/엔진 기본 (예상 67 GB) |
| 엔진 옵션 | `--max-model-len 65536 --max-num-seqs 4 --gpu-memory-utilization 0.85 --trust-remote-code --reasoning-parser deepseek_r1 --model-impl transformers` |
| API 별칭 | quality-vllm-kr-hyperclovax-seed-think-32b-transformers-64k |
| 측정 프로필 | quality |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "quality": "step_timeout_28800s"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| quality-gsm8k | 100/100 | 99 | 88/99 | 1 | 84 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 99 | 93/99 | 1 | 91 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 123 | 100/123 | 17 | 194 | None | None | None | None | None | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 88/100, 잘림 1, 평균 출력 662.4 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 93/100, 잘림 1, 평균 출력 606.3 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 100/140, 잘림 17, 평균 출력 1453.3 토큰

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
