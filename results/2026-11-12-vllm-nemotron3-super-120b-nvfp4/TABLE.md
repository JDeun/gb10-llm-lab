| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 177 | 0.57 | None | None | None | 1.74 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 177 | 0.48 | None | None | None | 11.38 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 177 | 0.35 | None | None | None | 15.88 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 177 | 0.35 | None | None | None | 15.08 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 177 | 0.76 | None | None | None | 11.07 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 177 | 0.76 | None | None | None | 11.08 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 177 | 0.56 | None | None | None | 11.09 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 177 | 0.76 | None | None | None | 11.08 | - |
| context-2k | 3/3 | 3 | 0/3 | 0 | 2833 | 1.45 | None | None | None | 12.05 | - |
| context-32k | 3/3 | 0 | 0/0 | 3 | 44120 | 1.68 | None | None | None | 15.54 | - |
| context-512 | 3/3 | 3 | 0/3 | 0 | 755 | 0.56 | None | None | None | 14.48 | - |
| context-60k | 3/3 | 2 | 1/2 | 1 | 80633 | 3.4 | None | None | None | 2.09 | - |
| context-8k | 3/3 | 3 | 0/3 | 0 | 11089 | 1.52 | None | None | None | 13.64 | - |
| sanity-2048 | 12/12 | 12 | 0/12 | 0 | 51 | 0.29 | None | None | None | 15.1 | - |
| sanity-512 | 12/12 | 12 | 0/12 | 0 | 51 | 0.3 | None | None | None | 15.24 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 177 | 0.36 | None | None | None | 15.75 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 177 | 0.36 | None | None | None | 15.75 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 177 | 0.36 | None | None | None | 15.76 | - |
