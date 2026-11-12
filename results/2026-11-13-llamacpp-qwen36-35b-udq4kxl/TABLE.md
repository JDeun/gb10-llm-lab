| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 0.4 | 0.4 | 438.82 | 0.0 | 2.5 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.06 | None | 89.32 | 63.12 | 53.42 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.06 | None | 87.7 | 66.63 | 65.81 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.06 | None | 87.19 | 66.27 | 63.17 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 168 | 0.24 | 0.32 | 573.04 | 39.31 | 38.08 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 168 | 0.24 | 0.33 | 574.6 | 39.31 | 38.05 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 168 | 0.13 | None | 83.79 | 38.67 | 38.08 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 168 | 0.21 | None | 55.35 | 39.22 | 38.13 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2864 | 0.26 | 1.14 | 2125.81 | 62.97 | 58.62 | - |
| context-32k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'http_error', 'status': 400, 'detail': '{"error":{" |
| context-512 | 3/3 | 3 | 3/3 | 0 | 763 | 0.25 | 0.4 | 2168.33 | 65.88 | 57.1 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11269 | 0.28 | 4.31 | 1997.38 | 60.23 | 56.7 | - |
| sanity-512 | 12/12 | 10 | 10/10 | 2 | 44 | 0.14 | 0.15 | 495.58 | 66.34 | 64.5 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 168 | 0.07 | None | 89.03 | 64.0 | 63.19 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | 89.56 | 64.2 | 63.0 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 168 | 0.06 | None | 87.54 | 63.94 | 63.18 | - |
