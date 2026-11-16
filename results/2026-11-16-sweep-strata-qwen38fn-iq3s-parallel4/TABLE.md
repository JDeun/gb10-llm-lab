| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 1.55 | 1.55 | 141.4 | 22.8 | 0.65 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 91.2 | 74.0 | 55.29 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 76.5 | 48.3 | 47.57 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 68.4 | 51.9 | 48.31 | - |
| concurrency1-client1 | 2/2 | 0 | - | 2 | 210 | 0.11 | None | 74.4 | 48.9 | 48.13 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.14 | None | 72.8 | 19.1 | 18.94 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.22 | None | 71.8 | 19.2 | 18.91 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.35 | None | 75.6 | 19.35 | 18.9 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.54 | None | 69.5 | 19.55 | 18.91 | - |
| concurrency8-client1 | 2/2 | 0 | - | 2 | 210 | 12.99 | None | 72.2 | 20.1 | 9.96 | - |
| concurrency8-client2 | 2/2 | 0 | - | 2 | 210 | 0.31 | None | 70.6 | 20.15 | 19.73 | - |
| concurrency8-client3 | 2/2 | 0 | - | 2 | 210 | 6.72 | None | 72.2 | 20.15 | 14.77 | - |
| concurrency8-client4 | 2/2 | 0 | - | 2 | 210 | 6.75 | None | 70.2 | 20.15 | 14.79 | - |
| concurrency8-client5 | 2/2 | 0 | - | 2 | 210 | 13.24 | None | 70.4 | 20.35 | 9.93 | - |
| concurrency8-client6 | 2/2 | 0 | - | 2 | 210 | 13.14 | None | 74.3 | 20.25 | 13.22 | - |
| concurrency8-client7 | 2/2 | 0 | - | 2 | 210 | 6.86 | None | 73.6 | 20.2 | 14.66 | - |
| concurrency8-client8 | 2/2 | 0 | - | 2 | 210 | 13.13 | None | 71.3 | 20.3 | 9.96 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.63 | 0.83 | 150.6 | 70.55 | 46.45 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.76 | 0.76 | 295.0 | 49.1 | 43.09 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 74.9 | 49.1 | 48.29 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 70.0 | 48.8 | 47.93 | - |
