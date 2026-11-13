| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 271 | 3.65 | 3.65 | 74.56 | 0.0 | 0.27 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 271 | 0.41 | None | 10.13 | 3.87 | 3.73 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 271 | 0.39 | None | 10.57 | 3.88 | 3.85 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2355 | 3.62 | 16.24 | 143.58 | 3.86 | 3.1 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 632 | 3.56 | None | 145.78 | 3.89 | 2.99 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 9348 | 4.08 | 59.92 | 135.73 | 3.84 | 3.08 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 46 | 1.6 | None | 24.58 | 3.84 | 3.53 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 271 | 0.63 | None | 10.13 | 3.85 | 3.83 | - |
