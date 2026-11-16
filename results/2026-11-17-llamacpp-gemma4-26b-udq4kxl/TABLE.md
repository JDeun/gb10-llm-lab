| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 180 | None | None | 416.28 | 0.0 | 2.22 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 180 | 0.15 | None | 73.59 | 51.45 | 42.6 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 180 | 0.14 | None | 77.17 | 52.71 | 52.04 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 180 | 0.14 | None | 77.75 | 52.09 | 49.59 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 180 | 0.33 | 0.38 | 644.09 | 33.29 | 32.36 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 180 | 0.33 | 0.39 | 646.27 | 33.29 | 32.36 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 180 | 0.36 | None | 59.31 | 33.13 | 32.41 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 180 | 0.37 | None | 54.84 | 32.91 | 32.41 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2900 | 0.28 | 1.12 | 103.44 | 52.04 | 46.89 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 45253 | 0.3 | 17.77 | 117.48 | 43.35 | 39.66 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 776 | 0.33 | 0.46 | 2041.65 | 52.98 | 50.34 | - |
| context-60k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'http_error', 'status': 400, 'detail': '{"error":{" |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11330 | 0.25 | 3.82 | 115.86 | 49.97 | 44.83 | - |
| quality-gsm8k | 100/100 | 53 | 52/53 | 47 | 89 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 97 | 93/97 | 3 | 107 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 127 | 127/127 | 37 | 163 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 72 | 61/72 | 28 | 154 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 42 | 42/42 | 98 | 195 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 65 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 494 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 51 | 0.19 | None | 445.96 | 54.25 | 52.59 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 180 | 0.15 | None | 80.64 | 54.34 | 53.57 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 180 | 0.16 | None | 85.64 | 54.37 | 53.39 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 180 | 0.14 | None | 81.52 | 54.36 | 53.68 | - |
