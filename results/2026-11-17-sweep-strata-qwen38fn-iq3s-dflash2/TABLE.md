| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 1.62 | 1.62 | 133.2 | 34.4 | 0.62 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.17 | None | 45.2 | 59.3 | 40.25 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.15 | None | 46.1 | 49.0 | 47.88 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.15 | None | 50.6 | 50.2 | 46.05 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 2.99 | None | 47.9 | 48.6 | 34.88 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 13.66 | None | 44.9 | 48.85 | 16.79 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 10.9 | None | 43.4 | 47.9 | 17.46 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 16.36 | None | 43.9 | 48.7 | 11.86 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.69 | 0.73 | 134.6 | 82.95 | 48.67 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.97 | 0.97 | 227.0 | 48.3 | 41.04 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.15 | None | 47.8 | 49.7 | 48.59 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.15 | None | 48.1 | 49.9 | 48.7 | - |
