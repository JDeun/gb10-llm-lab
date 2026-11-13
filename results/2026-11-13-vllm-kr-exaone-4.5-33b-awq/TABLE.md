| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 123 | 0.21 | None | None | None | 4.67 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 123 | 0.12 | None | None | None | 12.05 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 123 | 0.11 | None | None | None | 12.33 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 123 | 0.11 | None | None | None | 12.31 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 123 | 0.25 | None | None | None | 12.52 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 123 | 0.25 | None | None | None | 12.51 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 123 | 0.21 | None | None | None | 12.54 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 123 | 0.17 | None | None | None | 12.56 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2778 | 0.18 | None | None | None | 11.66 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 43551 | 52.7 | None | None | None | 5.8 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 733 | 0.17 | None | None | None | 12.3 | - |
| context-60k | 3/3 | 2 | 0/2 | 1 | 79493 | 102.89 | None | None | None | 4.78 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 10901 | 12.4 | None | None | None | 9.42 | - |
| sanity-2048 | 12/12 | 11 | 11/11 | 1 | 39 | 0.16 | None | None | None | 12.27 | - |
| sanity-512 | 12/12 | 6 | 6/6 | 6 | 39 | 0.13 | None | None | None | 12.26 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 123 | 0.11 | None | None | None | 12.54 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 123 | 0.11 | None | None | None | 12.55 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 123 | 0.12 | None | None | None | 12.53 | - |
