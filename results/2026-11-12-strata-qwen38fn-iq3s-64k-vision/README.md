# 2026-11-12 · Strata · Qwen3.8-Flash-Next IQ3_S · 64K · 이미지 입력 켬

[이미지 입력을 끈 실행](../2026-11-12-strata-qwen38fn-iq3s-64k/)과 같은 체크포인트·엔진에서 **`--vision gpu` 한 가지만 바꾼** 실행입니다.
Strata 문서(DGX_SPARK_LINUX.md)는 "GB10에서 이미지 입력은 시도하지 않았다"고 적고 있어, 이 결과가 이 장비에서의 첫 확인입니다.

| 항목 | 값 |
|---|---|
| 추가 구성 요소 | GPU 이미지 리더(mmproj 약 0.9 GB, 엔진 로그: 1024 image tokens 워밍업 0.6초) |
| 메모리 | 서버 기동 후 시스템 사용 약 96~98 GiB / 가용 약 23~25 GiB (이미지 입력 끈 실행과 거의 동일) |

## 결과

| 검사 | 결과 |
|---|---|
| 이미지 정답 검사 (`vision-check.json`) | **3/3 정답**, 오류 0 — 단색(red), 좌우 분할(left), 사각형 개수(3) |
| sanity 12문항 (512) | 12/12 완료·정답 |
| 텍스트 decode (엔진) | 51.4 / 53.4 / 53.9 tok/s — 이미지 입력 끈 실행(53.0 / 54.2 / 53.4)과 차이 없음 |

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.63 | 154.0 | 73.65 | 47.36 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 1.17 | 252.8 | 51.4 | 41.81 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.11 | 74.3 | 53.4 | 52.46 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.11 | 77.6 | 53.9 | 53.01 | - |

## 한계

- 이미지 검사는 96×96 합성 이미지 3장의 **정상 동작 확인**입니다. 사진·문서·도표 이해 품질을 대표하지 않습니다.
- 이미지 검사 도구는 저장소 밖(`~/llm/tools/vision_check.py`)에서 실행했습니다. 문항과 정답은 `vision-check.json`에 그대로 있습니다.
