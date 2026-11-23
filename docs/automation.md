# 무인 실험 자동화 (2026-11-12)

GB10 한 대가 [실행 큐](../configs/queue.json)를 사람 개입 없이 순서대로 처리합니다. 이 문서는 모든 자동 실행 결과에 공통으로 적용되는 **실험 조건**과 **코드 구조**를 설명합니다. 실행별 세부 설정은 각 결과 폴더의 `manifest.json`에 있습니다.

## 구성

| 파일 (`automation/`) | 역할 |
|---|---|
| `tools/lab_runner.py` | 큐 실행기. 항목마다 디스크 확보 → 다운로드 → 서버 시작 → 측정 → 내보내기·로컬 커밋 → 서버 종료 → 파일 삭제 |
| `tools/lab_suite.py` | 측정 단계 계획·실행, manifest 생성, 결과 내보내기와 자동 README·로컬 커밋 |
| `tools/export_public.py` | 공개용 내보내기: 경로·호스트명·사설 IP 마스킹, 긴 프롬프트를 sha256+앞부분으로 축약, 단계별 요약표(`TABLE.md`) |
| `tools/make_manifest.py` | 장비 정보(메모리·OS·커널·드라이버·저장장치·여유 공간)와 항목 정보를 합친 manifest |
| `tools/gen_context_cases.py` | 긴 입력 검색 문제 생성기 (`results/_shared/prompts/ctx-*.jsonl`과 같은 결과) |
| `tools/vision_check.py` | 합성 이미지 3장의 정답 검사 (단색, 좌우 분할, 사각형 개수) |
| `tools/concurrency.py` | 4개 동시 클라이언트 결과 합산 |
| `tools/soak.sh` | 지속 부하 시험 (30분 시험에 사용) |
| `tools/swap_runner.sh` | 실행 중인 항목이 끝난 뒤 새 실행기로 교체 (측정 재실행 없음) |
| `tools/serve-default.sh`, `run-vllm.sh` | 큐가 끝난 뒤의 상시 서빙 (vLLM Qwen3.6, Tailscale 주소 전용) |
| `tools/admin-setup.sh` | 1회성 관리자 설정 (Wi-Fi 절전 끔, snap 갱신 시간대, apt 자동 설치·재부팅 끔) |
| `tools/run-experiment.sh`, `run-lab-suite.sh` | 자동화 이전 수동 측정에 쓴 스크립트 (기록 보존용) |
| `systemd/*.service`, `*.timer` | 사용자 systemd 단위 (linger로 부팅 시 실행) |

호스트 고유 값은 저장소에 넣지 않고 GB10의 로컬 파일에서 읽습니다.

| 로컬 파일 | 내용 |
|---|---|
| `~/llm/host.env` | `TS_IP=<Tailscale IP>` |
| `~/llm/redact-terms.txt` | 마스킹할 사용자 이름·호스트명 (한 줄에 하나) |
| `~/llm/vllm.env` | 상시 서빙 API 키 (권한 600) |

## 측정 프로필

모든 요청은 `temperature 0`, 모델·엔진 기본 reasoning 설정, 동시 요청 1(동시성 단계 제외)입니다. 문제와 프롬프트는 저장소의 `prompts/`와 `results/_shared/prompts/`에 있습니다.

| 단계 | full | standard | slow | capacity |
|---|---|---|---|---|
| 출력 상한 단계 (throughput 프롬프트) | 1 / 16 / 64 / 256 | 1 / 16 / 64 / 256 | 1 / 16 / 64 | 1 / 16 / 64 |
| sanity 12문항 | 512 + 2048 예산 | 512 | 512 | 앞 4문항(`sanity-mini`), 512 |
| 긴 입력 검색 (출력 1024) | 항목의 `context` 목록 | 같음 | 같음 | 보통 512만 |
| 출력 속도 반복 | 256토큰 × 3 | 256토큰 × 3 | 256토큰 × 1 | 64토큰 × 1 |
| 4개 동시 요청 (각 2회, 256토큰) | O | O | - | - |
| 이미지 검사 | 항목의 `vision`이 참일 때 | 같음 | 같음 | 같음 |

- 긴 입력 라벨(512/2k/8k/32k/60k/120k)은 명목값입니다. 실제 입력은 라벨의 약 1.1~1.4배이고 결과표의 `prompt tok`에 실제 값이 있습니다.
- 각 ctx 파일의 3문항은 같은 레코드 목록을 공유하므로 2·3번째 요청은 캐시를 재사용할 수 있습니다. 결과표의 `TTFT cold` 열(엔진이 캐시 정보를 줄 때)이나 첫 문항을 첫 처리 값으로 봅니다.

## 시간 제한과 실패 처리

| 규칙 | 값 |
|---|---|
| 단계별 시간 제한 | 7,200초 (초과 시 그 단계만 `step_timeout`으로 기록하고 다음 단계 진행) |
| 소켓 무응답 제한 (bench.py) | 1,800초 |
| 서버 시작 대기 | 3,600초 기본, colibri 21,600초, 항목별 `start_timeout_s`로 변경 |
| 단계 전 서버 확인 | `/v1/models`가 응답하지 않으면 그 항목을 `server_down`으로 중단 |
| 자동 재시도 | `timeout`, `command_failed`, `server_down`, `server_exited`, `start_timeout`은 1회 재시도 (파일 유지). 그 밖의 실패와 두 번째 실패는 `failed`로 기록 |
| 엔진 미설치 | 그 항목을 건너뛰고 다음 항목 진행, 남은 항목이 모두 미설치 엔진이면 1시간마다 다시 확인 |
| 실패 기록 | 실패도 결과 폴더와 커밋으로 남김 (종류, 내용, 엔진 로그 끝부분) |

## 디스크와 파일 공유

- 시작 전 여유 공간이 `항목 크기 + 64 GiB`보다 작으면, 항목의 `may_evict`에 적힌 측정 완료 모델(Qwen3.8 IQ3_S)을 지우고, 그래도 부족하면 `storage_insufficient`로 실패 처리합니다.
- 측정이 끝나면 그 항목이 받은 파일을 지웁니다. HF 캐시는 저장소 폴더와 공용 `hub/blobs`의 실제 파일까지 지우며, 상시 서빙 모델(Qwen3.6 NVFP4)과 그 파일, 공용 폴더 자체는 삭제 대상에서 항상 제외합니다. docker(vLLM)가 root로 만든 파일은 같은 이미지 안에서 지웁니다.
- `keep_for`에 적힌 엔진 중 하나라도 설치돼 있으면 파일을 남겨, 바로 뒤 항목이 같은 GGUF로 다른 엔진을 측정합니다. 이것이 [엔진 비교 세트](candidates.md#엔진-비교-세트-2026-11-12-추가)의 방식입니다.

## 엔진별 실행 방식

| 엔진 | 포트 | 실행 |
|---|---|---|
| vLLM v0.32.0 | 8001 | `docker run vllm/vllm-openai:v0.32.0 <repo> --served-model-name <id> <vllm_args>` |
| Strata v0.2.13 | 8080 | `strata launch <launch> --access local --restart --no-tui --yes` (다운로드 포함) |
| llama.cpp v0.9.0 | 8002 | `llama-server -m <첫 shard> -ngl 999 -fa on --jinja <llama_args>` (sm_121 CUDA 빌드) |
| ik_llama.cpp | 8003 | 같은 명령, ARM 빌드 옵션 `-DGGML_NATIVE=OFF -DGGML_ARCH_FLAGS=-march=armv8.6-a+dotprod+i8mm+bf16` (이슈 #2651; GB10의 gcc 13은 `-mcpu=native`로 dotprod를 켜지 않음) |
| InferSSD 0.1.4 | 8080 | `inferssd serve -m <HF 캐시의 첫 shard>` 또는 `-hf <repo>` |
| Prism ML llama.cpp 포크 (prism 브랜치) | 8006 | 3진 Bonsai용 `PTQ1_0`·`PQ2_0` 커널, `-DLLAMA_BUILD_UI=OFF -DLLAMA_USE_PREBUILT_UI=OFF`로 빌드(기본 빌드는 내려받은 웹 UI 자산이 기대 버전과 달라 실패, `LLAMA_BUILD_HTML=OFF`로는 해결되지 않음) |
| colibri | 8005 | `coli import <첫 shard>` → `coli build --gpu auto` → `coli serve --auto-tier <colibri_args>` |

모든 서버는 `127.0.0.1`에만 바인딩합니다. 항목 사이에는 모든 엔진과 상시 서빙 컨테이너를 멈춥니다.

## 결과 반영 흐름

1. GB10이 결과를 `results/<날짜>-<항목 ID>/`에 내보내고 `results/gb10-runs` 브랜치에 **로컬 커밋만** 합니다. 자동 README에는 표와 조건만 있고 해석은 없습니다.
2. 다른 컴퓨터에서 그 커밋을 가져와 해석을 붙이고 푸시한 뒤 PR을 엽니다. main 병합은 사람이 승인합니다.

## 운영 중 고친 문제 (2026-11-12)

| 문제 | 영향 | 조치 |
|---|---|---|
| 측정 후 파일이 지워지지 않음 (HF 캐시의 공용 blob 구조, 실행기 이전에 생긴 폴더) | 디스크 323 GB 낭비 | 항목이 받은 파일을 링크 끝까지 추적해 삭제, 수동 정리 |
| 공용 `hub/blobs`가 새 폴더로 잡힐 수 있는 구조 | 상시 서빙 모델 삭제 위험 (실제 피해 없음) | 공용 폴더와 보존 모델 파일을 삭제 대상에서 항상 제외 |
| HF 해시를 내용 저장소 이름으로 기록 | gpt-oss `artifact.sha256` 오기록 | 첫 링크 이름(LFS sha256)으로 기록, 정정 커밋 |
| docker가 만든 root 파일 | 삭제 중 권한 오류로 실행기 중단 가능 | 컨테이너 안에서 삭제, 오류가 나도 계속 진행 |
| reasoning 파서 누락 | Nemotron sanity 0/12 (정답이 생각 과정과 함께 content에 들어감) | `--reasoning-parser deepseek_r1`로 재측정 항목 추가, 생각 과정을 쓰는 한국 모델에 미리 적용 |
| manifest 엔진 버전 표에 InferSSD·ik_llama.cpp·colibri 누락 (2026-11-13) | 실행기가 `KeyError`로 죽고 systemd가 1분마다 재시작하는 반복이 02:48~08:10(약 5시간 반, 222회) 지속 | 표 보강, 예상 못한 예외는 그 항목만 `runner_error`로 실패 처리하고 다음 항목 진행 |
| ik_llama.cpp ARM 빌드 3회 실패 | ik_llama.cpp 항목 지연 | gcc 13이 Cortex-X925를 몰라 `-mcpu=native`가 dotprod를 켜지 않음, fp16 벡터 연산도 필요 → `-march=armv8.6-a+dotprod+i8mm+bf16+fp16`로 빌드 성공 (2026-11-13 09:2x) |
| ik_llama.cpp에서 `-fmoe` 옵션이 없어짐 (fused MoE 기본 켜짐) | ik Qwen3.6 항목이 `unknown argument`로 실패 | 큐의 ik 항목 4개에서 제거, 재측정 |
| colibri가 CPU 전용으로 빌드됨 (`coli build`는 Makefile 기본값 `CUDA=0`) | colibri Qwen3.6 항목이 `--gpu`에서 2회 실패 | `CUDA=1`과 강제 재빌드(`MAKEFLAGS=-B`)로 빌드, 항목 재대기 |
| 항목 종료 시 상태 파일 전체를 덮어씀 | 실행 중에 다른 항목 상태를 고쳐도 되돌아감 | 자기 항목만 병합 저장, `~/llm/queue-reset.txt`에 적은 항목은 다음 순번에서 재대기 |
| 결과 폴더의 `runs/`가 루트 `.gitignore`의 `runs/` 규칙에 걸려 한 번도 커밋되지 않음 | 공개 결과에 요청별 원본(results.jsonl, summary.json)이 없었음 | `!results/*/runs/` 예외 추가, 수동 5건·자동 10건의 원본 추가 (2026-11-13) |

### 재측정 요청 방법

GB10에서 `echo <항목 ID> >> ~/llm/queue-reset.txt`를 실행하면 실행기가 다음 순번에 그 항목의 기록을 지우고 다시 실행합니다. 설정을 바꿔 다시 재려면 큐에 새 ID로 항목을 추가하는 편이 이전 결과를 보존합니다.
| InferSSD(`-hf`)가 받은 파일이 HF 공용 저장소에 남아 삭제되지 않음 (2026-11-16) | DeepSeek Q8 약 470 GB가 남아 뒤 항목 12개가 `storage_insufficient`로 연쇄 실패 | Strata를 뺀 모든 엔진은 HF 저장소 파일까지 삭제, 12개 재대기 |
| Nemotron-3-Ultra 550B(llama.cpp `--cpu-moe`)가 시스템 메모리를 소진 (2026-11-15 18:19) | 커널 OOM, Tailscale 중계 통신 약 45분 끊김 (원격 접속 불가) | 실행기 서비스에 `MemoryMax=108G`, `MemorySwapMax=4G`: 큰 모델은 실행기 단위 안에서만 종료되고 OS·sshd·tailscaled는 유지 |
| llama.cpp v0.9.0 미지원·불일치 GGUF | Ling-3.0-flash(`ssm_f_a` 텐서), MiniMax-M3.1-Flash(텐서 수), Solar-Open2(`solar-open2`), A.X-K2(`axk2`) 로드 실패 | 실패로 기록, 미지원 구조는 제외 목록에 추가 |

## 다운로드 예산 (2026-11-16, 회사 네트워크 사용량 제한)

- 첫 4일간 약 3.3 TB를 받아 회사 네트워크 사용량 제한에 걸린 뒤 도입했습니다.
- **주당 500 GB 단일 예산**(초대형 모델 약 1개 분량, `configs/queue.json`의 `defaults.download_budget.weekly_bytes`). 기록은 GB10의 `~/llm/download-ledger.json`.
- 실행 가능한 항목 중 **필요한 다운로드가 가장 작은 것부터** 실행합니다. 이미 받은 파일을 쓰는 항목은 0으로 계산되어 먼저 실행되므로, 같은 GGUF를 쓰는 엔진 묶음이 이어서 진행됩니다.
- 500 GB보다 큰 항목은 그 주에 다른 다운로드가 없을 때만 시작합니다. 받을 수 있는 항목이 없으면 6시간마다 다시 확인합니다.
- 일부만 받은 파일(예상 크기의 95% 미만)은 받아 둔 것으로 보지 않습니다.

### 2026-11-16 오후 사건

| 문제 | 영향 | 조치 |
|---|---|---|
| `swap_runner.sh`가 상태 파일에 남은 오래된 `running` 항목(멈춘 Muse 다운로드)을 기다림 | 실행기가 오전 코드로 계속 동작해 조건 비교 8개가 **품질 평가 없이** 끝남 | 가장 최근 시작한 `running` 항목을 기다리도록 수정, 8개 재측정 |
| 새 llama.cpp를 `llama.cpp-new`에서 빌드 후 폴더 이름 변경 | 실행 파일의 RUNPATH가 옛 경로를 가리켜 `libllama-server-impl.so`를 찾지 못함 → Ling 실패 | `llama.cpp-new` → `llama.cpp` 링크, 교체 스크립트에 반영, Ling 재대기 |
| 느린 회사 네트워크(약 1 MB/s)에서 다운로드 48시간 제한 | 500 GB 모델은 약 6일 걸려 시간 초과 후 실패 처리될 상황 | 다운로드 제한 14일, 다운로드 실패는 별도 횟수(최대 6회)로 이어받기 재시도 |
| 재시도마다 예산 장부에 같은 모델이 다시 기록 | 예산이 빨리 소진되고 재시도가 막힐 상황 | 저장소별 주 1회만 기록, 이미 기록된 저장소는 추가 예산 없이 이어받기 |

## 나중 실험 (`deferred`, 2026-11-17)

큐 항목에 `"deferred": true`를 붙이면 일반 항목이 모두 끝났거나, 남은 일반 항목이 다운로드 예산·엔진 미설치로 지금 실행할 수 없을 때만 실행합니다. GB10이 예산 대기로 쉬는 시간을 후속 실험에 씁니다. 관련 GitHub 이슈 번호는 항목의 `issue` 필드에 적습니다 (예: #14 Qwen3.8-Flash-Next 속도 개선).

- 2026-11-21: 큐 항목에 `"hold": "이유"`를 넣으면 runner가 그 항목을 고르지 않습니다(엔진 업데이트 대기 등). 필드를 지우면 다음 선택부터 실행 대상이 됩니다.

- 2026-11-23: Wi-Fi가 14시간 끊긴 채 다시 붙지 않은 사건(11-22~23, 재부팅은 없음). 절전 꺼짐과 자동 재연결 무제한 설정은 이미 돼 있었습니다. 그래서 `automation/netwatch/` watchdog을 root timer로 추가했습니다. 1분마다 게이트웨이나 1.1.1.1로 ping하고, 끊긴 상태가 이어지면 3분에 프로필 재연결, 6분에 Wi-Fi 끄고 켜기, 9분에 NetworkManager 재시작 순서로 단계를 올립니다. LAN은 되는데 Tailscale이 꺼져 있으면 tailscaled를 재시작합니다. 설치: `sudo bash ~/llm/netwatch/install.sh`, 로그: `journalctl -t net-watchdog`.
