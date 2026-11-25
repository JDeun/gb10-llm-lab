# 용도별 추천 (자동 생성)

`automation/tools/recommend.py`가 결과 폴더에서 계산합니다. 품질은 객관식·수학·코드·툴 호출 부분집합의 평균 정답률(zero-shot 부분집합, 공식 점수 아님)이고, 문항 수가 100~140개라 약 ±5~9%p 차이는 같은 수준으로 봅니다. 파레토 최적은 두 축 모두에서 더 나은 대안이 없는 조합입니다. 최종 추천은 confirm 프로필(3배 문항, 5회 반복)로 확인한 뒤 확정합니다.

품질 데이터가 있는 결과: 34개 / 전체 67개

## 대화·API 상시 서빙 (품질 × 단일 요청 속도)

| 결과 | 품질 | 단일 tok/s | 파레토 최적 |
|---|---|---|---|
| `issue14-strata-qwen38fn-iq3s-ctx32k-kvq4` | 0.927 | 54.0 | **예** |
| `sweep-strata-qwen38fn-iq3s-kvq4` | 0.926 | 53.8 |  |
| `issue14-strata-qwen38fn-iq3s-tune-quick` | 0.921 | 50.8 |  |
| `sweep-strata-qwen38fn-iq3s-quality` | 0.921 | 49.9 |  |
| `issue14-strata-qwen38fn-iq3s-tune-thorough` | 0.921 | 47.6 |  |
| `confirm-strata-qwen38fn-iq3s-ctx32k-kvq4` | 0.919 | 54.3 | **예** |
| `vllm-qwen38-27b-nvfp4-mtp-nothink-matched` | 0.890 | 15.9 |  |
| `sweep-vllm-qwen36-nothink` | 0.889 | 95.9 | **예** |
| `confirm-vllm-qwen36-nothink` | 0.889 | 95.2 |  |
| `strata-qwen36-35b-udq4kxl` | 0.874 | 65.5 |  |
| `ikllama-gpt-oss-120b-mxfp4` | 0.873 | 56.2 |  |
| `vllm-qwen38-27b-nvfp4-mtp-refpin` | 0.870 | 16.6 |  |
| `nariq-qwen38-27b-2.0bpw` | 0.869 | 19.3 |  |
| `llamacpp-gpt-oss-120b-mxfp4` | 0.864 | 55.2 |  |
| `llamacpp-inkling2mini-udq4kxl` | 0.862 | 36.9 |  |
| `prism-bonsai2-27b-ternary-ptq1_0` | 0.820 | 32.8 |  |
| `sweep-vllm-qwen36-mtp-conc16` | 0.802 | 114.2 | **예** |
| `sweep-vllm-qwen36-kvauto` | 0.797 | 109.4 |  |
| `prism-bonsai2-27b-ternary-pq2_0` | 0.757 | 27.3 |  |
| `llamacpp-bonsai2-27b-ternary-q2_0` | 0.755 | 26.6 |  |
| `ikllama-gemma4-26b-udq4kxl` | 0.693 | 54.4 |  |
| `llamacpp-gemma4-26b-udq4kxl` | 0.689 | 54.4 |  |
| `quality-llamacpp-kr-solar-open-100b-q4km-nothink` | 0.614 | 24.3 |  |

## 여러 사용자·배치 (품질 × 동시 처리 합계)

| 결과 | 품질 | 동시 합계 tok/s | 파레토 최적 |
|---|---|---|---|
| `issue14-strata-qwen38fn-iq3s-ctx32k-kvq4` | 0.927 | 81.0 | **예** |
| `sweep-strata-qwen38fn-iq3s-kvq4` | 0.926 | 79.3 |  |
| `sweep-strata-qwen38fn-iq3s-quality` | 0.921 | 77.3 |  |
| `issue14-strata-qwen38fn-iq3s-tune-quick` | 0.921 | 77.1 |  |
| `issue14-strata-qwen38fn-iq3s-tune-thorough` | 0.921 | 67.9 |  |
| `confirm-strata-qwen38fn-iq3s-ctx32k-kvq4` | 0.919 | 82.6 | **예** |
| `vllm-qwen38-27b-nvfp4-mtp-nothink-matched` | 0.890 | 178.0 | **예** |
| `sweep-vllm-qwen36-nothink` | 0.889 | 239.2 | **예** |
| `confirm-vllm-qwen36-nothink` | 0.889 | 483.6 | **예** |
| `strata-qwen36-35b-udq4kxl` | 0.874 | 151.8 |  |
| `ikllama-gpt-oss-120b-mxfp4` | 0.873 | 55.8 |  |
| `vllm-qwen38-27b-nvfp4-mtp-refpin` | 0.870 | 111.8 |  |
| `nariq-qwen38-27b-2.0bpw` | 0.869 | 60.0 |  |
| `llamacpp-gpt-oss-120b-mxfp4` | 0.864 | 106.4 |  |
| `llamacpp-inkling2mini-udq4kxl` | 0.862 | 74.9 |  |
| `prism-bonsai2-27b-ternary-ptq1_0` | 0.820 | 87.5 |  |
| `sweep-vllm-qwen36-mtp-conc16` | 0.802 | 544.6 | **예** |
| `sweep-vllm-qwen36-kvauto` | 0.797 | 272.8 |  |
| `prism-bonsai2-27b-ternary-pq2_0` | 0.757 | 78.8 |  |
| `llamacpp-bonsai2-27b-ternary-q2_0` | 0.755 | 78.6 |  |
| `ikllama-gemma4-26b-udq4kxl` | 0.693 | 54.2 |  |
| `llamacpp-gemma4-26b-udq4kxl` | 0.689 | 129.2 |  |
| `quality-llamacpp-kr-solar-open-100b-q4km-nothink` | 0.614 | 61.4 |  |

## 코딩·에이전트 (코드+툴 정답률 × 단일 요청 속도)

| 결과 | 코드·툴 정답률 | 단일 tok/s | 파레토 최적 |
|---|---|---|---|
| `llamacpp-gpt-oss-120b-mxfp4` | 0.985 | 55.2 | **예** |
| `ikllama-gpt-oss-120b-mxfp4` | 0.982 | 56.2 | **예** |
| `issue14-strata-qwen38fn-iq3s-tune-quick` | 0.982 | 50.8 |  |
| `sweep-strata-qwen38fn-iq3s-quality` | 0.982 | 49.9 |  |
| `issue14-strata-qwen38fn-iq3s-tune-thorough` | 0.982 | 47.6 |  |
| `vllm-qwen38-27b-nvfp4-mtp-nothink-matched` | 0.982 | 15.9 |  |
| `confirm-vllm-qwen36-nothink` | 0.979 | 95.2 | **예** |
| `confirm-strata-qwen38fn-iq3s-ctx32k-kvq4` | 0.979 | 54.3 |  |
| `issue14-strata-qwen38fn-iq3s-ctx32k-kvq4` | 0.979 | 54.0 |  |
| `sweep-strata-qwen38fn-iq3s-kvq4` | 0.979 | 53.8 |  |
| `sweep-vllm-qwen36-nothink` | 0.976 | 95.9 | **예** |
| `vllm-qwen38-27b-nvfp4-mtp-refpin` | 0.957 | 16.6 |  |
| `strata-qwen36-35b-udq4kxl` | 0.952 | 65.5 |  |
| `prism-bonsai2-27b-ternary-ptq1_0` | 0.942 | 32.8 |  |
| `sweep-vllm-qwen36-kvauto` | 0.918 | 109.4 | **예** |
| `sweep-vllm-qwen36-mtp-conc16` | 0.915 | 114.2 | **예** |
| `ikllama-gemma4-26b-udq4kxl` | 0.909 | 54.4 |  |
| `llamacpp-gemma4-26b-udq4kxl` | 0.887 | 54.4 |  |
| `quality-llamacpp-kr-solar-open-100b-q4km-nothink` | 0.271 | 24.3 |  |

## 긴 문서 (정답 낸 최대 입력 × 단일 요청 속도, 품질 무관)

| 결과 | 최대 입력 토큰 | 단일 tok/s | 파레토 최적 |
|---|---|---|---|
| `vllm-qwen36-35b-a3b-nvfp4` | 164,204 | 114.5 | **예** |
| `vllm-gemma4-26b-a4b` | 82,574 | 24.3 |  |
| `strata-qwen38fn-iq3s-128k` | 82,071 | 49.7 |  |
| `vllm-qwen38-27b-nvfp4-mtp-refpin` | 82,071 | 16.6 |  |
| `vllm-qwen38-27b-fp8` | 82,071 | 8.0 |  |
| `vllm-ornith-1.0-35b-reasoning-parser` | 82,029 | 30.2 |  |
| `vllm-qwen36-27b-fp8` | 82,029 | 8.0 |  |
| `strata-deepseek-v41-flash-200bpw` | 67,104 | 15.3 |  |
| `strata-deepseek-v41-flash-225bpw` | 67,104 | 10.7 |  |
| `ikllama-gemma4-26b-udq4kxl` | 45,253 | 54.4 |  |
| `llamacpp-gemma4-26b-udq4kxl` | 45,253 | 54.4 |  |
| `strata-qwen38fn-iq3s-64k` | 44,945 | 53.4 |  |
| `prism-bonsai2-27b-ternary-ptq1_0` | 44,945 | 32.8 |  |
| `prism-bonsai2-27b-ternary-pq2_0` | 44,945 | 27.3 |  |
| `llamacpp-bonsai2-27b-ternary-q2_0` | 44,945 | 26.6 |  |
| `nariq-qwen38-27b-2.0bpw` | 44,945 | 19.3 |  |
| `confirm-vllm-qwen36-nothink` | 44,905 | 95.2 |  |
| `colibri-qwen36-35b-udq4kxl` | 44,905 | 29.1 |  |
| `ikllama-qwen36-35b-udq4kxl` | 44,903 | 66.7 |  |
| `llamacpp-qwen36-35b-udq4kxl-ctx64k` | 44,903 | 65.9 |  |
| `strata-qwen36-35b-udq4kxl` | 44,903 | 65.5 |  |
| `vllm-kr-exaone-4.5-33b-awq` | 43,551 | 12.5 |  |
| `llamacpp-inkling2mini-udq4kxl` | 39,544 | 36.9 |  |
| `confirm-strata-qwen38fn-iq3s-ctx32k-kvq4` | 11,311 | 54.3 |  |
| `issue14-strata-qwen38fn-iq3s-ctx32k-kvq4` | 11,311 | 54.0 |  |
| `issue14-strata-qwen38fn-iq3s-tune-quick` | 11,311 | 50.8 |  |
| `issue14-strata-qwen38fn-iq3s-tune-thorough` | 11,311 | 47.6 |  |
| `llamacpp-qwen36-35b-udq4kxl` | 11,269 | 64.0 |  |
| `vllm-nemotron3-super-120b-nvfp4-reasoning-parser` | 11,089 | 15.7 |  |
| `vllm-mistral-medium-3.5-128b-nvfp4` | 11,088 | 2.5 |  |
| `ikllama-glm53-flash-udq2kxl` | 9,349 | 6.6 |  |
| `llamacpp-glm53-flash-udq2kxl` | 9,349 | 3.8 |  |
| `ikllama-gpt-oss-120b-mxfp4` | 9,254 | 56.2 |  |
| `llamacpp-gpt-oss-120b-mxfp4` | 9,254 | 55.2 |  |
| `vllm-gpt-oss-120b` | 9,254 | 35.1 |  |
| `vllm-kr-hyperclovax-seed-think-32b-transformers-64k` | 2,911 | 3.7 |  |
| `inferssd-qwen36-35b-udq4kxl` | 2,864 | 25.9 |  |
| `inferssd-deepseek-v41-flash-q8` | 2,369 | 8.0 |  |
| `vllm-kr-exaone-4.5-33b-awq-vision4k` | 733 | 12.4 |  |

## 최대 품질 순위

| 순위 | 결과 | 품질 | 세트별 정답률 |
|---|---|---|---|
| 1 | `issue14-strata-qwen38fn-iq3s-ctx32k-kvq4` | 0.927 | gsm8k 0.96, hrm8k-gsm8k 0.97, humaneval 0.96, kmmlu 0.76, mmlu-pro 0.91, tools-ko 1.00 |
| 2 | `sweep-strata-qwen38fn-iq3s-kvq4` | 0.926 | gsm8k 0.96, hrm8k-gsm8k 0.97, humaneval 0.96, kmmlu 0.76, mmlu-pro 0.91, tools-ko 1.00 |
| 3 | `sweep-strata-qwen38fn-iq3s-quality` | 0.921 | gsm8k 0.96, hrm8k-gsm8k 0.97, humaneval 0.96, kmmlu 0.74, mmlu-pro 0.89, tools-ko 1.00 |
| 4 | `issue14-strata-qwen38fn-iq3s-tune-quick` | 0.921 | gsm8k 0.96, hrm8k-gsm8k 0.97, humaneval 0.96, kmmlu 0.74, mmlu-pro 0.89, tools-ko 1.00 |
| 5 | `issue14-strata-qwen38fn-iq3s-tune-thorough` | 0.921 | gsm8k 0.96, hrm8k-gsm8k 0.97, humaneval 0.96, kmmlu 0.74, mmlu-pro 0.89, tools-ko 1.00 |
| 6 | `confirm-strata-qwen38fn-iq3s-ctx32k-kvq4` | 0.919 | gsm8k 0.98, hrm8k-gsm8k 0.95, humaneval 0.96, kmmlu 0.78, mmlu-pro 0.85, tools-ko 1.00 |
| 7 | `vllm-qwen38-27b-nvfp4-mtp-nothink-matched` | 0.890 | gsm8k 0.95, hrm8k-gsm8k 0.94, humaneval 0.96, kmmlu 0.65, mmlu-pro 0.84, tools-ko 1.00 |
| 8 | `quality-vllm-gemma4-26b-a4b` | 0.890 | gsm8k 0.96, hrm8k-gsm8k 0.94, humaneval 0.97, kmmlu 0.75, mmlu-pro 0.83 |
| 9 | `sweep-vllm-qwen36-nothink` | 0.889 | gsm8k 0.95, hrm8k-gsm8k 0.94, humaneval 0.95, kmmlu 0.68, mmlu-pro 0.81, tools-ko 1.00 |
| 10 | `confirm-vllm-qwen36-nothink` | 0.889 | gsm8k 0.97, hrm8k-gsm8k 0.92, humaneval 0.96, kmmlu 0.71, mmlu-pro 0.78, tools-ko 1.00 |
| 11 | `llamacpp-bonsai2-27b-ternary-q2_0-effort-medium` | 0.881 | gsm8k 0.96, hrm8k-gsm8k 0.95, humaneval 0.98, kmmlu 0.60, mmlu-pro 0.80, tools-ko 1.00 |
| 12 | `quality-prism-bonsai2-27b-ternary-ptq1_0-effort-medium` | 0.881 | gsm8k 0.96, hrm8k-gsm8k 0.95, humaneval 0.98, kmmlu 0.60, mmlu-pro 0.79, tools-ko 1.00 |
| 13 | `strata-qwen36-35b-udq4kxl` | 0.874 | gsm8k 0.95, hrm8k-gsm8k 0.92, humaneval 0.99, kmmlu 0.66, mmlu-pro 0.81, tools-ko 0.92 |
| 14 | `ikllama-gpt-oss-120b-mxfp4` | 0.873 | gsm8k 0.96, hrm8k-gsm8k 0.93, humaneval 0.96, kmmlu 0.63, mmlu-pro 0.76, tools-ko 1.00 |
| 15 | `vllm-qwen38-27b-nvfp4-mtp-refpin` | 0.870 | gsm8k 0.96, hrm8k-gsm8k 0.96, humaneval 0.91, kmmlu 0.59, mmlu-pro 0.79, tools-ko 1.00 |
| 16 | `nariq-qwen38-27b-2.0bpw` | 0.869 | gsm8k 0.90, hrm8k-gsm8k 0.95, mmlu-pro 0.76 |
| 17 | `llamacpp-gpt-oss-120b-mxfp4` | 0.864 | gsm8k 0.96, hrm8k-gsm8k 0.94, humaneval 0.97, kmmlu 0.57, mmlu-pro 0.74, tools-ko 1.00 |
| 18 | `llamacpp-inkling2mini-udq4kxl` | 0.862 | gsm8k 0.96, hrm8k-gsm8k 0.92, mmlu-pro 0.71 |
| 19 | `quality-llamacpp-bonsai2-27b-ternary-q2_0-nothink` | 0.862 | gsm8k 0.95, hrm8k-gsm8k 0.91, humaneval 0.94, kmmlu 0.57, mmlu-pro 0.80, tools-ko 1.00 |
| 20 | `quality-vllm-gpt-oss-120b` | 0.853 | gsm8k 0.96, hrm8k-gsm8k 0.93, humaneval 0.96, kmmlu 0.62, mmlu-pro 0.79 |
| 21 | `sweep-vllm-qwen36-think-budget16k` | 0.852 | gsm8k 0.94, hrm8k-gsm8k 0.93, humaneval 0.95, kmmlu 0.73, mmlu-pro 0.71 |
| 22 | `quality-prism-bonsai2-27b-ternary-ptq1_0-nothink` | 0.849 | gsm8k 0.95, hrm8k-gsm8k 0.92, humaneval 0.93, kmmlu 0.52, mmlu-pro 0.78, tools-ko 1.00 |
| 23 | `quality-vllm-kr-hyperclovax-seed-think-32b-transformers-64k` | 0.841 | gsm8k 0.88, hrm8k-gsm8k 0.93, mmlu-pro 0.71 |
| 24 | `prism-bonsai2-27b-ternary-ptq1_0` | 0.820 | gsm8k 0.93, hrm8k-gsm8k 0.95, humaneval 0.88, kmmlu 0.42, mmlu-pro 0.74, tools-ko 1.00 |
| 25 | `sweep-vllm-qwen36-mtp-conc16` | 0.802 | gsm8k 0.95, hrm8k-gsm8k 0.90, humaneval 0.83, kmmlu 0.61, mmlu-pro 0.52, tools-ko 1.00 |
| 26 | `sweep-vllm-qwen36-kvauto` | 0.797 | gsm8k 0.95, hrm8k-gsm8k 0.86, humaneval 0.84, kmmlu 0.61, mmlu-pro 0.53, tools-ko 1.00 |
| 27 | `quality-vllm-qwen38-27b-fp8` | 0.787 | gsm8k 0.96, hrm8k-gsm8k 0.94, humaneval 0.84, kmmlu 0.48, mmlu-pro 0.71 |
| 28 | `quality-vllm-qwen36-27b-fp8` | 0.778 | gsm8k 0.91, hrm8k-gsm8k 0.88, mmlu-pro 0.54 |
| 29 | `prism-bonsai2-27b-ternary-pq2_0` | 0.757 | gsm8k 0.94, hrm8k-gsm8k 0.95, kmmlu 0.38, mmlu-pro 0.76 |
| 30 | `llamacpp-bonsai2-27b-ternary-q2_0` | 0.755 | gsm8k 0.94, hrm8k-gsm8k 0.95, kmmlu 0.38, mmlu-pro 0.75 |
| 31 | `quality-vllm-kr-exaone-4.5-33b-awq` | 0.744 | gsm8k 0.95, hrm8k-gsm8k 0.91, humaneval 0.74, kmmlu 0.56, mmlu-pro 0.56 |
| 32 | `ikllama-gemma4-26b-udq4kxl` | 0.693 | gsm8k 0.54, hrm8k-gsm8k 0.92, humaneval 0.82, kmmlu 0.64, mmlu-pro 0.24, tools-ko 1.00 |
| 33 | `llamacpp-gemma4-26b-udq4kxl` | 0.689 | gsm8k 0.52, hrm8k-gsm8k 0.93, humaneval 0.77, kmmlu 0.61, mmlu-pro 0.30, tools-ko 1.00 |
| 34 | `quality-llamacpp-kr-solar-open-100b-q4km-nothink` | 0.614 | gsm8k 0.94, hrm8k-gsm8k 0.94, humaneval 0.54, kmmlu 0.50, mmlu-pro 0.76, tools-ko 0.00 |
