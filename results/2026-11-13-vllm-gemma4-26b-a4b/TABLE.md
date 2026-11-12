| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 177 | 0.88 | None | None | None | 1.14 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 177 | 0.11 | None | None | None | 22.18 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 177 | 0.11 | None | None | None | 24.45 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 177 | 0.11 | None | None | None | 24.06 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 177 | 0.2 | None | None | None | 22.71 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 177 | 0.2 | None | None | None | 22.71 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 177 | 0.22 | None | None | None | 22.67 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 177 | 0.15 | None | None | None | 22.75 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2897 | 0.85 | None | None | None | 6.88 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 45250 | 19.03 | None | None | None | 0.46 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 773 | 0.16 | None | None | None | 18.07 | - |
| context-60k | 3/3 | 3 | 3/3 | 0 | 82574 | 48.44 | None | None | None | 0.2 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11327 | 0.17 | None | None | None | 17.53 | - |
| sanity-2048 | 12/12 | 12 | 11/12 | 0 | 48 | 0.13 | None | None | None | 16.01 | - |
| sanity-512 | 12/12 | 12 | 11/12 | 0 | 48 | 0.17 | None | None | None | 14.43 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 177 | 0.11 | None | None | None | 24.2 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 177 | 0.11 | None | None | None | 24.25 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 177 | 0.11 | None | None | None | 24.27 | - |
