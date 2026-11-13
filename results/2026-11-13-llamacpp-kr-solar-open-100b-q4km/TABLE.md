| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 182 | None | None | 270.43 | 0.0 | 1.01 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 182 | 0.12 | None | 19.6 | 23.38 | 22.46 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 182 | 0.1 | None | 23.92 | 23.71 | 23.53 | - |
| context-2k | 3/3 | 1 | 0/1 | 2 | 2805 | 0.2 | None | 112.67 | 22.52 | 22.46 | - |
| context-512 | 3/3 | 3 | 0/3 | 0 | 791 | 0.2 | None | 112.54 | 23.49 | 22.99 | - |
| context-8k | 3/3 | 2 | 0/2 | 1 | 10829 | 0.23 | None | 108.95 | 19.72 | 19.58 | - |
| sanity-512 | 12/12 | 12 | 0/12 | 0 | 99 | 0.25 | None | 196.0 | 23.94 | 23.17 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 182 | 0.81 | None | 418.97 | 23.86 | 22.35 | - |
