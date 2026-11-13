# 2026-11-13 · ikllama · ikllama-qwen36-35b-udq4kxl (자동 실행)

**상태:** 실패 (`server_exited`)  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | unsloth/Qwen3.6-35B-A3B-GGUF |
| 받은 파일 | Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf (예상 22 GB) |
| 엔진 옵션 | `-c 65536 -fmoe` |
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

         --log-test               Run simple logging test
         --log-disable            Disable trace logs
         --log-enable             Enable trace logs
         --log-file FNAME         Specify a log filename (without extension)
         --log-new                Create a separate new log file on start. Each log file will have unique name: "<name>.<ID>.log"
         --log-append             Don't truncate the old log file.

cvector:

  -o,    --output FNAME           output file (default: 'control_vector.gguf')
         --positive-file FNAME    positive prompts file, one prompt per line (default: 'examples/cvector-generator/positive.txt')
         --negative-file FNAME    negative prompts file, one prompt per line (default: 'examples/cvector-generator/negative.txt')
         --pca-batch N            batch size used for PCA. Larger batch runs faster, but uses more memory (default: 100)
         --pca-iter N             number of iterations used for PCA (default: 1000)
         --method {pca,mean}      dimensionality reduction method to be used (default: pca)

export-lora:

  -m,    --model                  model path from which to load base model (default '')
         --lora FNAME             path to LoRA adapter  (can be repeated to use multiple adapters)
         --lora-scaled FNAME S    path to LoRA adapter with user defined scaling S  (can be repeated to use multiple adapters)
  -o,    --output FNAME           output file (default: 'ggml-lora-merged-f16.gguf')


```

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
