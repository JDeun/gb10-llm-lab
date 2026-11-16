| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 165 | 0.53 | None | None | None | 1.87 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 165 | 0.43 | None | None | None | 3.57 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 165 | 0.3 | None | None | None | 3.69 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 165 | 0.31 | None | None | None | 3.69 | - |
| concurrency4-client1 | 2/2 | 0 | - | 2 | 165 | 0.84 | None | None | None | 3.59 | - |
| concurrency4-client2 | 2/2 | 0 | - | 2 | 165 | 0.84 | None | None | None | 3.59 | - |
| concurrency4-client3 | 2/2 | 0 | - | 2 | 165 | 0.83 | None | None | None | 3.59 | - |
| concurrency4-client4 | 2/2 | 0 | - | 2 | 165 | 0.57 | None | None | None | 3.61 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2911 | 0.59 | None | None | None | 3.61 | - |
| context-32k | 3/3 | 3 | 1/3 | 0 | 45648 | 0.8 | None | None | None | 2.93 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 778 | 0.58 | None | None | None | 3.64 | - |
| context-8k | 3/3 | 3 | 2/3 | 0 | 11436 | 0.63 | None | None | None | 3.46 | - |
| sanity-2048 | 12/12 | 11 | 10/11 | 1 | 45 | 0.56 | None | None | None | 3.66 | - |
| sanity-512 | 12/12 | 11 | 10/11 | 1 | 45 | 0.59 | None | None | None | 3.67 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 165 | 0.41 | None | None | None | 3.68 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 165 | 0.31 | None | None | None | 3.68 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 165 | 0.31 | None | None | None | 3.68 | - |
