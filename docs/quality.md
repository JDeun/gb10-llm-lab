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
