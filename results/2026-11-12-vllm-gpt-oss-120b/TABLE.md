| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 245 | 0.58 | None | None | None | 1.72 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 245 | 0.15 | None | None | None | 32.64 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 245 | 0.15 | None | None | None | 34.17 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 245 | 0.15 | None | None | None | 34.8 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 245 | 0.19 | None | None | None | 31.7 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 245 | 0.22 | None | None | None | 31.62 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 245 | 0.19 | None | None | None | 31.7 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 245 | 0.22 | None | None | None | 31.63 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2400 | 0.21 | None | None | None | 32.11 | - |
| context-32k | 3/3 | 3 | 1/3 | 0 | 36704 | 0.26 | None | None | None | 28.41 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 682 | 0.36 | None | None | None | 31.69 | - |
| context-60k | 3/3 | 3 | 1/3 | 0 | 66979 | 22.96 | None | None | None | 11.95 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 9254 | 2.34 | None | None | None | 16.16 | - |
| sanity-2048 | 12/12 | 12 | 12/12 | 0 | 99 | 0.16 | None | None | None | 34.52 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 99 | 0.22 | None | None | None | 33.61 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 245 | 0.15 | None | None | None | 35.07 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 245 | 0.15 | None | None | None | 35.04 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 245 | 0.16 | None | None | None | 35.08 | - |
