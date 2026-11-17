| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 2.04 | 2.04 | 123.9 | 23.3 | 0.49 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.1 | None | 90.7 | 71.5 | 53.43 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 75.1 | 50.4 | 49.45 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 74.9 | 57.5 | 53.4 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.44 | None | 71.5 | 20.0 | 19.37 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.13 | None | 73.1 | 19.6 | 19.46 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.45 | None | 72.0 | 20.0 | 19.34 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.22 | None | 76.5 | 19.7 | 19.39 | - |
| quality-gsm8k | 100/100 | 100 | 96/100 | 0 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 97/100 | 0 | 140 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 162 | 158/162 | 2 | 194 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 100 | 74/100 | 0 | 177 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 140 | 125/140 | 0 | 227 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 11 | - | 1 | 94 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 740 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.64 | 0.89 | 149.3 | 69.7 | 41.97 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.75 | 0.75 | 298.6 | 49.3 | 43.3 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 76.2 | 49.9 | 49.13 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 77.4 | 50.5 | 49.71 | - |
