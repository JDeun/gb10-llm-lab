# 후보와 근거

검토일: 2026-11-12. **여기에는 사용자 GB10의 실측 결과가 없습니다.** 파일 크기는 확인 당시 배포 문서의 추정값이며 다운로드 전에 실제 선택 파일 목록을 합산해야 합니다. 같은 저장소의 모든 양자화 버전을 다운로드하지 않습니다.

| 후보 | 파일 용량 추정 | 근거와 현재 판단 |
|---|---:|---|
| 현재 Qwen3.6-35B-A3B-NVFP4 | 미확인 | 사용자가 이미 실행 중. 기준 측정부터 수행 |
| DeepSeek V4.1 Flash 2.25bpw | 274GB | Engram/drafter 포함. Strata의 GB10 실험 PR을 대조 후보로 검토 |
| DeepSeek V4 Pro IQ1_S | 337GB | 단일 GX10 CPU+mmap 개인 사례. 단문 결과이며 일반 품질 미평가 |
| Kimi K3 IQ1_S-XS | 539.7GiB ≈ 579.5GB | 모든 896 전문가 유지. 단일 GB10 실행 미확인 |
| Kimi K3 Unsloth UD-IQ1_S | 594GB | 대체 저비트 후보. 단일 GB10 실행 미확인 |
| Kimi K3 NVFP4/FP8 FTW | 1,610,936,311,808bytes | 단일 GB10 capacity 보고는 있으나 1TB SSD 범위에서 제외 |

## Kimi 저비트 후보

[qtum/6block 카드](https://huggingface.co/qtum/Kimi-K3-GGUF)의 IQ1_S-XS는 전체 전문가를 보존합니다. 제작자 실측은 대용량 RAM을 갖춘 다른 장비에서 수행됐으므로 해당 속도를 GB10 예상값으로 사용하지 않습니다. 같은 카드의 832-expert 버전은 일부 전문가를 제거하므로 전체 모델 비교에서 제외합니다.

[Unsloth UD-IQ1_S 파일 목록](https://huggingface.co/unsloth/Kimi-K3-GGUF/tree/main/UD-IQ1_S)은 다른 후보입니다. 두 파일을 동시에 보관할 계획은 아닙니다. 엔진의 Kimi 지원, ARM64/GB10 빌드, dense/KV/전문가의 메모리 배치부터 확인해야 합니다.

## 실행 재현 후보

[DeepSeek V4 Pro GX10 보고](https://github.com/epappas/gx10-cluster/blob/main/workspaces/inference/llamacpp-deepseek-v4-pro-gguf/README.md)는 CPU+mmap 경로를 사용했습니다. GPU 가속 성공으로 해석하지 않습니다. 문서 안에 오래된 미실행 표현과 뒤의 실행 기록이 함께 있으므로 제한된 개인 사례로 취급합니다.

[Strata DeepSeek 문서](https://github.com/Niko1221/Strata/blob/main/docs/DEEPSEEK41.md)와 [GB10 UMA PR #5453](https://github.com/Niko1221/Strata/pull/5453)은 대형 모델 runtime 비교 근거입니다. 미병합 코드의 결과를 기본 release 결과로 간주하지 않습니다. 전체 6 expert, 동일 정밀도·프로필을 고정합니다.

## 범위 밖 참고 결과

[Kimi FTW 카드](https://huggingface.co/oakmindai/Kimi-K3-NVFP4-FTW)와 [원시 결과](https://github.com/sixteen-miles-labs/sparklab/blob/main/benchmarks/gb10/results/GB10-KIMI-001.json)의 0.1613tok/s는 1.61TB NVFP4/FP8 artifact를 사용한 별도 실험입니다. 이를 580GB GGUF 속도로 옮겨 쓰지 않습니다. 출력 정확성 미평가와 greedy 일관성 한계를 포함한 capacity 근거입니다.
