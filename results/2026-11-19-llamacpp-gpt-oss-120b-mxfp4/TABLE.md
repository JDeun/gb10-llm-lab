| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 245 | None | None | 371.63 | 0.0 | 1.45 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 245 | 0.13 | None | 20.33 | 52.59 | 44.26 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 245 | 0.1 | None | 48.38 | 54.0 | 53.74 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 245 | 0.1 | None | 45.23 | 53.57 | 52.52 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 245 | 0.31 | None | 49.64 | 26.87 | 26.79 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 245 | 0.32 | None | 61.03 | 27.0 | 26.77 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 245 | 0.33 | None | 38.85 | 27.0 | 26.74 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 245 | 0.4 | None | 610.0 | 27.34 | 26.63 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2400 | 0.21 | None | 131.76 | 55.19 | 49.15 | - |
| context-32k | 3/3 | 3 | 1/3 | 0 | 36704 | 0.3 | None | 122.26 | 42.46 | 40.0 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 682 | 0.24 | None | 100.73 | 56.11 | 49.18 | - |
| context-60k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'http_error', 'status': 400, 'detail': '{"error":{" |
| context-8k | 3/3 | 3 | 3/3 | 0 | 9254 | 0.28 | None | 131.57 | 52.03 | 45.24 | - |
| quality-gsm8k | 100/100 | 100 | 96/100 | 0 | 133 | None | None | None | None | None | - |
| quality-hrm8k-gsm8k | 100/100 | 100 | 94/100 | 0 | 161 | None | None | None | None | None | - |
| quality-humaneval | 164/164 | 163 | 159/163 | 1 | 201 | None | None | None | None | None | - |
| quality-kmmlu | 100/100 | 99 | 57/99 | 1 | 200 | None | None | None | None | None | - |
| quality-mmlu-pro | 140/140 | 137 | 104/137 | 3 | 222 | None | None | None | None | None | - |
| quality-open-ko | 12/12 | 12 | - | 0 | 115 | None | None | None | None | None | - |
| quality-tools-ko | 12/12 | 12 | 12/12 | 0 | 339 | None | None | None | None | None | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 99 | 0.27 | None | 225.15 | 55.32 | 48.68 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 245 | 0.15 | None | 35.28 | 55.18 | 54.36 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 245 | 0.13 | None | 21.39 | 55.02 | 54.39 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 245 | 0.13 | None | 20.2 | 55.23 | 54.56 | - |
