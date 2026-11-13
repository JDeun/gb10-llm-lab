# 2026-11-13 · inferssd · inferssd-qwen36-35b-udq4kxl-ctx64k (자동 실행)

**상태:** 실패 (`server_down`)  
**작성:** 무인 실행기(`lab_runner.py`)가 생성했습니다. 해석은 아직 붙이지 않았습니다.

| 항목 | 값 |
|---|---|
| 저장소 | unsloth/Qwen3.6-35B-A3B-GGUF |
| 받은 파일 | Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf (예상 22 GB) |
| 엔진 옵션 | `` |
| API 별칭 | 263b1eb76bcb44bb629930dfcb84dd1cd3eff31bc32869874767cf4bc73a213a |
| 측정 프로필 | standard |
| 공간 확보로 지운 모델 | - |

단계 결과: `{
 "capacity-cap1": "ok",
 "capacity-cap16": "ok",
 "capacity-cap64": "ok",
 "capacity-cap256": "ok",
 "sanity-512": "ok",
 "context-512": "ok",
 "context-2k": "ok",
 "context-8k": "ok",
 "context-32k": "ok",
 "throughput-1": "server_down_before_step"
}`

## 결과

| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 4.92 | 4.92 | 34.33 | 1000000.0 | 0.2 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.52 | None | 8.23 | 12.15 | 8.72 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.21 | None | 22.16 | 34.36 | 33.41 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.23 | None | 20.15 | 25.4 | 23.29 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2864 | 6.1 | 6.19 | 473.9 | 38.13 | 18.09 | - |
| context-32k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'RemoteDisconnected', 'detail': 'Remote end closed  |
| context-512 | 3/3 | 3 | 3/3 | 0 | 763 | 4.37 | 4.45 | 176.24 | 38.51 | 17.56 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11269 | 11.43 | 11.53 | 992.57 | 36.88 | 13.97 | - |
| sanity-512 | 12/12 | 10 | 10/10 | 2 | 44 | 1.38 | 1.73 | 36.06 | 38.41 | 32.68 | - |


## 실패 정보

- 종류: `server_down`
- 내용: server stopped answering before step throughput-1

엔진 로그 끝부분:

```
yers of 256 experts, 8 a token, 1933312 bytes read an expert; CPU 12.5 + 9.24 us a route reading 7.20 GB/s, GPU graph reading 7.20 GB/s"}}, "threads": {"decode": 10, "batch": 19, "decode_cpus": [5, 6, 7, 8, 9, 15, 16, 17, 18, 19]}, "one_pass": true, "server_args": ["--ctx-checkpoints", "1"]}, "kept": [], "dropped": [], "notes": ["threads: decode on the performance cluster 5-9,15-19: pinned, one token streams Q4_K at 115.7 GB/s there against 84.3 GB/s on every CPU; prefill on 19 unpinned threads; no I/O CPU", "threads: decode 10 of them, Q4_K streams fastest at one token on 10 threads (115.7 GB/s)", "place.costs: cpu 12.5 + 9.24 us a route for one Q4_K/Q4_K/Q5_K expert, latent 2048 hidden 512, on 19 threads (the 16- and 20-thread measurements): 21.8 us at 1 token, 4745.8 us at 512 tokens", "place.costs: link omitted, NVIDIA GB10 shares host memory: no copy over a link", "place.costs: drive the drive BG7 KIOXIA 1024GB reads 7.20 GB/s with 1 MiB reads at QD 16, the best from its knee QD 4 up to QD 24 (a role read is 644437 bytes on average)", "vram.budget: default auto for GPU-c64e5fcb-935f-45b5-018c-2d480d08ef7c", "host.headroom_mib: 4096, the GPU shares host memory", "prefill.cpu_max_tokens: 0; 40 layers of 256 experts, 8 a token, 1933312 bytes read an expert; CPU 12.5 + 9.24 us a route reading 7.20 GB/s, GPU graph reading 7.20 GB/s", "prefill: one pass a prompt, -b and -ub as large as the context; a pass reads every expert it routes to once", "server: --ctx-checkpoints 1"]}}

```

측정이 끝난 모델 파일은 결과 커밋 후 디스크 확보를 위해 삭제합니다.
