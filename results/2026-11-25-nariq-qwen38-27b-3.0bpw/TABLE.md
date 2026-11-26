| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 1.21 | None | 521.32 | 0.0 | 0.83 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 40.59 | 19.14 | 17.8 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 39.85 | 19.28 | 19.18 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 39.08 | 19.32 | 18.93 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.65 | None | 197.37 | 15.57 | 15.04 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.23 | None | 39.35 | 15.21 | 15.07 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.66 | None | 219.01 | 15.57 | 15.03 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.54 | None | 23.43 | 15.5 | 15.07 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 0.74 | None | 721.17 | 18.77 | 15.73 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44945 | 0.97 | None | 563.4 | 15.24 | 13.09 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 0.72 | None | 739.77 | 18.94 | 15.26 | - |
| context-60k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'http_error', 'status': 400, 'detail': '{"error":{" |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 0.79 | None | 687.48 | 17.94 | 15.62 | - |
| quality-gsm8k | 100/100 | 99 | 90/99 | 1 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 95/100 | 0 | 140 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 118 | 105/118 | 21 | 227 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.28 | None | 206.44 | 19.24 | 18.08 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.4 | None | 511.44 | 19.12 | 18.64 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.18 | None | 41.7 | 19.13 | 18.95 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 38.8 | 19.21 | 19.12 | - |
