| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 0.36 | None | None | None | 2.77 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.3 | None | None | None | 20.26 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.2 | None | None | None | 30.26 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.2 | None | None | None | 28.68 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 168 | 0.4 | None | None | None | 26.11 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 168 | 0.41 | None | None | None | 26.09 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 168 | 0.4 | None | None | None | 26.12 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 168 | 0.27 | None | None | None | 26.12 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2864 | 0.35 | None | None | None | 28.21 | - |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44903 | 0.62 | None | None | None | 25.07 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 763 | 0.38 | None | None | None | 28.96 | - |
| context-60k | 3/3 | 3 | 3/3 | 0 | 82029 | 0.74 | None | None | None | 22.51 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11269 | 0.51 | None | None | None | 27.3 | - |
| sanity-2048 | 12/12 | 12 | 12/12 | 0 | 44 | 0.17 | None | None | None | 30.63 | - |
| sanity-512 | 12/12 | 9 | 9/9 | 3 | 44 | 0.18 | None | None | None | 30.67 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 168 | 0.21 | None | None | None | 30.13 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 168 | 0.21 | None | None | None | 30.2 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 168 | 0.21 | None | None | None | 30.21 | - |
