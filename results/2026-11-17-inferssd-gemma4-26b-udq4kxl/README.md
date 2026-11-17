# 2026-11-17 · inferssd · inferssd-gemma4-26b-udq4kxl (자동 실행)

**상태:** 실패 (`server_exited`)  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | unsloth/gemma-4-26B-A4B-it-GGUF |
| 받은 파일 | gemma-4-26B-A4B-it-UD-Q4_K_XL.gguf (예상 16 GB) |
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
inferssd: invalid Gemma4 RAM metadata: attention.head_count_kv

```

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
