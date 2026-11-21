| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 0.47 | 0.47 | 467.85 | 0.0 | 2.14 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 46.82 | 30.05 | 26.54 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 47.25 | 30.73 | 30.48 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 47.39 | 30.71 | 29.72 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.35 | None | 42.55 | 20.22 | 19.76 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.74 | None | 220.01 | 20.83 | 19.73 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.77 | 1.03 | 249.7 | 20.89 | 19.74 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.56 | None | 28.83 | 20.57 | 19.76 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 0.61 | None | 871.48 | 29.68 | 21.21 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44945 | 0.85 | None | 653.77 | 21.04 | 18.32 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 0.6 | None | 888.17 | 30.36 | 21.85 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 0.66 | None | 821.65 | 27.33 | 19.97 | - |
| quality-gsm8k | 100/100 | 100 | 94/100 | 0 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 95/100 | 0 | 140 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 47 | 38/47 | 53 | 177 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 117 | 106/117 | 23 | 227 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.3 | None | 238.51 | 30.74 | 28.26 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 1.16 | None | 544.37 | 27.34 | 24.41 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.24 | None | 43.91 | 27.33 | 26.75 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 44.81 | 27.35 | 27.14 | - |
