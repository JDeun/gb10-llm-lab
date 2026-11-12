| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 177 | 0.53 | None | None | None | 1.87 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 177 | 0.46 | None | None | None | 11.52 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 177 | 0.35 | None | None | None | 15.81 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 177 | 0.35 | None | None | None | 15.03 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 177 | 0.54 | None | None | None | 10.86 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 177 | 0.76 | None | None | None | 10.84 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 177 | 0.75 | None | None | None | 10.84 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 177 | 0.75 | None | None | None | 10.84 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2833 | 1.47 | None | None | None | 11.99 | - |
| context-32k | 3/3 | 0 | 0/0 | 3 | 44120 | 1.63 | None | None | None | 15.47 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 755 | 0.59 | None | None | None | 14.33 | - |
| context-60k | 3/3 | 0 | 0/0 | 2 | 80633 | 3.42 | None | None | None | 14.86 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11089 | 1.49 | None | None | None | 14.27 | - |
| sanity-2048 | 12/12 | 12 | 12/12 | 0 | 51 | 0.29 | None | None | None | 15.02 | - |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 51 | 0.29 | None | None | None | 14.98 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 177 | 0.36 | None | None | None | 15.69 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 177 | 0.35 | None | None | None | 15.71 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 177 | 0.35 | None | None | None | 15.71 | - |
