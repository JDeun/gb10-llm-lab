# 2026-11-25 · nariq · quality-nariq-qwen38-27b-2.0bpw-rest (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | nari-labs/Qwen3.8-27B-NariQ-GGUF |
| 받은 파일 | Qwen3.8-27B-NariQ-2.0bpw.gguf (예상 7 GB) |
| 엔진 옵션 | `-c 65536 --temp 1.0 --top-p 0.95 --top-k 20 --min-p 0` |
| API 별칭 | quality-nariq-qwen38-27b-2.0bpw-rest |
| 측정 프로필 | quality |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| quality-humaneval | 164/164 | 154 | 146/154 | 10 | 194 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 60 | 47/60 | 32 | 177 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 10 | - | 2 | 94 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 794 | None | None | None | None | None | - |

- 품질 `humaneval-subset-zeroshot`: 정답 146/164, 잘림 10, 평균 출력 2133.5 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 47/100, 잘림 32, 평균 출력 8332.3 토큰
- 품질 `open-ko-subset-zeroshot`: 정답 0/0, 잘림 2, 평균 출력 4938.8 토큰
- 품질 `tools-ko-subset-zeroshot`: 정답 12/12, 잘림 0, 평균 출력 85.8 토큰

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
