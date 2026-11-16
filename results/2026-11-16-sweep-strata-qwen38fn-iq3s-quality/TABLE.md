| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 1.49 | 1.49 | 180.1 | 33.4 | 0.67 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 93.8 | 51.8 | 41.41 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 79.4 | 50.8 | 49.94 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 76.9 | 59.0 | 54.78 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.13 | None | 75.1 | 19.9 | 19.75 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.48 | None | 57.7 | 20.35 | 19.67 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.37 | None | 75.3 | 20.2 | 19.68 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.22 | None | 73.6 | 20.0 | 19.7 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.64 | 0.82 | 149.3 | 72.15 | 43.67 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.75 | 0.75 | 299.8 | 51.2 | 44.74 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 75.5 | 52.0 | 51.08 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 76.1 | 52.4 | 51.5 | - |
