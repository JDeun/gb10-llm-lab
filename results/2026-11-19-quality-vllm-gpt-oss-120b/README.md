# 2026-11-19 · vllm · quality-vllm-gpt-oss-120b (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | openai/gpt-oss-120b |
| 받은 파일 | 전체/엔진 기본 (예상 65 GB) |
| 엔진 옵션 | `--max-model-len 131072 --gpu-memory-utilization 0.7 --max-num-seqs 4` |
| API 별칭 | quality-vllm-gpt-oss-120b |
| 측정 프로필 | quality |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| quality-gsm8k | 100/100 | 100 | 96/100 | 0 | 133 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 93/100 | 0 | 161 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 163 | 158/163 | 1 | 201 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 100 | 62/100 | 0 | 200 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 138 | 111/138 | 2 | 222 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 115 | None | None | None | None | None | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 96/100, 잘림 0, 평균 출력 288.9 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 93/100, 잘림 0, 평균 출력 375.6 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 158/164, 잘림 1, 평균 출력 591.1 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 62/100, 잘림 0, 평균 출력 1132.9 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 111/140, 잘림 2, 평균 출력 831.0 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 0, 평균 출력 1119.2 토큰

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
