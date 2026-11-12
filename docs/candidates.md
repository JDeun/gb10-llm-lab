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

## 추가 후보와 실행 순서 (2026-11-12 추가)

저장소 초기 목록 외에 실사용·비교 축을 채우는 후보를 `configs/models.json`에 추가했습니다. 크기는 HF 파일 목록 합계이며 다운로드 전에 다시 확인합니다.

| 순서 | 후보 | 크기 | 엔진 | 비교 축 |
|---|---|---:|---|---|
| 완료 | Qwen3.6-35B-A3B NVFP4 | 23 GB | vLLM | 현재 상시 서빙 기준선 |
| 완료 | Qwen3.8-Flash-Next IQ3_S | 84 GB | Strata | 64K / 이미지 / 128K |
| 진행 중 | DeepSeek-V4.1-Flash 2.00bpw (전문가 6개) | 257 GB | Strata | 대형 모델 대조군 |
| 1 | gpt-oss-120b MXFP4 | 65 GB | vLLM | 안정적인 텍스트 대조군 (Apache 2.0) |
| 2 | Nemotron-3-Super-120B-A12B NVFP4 | 80 GB | vLLM | NVIDIA 최적화 중형 |
| 3 | Qwen3.8-27B FP8 | 31 GB | vLLM | dense 품질 기준 |
| 4 | GLM-5.3-Flash UD-Q2_K_XL | 109 GB | llama.cpp | 321B, MIT 라이선스 |
| 5 | MiniMax-M3.1-Flash UD-IQ2_XXS | 135 GB | llama.cpp | 최신 대형 |
| 6 | Qwen3.8-Flash-Next UD-Q4_K_XL / Q8_0 | 111 / 188 GB | Strata | 같은 모델의 정밀도 비교 |
| 7 | Qwen3.8-2.4T-A95B UD-IQ1_S | 508 GB | llama.cpp | 2T급 최대 후보 (Kimi보다 작음) |
| 8 | Kimi K3 IQ1_S-XS | 580 GB | llama.cpp (v0.9.0, PR #26185로 정식 지원) | 최대 파라미터 후보 |

운영 원칙:
- 디스크 785 GiB 안에서 한 번에 대형 후보 하나만 둡니다. 측정을 마친 후보의 파일은 결과 커밋 후 삭제하고, 상시 서빙용 두 모델(Qwen3.6, Qwen3.8 IQ3_S)은 유지합니다. 7·8번 전에는 Qwen3.8 IQ3_S도 임시로 지울 수 있습니다.
- 다운로드는 Wi-Fi로 받으며 실측 약 10~35 MB/s입니다. 500 GB급 후보는 다운로드만 4~14시간이 걸릴 수 있습니다.
- 다운로드 중 측정한 run은 결과 README에 그 사실을 적습니다.
