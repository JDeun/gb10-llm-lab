# 공유 프롬프트: 긴 컨텍스트 검색 (ctx-*.jsonl)

입력 길이 단계별로 모델이 문맥 안의 정보를 정확히 찾는지 확인하는 고정 문제입니다.

- 형식: `bench.py --cases-file`용 JSONL. 파일마다 3문항(목표 레코드가 목록의 10% / 50% / 90% 위치).
- 내용: 결정적 난수(seed 20261112 + 목표 토큰 수)로 만든 레코드 목록 `Record NNNNN: code XXXX-XXXX; region ...; status ...; owner team-NN.`
  질문은 특정 레코드의 code를 묻고, 정답은 `expected_text`(정확 일치)입니다.
- 목표 길이: 512 / 2K / 8K / 32K / 60K / 120K 토큰(문자 수/3.4로 추정). **실제 토큰 수는 서버 usage의 prompt_tokens로 기록**하며 모델 토크나이저마다 다릅니다.
- 이 문제는 단순 검색(needle) 능력만 봅니다. 긴 문서 이해·추론 품질을 대표하지 않습니다.

| 파일 | 문자 수(문항당) |
|---|---:|
| ctx-512.jsonl | 1,901 |
| ctx-2k.jsonl | 7,135 |
| ctx-8k.jsonl | 27,993 |
| ctx-32k.jsonl | 111,585 |
| ctx-60k.jsonl | 204,109 |
| ctx-120k.jsonl | 408,149 |
