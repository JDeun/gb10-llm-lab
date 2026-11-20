# 2026-11-19 · inferssd · inferssd-gpt-oss-120b-mxfp4 (자동 실행)

**상태:** 실패 (`server_exited`)  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | ggml-org/gpt-oss-120b-GGUF |
| 받은 파일 | gpt-oss-120b-MXFP4.gguf (예상 63 GB) |
| 엔진 옵션 | `` |
| API 별칭 | None |
| 측정 프로필 | standard |
| 공간 확보로 지운 모델 | - |

## 결과

(측정 결과 없음)


## 실패 정보

- 종류: `server_exited`
- 내용: server process ended before answering

엔진 로그 끝부분:

```
Starting API at http://127.0.0.1:8080/v1
inferssd: no model profile for the GGUF architecture gpt-oss; choose one with --profile dsv, muse, qwen4exp, qwen35moe, gemma4

```

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
