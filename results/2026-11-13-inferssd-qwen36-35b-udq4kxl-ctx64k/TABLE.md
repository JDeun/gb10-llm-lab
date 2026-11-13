| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 3.27 | None | 1.32 | 1000000.0 | 0.31 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.56 | None | 7.48 | 11.31 | 8.08 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.22 | None | 21.93 | 34.14 | 33.15 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.26 | None | 18.75 | 24.59 | 22.39 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2864 | 4.59 | 4.6 | 629.65 | 38.33 | 20.78 | - |
| context-32k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'RemoteDisconnected', 'detail': 'Remote end closed  |
| context-512 | 3/3 | 3 | 3/3 | 0 | 763 | 3.04 | 3.08 | 251.7 | 38.39 | 21.18 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11269 | 9.72 | 9.79 | 1159.38 | 37.0 | 15.34 | - |
| sanity-512 | 12/12 | 10 | 10/10 | 2 | 44 | 1.55 | 1.91 | 31.92 | 38.46 | 33.17 | - |
