# 2026-11-14 · strata · strata-qwen38fn-udq4kxl (자동 실행)

**상태:** 실패 (`command_failed`)  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | unsloth/Qwen3.8-Flash-Next-GGUF (UD-Q4_K_XL) |
| 받은 파일 | 전체/엔진 기본 (예상 111 GB) |
| 엔진 옵션 | `--family qwen --model ud-q4_k_xl --context 64k --vision off --drafting mtp --tune skip` |
| API 별칭 | None |
| 측정 프로필 | standard |
| 공간 확보로 지운 모델 | - |

## 결과

(측정 결과 없음)


## 실패 정보

- 종류: `command_failed`
- 내용: <user-home>/.local/bin/strata launch --family qwen rc=2 strata: Qwen3.8-Flash-Next has no size UD-Q4_K_XL. It offers: Q2_0, IQ2_XS, IQ3_XXS, IQ3_S.


엔진 로그 끝부분:

```
ated in 5845 ms (22.07 tok/s); CPU lane 0.1% of the experts
maya ds4 serve: drafts 52 of 62 kept; per position (kept / reached): 1: 32/34 94% 2: 12/14 86% 3: 6/9 67% 4: 2/2 100%
maya ds4 serve: prompt 369 tokens = 224 reused + 145 read in 1133 ms (128.0 tok/s), 111 generated in 5545 ms (20.02 tok/s); CPU lane 0.1% of the experts
maya ds4 serve: drafts 39 of 51 kept; per position (kept / reached): 1: 22/29 76% 2: 11/12 92% 3: 4/4 100% 4: 2/2 100%
maya ds4 serve: 1 pictures, 1 read (1697 ms)
maya ds4 serve: prompt 228 tokens = 0 reused + 228 read in 3836 ms (59.4 tok/s), 58 generated in 3872 ms (14.98 tok/s); CPU lane 0.1% of the experts
maya ds4 serve: drafts 28 of 43 kept; per position (kept / reached): 1: 16/19 84% 2: 8/10 80% 3: 3/5 60% 4: 1/2 50%
maya ds4 serve: 1 pictures, 1 read (154 ms)
maya ds4 serve: prompt 235 tokens = 0 reused + 235 read in 2557 ms (91.9 tok/s), 37 generated in 1922 ms (19.25 tok/s); CPU lane 0.1% of the experts
maya ds4 serve: drafts 21 of 31 kept; per position (kept / reached): 1: 8/10 80% 2: 7/7 100% 3: 5/6 83% 4: 1/4 25%
maya ds4 serve: 1 pictures, 1 read (157 ms)
maya ds4 serve: prompt 229 tokens = 0 reused + 229 read in 2733 ms (83.8 tok/s), 42 generated in 1759 ms (23.87 tok/s); CPU lane 0.1% of the experts
maya ds4 serve: drafts 29 of 37 kept; per position (kept / reached): 1: 13/13 100% 2: 9/10 90% 3: 3/5 60% 4: 2/2 100% 5: 2/2 100%
ds4 slots: wrote 4 conversation(s) to <user-home>/.local/state/strata/launch/ds4-slots; 12 there in all

```

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
