| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 0.45 | 0.45 | 482.99 | 0.0 | 2.21 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 49.06 | 36.46 | 31.3 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 49.93 | 37.36 | 36.97 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 49.08 | 37.21 | 35.72 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.69 | 1.01 | 265.73 | 23.18 | 21.94 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.38 | None | 25.77 | 22.6 | 21.94 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.65 | None | 232.05 | 23.11 | 21.94 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.38 | None | 36.88 | 22.6 | 21.94 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 0.65 | None | 830.62 | 36.15 | 23.75 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44945 | 0.86 | None | 638.43 | 24.49 | 20.85 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 0.63 | None | 850.01 | 37.04 | 24.69 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 0.69 | None | 798.79 | 32.78 | 22.31 | - |
| quality-gsm8k | 100/100 | 100 | 93/100 | 0 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 95/100 | 0 | 140 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 155 | 145/155 | 9 | 194 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 53 | 42/53 | 46 | 177 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 118 | 103/118 | 22 | 227 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 11 | - | 1 | 94 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 794 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.29 | None | 249.9 | 37.41 | 33.77 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 1.15 | None | 541.18 | 32.76 | 28.65 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.23 | None | 47.58 | 32.79 | 31.98 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 48.7 | 32.81 | 32.53 | - |
