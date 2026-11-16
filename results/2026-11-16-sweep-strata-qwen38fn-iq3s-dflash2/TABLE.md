| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 2.9 | 2.9 | 73.8 | 34.2 | 0.35 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 57.1 | 54.0 | 39.95 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.14 | None | 51.3 | 50.2 | 49.09 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.15 | None | 52.3 | 59.9 | 53.7 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 10.58 | None | 49.9 | 50.0 | 18.36 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 13.18 | None | 49.9 | 50.05 | 17.16 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 15.79 | None | 50.4 | 50.0 | 12.26 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 2.75 | None | 50.4 | 50.0 | 36.68 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.7 | 0.87 | 130.7 | 81.8 | 43.29 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.81 | 0.81 | 274.2 | 49.9 | 43.32 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.15 | None | 50.3 | 50.1 | 48.97 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.14 | None | 51.0 | 50.1 | 48.99 | - |
