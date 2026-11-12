| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 2.79 | 2.79 | 60.95 | 1000000.0 | 0.36 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.52 | None | 8.25 | 12.32 | 8.78 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.24 | None | 20.85 | 34.74 | 33.66 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.21 | None | 22.81 | 25.47 | 23.54 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 168 | 15.09 | None | 7.57 | 26.95 | 15.62 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 168 | 25.24 | None | 6.63 | 29.34 | 7.68 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 168 | 29.53 | None | 7.68 | 27.15 | 6.57 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 168 | 20.41 | None | 7.13 | 28.59 | 9.73 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2864 | 6.2 | 6.33 | 466.18 | 25.03 | 14.46 | - |
| context-32k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'http_error', 'status': 400, 'detail': '{"error":{" |
| context-512 | 3/3 | 3 | 3/3 | 0 | 763 | 4.74 | 4.99 | 164.36 | 22.96 | 15.6 | - |
| context-8k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'http_error', 'status': 400, 'detail': '{"error":{" |
| sanity-512 | 12/12 | 10 | 10/10 | 2 | 44 | 1.42 | 1.82 | 33.22 | 31.78 | 28.65 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 168 | 0.8 | None | 7.57 | 23.73 | 22.09 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 168 | 0.64 | None | 7.91 | 25.91 | 24.33 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 168 | 0.6 | None | 7.2 | 26.8 | 25.23 | - |
