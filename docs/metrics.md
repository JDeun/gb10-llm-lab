# 측정 필드

비율은 0~1, 시간은 초, 파일 예산은 bytes입니다. null은 미측정 또는 분모가 없는 경우입니다.

| 필드 | 의미 |
|---|---|
| planned_requests | 실행 전에 계획한 요청 수 |
| attempted_requests | 클라이언트가 시작한 요청 수 |
| recorded_requests | 결과가 기록된 요청 수 |
| unrecorded_attempts | 시작했지만 결과 기록에 도달하지 못한 수 |
| unattempted_requests | 계획했지만 시작하지 못한 수 |
| request_coverage | 시도/계획. 계획 미상이면 null |
| run_status | completed/interrupted/stopped_on_transport_failure/client_error 등 |
| correctness_accuracy_on_completed_answers | 정답/완성되어 평가한 답변 |
| correctness_success_rate_on_attempted_requests | 정답/전체 시도 요청. 미완료·오류 포함 |
| correctness_success_rate_on_planned_requests | 정답/전체 계획 요청 |
| correctness_evaluation_coverage_on_attempted_requests | 평가 가능한 완성 답변/전체 시도 |
| ttft_semantic_s | 첫 내용 또는 reasoning 이벤트 도착 시간 |
| ttft_visible_answer_s | 첫 최종 답변 내용 도착 시간 |
| end_to_end_completion_tokens_per_s | 서버 usage 출력 토큰 수/전체 요청 시간 |
| engine_reported_decode_tokens_per_s | 서버 timings.predicted_per_second가 제공될 때만 기록 |

성능용 입력과 정답 채점용 입력은 **서로 다른 run**으로 실행합니다. 정답 없는 입력만 있는 run의 정확성 비율은 null입니다. 혼합 run은 전체 요청 분모에 정답 없는 입력도 포함하므로 정답률 비교에 사용하지 않습니다. 평가 대상 수는 correctness_checked_attempts/planned_correctness_requests로 확인할 수 있습니다.

정답 있는 요청에서 output cap, 빈 최종 답변, 스트림 누락은 incomplete이며 완성 오답과 구분합니다. HTTP/SSE 실패는 transport_error입니다. 하지만 예산 내 성공률 분모에는 남습니다. Ctrl-C 중단 요청도 가능한 부분 기록을 보존합니다.

요청을 다 시도한 것과 답변이 다 완성된 것은 다릅니다. run_status=completed는 모델의 정답률·완료율·가용성 통과를 의미하지 않습니다.

재집계할 때 results.jsonl 옆의 manifest.json과 summary.json도 유지해야 계획과 중단 상태를 보존할 수 있습니다. 결과 JSONL만 옮기면 계획이 미상일 수 있습니다.

telemetry는 클라이언트 호스트 전체의 카운터입니다. 실제 서버 프로세스의 메모리·I/O와 동일하다고 가정하지 않습니다. 초기 실험은 GB10에서 직접 실행합니다.
