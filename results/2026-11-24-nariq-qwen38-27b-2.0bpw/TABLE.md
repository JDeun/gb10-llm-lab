| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 0.44 | 0.44 | 495.63 | 0.0 | 2.27 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 38.68 | 18.9 | 17.34 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 36.69 | 19.5 | 19.39 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 35.66 | 19.54 | 19.08 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.52 | None | 23.24 | 15.49 | 15.07 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.64 | None | 223.34 | 15.55 | 15.03 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.64 | None | 201.61 | 15.55 | 15.04 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.23 | None | 38.47 | 15.21 | 15.06 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 0.74 | None | 725.3 | 19.03 | 15.97 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44945 | 0.96 | None | 570.13 | 15.37 | 13.2 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 0.73 | None | 735.51 | 19.41 | 15.65 | - |
| context-60k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'http_error', 'status': 400, 'detail': '{"error":{" |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 0.78 | None | 691.54 | 18.12 | 15.74 | - |
| quality-gsm8k | 100/100 | 99 | 90/99 | 1 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 95/100 | 0 | 140 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 119 | 106/119 | 20 | 227 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.25 | None | 213.88 | 19.47 | 18.42 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.38 | None | 523.02 | 19.29 | 18.82 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.16 | None | 43.68 | 19.39 | 19.23 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 39.25 | 19.3 | 19.2 | - |
