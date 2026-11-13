| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 170 | 0.22 | None | None | None | 4.5 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 170 | 0.17 | None | None | None | 20.25 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 170 | 0.23 | None | None | None | 26.57 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 170 | 0.21 | None | None | None | 24.56 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 170 | 19.32 | None | None | None | 9.93 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 170 | 15.76 | None | None | None | 12.5 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 170 | 22.79 | None | None | None | 8.79 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 170 | 12.22 | None | None | None | 20.26 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2866 | 4.27 | None | None | None | 1.34 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44905 | 91.17 | None | None | None | 0.07 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 765 | 1.22 | None | None | None | 4.71 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11271 | 16.14 | None | None | None | 0.43 | - |
| sanity-512 | 12/12 | 12 | 11/12 | 0 | 46 | 0.19 | None | None | None | 9.43 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 170 | 0.62 | None | None | None | 28.73 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 170 | 0.57 | None | None | None | 29.12 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 170 | 0.64 | None | None | None | 30.47 | - |
