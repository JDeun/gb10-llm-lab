| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 262 | None | None | 500.2 | 0.0 | 1.84 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 262 | 0.15 | None | 61.31 | 35.7 | 31.75 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 262 | 0.15 | None | 56.12 | 37.24 | 36.9 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 262 | 0.15 | None | 56.96 | 37.02 | 35.78 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 262 | 1.03 | 1.7 | 173.07 | 20.03 | 18.8 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 262 | 0.88 | None | 55.02 | 19.01 | 18.88 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 262 | 1.03 | 1.69 | 173.14 | 20.03 | 18.81 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 262 | 1.02 | 1.68 | 173.12 | 20.03 | 18.81 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2523 | 1.19 | 4.97 | 466.72 | 35.52 | 22.07 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 39544 | 2.92 | 182.25 | 188.08 | 28.67 | 13.44 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 676 | 0.9 | 1.23 | 630.85 | 37.37 | 27.08 | - |
| context-60k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'http_error', 'status': 400, 'detail': '{"error":{" |
| context-8k | 3/3 | 3 | 3/3 | 0 | 9914 | 1.56 | 30.61 | 356.88 | 33.56 | 19.92 | - |
| quality-gsm8k | 100/100 | 100 | 96/100 | 0 | 89 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 97 | 92/97 | 3 | 138 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 111 | 99/111 | 29 | 193 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 53 | 0.28 | None | 211.05 | 37.42 | 35.08 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 262 | 0.16 | None | 55.97 | 36.87 | 36.49 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 262 | 0.15 | None | 55.81 | 36.92 | 36.59 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 262 | 0.15 | None | 55.47 | 36.95 | 36.63 | - |
