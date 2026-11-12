# 2026-11-12 · Strata · Qwen3.8-Flash-Next IQ3_S · 64K

| 항목 | 값 |
|---|---|
| 모델 | Qwen3.8-Flash-Next (약 125B, 토큰당 약 6B 활성, Qwen4 구조 미리보기) |
| 체크포인트 | ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF `IQ3_S` (2 shards, 83.6 GB) — HF LFS sha256 일치 (`artifact.sha256`) |
| 엔진 | Strata v0.2.13 / engine 0.1.59 linux-aarch64-cuda13 (서명 feed의 prebuilt) |
| 실행 | `strata launch --family qwen --model iq3_s --context 64k --vision off --drafting mtp --tune skip --access local` |
| 런타임 | 전문가 24,576개 전부 GPU 캐시(mmap), PLE 표 RAM 고정, KV int8, MTP 드래프트, GB10 속도 스위치 5종 기본 켜짐 |
| 메모리 | 서버 기동 후 시스템 사용 약 96 GiB / 가용 약 24 GiB (`free -g`, 시스템 전체) |
| 상세 설정 | `manifest.json` |

## 결과 요약

| 구분 | 결과 |
|---|---|
| 정상 동작 (sanity 12문항) | 512 / 2048 토큰 예산 모두 **12/12 완료·정답** |
| 단일 요청 생성 속도 (엔진 decode) | 약 **53~54 tok/s** (256토큰 출력, warm) |
| 4개 동시 요청 | 합계 **81.2 tok/s**, 요청당 약 20.5 tok/s, 오류 0 |
| 긴 입력 검색 | 실제 805 / 2,906 / 11,311 / **44,945** 토큰 입력에서 **3/3 정답** (10·50·90% 위치) |
| 입력 처리 속도 (엔진 prefill) | 2.9K 1,800 tok/s · 11K 2,060 tok/s · 45K 1,956 tok/s |
| 첫 토큰까지 (TTFT) | 짧은 입력 0.1~0.6초 · 11K 5.6초 · 45K 6.5초 |
| 컨텍스트 한도 | "60k" 문제(실제 **82,071 토큰**)는 64K 창을 넘어 **HTTP 400으로 거부** (`requests are never truncated`) |

## 전체 표

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 1.46 | 186.2 | 33.7 | 0.69 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.1 | 96.7 | 72.3 | 54.66 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.12 | 67.3 | 63.2 | 57.89 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.12 | 74.0 | 53.7 | 52.76 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.63 | 154.0 | 73.2 | 47.0 | - |
| sanity-2048 | 12/12 | 12 | 12/12 | 0 | 86 | 0.61 | 154.1 | 73.15 | 48.05 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 1.14 | 735.8 | 67.3 | 24.54 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 1.66 | 1799.7 | 62.6 | 22.91 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 5.56 | 2060.4 | 74.2 | 13.62 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44945 | 6.45 | 1956.4 | 61.5 | 11.84 | - |
| context-60k | 1/3 | 0 | 0/0 | 0 | - | - | - | - | - | http_error 400: prompt 82,071 tokens > 65,536 context |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.87 | 255.2 | 53.0 | 45.17 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.12 | 72.4 | 54.2 | 53.2 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.11 | 81.2 | 53.4 | 52.5 | - |
| concurrency4-client1~4 | 2/2 ×4 | - | - | 8 | 210 | 0.13~0.41 | 71~80 | 20.6~21.0 | 20.3~20.4 | - |

## 해석과 한계

- **ctx 라벨은 명목값입니다.** 생성기의 문자/토큰 추정(3.4)이 이 토크나이저에서 실제보다 낮아, 실제 입력은 라벨의 약 1.4배입니다. 실제 값은 표의 `prompt tok`입니다.
- context run의 e2e tok/s는 긴 prefill과 reasoning 출력을 포함하므로 decode 속도가 아닙니다.
- 짧은 출력(cap1~64)의 decode 값은 드래프트 수용률 변동이 커 대표값으로 쓰지 않습니다.
- throughput-2/3, capacity 일부는 같은 프롬프트의 대화 캐시 재사용으로 TTFT·prefill이 첫 요청보다 짧습니다.
- 반복 수가 적습니다(throughput 3회, 동시성 1세트). 확인 실험 전 탐색값입니다.
- **사건 기록:** 첫 실행 시도는 13:27 DGX Dashboard의 시스템 업데이트 후 재부팅으로 서버가 내려가 전부 `Connection refused`로 실패했습니다. 원시 기록은 `local/`에 `FAILED-server-down-after-reboot-*`로 보존했고, 서버 재기동 후 동일 설정으로 다시 측정한 결과가 위 표입니다. 이후 드라이버는 단계마다 서버 응답을 확인하고 내려가 있으면 중단합니다.
