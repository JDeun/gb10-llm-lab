# 2026-11-12 · 0~1단계 파일럿 (장비 확인 + 기준 경로 확인)

**성격:** 측정 경로가 동작하는지 확인한 파일럿입니다. 품질 평가나 가용성 판정에 쓰지 않습니다.
`manifest.json`은 **템플릿 그대로(null)** 사용했습니다. 이후 실험부터는 모델별 manifest를 채워 기록합니다.

## 장비 (inventory-stage0.json)

| 항목 | 값 |
|---|---|
| 장치 | NVIDIA GB10 1대, Arm CPU 20코어, CPU·GPU 공유 메모리 121.6 GiB |
| OS / 커널 / 드라이버 | Ubuntu 24.04.5 / 7.0.0-1025-nvidia / 580.178.04 (CUDA 13.0) |
| 저장장치 | KIOXIA BG7 1TB, ext4, 측정 시점 여유 약 785 GiB |
| 네트워크 | Wi-Fi 연결(절전 켜짐), 유선 미연결 — 측정 중 SSH 끊김 1회 관찰 |

## 서버 구성

| 별칭 | 엔진 | 체크포인트 | 주요 설정 |
|---|---|---|---|
| vllm-qwen36 | vLLM v0.32.0 (docker `vllm/vllm-openai:v0.32.0`) | nvidia/Qwen3.6-35B-A3B-NVFP4 | NVIDIA DGX Spark 권장 명령: fp8 KV, MTP 3, max-model-len 262144, gpu-memory-utilization 0.4, max-num-seqs 4 |
| strata-qwen38fn-iq3s | Strata v0.2.13 (engine 0.1.59 linux-aarch64-cuda13) | ISTA-DASLab Qwen3.8-Flash-Next GSQ-RCO IQ3_S (sha256 HF 일치 확인) | 64K, vision off, MTP drafting, `--mmap-experts`, PLE RAM |

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|
| vllm-qwen36-api-check | 1/1 | 0 | 0/0 | 1 | 28 | 0.45 | - | - | 51.39 | - |
| vllm-qwen36-sanity-512 | 12/12 | 11 | 11/11 | 1 | 44 | 0.08 | - | - | 140.39 | - |
| vllm-qwen36-throughput-1 | 1/1 | 0 | - | 1 | 168 | 0.41 | - | - | 103.63 | - |
| strata-qwen38fn-iq3s-sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.65 | 151.0 | 73.65 | 44.31 | - |
| strata-qwen38fn-iq3s-throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.91 | 290.3 | 49.7 | 42.43 | - |
| strata-qwen38fn-iq3s-throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.11 | 77.9 | 49.1 | 48.32 | - |
| strata-qwen38fn-iq3s-throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.11 | 76.0 | 48.4 | 47.67 | - |

- `truncated`=출력 상한 도달. throughput run은 정답이 없는 성능 프롬프트이므로 complete=0이 정상입니다.
- vLLM은 엔진 decode 시간을 응답에 주지 않아 `decode tok/s (engine)`이 비어 있습니다. e2e 값은 prefill·네트워크를 포함합니다.
- Strata throughput-2/3은 같은 프롬프트의 대화 캐시를 재사용(205/210 토큰)해 TTFT·prefill 값이 첫 run과 다릅니다.
- 두 엔진의 chat template이 달라 같은 문제의 prompt 토큰 수가 다릅니다(44 vs 86).
- vLLM sanity의 미완료 1건은 reasoning이 512 토큰 상한에 걸린 것입니다(오답 아님, 예산 내 실패).

## 한계

반복 1~3회의 소표본입니다. sanity 12문항은 정상 동작 검사이며 일반 능력 비교가 아닙니다.
