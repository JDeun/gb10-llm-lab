# GB10 LLM Lab

**GB10 한 대(통합 메모리 121.6 GiB, NVMe 1 TB)에서 "돌아가는가"와 "쓸 만한가"를 함께 측정합니다.** 모델과 엔진 조합별로 속도·품질·컨텍스트·메모리를 재고, 용도별로 가장 효율적인 조합을 찾습니다.

측정은 GB10에서 자동으로 진행됩니다. 큐에 쌓인 조합을 하나씩 실행하고, 결과를 정리해 저장소에 커밋합니다.

| 현황 (2026-11-25) | |
|---|---|
| 측정 완료 / 실패 | 60 / 17 |
| 결과 묶음 | 102개 (품질 측정 포함 32개) |
| 큐에 남은 조합 | 128개 |
| 후보 모델 | 41개 |
| 엔진 | vLLM, llama.cpp, ik_llama.cpp, Strata, InferSSD, colibri, Prism, NariQ 포크 |

## 먼저 볼 문서

| 무엇을 알고 싶은가 | 문서 |
|---|---|
| **용도별 추천 조합** (파레토 최적) | [`results/RECOMMENDATION.md`](results/RECOMMENDATION.md) |
| 전체 측정 결과 표 | [`results/SUMMARY.md`](results/SUMMARY.md) |
| **모델별 라이선스와 출처 URL** | [`docs/licenses.md`](docs/licenses.md) |
| 후보 모델 목록과 선정 근거 | [`docs/candidates.md`](docs/candidates.md) |
| 품질 평가 방법 | [`docs/quality.md`](docs/quality.md) |
| 자동화 구조와 사고 기록 | [`docs/automation.md`](docs/automation.md) |
| 서버 운영 (서빙·복구) | [`docs/operations.md`](docs/operations.md) |
| 측정 지표 정의 | [`docs/metrics.md`](docs/metrics.md) · [`docs/protocol.md`](docs/protocol.md) |

## 지금까지의 결론

품질은 객관식·수학·코드·툴 호출 부분집합의 평균 정답률입니다. **공식 벤치마크 점수가 아닙니다.** 문항이 100~420개라 ±5%p 안팎 차이는 같은 수준으로 봅니다.

| 용도 | 추천 | 품질 | 단일 | 동시 16명 | 라이선스 |
|---|---|---|---|---|---|
| **여러 명이 쓰는 서비스** | Qwen3.6-35B-A3B NVFP4 · vLLM · 생각 끔 | 0.889 | 95 tok/s | 484 tok/s | Apache 2.0 |
| **품질 최우선** | Qwen3.8-Flash-Next IQ3_S · Strata | 0.919 | 54 tok/s | 83 tok/s | Qwen Community 1.0 (조건부) |
| **코딩·에이전트** | gpt-oss-120b · llama.cpp | 코드·툴 0.985 | 55 tok/s | — | Apache 2.0 |

**측정하면서 반복해서 확인된 것**

- **생각(추론)을 끄거나 줄이면 품질이 올라가는 경우가 많습니다.** 생각이 길면 답이 출력 한도에 걸려 잘리고, 잘린 답은 오답이 됩니다. 모델마다 최적점이 달라서(완전히 끔 / 중간 / 켬) 조합마다 따로 재야 합니다. → [`docs/quality.md`](docs/quality.md)
- **같은 모델도 엔진에 따라 크게 달라집니다.** Gemma 4는 vLLM에서 잘림 0%, llama.cpp에서 35%였습니다. 엔진 기본값이 달라서입니다.
- **작게 압축한 모델이 의외로 강합니다.** 27B를 3진 압축한 6 GB 파일이 원본 FP8(27 GB)보다 품질과 속도 모두 앞섰습니다.
- **라이선스를 먼저 봐야 합니다.** 품질 1위 모델은 Apache 2.0이 아니고, 후보 중 하나는 상업적 사용이 금지돼 있습니다.

## 측정 방식

### 자동 실행

GB10의 user systemd 서비스(`lab-runner`)가 큐를 읽어 한 번에 하나씩 실행합니다.

```
큐에서 다음 항목 선택 → 가중치 다운로드 → 엔진 기동 → 측정 → 결과 커밋 → 모델 삭제
```

- **선택 순서:** ① 이미 받아둔 파일이 있는 항목(엔진 체인 유지) → ② 라이선스 등급(`free` → `conditional` → `non_commercial`) → ③ 다운로드 크기
- **다운로드 예산:** 주당 500 GB. 회사 네트워크 제한 때문이며, 저장소당 주 1회만 차감합니다.
- GB10은 **로컬 커밋까지만** 합니다. 원격 푸시와 PR은 사람이 확인한 뒤 진행합니다.
- 측정이 끝난 모델 파일은 자동으로 지웁니다. 다음 엔진이 같은 파일을 쓰면 남겨둡니다(`keep_for`).

### 측정 항목

| 단계 | 무엇을 재나 |
|---|---|
| capacity | 출력 길이를 늘려가며 한계 확인 |
| context | 512 / 2K / 8K / 32K / 60K 입력에서 정답을 내는지 |
| throughput | 단일 요청 생성 속도 (5회 반복) |
| concurrency | 동시 1·4·8·16명일 때 합계 처리량과 첫 응답 시간 |
| quality | MMLU-Pro, KMMLU, GSM8K, HRM8K, HumanEval, 툴 호출, 한국어 자유 답변 |

- **잘린 답은 오답과 따로 셉니다.** 생각이 길어 출력 한도에 걸린 것과 틀린 것은 다른 문제입니다.
- HumanEval은 네트워크를 끊은 도커 샌드박스에서 채점합니다.
- 한국어 자유 답변은 Mac의 Codex CLI가 모델 이름을 가리고 A/B 위치를 바꿔가며 비교합니다.
- 최종 후보는 `confirm` 프로필(문항 3배, 속도 5회 반복)로 다시 확인합니다.

### 결과 구조

```
results/<날짜>-<항목id>/
  README.md      측정 조건과 결과 표
  manifest.json  모델·엔진 리비전, 체크섬
  steps.json     단계별 성공/실패
  runs/          단계별 원시 응답과 집계
  concurrency*-summary.json
```

## 모델을 새로 추가할 때

**측정보다 라이선스 확인이 먼저입니다.**

1. Hugging Face에서 라이선스를 확인합니다. `other`로 나오면 LICENSE 원문을 읽습니다.
2. 재배포본이면 원본 모델의 라이선스도 봅니다. 재배포자가 원본보다 느슨한 조건을 붙일 수는 없습니다.
3. [`docs/licenses.md`](docs/licenses.md)에 모델명·라이선스·URL·확인한 조항을 적습니다.
4. 큐에 항목을 넣고 등급을 부여합니다.
   ```bash
   python3 automation/tools/tag_licenses.py configs/queue.json
   ```

절차 상세는 [`docs/licenses.md` §6](docs/licenses.md)에 있습니다.

## 저장소 구조

```
automation/tools/   실행기와 측정 도구 (lab_runner, lab_suite, quality_eval, judge_codex, recommend ...)
automation/systemd/ GB10 서비스 정의
automation/netwatch/ 네트워크 끊김 복구 watchdog
configs/queue.json  측정할 조합 (GB10 큐의 사본)
configs/models.json 후보 모델 목록
docs/               방법론·라이선스·후보·사고 기록
results/            측정 결과 묶음과 종합 표
benchmarks/         수동 측정용 CLI (초기 도구)
```

## 읽을 때 주의할 점

- 품질 점수는 **부분집합 zero-shot 정답률**입니다. 공식 리더보드 점수와 비교하면 안 됩니다.
- 속도는 짧은 프롬프트와 짧은 출력 기준입니다. 실제 사용 패턴(긴 문맥, 긴 답변)에서는 달라집니다.
- 외부에서 공개한 수치는 우리 측정과 구분해 표기합니다.
- 공개 저장소이므로 IP·호스트명·API 키는 들어가지 않습니다. 결과 공개 전에 자동으로 걸러냅니다.

## 개발 검증

```bash
python3 -m unittest discover -s tests -v
python3 benchmarks/validate_project.py
```

로컬 모의 HTTP/SSE와 예산 계산만 검사합니다. **CI 통과는 측정 결과의 정확성을 보증하지 않습니다.**
