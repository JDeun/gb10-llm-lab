# 2026-11-24 · prism · quality-prism-bonsai2-27b-ternary-ptq1_0-effort-medium (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | prism-ml/Ternary-Bonsai-2-27B-gguf |
| 받은 파일 | Ternary-Bonsai-2-27B-PTQ1_0.gguf (예상 6 GB) |
| 엔진 옵션 | `-c 65536` |
| API 별칭 | quality-prism-bonsai2-27b-ternary-ptq1_0-effort-medium |
| 측정 프로필 | quality |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| quality-gsm8k | 100/100 | 100 | 96/100 | 0 | 82 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 95/100 | 0 | 98 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 164 | 161/164 | 0 | 152 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 95 | 60/95 | 4 | 135 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 138 | 111/138 | 2 | 185 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 52 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 756 | None | None | None | None | None | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 96/100, 잘림 0, 평균 출력 317.5 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 95/100, 잘림 0, 평균 출력 394.4 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 161/164, 잘림 0, 평균 출력 879.9 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 60/100, 잘림 4, 평균 출력 2787.3 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 111/140, 잘림 2, 평균 출력 1956.0 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 0, 평균 출력 1093.2 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 97.0 토큰

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
