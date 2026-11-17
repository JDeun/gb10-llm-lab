| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 180 | None | None | 1096.11 | 1000000.0 | 5.46 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 180 | 0.09 | None | 46.16 | 58.03 | 50.91 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 180 | 0.09 | None | 53.98 | 54.09 | 53.69 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 180 | 0.09 | None | 53.78 | 55.55 | 53.89 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 180 | 7.17 | None | 45.1 | 54.44 | 33.75 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 180 | 14.24 | None | 46.38 | 54.46 | 13.56 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 180 | 9.53 | None | 46.31 | 54.45 | 20.32 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 180 | 11.88 | None | 46.24 | 54.45 | 15.81 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2900 | 0.13 | None | 360.82 | 51.37 | 49.52 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 45253 | 0.22 | None | 255.82 | 41.72 | 39.28 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 776 | 0.12 | None | 361.16 | 52.63 | 51.92 | - |
| context-60k | 3/3 | 3 | 2/3 | 0 | 49810 | 30.06 | None | 1687.65 | 42.57 | 0.47 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11330 | 0.15 | None | 326.37 | 49.21 | 46.61 | - |
| quality-gsm8k | 100/100 | 55 | 54/55 | 45 | 89 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 97 | 92/97 | 3 | 107 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 134 | 134/134 | 30 | 163 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 73 | 64/73 | 27 | 154 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 36 | 34/36 | 104 | 195 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 65 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 494 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 51 | 0.15 | None | 705.07 | 55.07 | 53.75 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 180 | 2.88 | None | 1798.98 | 54.35 | 33.99 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 180 | 0.72 | None | 43.79 | 54.39 | 47.71 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 180 | 0.11 | None | 46.14 | 54.43 | 53.78 | - |
