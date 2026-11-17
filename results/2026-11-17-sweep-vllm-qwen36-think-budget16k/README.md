# 2026-11-17 · vllm · sweep-vllm-qwen36-think-budget16k (자동 실행)

**상태:** 완료  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | nvidia/Qwen3.6-35B-A3B-NVFP4 |
| 받은 파일 | 전체/엔진 기본 (예상 23 GB) |
| 엔진 옵션 | `--max-model-len 65536 --trust-remote-code --kv-cache-dtype fp8 --attention-backend flashinfer --moe-backend marlin --gpu-memory-utilization 0.6 --max-num-seqs 16 --max-num-batched-tokens 8192 --enable-chunked-prefill --async-scheduling --enable-prefix-caching --reasoning-parser qwen3 --speculative-config {"method":"mtp","num_speculative_tokens":3,"moe_backend":"triton"} --enable-auto-tool-choice --tool-call-parser qwen3_xml` |
| API 별칭 | sweep-vllm-qwen36-think-budget16k |
| 측정 프로필 | quality |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "quality": "ok"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| quality-gsm8k | 100/100 | 100 | 94/100 | 0 | 82 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 97 | 93/97 | 3 | 98 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 163 | 156/163 | 1 | 152 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 100 | 73/100 | 0 | 135 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 110 | 99/110 | 30 | 185 | None | None | None | None | None | - |

- 품질 `gsm8k-subset-zeroshot`: 정답 94/100, 잘림 0, 평균 출력 1278.9 토큰
- 품질 `hrm8k-gsm8k-subset-zeroshot`: 정답 93/100, 잘림 3, 평균 출력 1756.6 토큰
- 품질 `humaneval-subset-zeroshot`: 정답 156/164, 잘림 1, 평균 출력 2708.2 토큰
- 품질 `kmmlu-subset-zeroshot`: 정답 73/100, 잘림 0, 평균 출력 3019.5 토큰
- 품질 `mmlu-pro-subset-zeroshot`: 정답 99/140, 잘림 30, 평균 출력 6676.6 토큰

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
