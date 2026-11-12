| part | attempted/planned | complete | correct/graded | truncated | prompt tok (med) | TTFT s (med) | TTFT cold s (max, no cache reuse) | prefill tok/s (engine) | decode tok/s (engine) | e2e tok/s | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| context-120k | 1/3 | 0 | 0/0 | 0 | None | None | None | None | None | None | {'kind': 'http_error', 'status': 400, 'detail': '{"error": { |
| context-32k | 3/3 | 3 | 3/3 | 0 | 44945 | 13.36 | 31.35 | 992.7 | 59.5 | 6.19 | - |
| context-60k | 3/3 | 3 | 3/3 | 0 | 82071 | 2.31 | 47.78 | 100.1 | 49.7 | 24.07 | - |
| throughput-1 | 1/1 | 0 | - | 1 | 210 | 1.25 | 1.25 | 177.8 | 47.4 | 38.64 | - |
| throughput-2 | 1/1 | 0 | - | 1 | 210 | 0.13 | None | 62.9 | 49.9 | 49.01 | - |
| throughput-3 | 1/1 | 0 | - | 1 | 210 | 0.11 | None | 75.5 | 49.7 | 48.92 | - |
