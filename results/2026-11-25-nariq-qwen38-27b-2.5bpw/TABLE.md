| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 1.24 | None | 523.79 | 0.0 | 0.8 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 41.8 | 19.47 | 18.11 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 39.04 | 19.33 | 19.23 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 38.86 | 19.35 | 18.96 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.53 | None | 23.74 | 15.48 | 15.06 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.66 | None | 221.57 | 15.55 | 15.01 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.23 | None | 39.37 | 15.2 | 15.05 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.65 | None | 198.41 | 15.55 | 15.02 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 0.73 | None | 727.4 | 18.96 | 15.96 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44945 | 0.96 | None | 570.78 | 15.34 | 13.2 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 0.72 | None | 740.8 | 19.24 | 15.56 | - |
| context-60k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'http_error', 'status': 400, 'detail': '{"error":{" |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 0.79 | None | 679.65 | 18.09 | 15.77 | - |
| quality-gsm8k | 100/100 | 99 | 90/99 | 1 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 95/100 | 0 | 140 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 119 | 105/119 | 21 | 227 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.26 | None | 210.25 | 19.34 | 18.34 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.38 | None | 525.23 | 19.3 | 18.82 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.17 | None | 43.06 | 19.39 | 19.22 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 38.49 | 19.19 | 19.09 | - |
