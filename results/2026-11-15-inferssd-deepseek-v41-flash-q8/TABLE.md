| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity-cap1 | 1/1 | 0 | - | 1 | 224 | 22.87 | 22.87 | 9.8 | 1000000.0 | 0.04 | - |
| capacity-cap16 | 1/1 | 0 | - | 1 | 224 | 2.16 | None | 1.87 | 2.52 | 1.88 | - |
| capacity-cap64 | 1/1 | 0 | - | 1 | 224 | 1.26 | None | 3.22 | 5.97 | 5.34 | - |
| context-2k | 3/3 | 3 | 3/3 | 0 | 2369 | 32.84 | 33.14 | 72.2 | 8.4 | 0.87 | - |
| context-512 | 3/3 | 3 | 3/3 | 0 | 646 | 26.33 | 26.49 | 24.56 | 8.97 | 1.05 | - |
| context-8k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'http_error', 'status': 400, 'detail': '{"error":{" |
| sanity-512 | 12/12 | 12 | 12/12 | 0 | 65 | 13.85 | 15.25 | 4.45 | 8.57 | 2.39 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 224 | 0.83 | None | 5.06 | 8.02 | 7.82 | - |
