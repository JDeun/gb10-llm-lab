# GB10 LLM Lab

**GB10 한 대와 내장 SSD 1TB에서 모델 크기·정확성·속도·메모리·안정성을 측정해, 조건별로 사용할 수 있는 최대 모델을 찾습니다.**

현재 상태: 측정 도구와 실험 프로토콜 준비. **사용자 GB10의 실측 결과는 아직 없습니다.** RAM 용량, 실제 빈 SSD 공간, 현재 서빙 프로그램은 확인 전입니다. 현재 Qwen3.6-35B-A3B-NVFP4 실행 사실과 SSD 1TB는 사용자 제공 정보입니다.

## 결과로 답할 질문

1. 전체 전문가를 유지한 모델 중 어떤 규모까지 지정된 작업을 완료하는가?
2. 그 모델은 고정된 문제를 얼마나 정확하게, 얼마나 자주 끝까지 해결하는가?
3. 품질·첫 응답 시간·생성 속도·컨텍스트 조건을 주었을 때 가장 큰 모델은 무엇인가?
4. 같은 체크포인트와 정밀도를 유지하며 어떤 실행 설정이 빨라지는가?

가용성 기준은 임의의 한 숫자로 정하지 않습니다. `configs/policy.json`의 미정 기준은 null입니다. 기준을 정하기 전에는 크기–품질–속도의 비교표를 만들고, 최종 확인 실험 전에 조건을 고정합니다. **미정 값을 통과로 처리하지 않습니다.**

## 지금 할 일: GB10에서 장비 정보 수집

Python 3.10 이상과 표준 라이브러리만 필요합니다.

```bash
git clone https://github.com/JDeun/gb10-llm-lab.git
cd gb10-llm-lab
mkdir -p local
python3 benchmarks/bench.py inventory \
  --model-dir /실제/모델/디렉터리 \
  --output local/inventory.json
```

`--model-dir`를 모델을 저장할 **실제 존재하는 경로**로 바꿉니다. 메모리·디스크 정보는 이 명령을 실행한 컴퓨터의 정보입니다. **GB10 자체에서 실행**해야 합니다. 새 출력 파일만 허용하므로 다시 실행할 때는 다른 이름을 사용합니다.

다음으로 필요한 정보는 `local/inventory.json`, 현재 Qwen의 **서빙 프로그램/실행 명령**, **API 주소와 모델 별칭**입니다. 결과를 공유하기 전 경로 등 필요한 내용을 확인합니다. `local/`는 Git에서 제외됩니다.

## 현재 Qwen으로 측정 경로 확인

이미 실행 중인 서버에 한 요청만 보냅니다. 아래 API 주소와 별칭은 실제 값으로 바꿉니다.

```bash
python3 benchmarks/bench.py run \
  --base-url http://127.0.0.1:8000 \
  --model '실제_API_모델_별칭' \
  --model-dir /실제/모델/디렉터리 \
  --max-tokens 32 \
  --repeats 1 \
  --case-label qwen-api-check \
  --output-dir local/qwen-api-check
```

기본은 산술 문제 한 개입니다. 추론 중 출력 제한에 걸리면 **미완료**로 남으며, 완성 오답과 구분합니다. 이 확인이 끝나면 `configs/manifest.example.json`을 복사해 실제 모델/엔진 설정을 기록하고 다음 단계로 진행합니다.

### 정상 동작 검사

```bash
python3 benchmarks/bench.py run \
  --base-url http://127.0.0.1:8000 \
  --model '실제_API_모델_별칭' \
  --cases-file prompts/sanity.jsonl \
  --max-tokens 512 \
  --repeats 1 \
  --manifest local/manifest.json \
  --case-label integration-sanity-v1 \
  --output-dir local/qwen-sanity
```

이는 직접 작성한 **12개 정상 동작 검사**입니다. 일반 능력 벤치마크가 아니며 512토큰이 모든 reasoning 모델에 충분한 것도 아닙니다. 정식 품질 평가는 별도 고정 문제·채점기·생성 예산을 사용합니다. 계획 대비 실행 비율, 미완료율, 조건부 정답률과 예산 내 성공률을 함께 기록합니다.

### 출력 속도 탐색

```bash
python3 benchmarks/bench.py run \
  --base-url http://127.0.0.1:8000 \
  --model '실제_API_모델_별칭' \
  --prompt-file prompts/throughput_ko.txt \
  --max-tokens 256 \
  --repeats 1 \
  --manifest local/manifest.json \
  --telemetry \
  --case-label qwen-throughput-pilot \
  --output-dir local/qwen-throughput-pilot
```

실제 출력 토큰 수는 서버 usage에서 가져옵니다. SSE 청크를 토큰으로 세지 않습니다. 엔진 내부 생성 시간은 서버가 명시적으로 제공할 때만 기록합니다. 전체 응답시간으로 계산한 처리량은 순수 decode 속도와 다릅니다.

## 큰 모델로 넘어가기 전

```bash
python3 benchmarks/preflight.py \
  --inventory local/inventory.json \
  --catalog configs/models.json \
  --candidate kimi-k3-iq1s-xs \
  --output local/kimi-storage-preflight.json
```

파일이 들어갈 공간을 추정하는 도구입니다. **RAM 적합성이나 엔진 지원을 보증하지 않습니다.** 추가 준비 공간이 미확인이면 하한만 검사하고 미확정으로 표시합니다. 기본 64GiB 여유는 조정 가능한 계획 값이며 하드웨어의 공식 요구량이 아닙니다.

최대 후보는 전체 전문가를 유지한 Kimi K3 저비트 GGUF 약 580~594GB입니다. 단일 GB10에서의 실행 경로는 아직 검증하지 못했습니다. 337GB DeepSeek V4 Pro CPU+mmap 개인 사례는 재현 후보, Strata DeepSeek는 대형 모델 대조군입니다. **1.61TB Kimi FTW는 현재 1TB 범위에서 제외**합니다. 후보별 근거와 한계는 [후보 문서](docs/candidates.md)에 있습니다.

한 번에 하나의 양자화 버전을 다룹니다. 모델별 설치와 다운로드 명령은 실제 RAM·빈 공간·지원 엔진·고정 리비전을 확인한 뒤 기록합니다.

## 실험 순서

| 단계 | 실행 | 남길 결과 |
|---|---|---|
| 0 | 장비·공간·현재 서버 확인 | inventory와 기준 manifest |
| 1 | 현재 Qwen 기준 측정 | 정상 동작, 완료율, TTFT, 실제 출력량 |
| 2 | 대형 후보 실행 경로 검증 | 성공과 실패 원인, 고정 체크포인트 |
| 3 | 출력 길이와 입력 컨텍스트를 각각 확대 | 용량 한계와 메모리/I/O |
| 4 | 고정 품질 평가와 반복 속도 측정 | 점수·분모·불확실성·지연 |
| 5 | 같은 모델의 최적화 A/B | 변경 한 가지의 효과, 품질 유지 여부 |
| 6 | 유망한 최종 구성 지속 실행 | 조건별 최대치와 한계 |

자세한 정의는 [프로토콜](docs/protocol.md), 집계 필드는 [측정 지표](docs/metrics.md), 외부 평가 연동 범위는 [품질 평가 계획](docs/quality.md)을 따릅니다.

## 도구의 범위

모델 다운로드·설치·서버 기동/종료·전역 캐시 삭제·전원 설정 변경을 자동 수행하지 않습니다. 초기 GitHub Actions는 **CPU에서 측정 코드만 검사**합니다. 실제 GB10 벤치는 수동으로 실행하며, 공개 저장소 이벤트에 연결된 self-hosted GPU runner는 구성하지 않습니다.

`--timeout 1200`은 소켓 무응답 시간이며 총 실행시간 제한이 아닙니다. Ctrl-C는 클라이언트를 종료하며 서버의 추론 취소 여부는 해당 서버에 달려 있습니다. 서버가 별도 reasoning 필드를 주지 않으면 content 안의 생각과 답변을 자동 구분하지 않습니다.

`--api-key-env`로 기존 환경변수의 키를 사용할 수 있습니다. `--extra-body`는 API별 옵션을 명시하는 JSON 파일입니다. 지원하지 않는 API 옵션에 자동 재시도하지 않습니다.

## 개발 검증

```bash
python3 -m unittest discover -s tests -v
python3 benchmarks/validate_project.py
```

로컬 모의 HTTP/SSE와 파일시스템 예산 계산만 검사합니다. **CPU CI 통과는 모델 정확성이나 GB10 성능 측정 결과가 아닙니다.**

## 결과 저장

원시 실행은 `local/`에 보관합니다. 공개할 결과만 검토 후 `results/`에 넣습니다. 가중치와 다운로드 캐시는 Git에 넣지 않습니다. 외부 제작자의 수치는 자신의 실측과 구분합니다.
