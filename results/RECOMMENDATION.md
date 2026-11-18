# 용도별 추천 (자동 생성)

`automation/tools/recommend.py`가 결과 폴더에서 계산합니다. 품질은 객관식·수학·코드·툴 호출 부분집합의 평균 정답률(zero-shot 부분집합, 공식 점수 아님)이고, 문항 수가 100~140개라 약 ±5~9%p 차이는 같은 수준으로 봅니다. 파레토 최적은 두 축 모두에서 더 나은 대안이 없는 조합입니다. 최종 추천은 confirm 프로필(3배 문항, 5회 반복)로 확인한 뒤 확정합니다.

품질 데이터가 있는 결과: 11개 / 전체 44개

## 대화·API 상시 서빙 (품질 × 단일 요청 속도)

| 결과 | 품질 | 단일 tok/s | 파레토 최적 |
|---|---|---|---|
| `sweep-strata-qwen38fn-iq3s-kvq4` | 0.926 | 53.8 | **예** |
| `sweep-strata-qwen38fn-iq3s-quality` | 0.921 | 49.9 |  |
| `sweep-vllm-qwen36-nothink` | 0.889 | 95.9 | **예** |
| `strata-qwen36-35b-udq4kxl` | 0.874 | 65.5 |  |
| `sweep-vllm-qwen36-mtp-conc16` | 0.802 | 114.2 | **예** |
| `sweep-vllm-qwen36-kvauto` | 0.797 | 109.4 |  |
| `ikllama-gemma4-26b-udq4kxl` | 0.693 | 54.4 |  |
| `llamacpp-gemma4-26b-udq4kxl` | 0.689 | 54.4 |  |

## 여러 사용자·배치 (품질 × 동시 처리 합계)

| 결과 | 품질 | 동시 합계 tok/s | 파레토 최적 |
|---|---|---|---|
| `sweep-strata-qwen38fn-iq3s-kvq4` | 0.926 | 79.3 | **예** |
| `sweep-strata-qwen38fn-iq3s-quality` | 0.921 | 77.3 |  |
| `sweep-vllm-qwen36-nothink` | 0.889 | 239.2 | **예** |
| `strata-qwen36-35b-udq4kxl` | 0.874 | 151.8 |  |
| `sweep-vllm-qwen36-mtp-conc16` | 0.802 | 544.6 | **예** |
| `sweep-vllm-qwen36-kvauto` | 0.797 | 272.8 |  |
| `ikllama-gemma4-26b-udq4kxl` | 0.693 | 54.2 |  |
| `llamacpp-gemma4-26b-udq4kxl` | 0.689 | 129.2 |  |

## 코딩·에이전트 (코드+툴 정답률 × 단일 요청 속도)

| 결과 | 코드·툴 정답률 | 단일 tok/s | 파레토 최적 |
|---|---|---|---|
| `sweep-strata-qwen38fn-iq3s-quality` | 0.982 | 49.9 | **예** |
| `sweep-strata-qwen38fn-iq3s-kvq4` | 0.979 | 53.8 | **예** |
| `sweep-vllm-qwen36-nothink` | 0.976 | 95.9 | **예** |
| `strata-qwen36-35b-udq4kxl` | 0.952 | 65.5 |  |
| `sweep-vllm-qwen36-kvauto` | 0.918 | 109.4 | **예** |
| `sweep-vllm-qwen36-mtp-conc16` | 0.915 | 114.2 | **예** |
| `ikllama-gemma4-26b-udq4kxl` | 0.909 | 54.4 |  |
| `llamacpp-gemma4-26b-udq4kxl` | 0.887 | 54.4 |  |

## 긴 문서 (정답 낸 최대 입력 × 단일 요청 속도, 품질 무관)

| 결과 | 최대 입력 토큰 | 단일 tok/s | 파레토 최적 |
|---|---|---|---|
| `vllm-qwen36-35b-a3b-nvfp4` | 164,204 | 114.5 | **예** |
| `vllm-gemma4-26b-a4b` | 82,574 | 24.3 |  |
| `strata-qwen38fn-iq3s-128k` | 82,071 | 49.7 |  |
| `vllm-qwen38-27b-fp8` | 82,071 | 8.0 |  |
| `vllm-ornith-1.0-35b-reasoning-parser` | 82,029 | 30.2 |  |
| `vllm-qwen36-27b-fp8` | 82,029 | 8.0 |  |
| `strata-deepseek-v41-flash-200bpw` | 67,104 | 15.3 |  |
| `strata-deepseek-v41-flash-225bpw` | 67,104 | 10.7 |  |
| `ikllama-gemma4-26b-udq4kxl` | 45,253 | 54.4 |  |
| `llamacpp-gemma4-26b-udq4kxl` | 45,253 | 54.4 |  |
| `strata-qwen38fn-iq3s-64k` | 44,945 | 53.4 |  |
| `colibri-qwen36-35b-udq4kxl` | 44,905 | 29.1 |  |
| `ikllama-qwen36-35b-udq4kxl` | 44,903 | 66.7 |  |
| `llamacpp-qwen36-35b-udq4kxl-ctx64k` | 44,903 | 65.9 |  |
| `strata-qwen36-35b-udq4kxl` | 44,903 | 65.5 |  |
| `vllm-kr-exaone-4.5-33b-awq` | 43,551 | 12.5 |  |
| `llamacpp-qwen36-35b-udq4kxl` | 11,269 | 64.0 |  |
| `vllm-nemotron3-super-120b-nvfp4-reasoning-parser` | 11,089 | 15.7 |  |
| `vllm-mistral-medium-3.5-128b-nvfp4` | 11,088 | 2.5 |  |
| `ikllama-glm53-flash-udq2kxl` | 9,349 | 6.6 |  |
| `llamacpp-glm53-flash-udq2kxl` | 9,349 | 3.8 |  |
| `vllm-gpt-oss-120b` | 9,254 | 35.1 |  |
| `vllm-kr-hyperclovax-seed-think-32b-transformers-64k` | 2,911 | 3.7 |  |
| `inferssd-qwen36-35b-udq4kxl` | 2,864 | 25.9 |  |
| `inferssd-deepseek-v41-flash-q8` | 2,369 | 8.0 |  |
| `vllm-kr-exaone-4.5-33b-awq-vision4k` | 733 | 12.4 |  |

## 최대 품질 순위

| 순위 | 결과 | 품질 | 세트별 정답률 |
|---|---|---|---|
| 1 | `sweep-strata-qwen38fn-iq3s-kvq4` | 0.926 | gsm8k 0.96, hrm8k-gsm8k 0.97, humaneval 0.96, kmmlu 0.76, mmlu-pro 0.91, tools-ko 1.00 |
| 2 | `sweep-strata-qwen38fn-iq3s-quality` | 0.921 | gsm8k 0.96, hrm8k-gsm8k 0.97, humaneval 0.96, kmmlu 0.74, mmlu-pro 0.89, tools-ko 1.00 |
| 3 | `sweep-vllm-qwen36-nothink` | 0.889 | gsm8k 0.95, hrm8k-gsm8k 0.94, humaneval 0.95, kmmlu 0.68, mmlu-pro 0.81, tools-ko 1.00 |
| 4 | `strata-qwen36-35b-udq4kxl` | 0.874 | gsm8k 0.95, hrm8k-gsm8k 0.92, humaneval 0.99, kmmlu 0.66, mmlu-pro 0.81, tools-ko 0.92 |
| 5 | `sweep-vllm-qwen36-think-budget16k` | 0.852 | gsm8k 0.94, hrm8k-gsm8k 0.93, humaneval 0.95, kmmlu 0.73, mmlu-pro 0.71 |
| 6 | `sweep-vllm-qwen36-mtp-conc16` | 0.802 | gsm8k 0.95, hrm8k-gsm8k 0.90, humaneval 0.83, kmmlu 0.61, mmlu-pro 0.52, tools-ko 1.00 |
| 7 | `sweep-vllm-qwen36-kvauto` | 0.797 | gsm8k 0.95, hrm8k-gsm8k 0.86, humaneval 0.84, kmmlu 0.61, mmlu-pro 0.53, tools-ko 1.00 |
| 8 | `quality-vllm-qwen38-27b-fp8` | 0.787 | gsm8k 0.96, hrm8k-gsm8k 0.94, humaneval 0.84, kmmlu 0.48, mmlu-pro 0.71 |
| 9 | `quality-vllm-kr-exaone-4.5-33b-awq` | 0.744 | gsm8k 0.95, hrm8k-gsm8k 0.91, humaneval 0.74, kmmlu 0.56, mmlu-pro 0.56 |
| 10 | `ikllama-gemma4-26b-udq4kxl` | 0.693 | gsm8k 0.54, hrm8k-gsm8k 0.92, humaneval 0.82, kmmlu 0.64, mmlu-pro 0.24, tools-ko 1.00 |
| 11 | `llamacpp-gemma4-26b-udq4kxl` | 0.689 | gsm8k 0.52, hrm8k-gsm8k 0.93, humaneval 0.77, kmmlu 0.61, mmlu-pro 0.30, tools-ko 1.00 |
