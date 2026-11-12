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

## 2차 추가 후보 (2026-11-12): 범용·한국 모델·극한 규모

무인 실행기 큐(`~/llm/queue.json`, 23개)에 추가한 후보입니다. 크기는 HF 파일 목록 합계입니다.

| 구분 | 후보 | 크기 | 엔진 |
|---|---|---:|---|
| 범용 | Gemma 4 26B-A4B (이미지) | 52 GB | vLLM |
| 범용 | Ornith-1.0-35B | 70 GB | vLLM |
| 범용 | Qwen3.6-27B FP8 (dense, 이미지) | 31 GB | vLLM |
| 범용 | Ling-3.0-flash 127.5B Q4_K_M (MIT) | 75 GB | llama.cpp |
| 범용 | Mistral-Medium-3.5 128B dense NVFP4 | 95 GB | vLLM |
| 한국 | LG EXAONE-4.5-33B AWQ (이미지) | 23 GB | vLLM |
| 한국 | NAVER HyperCLOVAX-SEED-Think-32B (이미지) | 67 GB | vLLM |
| 한국 | Trillion Labs Gravity-30B-A5B | 59 GB | vLLM |
| 한국 | Upstage Solar-Open-100B Q4_K_M | 62 GB | llama.cpp |
| 한국 | Upstage Solar-Open2-250B Q2_K | 95 GB | llama.cpp |
| 한국·극한 | **SKT A.X-K2 692B IQ4_XS (공식 GGUF)** | 370 GB | llama.cpp (mmap) |
| 극한·Strata | **DeepSeek-V4.1-Flash 2.25bpw** (최고 품질 세트, 전문가 6개) | 274 GB | Strata |
| 극한·Strata | Qwen3.8-Flash-Next Q8_0 (메모리 초과분 SSD) | 188 GB | Strata |
| 극한 | Nemotron-3-Ultra 550B-A55B UD-IQ2_XXS | 194 GB | llama.cpp (mmap) |
| 극한 | Qwen3.8-2.4T-A95B UD-IQ1_S | 508 GB | llama.cpp (mmap) |
| 극한 | Kimi K3 2.8T IQ1_S-XS | 580 GB | llama.cpp (mmap) |

### 극한 규모를 두 경로로 나눈 이유

- **Strata**는 Qwen3.8-Flash-Next·Qwen3.6·DeepSeek-V4.1-Flash 계열만 지원합니다. Kimi K3 지원 요청(이슈 #1954)은 "계획 없음"으로 닫혔고, GLM-5.3-Flash는 커뮤니티 포크에서만 동작합니다. 그래서 Strata 극한은 **지원 모델의 최대 정밀도·최대 크기 세트**(DeepSeek 2.25bpw, Qwen3.8 Q8_0)로 측정합니다.
- Strata가 지원하지 않는 초대형 모델은 **llama.cpp v0.9.0(Kimi-K3 정식 지원, PR #26185)**에서 전문가 가중치를 SSD mmap으로 두고(`--cpu-moe`) 실행 가능 여부·속도를 측정합니다.

### 제외한 후보와 이유

| 후보 | 이유 |
|---|---|
| LG K-EXAONE-2.0-750B-A37B (Apache 2.0) | NVFP4 526 GB는 vLLM 메모리 한도 초과, 커뮤니티 GGUF는 제작자가 "NOT_WORKING"으로 표시 |
| NC AI VAETKI 112B | 양자화 파일 없음 (BF16 약 224 GB) |
| Kakao kanana-2 | 공개 모델이 3B 이하 |
| DeepSeek-V4-Pro | GGUF가 UD-Q4/Q8뿐이라 1 TB 범위 초과 |

## 엔진 비교 세트 (2026-11-12 추가)

같은 GGUF 파일을 한 번만 받아 여러 엔진이 이어서 사용합니다(앞 항목이 `keep_for`로 파일을 남김). 엔진만 바뀌는 비교입니다.

| 세트 | 공유 파일 | 엔진 |
|---|---|---|
| A | Qwen3.6-35B-A3B UD-Q4_K_XL (22 GB) | llama.cpp · ik_llama.cpp · InferSSD · colibri (+ vLLM NVFP4 기준) |
| B | GLM-5.3-Flash UD-Q2_K_XL (109 GB) | llama.cpp · ik_llama.cpp · colibri |
| C | Muse-Spark-Open 816B UD-Q4_K_XL (505 GB) | InferSSD · colibri · llama.cpp |
| Kimi | Kimi K3 IQ1_S-XS (580 GB) | llama.cpp · ik_llama.cpp · colibri |
| 2.4T | Qwen3.8-2.4T UD-IQ1_S (508 GB) | llama.cpp · ik_llama.cpp |

colibri 전용 극한 후보: Mistral-Large-4 1T (233 GB), GLM-5.3 744B (217 GB), Inkling 975B UD-IQ1_M (285 GB), MiMo-V2.6 Pro 1.02T 2.0bpw (256 GB), MiMo-V2.6 Flash 309B Q2_K (126 GB).

엔진은 InferSSD 0.1.4, ik_llama.cpp(ARM에서 `-DGGML_NATIVE=OFF -DGGML_ARCH_FLAGS=-mcpu=native`, 이슈 #2651), colibri(`coli import` → `build` → `serve`)를 GB10에 설치했습니다.

## 현재 실행 큐 전체 (`configs/queue.json`, 2026-11-12)

무인 실행기가 이 순서로 처리합니다. 이 표는 `configs/queue.json`에서 생성했으며, 큐가 바뀌면 함께 갱신합니다. 측정 단계와 프로필 정의는 [automation.md](automation.md)에 있습니다.

| # | 항목 ID | 엔진 | 프로필 | 받는 파일 | 크기 | 이미지 검사 | 입력 길이 단계 |
|---|---|---|---|---|---:|---|---|
| 1 | `strata-deepseek-v41-flash-200bpw` | strata | standard | ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF (IST-DAS 2.00bpw) · 엔진 기본 | 257 GB | O | 512 / 2k / 8k / 32k / 60k |
| 2 | `vllm-gpt-oss-120b` | vllm | full | openai/gpt-oss-120b · 엔진 기본 | 65 GB | - | 512 / 2k / 8k / 32k / 60k |
| 3 | `vllm-nemotron3-super-120b-nvfp4` | vllm | full | nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 · 엔진 기본 | 80 GB | - | 512 / 2k / 8k / 32k / 60k |
| 4 | `vllm-qwen38-27b-fp8` | vllm | full | Qwen/Qwen3.8-27B-FP8 · 엔진 기본 | 31 GB | O | 512 / 2k / 8k / 32k / 60k |
| 5 | `vllm-nemotron3-super-120b-nvfp4-reasoning-parser` | vllm | full | nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 · 엔진 기본 | 80 GB | - | 512 / 2k / 8k / 32k / 60k |
| 6 | `vllm-gemma4-26b-a4b` | vllm | full | google/gemma-4-26B-A4B-it · 엔진 기본 | 52 GB | O | 512 / 2k / 8k / 32k / 60k |
| 7 | `vllm-ornith-1.0-35b` | vllm | full | ornith-ai/Ornith-1.0-35B · 엔진 기본 | 70 GB | - | 512 / 2k / 8k / 32k / 60k |
| 8 | `vllm-qwen36-27b-fp8` | vllm | full | Qwen/Qwen3.6-27B-FP8 · 엔진 기본 | 31 GB | O | 512 / 2k / 8k / 32k / 60k |
| 9 | `llamacpp-qwen36-35b-udq4kxl` | llamacpp | standard | unsloth/Qwen3.6-35B-A3B-GGUF · Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf | 22 GB | - | 512 / 2k / 8k / 32k |
| 10 | `ikllama-qwen36-35b-udq4kxl` | ikllama | standard | unsloth/Qwen3.6-35B-A3B-GGUF · Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf | 22 GB | - | 512 / 2k / 8k / 32k |
| 11 | `inferssd-qwen36-35b-udq4kxl` | inferssd | standard | unsloth/Qwen3.6-35B-A3B-GGUF · Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf | 22 GB | - | 512 / 2k / 8k / 32k |
| 12 | `vllm-ornith-1.0-35b-reasoning-parser` | vllm | full | ornith-ai/Ornith-1.0-35B · 엔진 기본 | 70 GB | - | 512 / 2k / 8k / 32k / 60k |
| 13 | `llamacpp-qwen36-35b-udq4kxl-ctx64k` | llamacpp | standard | unsloth/Qwen3.6-35B-A3B-GGUF · Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf | 22 GB | - | 512 / 2k / 8k / 32k |
| 14 | `inferssd-qwen36-35b-udq4kxl-ctx64k` | inferssd | standard | unsloth/Qwen3.6-35B-A3B-GGUF · Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf | 22 GB | - | 512 / 2k / 8k / 32k |
| 15 | `colibri-qwen36-35b-udq4kxl` | colibri | standard | unsloth/Qwen3.6-35B-A3B-GGUF · Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf | 22 GB | - | 512 / 2k / 8k / 32k |
| 16 | `vllm-kr-exaone-4.5-33b-awq` | vllm | full | LGAI-EXAONE/EXAONE-4.5-33B-AWQ · 엔진 기본 | 23 GB | O | 512 / 2k / 8k / 32k / 60k |
| 17 | `vllm-kr-hyperclovax-seed-think-32b` | vllm | full | naver-hyperclovax/HyperCLOVAX-SEED-Think-32B · 엔진 기본 | 67 GB | O | 512 / 2k / 8k / 32k / 60k |
| 18 | `vllm-kr-gravity-30b-a5b` | vllm | full | trillionlabs/Gravity-30B-A5B-Preview · 엔진 기본 | 59 GB | - | 512 / 2k / 8k / 32k / 60k |
| 19 | `llamacpp-kr-solar-open-100b-q4km` | llamacpp | slow | mradermacher/Solar-Open-100B-GGUF · Solar-Open-100B.Q4_K_M.gguf | 62 GB | - | 512 / 2k / 8k |
| 20 | `llamacpp-ling-3.0-flash-q4km` | llamacpp | slow | AtomicChat/Ling-3.0-flash-GGUF · Q4_K_M_STOCK/* | 75 GB | - | 512 / 2k / 8k |
| 21 | `llamacpp-glm53-flash-udq2kxl` | llamacpp | slow | unsloth/GLM-5.3-Flash-GGUF · UD-Q2_K_XL/* | 109 GB | - | 512 / 2k / 8k |
| 22 | `ikllama-glm53-flash-udq2kxl` | ikllama | slow | unsloth/GLM-5.3-Flash-GGUF · UD-Q2_K_XL/* | 109 GB | - | 512 / 2k / 8k |
| 23 | `colibri-glm53-flash-udq2kxl` | colibri | slow | unsloth/GLM-5.3-Flash-GGUF · UD-Q2_K_XL/* | 109 GB | - | 512 / 2k / 8k |
| 24 | `llamacpp-minimax-m31-flash-udiq2xxs` | llamacpp | slow | unsloth/MiniMax-M3.1-Flash-GGUF · UD-IQ2_XXS/* | 135 GB | - | 512 / 2k / 8k |
| 25 | `llamacpp-kr-solar-open2-250b-q2k` | llamacpp | slow | prometheusAIR/Solar-Open2-250B-GGUF · Q2_K/* | 95 GB | - | 512 / 2k / 8k |
| 26 | `vllm-mistral-medium-3.5-128b-nvfp4` | vllm | slow | nvidia/Mistral-Medium-3.5-128B-NVFP4 · 엔진 기본 | 95 GB | - | 512 / 2k / 8k |
| 27 | `strata-qwen38fn-udq4kxl` | strata | standard | unsloth/Qwen3.8-Flash-Next-GGUF (UD-Q4_K_XL) · 엔진 기본 | 111 GB | - | 512 / 2k / 8k / 32k |
| 28 | `strata-qwen38fn-q8` | strata | standard | unsloth/Qwen3.8-Flash-Next-GGUF (Q8_0) · 엔진 기본 | 188 GB | - | 512 / 2k / 8k / 32k |
| 29 | `strata-deepseek-v41-flash-225bpw` | strata | standard | ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF (IST-DAS 2.25bpw) · 엔진 기본 | 274 GB | O | 512 / 2k / 8k / 32k / 60k |
| 30 | `llamacpp-nemotron3-ultra-550b-udiq2xxs` | llamacpp | capacity | unsloth/NVIDIA-Nemotron-3-Ultra-550B-A55B-GGUF · UD-IQ2_XXS/* | 194 GB | - | 512 |
| 31 | `llamacpp-kr-ax-k2-iq4xs` | llamacpp | capacity | skt/A.X-K2-GGUF · A.X-K2-IQ4_XS.gguf | 370 GB | - | 512 |
| 32 | `inferssd-qwen38fn-iq4xs` | inferssd | standard | bartowski/Qwen3.8-Flash-Next-GGUF · 엔진 기본 | 100 GB | - | 512 / 2k / 8k / 32k |
| 33 | `inferssd-deepseek-v41-flash-q8` | inferssd | slow | mrfakename/DeepSeek-V4.1-Flash-1017-GGUF · 엔진 기본 | 505 GB | - | 512 / 2k / 8k |
| 34 | `inferssd-muse-spark-open-816b` | inferssd | slow | unsloth/Muse-Spark-Open-816B-A42B-GGUF · UD-Q4_K_XL/* | 505 GB | - | 512 / 2k / 8k |
| 35 | `colibri-muse-spark-open-816b-udq4kxl` | colibri | slow | unsloth/Muse-Spark-Open-816B-A42B-GGUF · UD-Q4_K_XL/* | 505 GB | - | 512 / 2k / 8k |
| 36 | `llamacpp-muse-spark-open-816b-udq4kxl` | llamacpp | slow | unsloth/Muse-Spark-Open-816B-A42B-GGUF · UD-Q4_K_XL/* | 505 GB | - | 512 / 2k / 8k |
| 37 | `llamacpp-qwen38-24t-udiq1s` | llamacpp | capacity | unsloth/Qwen3.8-2.4T-A95B-GGUF · UD-IQ1_S/* | 508 GB | - | 512 |
| 38 | `ikllama-qwen38-24t-udiq1s` | ikllama | capacity | unsloth/Qwen3.8-2.4T-A95B-GGUF · UD-IQ1_S/* | 508 GB | - | 512 |
| 39 | `colibri-mistral-large-4-1t-udiq1s` | colibri | capacity | unsloth/Mistral-Large-4-1T-A52B-GGUF · UD-IQ1_S/* | 233 GB | - | 512 |
| 40 | `colibri-glm-5.3-744b-udiq1s` | colibri | capacity | unsloth/GLM-5.3-GGUF · UD-IQ1_S/* | 217 GB | - | 512 |
| 41 | `colibri-mimo-v2.6-flash-q2k` | colibri | slow | ggml-org/MiMo-V2.6-Flash-RL-GGUF · MiMo-V2.6-Flash-RL-Q2_K.gguf | 126 GB | - | 512 / 2k / 8k |
| 42 | `colibri-inkling-975b-udiq1m` | colibri | capacity | unsloth/inkling-GGUF · UD-IQ1_M/* | 285 GB | - | 512 |
| 43 | `colibri-mimo-v2.6-pro-1t-bpw2` | colibri | capacity | AesSedai/MiMo-V2.6-Pro-MOPD-GGUF · BPW2.0/* | 256 GB | - | 512 |
| 44 | `llamacpp-kimi-k3-iq1s-xs` | llamacpp | capacity | qtum/Kimi-K3-GGUF · Kimi-K3-IQ1_S-XS-* | 579 GB | - | 512 |
| 45 | `ikllama-kimi-k3-iq1s-xs` | ikllama | capacity | qtum/Kimi-K3-GGUF · Kimi-K3-IQ1_S-XS-* | 579 GB | - | 512 |
| 46 | `colibri-kimi-k3-iq1s-xs` | colibri | capacity | qtum/Kimi-K3-GGUF · Kimi-K3-IQ1_S-XS-* | 579 GB | - | 512 |
