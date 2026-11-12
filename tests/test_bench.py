"""Local protocol tests. No model/GPU/remote service is used."""
import contextlib
import importlib.util
import io
import json
import os
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("gb10_bench", Path(__file__).resolve().parents[1] / "benchmarks" / "bench.py")
bench = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bench)


def frame(obj):
    return ("data: " + json.dumps(obj, ensure_ascii=False) + "\n\n").encode()


def stream(answer="391", finish="stop", done=True, tokens=3, reasoning=""):
    data = frame({"choices": [{"delta": {"role": "assistant"}, "finish_reason": None}]})
    if reasoning:
        data += frame({"choices": [{"delta": {"reasoning_content": reasoning}}]})
    data += frame({"choices": [{"delta": {"content": answer}, "finish_reason": finish}]})
    data += frame({"choices": [], "usage": {"prompt_tokens": 14, "completion_tokens": tokens},
                   "timings": {"predicted_per_second": 4.25}})
    return data + (b"data: [DONE]\n\n" if done else b"")


@contextlib.contextmanager
def fake_server(payload, status=200, content_type="text/event-stream", headers=None):
    requests = []
    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"
        def do_POST(self):
            body = self.rfile.read(int(self.headers["Content-Length"]))
            requests.append((self.path, dict(self.headers), json.loads(body)))
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(payload)))
            self.send_header("Connection", "close")
            for k, v in (headers or {}).items():
                self.send_header(k, v)
            self.end_headers()
            # Exercise fragmented transport and UTF-8 boundaries.
            for start in range(0, len(payload), 7):
                self.wfile.write(payload[start:start + 7])
                self.wfile.flush()
        def log_message(self, *args):
            pass
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}", requests
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


class BenchmarkTests(unittest.TestCase):
    def invoke(self, payload, flags=None, status=200):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        out = Path(temp.name) / "run"
        with fake_server(payload, status) as (url, requests), patch.object(bench, "inventory", return_value={"test_only": True}), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            code = bench.main(["run", "--base-url", url + "/v1", "--model", "already-served-model", "--output-dir", str(out)] + (flags or []))
        return code, out, requests

    def record(self, out):
        return json.loads((out / "results.jsonl").read_text().splitlines()[0])

    def test_fragmented_sse_multiline_utf8_and_comments(self):
        raw = ': heartbeat\r\nevent: message\r\ndata: {"a":\r\ndata: "한국어"}\r\n\r\ndata: [DONE]\n\n'.encode()
        messages = list(bench.sse_messages([raw[i:i + 1] for i in range(len(raw))]))
        self.assertEqual(json.loads(messages[0]), {"a": "한국어"})
        self.assertEqual(messages[1], "[DONE]")

    def test_success_only_one_request_and_server_token_counts(self):
        code, out, requests = self.invoke(stream(reasoning="곱셈 확인"))
        self.assertEqual(code, 0)
        self.assertEqual(len(requests), 1)
        path, headers, body = requests[0]
        self.assertEqual(path, "/v1/chat/completions")
        self.assertEqual(body["max_tokens"], 32)
        self.assertTrue(body["stream_options"]["include_usage"])
        r = self.record(out)
        self.assertEqual(r["reasoning"], "곱셈 확인")
        self.assertTrue(r["correctness_pass"])
        self.assertEqual(r["completion_tokens"], 3)
        self.assertEqual(r["semantic_sse_events"], 2)
        self.assertLessEqual(r["ttft_semantic_s"], r["ttft_visible_answer_s"])
        self.assertAlmostEqual(r["end_to_end_completion_tokens_per_s"], 3 / r["elapsed_s"])
        self.assertEqual(r["engine_reported_decode_tokens_per_s"], 4.25)

    def test_truncated_partial_answer_cannot_pass(self):
        code, out, _ = self.invoke(stream(answer="391", finish="length"))
        r = self.record(out)
        self.assertEqual(code, 1)
        self.assertTrue(r["transport_complete"])
        self.assertTrue(r["output_truncated"])
        self.assertIsNone(r["correctness_pass"])
        self.assertEqual(r["correctness_status"], "incomplete")
        self.assertEqual(r["correctness_detail"], "output_truncated")
        summary = json.loads((out / "summary.json").read_text())
        self.assertEqual(summary["correctness_evaluated"], 0)
        self.assertEqual(summary["correctness_failed"], 0)
        self.assertEqual(summary["correctness_incomplete"], 1)

    def test_missing_done_is_incomplete(self):
        code, out, _ = self.invoke(stream(done=False))
        r = self.record(out)
        self.assertEqual(code, 1)
        self.assertFalse(r["transport_complete"])
        self.assertIsNone(r["correctness_pass"])
        self.assertEqual(r["correctness_status"], "incomplete")
        self.assertEqual(r["correctness_detail"], "missing_done_marker")
        self.assertIsNone(r["end_to_end_completion_tokens_per_s"])

    def test_reasoning_answer_is_not_final_answer(self):
        code, out, _ = self.invoke(stream(answer="", reasoning="391"))
        r = self.record(out)
        self.assertEqual(code, 1)
        self.assertIsNone(r["correctness_pass"])
        self.assertEqual(r["correctness_status"], "incomplete")
        self.assertEqual(r["correctness_detail"], "empty_final_text")
        self.assertIsNone(r["ttft_visible_answer_s"])

    def test_no_usage_means_no_invented_token_counts(self):
        payload = frame({"choices": [{"delta": {"content": "391"}, "finish_reason": "stop"}]}) + b"data: [DONE]\n\n"
        code, out, _ = self.invoke(payload)
        r = self.record(out)
        self.assertEqual(code, 0)
        self.assertIsNone(r["completion_tokens"])
        self.assertIsNone(r["end_to_end_completion_tokens_per_s"])
        self.assertIsNone(r["engine_reported_decode_tokens_per_s"])

    def test_http_error_and_api_key_redaction(self):
        secret = "secret-for-local-test-only"
        with patch.dict(os.environ, {"GB10_TEST_KEY": secret}):
            code, out, requests = self.invoke(('invalid key ' + secret).encode(), ["--api-key-env", "GB10_TEST_KEY"], status=400)
        self.assertEqual(code, 1)
        self.assertEqual(requests[0][1]["Authorization"], "Bearer " + secret)
        self.assertEqual(self.record(out)["error"]["status"], 400)
        self.assertIsNone(self.record(out)["correctness_pass"])
        self.assertEqual(self.record(out)["correctness_status"], "transport_error")
        for path in out.iterdir():
            self.assertNotIn(secret, path.read_text())

    def test_secret_redaction_in_sse_keys_and_values(self):
        secret = "secret-for-local-test-only"
        payload = frame({"choices": [{"delta": {"content": "391"}, "finish_reason": "stop"}], secret: secret}) + b"data: [DONE]\n\n"
        with patch.dict(os.environ, {"GB10_TEST_KEY": secret}):
            code, out, _ = self.invoke(payload, ["--api-key-env", "GB10_TEST_KEY"])
        self.assertEqual(code, 0)
        for path in out.iterdir():
            self.assertNotIn(secret, path.read_text())

    def test_cases_file_exact_json_types(self):
        with tempfile.TemporaryDirectory() as tmp:
            cases = Path(tmp) / "cases.jsonl"
            cases.write_text(json.dumps({"id": "json", "prompt": "Return JSON", "expected_json": {"valid": True, "count": 2}}))
            code, out, _ = self.invoke(stream(answer='{"valid":1,"count":2}'), ["--cases-file", str(cases)])
            self.assertEqual(code, 1)
            self.assertFalse(self.record(out)["correctness_pass"])
            self.assertEqual(self.record(out)["correctness_status"], "failed")
            code, out, _ = self.invoke(stream(answer='{"valid":true,"count":2}'), ["--cases-file", str(cases)])
            self.assertEqual(code, 0)
            self.assertTrue(self.record(out)["correctness_pass"])

    def test_extra_body_cannot_override_stream_and_existing_dir_refused(self):
        with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stderr(io.StringIO()):
            extra = Path(tmp) / "extra.json"
            extra.write_text('{"stream":false}')
            args = ["run", "--model", "x", "--output-dir", str(Path(tmp) / "new"), "--extra-body", str(extra)]
            self.assertEqual(bench.main(args), 2)
            self.assertFalse((Path(tmp) / "new").exists())
            self.assertEqual(bench.main(["run", "--model", "x", "--output-dir", tmp]), 2)

    def test_system_counters_are_not_summed_across_partitions(self):
        fake = {"/proc/diskstats": "259 0 nvme0n1 1 0 10 0 2 0 20 0 0 5 0\n259 1 nvme0n1p1 1 0 8 0 2 0 18 0 0 3 0",
                "/proc/meminfo": "MemAvailable: 1024 kB\nMemTotal: 2048 kB\n",
                "/proc/vmstat": "pswpout 7\noom_kill 0", "/proc/pressure/io": "some avg10=0.00 total=5"}
        with patch.object(bench, "read_text", side_effect=lambda p: fake.get(p)):
            sample = bench.system_sample()
        self.assertEqual(sample["disk_counters"]["nvme0n1"]["read_bytes"], 5120)
        self.assertEqual(sample["disk_counters"]["nvme0n1p1"]["read_bytes"], 4096)
        self.assertEqual(sample["vmstat_counters"]["pswpout"], 7)
        self.assertEqual(sample["scope"], "whole_system_not_model_process")

    def test_accuracy_success_rate_and_coverage_have_distinct_denominators(self):
        _, out, _ = self.invoke(stream())
        good = self.record(out)
        incomplete = dict(good, correctness_pass=None, correctness_status="incomplete", final_text_complete=False)
        error = dict(good, correctness_pass=None, correctness_status="transport_error", final_text_complete=False,
                     transport_complete=False, error={"kind": "http_error"})
        report = bench.summarize([good, incomplete, error], planned_requests=5, planned_correctness_requests=5)
        self.assertEqual(report["correctness_accuracy_on_completed_answers"], 1)
        self.assertAlmostEqual(report["correctness_success_rate_on_attempted_requests"], 1 / 3)
        self.assertEqual(report["correctness_success_rate_on_planned_requests"], .2)
        self.assertEqual(report["request_coverage"], .6)
        self.assertAlmostEqual(report["correctness_evaluation_coverage_on_attempted_requests"], 1 / 3)
        self.assertEqual(report["unattempted_requests"], 2)
        self.assertIsNone(bench.summarize([good])["planned_requests"])
        self.assertIsNone(bench.summarize([good])["request_coverage"])

    def test_transport_failure_preserves_planned_count(self):
        code, out, requests = self.invoke(b"bad request", ["--repeats", "3"], status=400)
        report = json.loads((out / "summary.json").read_text())
        self.assertEqual(code, 1)
        self.assertEqual(len(requests), 1)
        self.assertEqual(report["planned_requests"], 3)
        self.assertEqual(report["attempted_requests"], 1)
        self.assertEqual(report["run_status"], "stopped_on_transport_failure")
        self.assertIsNone(report["correctness_accuracy_on_completed_answers"])
        self.assertEqual(report["correctness_success_rate_on_attempted_requests"], 0)

    def test_effective_parameters_category_and_unknown_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            extra, cases, manifest = (Path(tmp) / name for name in ("extra.json", "cases.jsonl", "manifest.json"))
            extra.write_text('{"max_tokens":64,"temperature":0.5,"stream_options":null}')
            cases.write_text(json.dumps({"id": "a", "category": "arithmetic", "prompt": "17*23?", "expected_text": "391"}))
            manifest.write_text('{"engine_revision":null}')
            code, out, requests = self.invoke(stream(), ["--extra-body", str(extra), "--cases-file", str(cases), "--manifest", str(manifest)])
        self.assertEqual(code, 0)
        self.assertEqual(self.record(out)["category"], "arithmetic")
        metadata = json.loads((out / "manifest.json").read_text())
        self.assertEqual(metadata["max_tokens"], 64)
        self.assertEqual(metadata["temperature"], .5)
        self.assertIsNone(metadata["supplied_manifest"]["engine_revision"])
        for key, value in metadata["effective_request_parameters"].items():
            self.assertEqual(requests[0][2][key], value)

    def test_unscored_prompt_does_not_invent_accuracy(self):
        with tempfile.TemporaryDirectory() as tmp:
            prompt = Path(tmp) / "prompt.txt"
            prompt.write_text("Tell a story")
            _, out, _ = self.invoke(stream(finish="length"), ["--prompt-file", str(prompt)])
        report = json.loads((out / "summary.json").read_text())
        self.assertEqual(report["planned_correctness_requests"], 0)
        self.assertEqual(report["correctness_checked_attempts"], 0)
        self.assertIsNone(report["correctness_accuracy_on_completed_answers"])
        self.assertIsNone(report["correctness_success_rate_on_attempted_requests"])

    def test_keyboard_interrupt_is_recorded_and_resummarized(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(bench, "inventory", return_value={}), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            out = Path(tmp) / "run"
            with patch.object(bench.urllib.request.OpenerDirector, "open", side_effect=KeyboardInterrupt):
                code = bench.main(["run", "--model", "served", "--repeats", "3", "--output-dir", str(out)])
            report = json.loads((out / "summary.json").read_text())
            self.assertEqual(code, 130)
            self.assertEqual(report["run_status"], "interrupted")
            self.assertEqual(report["attempted_requests"], 1)
            self.assertEqual(report["recorded_requests"], 1)
            self.assertEqual(report["correctness_incomplete"], 1)
            self.assertEqual(report["correctness_success_rate_on_attempted_requests"], 0)
            self.assertAlmostEqual(report["request_coverage"], 1 / 3)
            target = Path(tmp) / "resummary.json"
            self.assertEqual(bench.main(["summarize", str(out / "results.jsonl"), "--output", str(target)]), 0)
            self.assertEqual(json.loads(target.read_text()), report)

    def test_interrupt_outside_request_keeps_unrecorded_attempt(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(bench, "inventory", return_value={}), patch.object(bench, "request_once", side_effect=KeyboardInterrupt), contextlib.redirect_stderr(io.StringIO()):
            out = Path(tmp) / "run"
            self.assertEqual(bench.main(["run", "--model", "served", "--output-dir", str(out)]), 130)
            report = json.loads((out / "summary.json").read_text())
            self.assertEqual(report["attempted_requests"], 1)
            self.assertEqual(report["unrecorded_attempts"], 1)
            self.assertEqual(report["correctness_success_rate_on_attempted_requests"], 0)

    def test_inventory_is_explicitly_client_host_and_cgroup_root(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(bench, "command_result", return_value={"available": False}), patch.object(bench, "read_text", return_value=None):
            report = bench.inventory(tmp)
        self.assertEqual(report["scope"], "benchmark_client_host")
        self.assertIsNone(report["inference_server_is_this_host"])
        self.assertEqual(report["cgroup_v2_read_root"], "/sys/fs/cgroup")
        self.assertIn("not_verified_model_process_limits", report["cgroup_v2_scope"])
        self.assertIsNone(report["cgroup_v2"]["memory.max"])


if __name__ == "__main__":
    unittest.main()
