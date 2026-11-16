| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 0.41 | None | None | None | 2.43 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.5 | None | None | None | 27.66 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 108.92 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 102.13 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 168 | 0.23 | None | None | None | 68.26 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 168 | 0.21 | None | None | None | 69.09 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 168 | 0.25 | None | None | None | 69.92 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 168 | 0.25 | None | None | None | 69.05 | - |
| quality-gsm8k | 100/100 | 99 | 95/99 | 1 | 82 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 91 | 86/91 | 9 | 98 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 142 | 137/142 | 22 | 152 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 80 | 61/80 | 20 | 135 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 82 | 74/82 | 58 | 185 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 52 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 756 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 10 | 10/10 | 2 | 44 | 0.08 | None | None | None | 136.16 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 110.02 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 109.38 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 168 | 0.09 | None | None | None | 102.19 | - |
