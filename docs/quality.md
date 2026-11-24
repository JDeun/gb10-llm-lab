# 정확성 평가 계획

## 현재 구현 범위

`benchmarks/bench.py`는 API 응답과 지정된 정답의 exact text/JSON 비교를 구현합니다. `prompts/sanity.jsonl`은 직접 만든 12개 정상 동작 검사입니다. **MMLU-Pro 등의 표준 벤치마크를 이미 수행하거나 구현한 상태가 아닙니다.**

산술·JSON·값 추출을 통과해도 일반 추론·코딩·한국어 지식 성능을 입증하지 않습니다. 현재 검사로 확인하는 것은 템플릿·종료·정답 필드·스트림·기초 응답의 정상 동작입니다.

## 다음 평가 단계

1. **탐색 세트:** 고정 ID의 작은 문제 묶음으로 시간과 채점 파이프라인 검증. tuning 문제와 확인 문제를 분리.
2. **일반 능력:** MMLU-Pro 등 공개 평가의 공식 task/채점기를 검토하고, 엔진 API가 실제 지원하는 요청 방식으로 연결.
3. **업무 성능:** 한국어 문서 QA, 정보 추출, JSON 도구 인자 같은 문제를 별도 범주로 평가.
4. **최종 확인:** 선택한 문제 ID·데이터 리비전·하네스 커밋·생성 예산·채점 규칙을 고정한 뒤 비교.

[EleutherAI API guide](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/API_guide.md)는 OpenAI 호환 local API 경로를 설명합니다. 모든 task가 chat 생성만으로 평가 가능한 것은 아닙니다. loglikelihood가 필요한 task와 generate-until task를 구분하고, 서버 지원을 검증한 조합만 사용합니다.

[MMLU-Pro 공식 저장소](https://github.com/TIGER-AI-Lab/MMLU-Pro)는 일반 능력 평가 후보의 기준 문서입니다. 선택 문제, 정답, prompt format, few-shot 예시, 답 추출 규칙을 임의로 바꾼 점수를 공식 점수와 동일하게 표시하지 않습니다.

작은 subset이나 zero-shot 변형은 별도의 이름으로 표시합니다. `--limit`를 쓴 개발 결과를 전체 benchmark 점수로 부르지 않습니다. 모델 공개 카드의 점수를 로컬 저비트 실행의 점수로 재사용하지 않습니다.

## 필요한 고정 정보

데이터셋 ID/리비전/라이선스, sample ID 목록과 hash, task YAML/채점기 커밋, prompt template, 모델/양자화 해시, thinking/temperature/seed, 토큰 예산, 완료율과 모든 분모를 저장합니다.

생성 답변 코드를 실행하는 평가는 격리된 실행 환경과 검증기를 준비한 뒤 별도 구현합니다. 이 초기 키트는 모델이 만든 코드를 실행하지 않습니다.

## 품질과 속도 비교

정확성용 문제와 throughput용 입력은 목적이 다릅니다. 같은 모델의 runtime 개선을 검증할 때 동일 문제에서 답변 변화도 확인합니다. 양자화 손실을 측정하려면 같은 모델의 신뢰할 수 있는 reference가 필요하며, 현재 Qwen 기준은 업무상 비교점으로 사용합니다.

## 구현한 답변 품질 평가 (2026-11-16)

`automation/tools/quality_eval.py`가 OpenAI 호환 API로 생성만 사용하는 zero-shot 평가를 수행합니다. 점수 이름은 `<set>-subset-zeroshot`이며 **공식 벤치마크 점수와 비교하지 않습니다.**

| 세트 | 데이터 (리비전, 라이선스) | 문항 | 형식 | 채점 |
|---|---|---|---|---|
| `mmlu-pro` | TIGER-Lab/MMLU-Pro `b189ec765a`, MIT | 140 (test, seed 고정 무작위) | 10지선다, 마지막 줄 `The answer is (X)` | 마지막 선택지 문자 일치 |
| `kmmlu` | HAERAE-HUB/KMMLU `d61b3f19e5`, CC-BY-ND-4.0 | 100 (20개 과목 × 5, 특허 과목 포함) | 4지선다, 마지막 줄 `정답: (X)` | 문자 일치 |
| `gsm8k` | openai/gsm8k `740312add8`, MIT | 100 (test) | 수학 서술, `The answer is <number>` | 숫자 일치 |
| `hrm8k-gsm8k` | HAERAE-HUB/HRM8K `c360cabf8d`, MIT | 100 (GSM8K 한국어) | `정답: 숫자` | 숫자 일치 |
| `open-ko` | 직접 작성 12문항 (`results/_shared/quality/open-ko.jsonl`) | 12 | 서술형 (업무 메일, 요약, 설명, 코드 리뷰, SQL, 특허 청구항 분해·대비, 뉘앙스, 불확실한 사실, 거절, 구조화) | 자동 채점 없음, 정성 비교용 응답 저장 |

- 공통 조건: `temperature 0`, 출력 예산 4,096 토큰, 동시 4요청, 모델·엔진 기본 reasoning (조건 비교 항목은 `extra_body`로 변경).
- 분모: 계획(N)·시도·완료(잘림 아님)·채점 가능·정답(K)을 모두 저장합니다. 잘림(`finish_reason=length`)은 오답과 구분해 `truncated_outputs`로 셉니다.
- 문제 본문은 커밋하지 않습니다(KMMLU 라이선스). seed와 문제 ID 목록(`results/_shared/quality/manifest.json`)으로 같은 문제를 다시 받을 수 있습니다.
- 모델이 만든 코드는 실행하지 않습니다. 코드 문항은 정성 비교만 합니다.

### 정성 평가 계획

`open-ko` 응답은 모델별 결과 폴더의 `runs/quality-open-ko/results.jsonl`에 저장됩니다. 같은 문항의 여러 모델 응답을 모델 이름을 가린 채 나란히 보고 점수를 매기는 비교 페이지를 별도로 만들 예정입니다(사람 평가). 자동 판정(LLM-as-judge)은 판정 모델·프롬프트를 고정한 뒤 별도 항목으로 추가합니다.

### 자동 판정 (LLM-as-judge, 2026-11-16)

`automation/tools/judge_codex.py`가 Mac의 Codex CLI(`codex exec`, 판정 모델 `gpt-6.1-sol`, 읽기 전용·기록 없음 모드, JSON 스키마 출력)로 `open-ko` 응답을 판정합니다.

- 방식: 기준 모델 대비 쌍대 비교. 모델 이름은 가리고 A/B 위치를 바꿔 문항마다 2회 판정, 승·무·패와 1~10점, 위치 일관성(두 판정이 같은 결과인 문항 수)을 기록합니다.
- 판정 프롬프트 sha: 결과 JSON의 `judge.template_sha`. 판정 모델이나 프롬프트가 바뀐 결과끼리는 비교하지 않습니다.
- 실행: GB10의 결과를 가져온 Mac 저장소에서 `python3 automation/tools/judge_codex.py --candidate results/<후보> --reference results/<기준>`. 결과는 `results/_shared/judgments/`에 저장합니다.
- 외부 전송: 직접 작성한 비민감 문항과 공개 모델의 응답만 판정 서비스로 보냅니다. 회사 데이터가 들어간 문항은 이 경로로 판정하지 않습니다.
- 한계: 판정 모델의 선호(길이, 문체, 자사 모델 계열)가 섞일 수 있습니다. 사람 평가와 함께 봅니다.

## 실전 과제와 최종 확인 (2026-11-16 추가)

| 세트 | 내용 | 채점 |
|---|---|---|
| `humaneval` | openai/openai_humaneval 164문항 전체 (MIT) | 응답의 마지막 ```python 블록 + 공식 테스트를 **격리 컨테이너**에서 실행해 통과 여부 (pass@1, temperature 0) |
| `tools-ko` | 직접 작성 12문항 (`results/_shared/quality/tools-ko.jsonl`): 날씨·특허 검색·일정·환율·메신저·주가 6개 도구 | 첫 tool call의 함수 이름과 필수 인자 일치(대소문자·공백·문장부호 무시, 같은 뜻 표기 허용) |

- 격리 컨테이너: `python:3.12-slim`, 네트워크 없음, 읽기 전용 루트, `/tmp` 16 MB, 메모리 512 MB, CPU 1, 프로세스 64개, 15초, 권한 없는 사용자(65534). 네트워크 차단을 실제로 확인했습니다.
- vLLM은 tool parser(`--enable-auto-tool-choice`)를 켠 항목에서만 `tools-ko`를 실행합니다.
- **confirm 프로필**(최종 후보 확인): `-l` 세트(MMLU-Pro 420, KMMLU 300, GSM8K 300, HRM8K 300) + humaneval + tools-ko + open-ko, sanity 2048, 속도 5회 반복, 동시성. 상위 후보를 고른 뒤 큐에 추가합니다.
- **용도별 추천**: `automation/tools/recommend.py`가 `results/RECOMMENDATION.md`를 만듭니다(대화·배치·코딩·긴 문서·최대 품질, 파레토 최적 표시). 결과를 가져올 때마다 다시 생성합니다.

## 생각(추론) 조절 변형 (2026-11-24)

- **언제 추가하나:** 품질 측정에서 답이 출력 한도에 걸려 잘린 비율이 5%를 넘으면, 그 모델의 생각 조절 변형을 같은 엔진 설정으로 추가합니다.
  - 잘린 답은 오답과 따로 셉니다(`truncated_outputs`).
- **어떤 키로 끄나:** 모델 템플릿마다 키가 다르므로 채팅 템플릿을 먼저 확인합니다.

  | 모델 | 끄는 방법 |
  |---|---|
  | Qwen·EXAONE·Gemma | `chat_template_kwargs.enable_thinking: false` |
  | Solar Open | `reasoning_effort: "minimal"`(`enable_thinking` 무시) |
  | HyperCLOVAX-SEED-Think | `skip_reasoning: true` |
  | Inkling 2 | `reasoning_effort` 0.0~0.99(기본 0.9, "none"=0.0) |
  | gpt-oss·Bonsai | `reasoning_effort` low/medium |

- **엔진 기본값 주의:** llama.cpp는 템플릿 기본값과 달리 생각을 켜는 경우가 있습니다. 예를 들어 Gemma 4는 vLLM에서 잘림 0%였지만 llama.cpp에서는 35%였습니다.
- **판정:** 같은 모델의 생각 끔·중간·기본을 나란히 두고, 용도(대화 서비스 vs 추론·수학)별로 고릅니다.
