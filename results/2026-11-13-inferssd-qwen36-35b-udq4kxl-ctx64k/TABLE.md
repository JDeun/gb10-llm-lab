| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 168 | 4.92 | 4.92 | 34.33 | 1000000.0 | 0.2 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 168 | 0.52 | None | 8.23 | 12.15 | 8.72 | - |
| capacity-cap256 | 1/1 | 0 | - | 1 | 168 | 0.21 | None | 22.16 | 34.36 | 33.41 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 168 | 0.23 | None | 20.15 | 25.4 | 23.29 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2864 | 6.1 | 6.19 | 473.9 | 38.13 | 18.09 | - |
| context-32k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'RemoteDisconnected', 'detail': 'Remote end closed  |
| context-512 | 3/3 | 3 | 3/3 | 0 | 763 | 4.37 | 4.45 | 176.24 | 38.51 | 17.56 | - |
| context-8k | 3/3 | 3 | 3/3 | 0 | 11269 | 11.43 | 11.53 | 992.57 | 36.88 | 13.97 | - |
| sanity-512 | 12/12 | 10 | 10/10 | 2 | 44 | 1.38 | 1.73 | 36.06 | 38.41 | 32.68 | - |
