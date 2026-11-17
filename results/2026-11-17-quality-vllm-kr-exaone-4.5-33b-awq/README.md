# 2026-11-17 · vllm · quality-vllm-kr-exaone-4.5-33b-awq (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | LGAI-EXAONE/EXAONE-4.5-33B-AWQ |
| 받은 파일 | 전체/엔진 기본 (예상 23 GB) |
| 엔진 옵션 | `--max-model-len 131072 --max-num-seqs 4 --gpu-memory-utilization 0.6 --trust-remote-code --reasoning-parser deepseek_r1` |
| API 별칭 | quality-vllm-kr-exaone-4.5-33b-awq |
| 측정 프로필 | quality |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| quality-gsm8k | 100/100 | 97 | 95/97 | 3 | 74 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 95 | 91/95 | 5 | 77 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 126 | 122/126 | 38 | 133 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 77 | 56/77 | 23 | 110 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 84 | 78/84 | 56 | 158 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 10 | - | 2 | 42 | None | None | None | None | None | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 95/100, 잘림 3, 평균 출력 863.2 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 91/100, 잘림 5, 평균 출력 1198.0 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 122/164, 잘림 38, 평균 출력 2116.0 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 56/100, 잘림 23, 평균 출력 1985.2 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 78/140, 잘림 56, 평균 출력 2474.1 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 2, 평균 출력 2288.9 토큰

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
