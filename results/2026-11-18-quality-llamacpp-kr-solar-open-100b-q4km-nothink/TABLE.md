| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 182 | None | None | 275.52 | 0.0 | 1.02 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 182 | 0.12 | None | 20.74 | 24.17 | 22.96 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 182 | 0.11 | None | 24.48 | 24.37 | 24.3 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 182 | 0.1 | None | 23.65 | 24.4 | 24.22 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 182 | 0.35 | None | 22.5 | 15.5 | 15.41 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 182 | 0.33 | None | 360.24 | 15.61 | 15.43 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 182 | 0.32 | None | 359.32 | 15.61 | 15.43 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 182 | 0.33 | None | 22.35 | 15.61 | 15.42 | - |
| context-2k | 3/3 | 3 | 0/3 | 0 | 2805 | 0.19 | None | 116.47 | 22.79 | 22.47 | - |
| context-512 | 3/3 | 3 | 0/3 | 0 | 791 | 0.19 | None | 117.2 | 23.76 | 23.2 | - |
| context-8k | 3/3 | 1 | 0/1 | 2 | 10829 | 0.23 | None | 113.34 | 19.96 | 19.88 | - |
| quality-gsm8k | 100/100 | 100 | 94/100 | 0 | 139 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 99 | 94/99 | 1 | 138 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 84 | 89/84 | 80 | 208 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 64 | 50/64 | 36 | 163 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 113 | 107/113 | 27 | 230 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 9 | - | 3 | 99 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 0 | 0/0 | 0 | None | None | None | None | None | None | HTTPError: HTTP Error 500: Internal Server Error |
| sanity-512 | 12/12 | 12 | 0/12 | 0 | 99 | 0.25 | None | 199.32 | 24.2 | 23.45 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 182 | 0.47 | None | 23.35 | 24.29 | 23.44 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 182 | 0.12 | None | 23.21 | 24.2 | 24.12 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 182 | 0.1 | None | 23.16 | 24.27 | 24.22 | - |
