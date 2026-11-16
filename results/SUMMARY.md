# 결과 요약표 (자동 생성)

각 결과 폴더의 `runs/`에서 계산했습니다. 단일 속도는 엔진이 decode 속도를 주면 그 값, 아니면 요청 전체 기준(e2e)입니다. 해석과 한계는 각 결과의 README와 [automation.md](../docs/automation.md)를 보십시오. 실패한 항목(폴더에 runs가 없거나 측정 전 실패)은 표에 나오지 않습니다.

| 결과 | 엔진 | sanity 512 (2048) | 단일 tok/s (중앙값) | 4동시 합계 tok/s | 이미지 | 3/3 통과한 최대 입력 |
|---|---|---|---|---|---|---|
| `strata-deepseek-v41-flash-200bpw` | strata | 12/12 | 15.3 | 19 | 3/3 | 67K |
| `strata-qwen38fn-iq3s-128k` | Strata | - | 49.7 | - | - | 82K |
| `strata-qwen38fn-iq3s-64k` | Strata | 12/12 (12/12@2048) | 53.4 | 81 | - | 45K |
| `strata-qwen38fn-iq3s-64k-vision` | Strata | 12/12 | 53.4 | - | 3/3 | - |
| `vllm-gpt-oss-120b` | vllm | 12/12 (12/12@2048) | 35.1 | 126 | - | 9K |
| `vllm-nemotron3-super-120b-nvfp4` | vllm | 0/12 (0/12@2048) | 15.8 | 44 | - | - |
| `vllm-nemotron3-super-120b-nvfp4-reasoning-parser` | vllm | 12/12 (12/12@2048) | 15.7 | 43 | - | 11K |
| `vllm-qwen36-35b-a3b-nvfp4` | vLLM | 12/12 (12/12@2048) | 114.5 | 270 | 3/3 | 164K |
| `vllm-qwen38-27b-fp8` | vllm | 12/12 (12/12@2048) | 8.0 | 31 | 3/3 | 82K |
| `colibri-qwen36-35b-udq4kxl` | colibri | 11/12 | 29.1 | 35 | - | 45K |
| `ikllama-qwen36-35b-udq4kxl` | ikllama | 10/12 | 66.7 | 66 | - | 45K |
| `inferssd-qwen36-35b-udq4kxl` | inferssd | 10/12 | 25.9 | 26 | - | 3K |
| `inferssd-qwen36-35b-udq4kxl-ctx64k` | inferssd | 10/12 | - | - | - | 11K |
| `llamacpp-kr-solar-open-100b-q4km` | llamacpp | 0/12 | 23.9 | - | - | - |
| `llamacpp-qwen36-35b-udq4kxl` | llamacpp | 10/12 | 64.0 | 152 | - | 11K |
| `llamacpp-qwen36-35b-udq4kxl-ctx64k` | llamacpp | 10/12 | 65.9 | 152 | - | 45K |
| `vllm-gemma4-26b-a4b` | vllm | 11/12 (11/12@2048) | 24.3 | 91 | 3/3 | 83K |
| `vllm-kr-exaone-4.5-33b-awq` | vllm | 6/12 (11/12@2048) | 12.5 | 50 | 0/3 | 44K |
| `vllm-kr-exaone-4.5-33b-awq-vision4k` | vllm | - | 12.4 | - | 1/3 | 1K |
| `vllm-kr-hyperclovax-seed-think-32b-transformers-64k` | vllm | 10/12 (10/12@2048) | 3.7 | 14 | 3/3 | 3K |
| `vllm-ornith-1.0-35b` | vllm | 0/12 (0/12@2048) | 30.3 | 105 | - | - |
| `vllm-ornith-1.0-35b-reasoning-parser` | vllm | 9/12 (12/12@2048) | 30.2 | 104 | - | 82K |
| `vllm-qwen36-27b-fp8` | vllm | 10/12 (12/12@2048) | 8.0 | 31 | 3/3 | 82K |
| `ikllama-glm53-flash-udq2kxl` | ikllama | 12/12 | 6.6 | - | - | 9K |
| `llamacpp-glm53-flash-udq2kxl` | llamacpp | 12/12 | 3.8 | - | - | 9K |
| `strata-deepseek-v41-flash-225bpw` | strata | 12/12 | 10.7 | 11 | 3/3 | 67K |
| `vllm-mistral-medium-3.5-128b-nvfp4` | vllm | 11/12 | 2.5 | - | - | 11K |
| `inferssd-deepseek-v41-flash-q8` | inferssd | 12/12 | 8.0 | - | - | 2K |

## 주의할 행

- `vllm-nemotron3-super-120b-nvfp4`, `vllm-ornith-1.0-35b`, `llamacpp-kr-solar-open-100b-q4km`의 0/12는 reasoning이 답과 분리되지 않은 **측정 설정 문제**입니다. 앞의 둘은 파서를 붙인 재측정 행을 보십시오.
- `vllm-kr-exaone-4.5-33b-awq`, `vllm-qwen36-27b-fp8` 등의 512 예산 저점수는 reasoning이 예산을 다 쓴 미완료이며, 괄호의 2048 예산 값이 정확도에 가깝습니다.
- "3/3 통과한 최대 입력"이 작은 행 중 일부는 엔진의 컨텍스트 설정 한계입니다(llama.cpp 32K, InferSSD 기본값).
