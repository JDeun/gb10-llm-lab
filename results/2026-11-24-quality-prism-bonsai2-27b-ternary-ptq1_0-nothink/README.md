# 2026-11-24 · prism · quality-prism-bonsai2-27b-ternary-ptq1_0-nothink (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | prism-ml/Ternary-Bonsai-2-27B-gguf |
| 받은 파일 | Ternary-Bonsai-2-27B-PTQ1_0.gguf (예상 6 GB) |
| 엔진 옵션 | `-c 65536` |
| API 별칭 | quality-prism-bonsai2-27b-ternary-ptq1_0-nothink |
| 측정 프로필 | quality |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| quality-gsm8k | 100/100 | 100 | 95/100 | 0 | 84 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 92/100 | 0 | 100 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 164 | 152/164 | 0 | 154 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 95 | 52/95 | 5 | 137 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 139 | 109/139 | 1 | 187 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 54 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 758 | None | None | None | None | None | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 95/100, 잘림 0, 평균 출력 401.0 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 92/100, 잘림 0, 평균 출력 235.8 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 152/164, 잘림 0, 평균 출력 240.7 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 52/100, 잘림 5, 평균 출력 2179.2 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 109/140, 잘림 1, 평균 출력 1883.3 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 0, 평균 출력 660.6 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 43.3 토큰

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
