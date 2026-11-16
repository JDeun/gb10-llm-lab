| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 271 | 4.06 | 4.06 | 73.3 | 1000000.0 | 0.25 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 271 | 0.35 | None | 17.71 | 6.84 | 5.96 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 271 | 0.35 | None | 16.08 | 6.62 | 6.39 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2355 | 4.11 | 24.28 | 75.53 | 6.66 | 3.99 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 632 | 7.5 | 7.66 | 84.74 | 6.66 | 3.18 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 9348 | 12.83 | 91.38 | 90.66 | 6.59 | 2.59 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 46 | 1.38 | 1.72 | 35.37 | 6.64 | 5.7 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 271 | 0.65 | None | 16.17 | 6.58 | 6.48 | - |
