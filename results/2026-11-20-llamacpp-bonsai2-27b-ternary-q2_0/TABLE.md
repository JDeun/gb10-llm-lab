| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 0.61 | 0.61 | 357.05 | 0.0 | 1.63 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 39.09 | 25.29 | 22.15 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 40.4 | 25.79 | 25.57 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 39.22 | 25.83 | 24.93 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.22 | None | 40.69 | 19.99 | 19.72 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.61 | None | 231.71 | 20.56 | 19.7 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.64 | 0.99 | 260.29 | 20.62 | 19.71 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.42 | None | 27.06 | 20.31 | 19.74 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 0.74 | None | 740.49 | 25.07 | 17.83 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44945 | 0.94 | None | 583.96 | 19.23 | 16.66 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 0.74 | None | 737.89 | 25.6 | 18.21 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 0.78 | None | 695.65 | 23.6 | 17.14 | - |
| quality-gsm8k | 100/100 | 100 | 94/100 | 0 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 95/100 | 0 | 140 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 47 | 38/47 | 51 | 177 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 119 | 105/119 | 21 | 227 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.25 | None | 227.24 | 25.79 | 24.37 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 1.13 | None | 555.66 | 26.6 | 23.88 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.17 | None | 45.8 | 26.58 | 26.22 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 40.95 | 26.69 | 26.48 | - |
