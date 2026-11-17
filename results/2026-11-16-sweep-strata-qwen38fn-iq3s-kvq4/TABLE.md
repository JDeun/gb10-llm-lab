| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 210 | 1.75 | 1.75 | 124.0 | 25.6 | 0.57 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 83.2 | 57.0 | 44.5 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 210 | 0.15 | None | 56.0 | 52.1 | 50.94 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 210 | 0.16 | None | 54.9 | 41.5 | 38.52 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 210 | 0.22 | None | 68.6 | 20.25 | 19.92 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 210 | 0.44 | None | 68.2 | 20.5 | 19.85 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 210 | 0.34 | None | 74.3 | 20.35 | 19.9 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 210 | 0.14 | None | 73.6 | 20.15 | 19.98 | - |
| quality-gsm8k | 100/100 | 100 | 96/100 | 0 | 124 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 97/100 | 0 | 140 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 163 | 157/163 | 1 | 194 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 100 | 76/100 | 0 | 177 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 139 | 127/139 | 1 | 227 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 11 | - | 1 | 94 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 740 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 86 | 0.62 | 0.67 | 149.0 | 65.3 | 45.88 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 0.74 | 0.74 | 301.9 | 53.8 | 46.82 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 73.9 | 53.8 | 52.81 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.12 | None | 69.2 | 53.5 | 52.53 | - |
