| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 170 | 0.41 | None | None | None | 2.46 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 170 | 0.48 | None | None | None | 25.6 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 170 | 0.09 | None | None | None | 98.78 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 170 | 0.09 | None | None | None | 91.09 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 170 | 0.19 | None | None | None | 59.85 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 170 | 0.17 | None | None | None | 63.74 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 170 | 0.18 | None | None | None | 64.11 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 170 | 0.2 | None | None | None | 61.78 | - |
| quality-gsm8k | 100/100 | 100 | 95/100 | 0 | 84 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 94/100 | 0 | 100 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 164 | 156/164 | 0 | 154 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 98 | 68/98 | 2 | 137 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 130 | 114/130 | 10 | 187 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 54 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 758 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 46 | 0.08 | None | None | None | 39.12 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 170 | 0.09 | None | None | None | 90.62 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 170 | 0.1 | None | None | None | 95.87 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 170 | 0.09 | None | None | None | 98.84 | - |
