# 2026-11-26 · llamacpp · quality-llamacpp-gemma4-26b-nothink (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | unsloth/gemma-4-26B-A4B-it-GGUF |
| 받은 파일 | gemma-4-26B-A4B-it-UD-Q4_K_XL.gguf (예상 16 GB) |
| 엔진 옵션 | `-c 65536` |
| API 별칭 | quality-llamacpp-gemma4-26b-nothink |
| 측정 프로필 | quality |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| quality-gsm8k | 100/100 | 100 | 96/100 | 0 | 86 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 94/100 | 0 | 104 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 164 | 160/164 | 0 | 160 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 99 | 71/99 | 1 | 151 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 140 | 118/140 | 0 | 192 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 62 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 496 | None | None | None | None | None | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 96/100, 잘림 0, 평균 출력 248.1 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 94/100, 잘림 0, 평균 출력 236.6 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 160/164, 잘림 0, 평균 출력 274.2 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 71/100, 잘림 1, 평균 출력 532.0 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 118/140, 잘림 0, 평균 출력 638.6 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 0, 평균 출력 643.5 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 26.1 토큰

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
