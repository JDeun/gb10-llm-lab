| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 0.41 | None | None | None | 2.46 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.34 | None | None | None | 19.51 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.2 | None | None | None | 30.48 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.2 | None | None | None | 28.79 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 168 | 0.4 | None | None | None | 26.2 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 168 | 0.27 | None | None | None | 26.21 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 168 | 0.41 | None | None | None | 26.17 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 168 | 0.4 | None | None | None | 26.19 | - |
| context-2k | 3/3 | 3 | 0/3 | 0 | 2864 | 0.41 | None | None | None | 28.03 | - |
| context-32k | 3/3 | 3 | 0/3 | 0 | 44903 | 0.63 | None | None | None | 25.2 | - |
| context-512 | 3/3 | 3 | 0/3 | 0 | 763 | 0.38 | None | None | None | 29.16 | - |
| context-60k | 3/3 | 3 | 0/3 | 0 | 82029 | 0.71 | None | None | None | 22.66 | - |
| context-8k | 3/3 | 3 | 0/3 | 0 | 11269 | 0.54 | None | None | None | 27.27 | - |
| sanity-2048 | 12/12 | 12 | 0/12 | 0 | 44 | 0.16 | None | None | None | 30.83 | - |
| sanity-512 | 12/12 | 9 | 0/9 | 3 | 44 | 0.17 | None | None | None | 30.87 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 168 | 0.21 | None | None | None | 30.41 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 168 | 0.2 | None | None | None | 30.24 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 168 | 0.2 | None | None | None | 30.3 | - |
