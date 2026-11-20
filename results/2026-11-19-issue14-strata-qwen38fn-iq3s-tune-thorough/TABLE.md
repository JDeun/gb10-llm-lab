| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 1.56 | 1.56 | 139.2 | 31.6 | 0.64 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 74.1 | 51.5 | 40.3 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.15 | None | 53.5 | 35.0 | 34.49 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.15 | None | 54.5 | 52.6 | 48.2 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.14 | None | 72.2 | 17.2 | 17.09 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.44 | None | 52.2 | 17.5 | 17.03 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.25 | None | 72.2 | 17.3 | 17.05 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.61 | None | 51.1 | 17.7 | 17.04 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2906 | 1.75 | 8.71 | 1710.1 | 61.0 | 18.09 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 805 | 1.2 | 2.4 | 698.0 | 62.5 | 24.18 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11311 | 5.92 | 5.93 | 1929.6 | 70.0 | 12.78 | - |
| quality-gsm8k | 100/100 | 100 | 96/100 | 0 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 97/100 | 0 | 140 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 162 | 158/162 | 2 | 194 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 100 | 74/100 | 0 | 177 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 140 | 125/140 | 0 | 227 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 11 | - | 1 | 94 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 740 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.66 | 0.95 | 144.2 | 68.0 | 41.69 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 1.1 | 1.1 | 200.0 | 37.8 | 32.68 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 74.2 | 47.6 | 46.81 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 72.5 | 47.6 | 46.8 | - |
