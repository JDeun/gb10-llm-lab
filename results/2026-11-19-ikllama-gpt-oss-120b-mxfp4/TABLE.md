| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 245 | None | None | 556.66 | 1000000.0 | 2.15 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 245 | 0.1 | None | 47.73 | 57.66 | 50.06 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 245 | 0.1 | None | 49.04 | 55.68 | 55.18 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 245 | 0.1 | None | 48.91 | 55.8 | 53.84 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 245 | 11.55 | None | 51.48 | 56.19 | 16.27 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 245 | 6.96 | None | 51.74 | 55.98 | 34.6 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 245 | 9.25 | None | 51.15 | 56.17 | 20.9 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 245 | 13.82 | None | 51.55 | 56.04 | 13.96 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2400 | 0.19 | None | 151.03 | 54.92 | 49.26 | - |
| context-32k | 3/3 | 3 | 1/3 | 0 | 36704 | 0.29 | None | 145.66 | 39.22 | 37.54 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 682 | 0.17 | None | 152.88 | 56.03 | 51.2 | - |
| context-60k | 3/3 | 3 | 2/3 | 0 | 34211 | 25.35 | 25.92 | 1360.51 | 40.39 | 2.67 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 9254 | 0.21 | None | 152.92 | 50.48 | 45.29 | - |
| quality-gsm8k | 100/100 | 100 | 96/100 | 0 | 133 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 93/100 | 0 | 161 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 164 | 158/164 | 0 | 201 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 100 | 63/100 | 0 | 200 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 136 | 106/136 | 4 | 222 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 115 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 339 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 99 | 0.22 | None | 266.0 | 56.45 | 51.42 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 245 | 0.91 | 0.91 | 700.77 | 55.5 | 46.84 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 245 | 0.1 | None | 50.69 | 56.17 | 55.57 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 245 | 0.1 | None | 50.22 | 56.15 | 55.62 | - |
