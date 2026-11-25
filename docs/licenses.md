# 모델 라이선스 정리

이 저장소에서 측정했거나 후보로 올린 모델의 라이선스와 출처 URL입니다.

> **이 문서는 법률 자문이 아닙니다.** 라이선스 원문을 읽고 정리한 것이고, 조사 기준일은 2026-11-25입니다.
> 라이선스는 바뀔 수 있으니 **납품이나 외부 배포 전에는 원문을 다시 확인하고 법무 검토를 받으세요.**
> 각 줄의 "확인한 조항"은 해당 모델의 `LICENSE` 파일에서 직접 읽은 내용입니다.

## 요약: 납품 가능성으로 나눈 세 묶음

| 묶음 | 뜻 | 해당 모델 |
|---|---|---|
| **A. 제약 없음** | Apache 2.0 또는 MIT. 고지만 지키면 상업적 납품에 문제 없음 | Qwen3.6-35B-A3B, Qwen3.8-27B(원본·RedHatAI NVFP4), Gemma 4, gpt-oss-120b, Inkling 2, Bonsai, NariQ, GLM-5.3-Flash, DeepSeek V4.1 Flash, Ling, MiMo, Ornith, Gravity, A.X-K2 |
| **B. 조건부 가능** | 상업적 사용은 되지만 규모 기준·브랜드 표시·통지 의무 등이 붙음 | Qwen3.8-Flash-Next, Kimi K3, Qwen3.8-2.4T, Solar Open, HyperCLOVAX, GLM-5.3(대형), NVIDIA 계열(QAD 등), Mistral, Muse, Nemotron |
| **C. 상업적 사용 불가** | 연구·교육 전용 | **EXAONE 4.5** |

**가장 중요한 두 가지**
1. **품질 1위인 Qwen3.8-Flash-Next는 Apache 2.0이 아닙니다.** Qwen Community License 1.0이고, **Model as a Service(모델을 서비스로 제공) 사업에는 Qwen의 별도 라이선스가 필요합니다.** 사내 전용으로만 쓰면 예외에 해당합니다(아래 §2 참고).
2. **EXAONE 4.5는 상업적 사용이 명시적으로 금지돼 있습니다.** 후보에서 빼야 합니다.

---

## 1. A묶음 — Apache 2.0 / MIT (제약 없음)

고지(저작권·라이선스 사본) 유지 외에 상업적 사용 제한이 없습니다.

| 모델 | 라이선스 | URL |
|---|---|---|
| Qwen3.6-35B-A3B NVFP4 (**현 추천 조합**) | Apache 2.0 | https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4 |
| Qwen3.6-35B-A3B GGUF | Apache 2.0 | https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF |
| Qwen3.8-27B NVFP4 (**현 납품 모델**) | Apache 2.0 | https://huggingface.co/RedHatAI/Qwen3.8-27B-NVFP4 |
| Qwen3.8-27B FP8 | Apache 2.0 | https://huggingface.co/Qwen/Qwen3.8-27B-FP8 |
| Qwen3.6-27B FP8 | Apache 2.0 | https://huggingface.co/Qwen/Qwen3.6-27B-FP8 |
| Qwen3.8-27B NariQ GGUF | Apache 2.0 | https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF |
| Ternary-Bonsai-2-27B | Apache 2.0 | https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf |
| Gemma 4 26B-A4B | Apache 2.0 | https://huggingface.co/google/gemma-4-26B-A4B-it |
| Gemma 4 26B GGUF | Apache 2.0 | https://huggingface.co/unsloth/gemma-4-26B-A4B-it-GGUF |
| gpt-oss-120b | Apache 2.0 | https://huggingface.co/openai/gpt-oss-120b |
| gpt-oss-120b GGUF | Apache 2.0 | https://huggingface.co/ggml-org/gpt-oss-120b-GGUF |
| Inkling 2 Mini | Apache 2.0 | https://huggingface.co/thinkingmachines/Inkling-2-Mini |
| Inkling 2 Mini GGUF (ggml-org) | 표기 없음 (원본 Apache 2.0 상속으로 봄) | https://huggingface.co/ggml-org/Inkling-2-Mini-GGUF |
| Inkling 2 Small | Apache 2.0 | https://huggingface.co/thinkingmachines/Inkling-2-Small |
| Inkling 2 Small GGUF | Apache 2.0 | https://huggingface.co/bartowski/Inkling-2-Small-GGUF |
| Qwen3.8-Flash-Next GSQ-RCO GGUF | Apache 2.0 **(표기 불일치 — §2 경고 참고)** | https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF |
| GLM-5.3-Flash | MIT | https://huggingface.co/zai-org/GLM-5.3-Flash |
| GLM-5.3-Flash GGUF | MIT | https://huggingface.co/unsloth/GLM-5.3-Flash-GGUF |
| DeepSeek V4.1 Flash GGUF | MIT | https://huggingface.co/mrfakename/DeepSeek-V4.1-Flash-1017-GGUF |
| DeepSeek V4.1 Flash GSQ-RCO | MIT | https://huggingface.co/ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF |
| Ling-3.0-flash GGUF | MIT | https://huggingface.co/AtomicChat/Ling-3.0-flash-GGUF |
| MiMo-V2.6-Flash-RL GGUF | MIT | https://huggingface.co/ggml-org/MiMo-V2.6-Flash-RL-GGUF |
| Ornith-1.0-35B | MIT | https://huggingface.co/ornith-ai/Ornith-1.0-35B |
| Gravity-30B-A5B | Apache 2.0 | https://huggingface.co/trillionlabs/Gravity-30B-A5B-Preview |
| A.X-K2 GGUF (SKT) | Apache 2.0 | https://huggingface.co/skt/A.X-K2-GGUF |
| MiMo-V2.6-Pro MOPD GGUF | 표기 없음 | https://huggingface.co/AesSedai/MiMo-V2.6-Pro-MOPD-GGUF |

---

## 2. B묶음 — 조건부 상업적 사용

### Qwen Community License 1.0 — **현재 품질 1위 모델**

| 모델 | URL |
|---|---|
| Qwen3.8-Flash-Next GGUF (unsloth) | https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF |
| Qwen3.8-Flash-Next GGUF (bartowski) | https://huggingface.co/bartowski/Qwen3.8-Flash-Next-GGUF |
| Qwen3.8-Flash-Next NVFP4 (NVIDIA) | https://huggingface.co/nvidia/Qwen3.8-Flash-Next-NVFP4 (NVIDIA 라이선스도 겹침) |
| Qwen3.8-Flash-Next RAZOR NVFP4 | https://huggingface.co/cleyesode/Qwen3.8-Flash-Next-RAZOR-65B-A6B-NVFP4 |

**확인한 조항** (원문: https://huggingface.co/Qwen/Qwen3.8-Flash-Next/raw/main/LICENSE)
- 사용·복제·수정·배포·판매·호스팅·파인튜닝·파생물 제작을 폭넓게 허용합니다.
- **조건 1:** 월간 활성 사용자 1억 명 초과 또는 월 매출 2천만 달러 초과인 상업 제품에 쓰면, 제품 화면에 모델 이름을 눈에 띄게 표시해야 합니다. (우리 규모에는 해당 없음)
- **조건 2 (중요):** **Model as a Service 또는 AI Work Assistant 사업을 하면, 상업적 사용 전에 Qwen에서 별도 라이선스를 받아야 합니다.** 다만 **사내 내부 사용은 예외**입니다. 단, 모델이나 그 출력, 모델 능력을 제3자에게 제공하지 않는 경우에 한합니다.
- **우리 상황에 대한 해석:** 고객사에 설치해 그 고객사 직원만 쓰는 온프레미스 납품이 "내부 사용"인지 "제3자 제공"인지가 갈립니다. **법무 검토가 필요한 지점입니다.** 사내 전용 챗봇이면 문제가 없을 가능성이 높습니다.

> **⚠️ 표기 불일치:** ISTA-DASLab의 Qwen3.8-Flash-Next GGUF(우리가 Strata로 측정한 1위 파일)는 Apache 2.0으로 표기돼 있습니다. 하지만 원본 모델은 Qwen Community License입니다. **재배포자가 원본보다 느슨한 라이선스를 붙일 수는 없으므로, 원본 조건을 따르는 것이 안전합니다.**

### NVIDIA Open Model Agreement

| 모델 | URL |
|---|---|
| Qwen3.8-27B NVFP4-QAD | https://huggingface.co/nvidia/Qwen3.8-27B-NVFP4-QAD |
| Qwen3.8-Flash-Next NVFP4 | https://huggingface.co/nvidia/Qwen3.8-Flash-Next-NVFP4 |
| Mistral-Medium-3.5-128B NVFP4 | https://huggingface.co/nvidia/Mistral-Medium-3.5-128B-NVFP4 |
| Kimi-K3 NVFP4-FTW | https://huggingface.co/oakmindai/Kimi-K3-NVFP4-FTW |

**확인한 조항** (원문: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-agreement/)
- Apache 2.0을 변형한 형태입니다. 상업적 사용과 파생물 배포를 허용하고, NVIDIA는 출력물에 소유권을 주장하지 않습니다.
- **파생물에 자체 라이선스 조건을 붙일 수 있습니다**(3조 마지막 문단). 다만 받는 쪽에 NVIDIA 라이선스 사본을 전달하고(3a), 원본의 저작권·특허·상표·저작자 표시를 유지해야 합니다(3b).
- **⚠️ 면책 의무 (7조):** 제3자 청구로부터 NVIDIA를 면책해야 합니다. **납품 계약서와 충돌하는지 확인이 필요합니다.**
- 준거법은 미국 델라웨어주, 관할은 캘리포니아 산타클라라 카운티입니다.
- **파인튜닝 목적이라면** 이 파일 대신 Apache 2.0인 원본(https://huggingface.co/Qwen/Qwen3.8-27B)으로 학습한 뒤 직접 압축하는 편이 라이선스가 단순합니다.

### Kimi K3 / MiniMax / GLM-5.3 / Mistral — 매출 기준 조건

| 모델 | 라이선스 | URL |
|---|---|---|
| Kimi K3 GGUF | kimi-k3 | https://huggingface.co/qtum/Kimi-K3-GGUF · https://huggingface.co/unsloth/Kimi-K3-GGUF |
| MiniMax-M3.1-Flash | minimax-community | https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash |
| MiniMax-M3.1-Flash GGUF | minimax-community | https://huggingface.co/unsloth/MiniMax-M3.1-Flash-GGUF |
| GLM-5.3 (대형) GGUF | glm-5.3 | https://huggingface.co/unsloth/GLM-5.3-GGUF |
| Mistral-Large-4-1T GGUF | mistral-ecosystem-open-weight | https://huggingface.co/unsloth/Mistral-Large-4-1T-A52B-GGUF |
| Muse-Spark-Open-816B GGUF | muse-model-license | https://huggingface.co/unsloth/Muse-Spark-Open-816B-A42B-GGUF |

**확인한 조항**
- **Kimi K3:** 매출 2천만 달러 초과 시 별도 라이선스가 필요합니다. 월간 활성 사용자 1억 명 또는 매출 2천만 달러 초과 시 모델 이름 표시 의무가 있습니다.
- **MiniMax:** 기본은 **비상업적 사용**이고, 상업적 사용 시 조건이 붙습니다. 연 매출 2천만 달러 초과면 **사전 서면 승인**이 필요하고, 그 미만이면 **1회 통지**로 됩니다. 파인튜닝한 파생물의 상업적 배포도 "상업적 사용"에 포함됩니다. 금지 용도 부칙이 따로 있습니다.

### Solar Open (Upstage) — 브랜드 표시 의무

| 모델 | URL |
|---|---|
| Solar-Open-100B GGUF | https://huggingface.co/mradermacher/Solar-Open-100B-GGUF |
| Solar-Open2-250B GGUF | https://huggingface.co/prometheusAIR/Solar-Open2-250B-GGUF |

**확인한 조항** (원문: https://huggingface.co/upstage/Solar-Open-100B/raw/main/LICENSE)
- Apache 2.0의 조항을 그대로 채택하고 상업적 사용을 허용합니다.
- **추가 조건 (4조 e항):** 파생 AI 모델을 배포하면 **'Solar' 브랜드를 표기해야 합니다.** Apache 2.0의 상표 조항(6조)에 대한 예외입니다.

### HyperCLOVAX (NAVER)

| 모델 | URL |
|---|---|
| HyperCLOVAX-SEED-Think-32B | https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-32B |

**확인한 조항**
- 비독점·전 세계·**양도 불가·철회 가능**한 라이선스입니다. (Apache 2.0의 "irrevocable"과 다릅니다)
- **4조 추가 상업 조항:** ① 월간 활성 사용자 1천만 명 초과이거나, ② **NAVER의 제품·서비스와 실질적으로 유사하거나 직접 경쟁하는 제품을 제공하면** NAVER에 라이선스를 요청해야 합니다. NAVER의 재량으로 허가되며, 허가 전에는 권리를 행사할 수 없습니다.
- 금지 용도 정책이 있고, NAVER가 라이선스를 수시로 갱신할 수 있습니다.
- 분쟁은 대한상사중재원(KCAB) 중재, 서울, 영어로 진행합니다.
- **증류(distillation)로 만든 모델도 파생 모델로 봅니다.** 합성 데이터 생성 방식도 포함됩니다.

### 기타 B묶음

| 모델 | 라이선스 | URL |
|---|---|---|
| Qwen3.8-2.4T-A95B | qwen3.8-max | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B |
| Qwen3.8-2.4T GGUF | qwen3.8-max | https://huggingface.co/unsloth/Qwen3.8-2.4T-A95B-GGUF |
| Nemotron-3-Super-120B NVFP4 | nvidia-nemotron-open-model-license | https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 |
| Nemotron-3-Ultra-550B GGUF | openmdw-1.1 | https://huggingface.co/unsloth/NVIDIA-Nemotron-3-Ultra-550B-A55B-GGUF |

---

## 3. C묶음 — 상업적 사용 불가

### EXAONE 4.5 (LG AI Research) — **납품 불가**

| 모델 | URL |
|---|---|
| EXAONE-4.5-33B-AWQ | https://huggingface.co/LGAI-EXAONE/EXAONE-4.5-33B-AWQ |

**확인한 조항** (원문: https://huggingface.co/LGAI-EXAONE/EXAONE-4.5-33B/raw/main/LICENSE)
- "**연구 및 교육 목적으로만**(solely for research and educational purposes) 접근·다운로드·설치·사용할 수 있다."
- "**3.1 상업적 사용:** 라이선시는 모델, 파생물, 출력물을 **상업적 목적으로 사용하는 것이 명시적으로 금지된다.**"
- 상업적 응용이나 외부 배포는 별도 합의 없이는 엄격히 금지됩니다.
- **결론: 사내 연구 비교용으로는 쓸 수 있지만, 납품 제품에는 넣을 수 없습니다.** 후보 목록에서 제외 대상으로 표시해야 합니다.

---

## 4. 파인튜닝해서 만든 모델의 라이선스

자주 나오는 질문이라 따로 정리합니다.

| 원본 라이선스 | 파인튜닝 결과물에 자체 라이선스를 붙일 수 있나 | 따라오는 의무 |
|---|---|---|
| Apache 2.0 / MIT | **가능** | 저작권·라이선스 고지 유지 |
| NVIDIA Open Model Agreement | **가능** (3조 마지막 문단에 명시) | 라이선스 사본 전달, 저작자 표시 유지, **NVIDIA 면책** |
| Qwen Community 1.0 | 가능 | MaaS 사업이면 별도 라이선스, 규모 초과 시 이름 표시 |
| Solar Open | 가능 | **'Solar' 브랜드 표기 필수** |
| HyperCLOVAX | 가능하나 파생 모델도 같은 조건 | NAVER 조건 승계, 경쟁 제품 금지 |
| MiniMax | 상업적 배포 시 통지 또는 승인 | 매출 기준에 따라 다름 |
| EXAONE | **불가** (상업적 사용 금지) | — |

**원칙:** 어떤 라이선스든 **원본의 라이선스를 떼어낼 수는 없습니다.** 내 제품 전체에 회사 계약서를 적용하되, 모델 부분의 원 라이선스와 고지는 함께 실어야 합니다.

**실무 권고:** 파인튜닝이 목적이면 **Apache 2.0 원본으로 학습**하세요. 양자화된 재배포본(NVIDIA·RedHat 등)으로 학습하면 라이선스가 겹치고, 기술적으로도 압축된 가중치에 추가 학습을 하는 것은 품질 손실 위험이 있습니다.

---

## 5. 엔진 라이선스 (참고)

모델과 별개로 추론 엔진도 납품 대상에 포함됩니다.

| 엔진 | 라이선스 | URL |
|---|---|---|
| vLLM | Apache 2.0 | https://github.com/vllm-project/vllm |
| llama.cpp | MIT | https://github.com/ggml-org/llama.cpp |
| ik_llama.cpp | MIT (llama.cpp 포크) | https://github.com/ikawrakow/ik_llama.cpp |
| nari-llama.cpp | MIT (llama.cpp 포크) | https://github.com/nari-labs/nari-llama.cpp |
| Prism ML llama.cpp 포크 | MIT (llama.cpp 포크) | https://github.com/prism-ml/llama.cpp |
| Strata | **확인 필요** | 납품 검토 시 반드시 확인 |
| InferSSD, colibri | **확인 필요** | 납품 검토 시 반드시 확인 |

---

## 6. 다음에 할 일

- [ ] **EXAONE 4.5를 후보에서 제외 표시** (상업적 사용 불가)
- [ ] **Qwen3.8-Flash-Next의 "내부 사용" 예외 범위 법무 검토** — 온프레미스 납품이 해당되는지
- [ ] **NVIDIA 면책 조항(7조)이 납품 계약과 충돌하는지 검토**
- [ ] Strata·InferSSD·colibri 엔진 라이선스 확인
- [ ] 분기마다 이 문서 재확인 (라이선스는 바뀝니다)
