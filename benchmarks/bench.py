#!/usr/bin/env python3
"""Read-only inventory and HTTP/SSE measurement of an already running model.

No models are downloaded, started, stopped, or reconfigured. --timeout is a
socket inactivity timeout, NOT a total run deadline. Ctrl-C stops the client;
whether a disconnected request is cancelled is controlled by the server.
"""
import argparse
import json
import math
import os
import platform
import shutil
import statistics
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


SANITY = [
    {"id": "multiply", "prompt": "Calculate 17 * 23. Reply with only the integer, no explanation.", "expected_text": "391"},
    {"id": "subtract", "prompt": "Calculate 1000 - 417. Reply with only the integer, no explanation.", "expected_text": "583"},
    {"id": "korean_json", "prompt": '이 문장의 정보만 추출하세요: "제품은 연필이고 수량은 3개입니다." 답변은 설명이나 코드 블록 없이 JSON 객체 하나여야 합니다. 키는 item과 count이며 count는 정수입니다.', "expected_json": {"item": "연필", "count": 3}},
    {"id": "lookup", "prompt": "Records: A=18, B=42, C=7. Return only the value of B.", "expected_text": "42"},
    {"id": "boolean_json", "prompt": 'Return exactly the JSON object with key "valid" set to boolean true and key "count" set to integer 2. No explanation or code fences.', "expected_json": {"valid": True, "count": 2}},
    {"id": "korean_lookup", "prompt": "기록: 파랑=12, 초록=25, 노랑=8. 초록에 해당하는 숫자만 답하세요.", "expected_text": "25"},
]
SENSITIVE = {"authorization", "api_key", "password", "access_token", "refresh_token", "secret"}


def utc():
    return datetime.now(timezone.utc).isoformat()


def redact(value, secret=""):
    if isinstance(value, dict):
        return {redact(k, secret): "[REDACTED]" if k.lower() in SENSITIVE else redact(v, secret) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [redact(v, secret) for v in value]
    if isinstance(value, str) and secret:
        return value.replace(secret, "[REDACTED]")
    return value


def dump(path, value, secret=""):
    with Path(path).open("x", encoding="utf-8") as f:
        json.dump(redact(value, secret), f, ensure_ascii=False, indent=2, allow_nan=False)
        f.write("\n")


def read_text(path):
    try:
        return Path(path).read_text().strip()
    except (OSError, UnicodeError):
        return None


def pairs(path, allowed=None):
    text = read_text(path)
    out = {}
    for line in (text or "").splitlines():
        fields = line.replace(":", "").split()
        if len(fields) >= 2 and (allowed is None or fields[0] in allowed):
            try:
                out[fields[0]] = int(fields[1])
            except ValueError:
                continue
    return out


def system_sample():
    """Counters are system-wide; disk sectors are 512 bytes, not token counts."""
    disks = {}
    for line in (read_text("/proc/diskstats") or "").splitlines():
        p = line.split()
        if len(p) >= 14 and not p[2].startswith(("loop", "ram")):
            disks[p[2]] = {"read_bytes": int(p[5]) * 512, "write_bytes": int(p[9]) * 512,
                           "io_ms": int(p[12])}
    return {"timestamp_utc": utc(), "monotonic_s": time.monotonic(), "scope": "whole_system_not_model_process",
            "host_scope": "benchmark_client_host",
            "meminfo_kib": pairs("/proc/meminfo", {"MemTotal", "MemAvailable", "SwapTotal", "SwapFree", "Cached", "Dirty", "Writeback"}),
            "vmstat_counters": pairs("/proc/vmstat", {"pswpin", "pswpout", "pgmajfault", "oom_kill"}),
            "io_pressure": read_text("/proc/pressure/io"), "disk_counters": disks}


def command_result(command):
    if not shutil.which(command[0]):
        return {"available": False}
    try:
        r = subprocess.run(command, capture_output=True, text=True, timeout=5, check=False)
        return {"available": True, "returncode": r.returncode, "output": (r.stdout + r.stderr).strip()[:6000]}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"available": True, "error": type(exc).__name__}


def inventory(model_dir):
    p = Path(model_dir).resolve(strict=True)
    usage = shutil.disk_usage(p)
    return {"captured_utc": utc(), "scope": "benchmark_client_host", "inference_server_is_this_host": None,
            "platform": {"system": platform.system(), "machine": platform.machine(),
             "kernel": platform.release(), "python": platform.python_version(), "logical_cpus": os.cpu_count()},
            "memory": system_sample(),
            "cgroup_v2": {name: read_text("/sys/fs/cgroup/" + name) for name in
                          ("memory.max", "memory.high", "memory.current", "memory.swap.max", "memory.swap.current")},
            "cgroup_v2_read_root": "/sys/fs/cgroup",
            "cgroup_v2_scope": "values_at_read_root_not_verified_model_process_limits",
            "disk": {"checked_path": str(p), "total_bytes": usage.total, "free_bytes": usage.free},
            "versions": {name: command_result(cmd) for name, cmd in {
                "cuda_compiler": ["nvcc", "--version"], "strata": ["strata", "--version"],
                "llama_server": ["llama-server", "--version"]}.items()},
            "gpu": command_result(["nvidia-smi", "--query-gpu=name,driver_version,power.draw,temperature.gpu",
                                   "--format=csv,noheader,nounits"]),
            "notes": ["This inventory and telemetry describe the client host; the inference server may be elsewhere.",
                      "Cgroup values are read at the stated root, not resolved for the model process; ancestor limits may also apply.",
                      "GB10 CPU/GPU share memory: count the pool once.",
                      "nvidia-smi memory can be N/A on GB10; host MemAvailable includes reclaimable memory.",
                      "Do not sum whole-disk and partition counters; other processes affect all system counters.",
                      "This does not inventory model weights, processes, SSH settings, or environment variables."]}


def sse_messages(chunks):
    """Parse arbitrary byte fragments, CRLF, comments and multi-line data fields."""
    buffer = b""
    data = []
    for chunk in chunks:
        buffer += chunk
        while b"\n" in buffer:
            line, buffer = buffer.split(b"\n", 1)
            line = line.rstrip(b"\r").decode("utf-8")
            if not line:
                if data:
                    yield "\n".join(data)
                    data = []
            elif line.startswith("data:"):
                value = line[5:]
                data.append(value[1:] if value.startswith(" ") else value)
    if buffer:
        line = buffer.rstrip(b"\r").decode("utf-8")
        if line.startswith("data:"):
            data.append(line[5:].lstrip(" "))
    if data:
        yield "\n".join(data)


def text_value(value):
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return "".join(x.get("text", "") for x in value if isinstance(x, dict) and isinstance(x.get("text"), str))
    return ""


def valid_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def strict_json_equal(actual, expected):
    # Python's bool == 1 must not turn a JSON type error into a pass.
    if type(actual) is not type(expected):
        return False
    if isinstance(actual, dict):
        return actual.keys() == expected.keys() and all(strict_json_equal(actual[k], expected[k]) for k in actual)
    if isinstance(actual, list):
        return len(actual) == len(expected) and all(strict_json_equal(a, b) for a, b in zip(actual, expected))
    return actual == expected


def correctness(case, record):
    if "expected_text" not in case and "expected_json" not in case:
        return None, "not_evaluated", None
    if record["error"] and record["error"]["kind"] == "interrupted":
        return None, "incomplete", "client_interrupted"
    if record["error"]:
        return None, "transport_error", record["error"]["kind"]
    if not record["done_marker"]:
        return None, "incomplete", "missing_done_marker"
    if record["finish_reason"] == "length":
        return None, "incomplete", "output_truncated"
    if record["finish_reason"] != "stop":
        return None, "incomplete", "unfinished_finish_reason"
    if not record["response"].strip():
        return None, "incomplete", "empty_final_text"
    if "expected_text" in case:
        passed = record["response"].strip() == case["expected_text"]
        return passed, "passed" if passed else "failed", None
    try:
        passed = strict_json_equal(json.loads(record["response"]), case["expected_json"])
        return passed, "passed" if passed else "failed", None
    except (ValueError, TypeError):
        return False, "failed", "invalid_json"


def request_parameters(args, extra):
    return {"stream": True, "stream_options": {"include_usage": True}, "max_tokens": args.max_tokens,
            "temperature": args.temperature, **extra}


def request_once(url, model, case, args, extra, secret, event_file, request_id):
    body = {"model": model, "messages": [{"role": "user", "content": case["prompt"]}],
            **request_parameters(args, extra)}
    headers = {"Content-Type": "application/json", "Accept": "text/event-stream"}
    if secret:
        headers["Authorization"] = "Bearer " + secret
    req = urllib.request.Request(url, data=json.dumps(body, ensure_ascii=False).encode(), headers=headers, method="POST")
    start = time.monotonic()
    r = {"request_id": request_id, "case_id": case["id"], "case_label": args.case_label,
         "category": case.get("category"),
         "started_utc": utc(), "request": body, "response": "", "reasoning": "", "usage": None,
         "engine_timings": None, "done_marker": False, "finish_reason": None, "error": None,
         "ttft_semantic_s": None, "ttft_visible_answer_s": None, "last_semantic_s": None,
         "semantic_sse_events": 0, "timeout_scope": "socket_inactivity_not_total_run_deadline"}
    try:
        # Do not follow redirects with an Authorization header.
        class NoRedirect(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, req, fp, code, msg, headers, newurl):
                return None
        opener = urllib.request.build_opener(NoRedirect)
        with opener.open(req, timeout=args.timeout) as response:
            if "text/event-stream" not in response.headers.get("Content-Type", "").lower():
                raise ValueError("Server did not return text/event-stream; verify its streaming API compatibility.")
            for message in sse_messages(iter(response.readline, b"")):
                elapsed = time.monotonic() - start
                if message.strip() == "[DONE]":
                    r["done_marker"] = True
                    break
                obj = json.loads(message)
                if not isinstance(obj, dict):
                    raise ValueError("SSE JSON payload must be an object")
                event_file.write(json.dumps(redact({"request_id": request_id, "elapsed_s": elapsed, "data": obj}, secret), ensure_ascii=False) + "\n")
                event_file.flush()
                if obj.get("error"):
                    raise ValueError("Server SSE error: " + json.dumps(obj["error"], ensure_ascii=False))
                if isinstance(obj.get("usage"), dict):
                    r["usage"] = obj["usage"]
                if isinstance(obj.get("timings"), dict):
                    r["engine_timings"] = obj["timings"]
                choices = obj.get("choices", [])
                if len(choices) > 1:
                    raise ValueError("Only one completion choice is supported")
                if not choices:
                    continue
                choice = choices[0]
                delta = choice.get("delta") or {}
                content = text_value(delta.get("content"))
                reasoning = text_value(delta.get("reasoning_content")) or text_value(delta.get("reasoning"))
                if content or reasoning:
                    if r["ttft_semantic_s"] is None:
                        r["ttft_semantic_s"] = elapsed
                    r["last_semantic_s"] = elapsed
                    r["semantic_sse_events"] += 1
                if content and r["ttft_visible_answer_s"] is None:
                    r["ttft_visible_answer_s"] = elapsed
                r["response"] += content
                r["reasoning"] += reasoning
                if choice.get("finish_reason") is not None:
                    r["finish_reason"] = choice["finish_reason"]
    except KeyboardInterrupt:
        r["error"] = {"kind": "interrupted", "detail": "Client interrupted; server cancellation is server-specific."}
    except urllib.error.HTTPError as exc:
        detail = exc.read(8192).decode("utf-8", errors="replace")
        r["error"] = {"kind": "http_error", "status": exc.code, "detail": detail,
                      "hint": "No automatic retry. Check model alias, authentication, stream_options and extra-body compatibility."}
    except (OSError, ValueError, TypeError, KeyError) as exc:
        r["error"] = {"kind": type(exc).__name__, "detail": str(exc)}
    r["elapsed_s"] = time.monotonic() - start
    r["transport_complete"] = r["done_marker"] and r["error"] is None
    r["output_truncated"] = r["finish_reason"] == "length"
    r["final_text_complete"] = bool(r["response"].strip()) and r["transport_complete"] and r["finish_reason"] == "stop"
    tokens = (r["usage"] or {}).get("completion_tokens")
    r["completion_tokens"] = tokens if isinstance(tokens, int) and not isinstance(tokens, bool) and tokens >= 0 else None
    r["end_to_end_completion_tokens_per_s"] = (r["completion_tokens"] / r["elapsed_s"]
            if r["completion_tokens"] is not None and r["transport_complete"] else None)
    timings = r["engine_timings"] or {}
    speed = timings.get("predicted_per_second")
    r["engine_reported_decode_tokens_per_s"] = speed if valid_number(speed) and speed >= 0 else None
    r["engine_decode_source"] = "server.timings.predicted_per_second" if r["engine_reported_decode_tokens_per_s"] is not None else None
    r["correctness_pass"], r["correctness_status"], r["correctness_detail"] = correctness(case, r)
    return redact(r, secret)


def percentile(values, q):
    vals = sorted(values)
    x = (len(vals) - 1) * q
    lo = int(x)
    return vals[lo] + (vals[min(lo + 1, len(vals) - 1)] - vals[lo]) * (x - lo)


def summarize(records, planned_requests=None, attempted_requests=None, run_status=None, planned_correctness_requests=None):
    attempted = len(records) if attempted_requests is None else attempted_requests
    passed = sum(r["correctness_pass"] is True for r in records)
    evaluated = sum(r["correctness_pass"] is not None for r in records)
    checked = sum(r.get("correctness_status") != "not_evaluated" for r in records)
    has_checks = checked > 0 or (planned_correctness_requests or 0) > 0
    if run_status is None:
        if any((r.get("error") or {}).get("kind") == "interrupted" for r in records):
            run_status = "interrupted"
        elif planned_requests is not None:
            run_status = "completed" if attempted == planned_requests else "partial"
    output = {"request_count": len(records), "recorded_requests": len(records),
              "planned_requests": planned_requests, "attempted_requests": attempted,
              "unrecorded_attempts": attempted - len(records),
              "unattempted_requests": planned_requests - attempted if planned_requests is not None else None,
              "request_coverage": attempted / planned_requests if planned_requests else None,
              "run_status": run_status,
              "final_text_complete_requests": sum(r["final_text_complete"] for r in records),
              "planned_correctness_requests": planned_correctness_requests,
              "correctness_checked_attempts": checked,
              "correctness_accuracy_on_completed_answers": passed / evaluated if evaluated else None,
              "correctness_success_rate_on_attempted_requests": passed / attempted if attempted and has_checks else None,
              "correctness_success_rate_on_planned_requests": passed / planned_requests if planned_requests and has_checks else None,
              "correctness_evaluation_coverage_on_attempted_requests": evaluated / attempted if attempted and has_checks else None,
              "transport_failures": sum(not r["transport_complete"] for r in records),
              "truncated_outputs": sum(r["output_truncated"] for r in records),
              "correctness_evaluated": sum(r["correctness_pass"] is not None for r in records),
              "correctness_passed": sum(r["correctness_pass"] is True for r in records),
              "correctness_failed": sum(r["correctness_pass"] is False for r in records),
              "correctness_incomplete": sum(r.get("correctness_status") == "incomplete" for r in records),
              "correctness_transport_errors": sum(r.get("correctness_status") == "transport_error" for r in records),
              "correctness_not_evaluated": sum(r.get("correctness_status") == "not_evaluated" for r in records), "metrics": {},
              "notes": ["Descriptive summaries, not confidence intervals; a small-n p95 is unstable.",
                        "SSE events are not tokens. Token counts come only from server usage.",
                        "End-to-end throughput includes prefill and network time and is not decode speed.",
                        "Semantic TTFT may be reasoning; visible-answer TTFT is recorded separately.",
                        "Conditional accuracy divides passes by completed, evaluated answers only; always read coverage and success rates alongside it.",
                        "Attempted/planned success rates use ALL requests as their denominators, including incomplete, failed transport and unscored cases. Rates are null if no correctness checks are known.",
                        "Missing planned counts remain null; a detached results file does not establish a complete experiment.",
                        "Repeated identical prompts may reuse server prefix caches; cold cache is never implied."]}
    for name in ("elapsed_s", "ttft_semantic_s", "ttft_visible_answer_s", "end_to_end_completion_tokens_per_s", "engine_reported_decode_tokens_per_s"):
        values = [r[name] for r in records if r["transport_complete"] and valid_number(r.get(name))]
        output["metrics"][name] = {"n": len(values), "median": statistics.median(values), "p95": percentile(values, .95),
                                    "min": min(values), "max": max(values)} if values else {"n": 0}
    return output


def validate_case(case):
    if not isinstance(case, dict) or not isinstance(case.get("id"), str) or not isinstance(case.get("prompt"), str):
        raise ValueError("Each case needs string id and prompt")
    if not case["id"] or not case["prompt"]:
        raise ValueError("Case id and prompt must not be empty")
    if "expected_text" in case and not isinstance(case["expected_text"], str):
        raise ValueError("expected_text must be a string")
    if "expected_text" in case and "expected_json" in case:
        raise ValueError("Use only one of expected_text and expected_json")
    return case


def run(args):
    parsed = urllib.parse.urlsplit(args.base_url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname or parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise ValueError("base-url must be an HTTP(S) origin/path without credentials, query, or fragment")
    base = args.base_url.rstrip("/")
    url = base + ("/chat/completions" if parsed.path.rstrip("/").endswith("/v1") else "/v1/chat/completions")
    secret = os.environ.get(args.api_key_env, "") if args.api_key_env else ""
    if args.api_key_env and not secret:
        raise ValueError("The selected API key environment variable is empty")
    extra = json.loads(Path(args.extra_body).read_text()) if args.extra_body else {}
    if not isinstance(extra, dict) or {"stream", "model", "messages"} & extra.keys():
        raise ValueError("extra-body must be an object and may not override stream, model, or messages")
    if extra.get("n", 1) != 1:
        raise ValueError("Only n=1 is supported")
    if args.cases_file:
        cases = [validate_case(json.loads(line)) for line in Path(args.cases_file).read_text().splitlines() if line.strip()]
    elif args.prompt_file:
        cases = [validate_case({"id": "custom", "prompt": Path(args.prompt_file).read_text()})]
    else:
        cases = SANITY if args.suite else SANITY[:1]
    if not cases or len({c["id"] for c in cases}) != len(cases):
        raise ValueError("Cases must be nonempty and have unique ids")
    manifest = json.loads(Path(args.manifest).read_text()) if args.manifest else {}
    if not isinstance(manifest, dict):
        raise ValueError("manifest must be a JSON object")
    planned = len(cases) * args.repeats
    planned_checks = sum("expected_text" in c or "expected_json" in c for c in cases) * args.repeats
    effective = request_parameters(args, extra)
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=False)
    dump(out / "inventory.json", inventory(args.model_dir), secret)
    dump(out / "manifest.json", {"created_utc": utc(), "model": args.model, "endpoint": url,
         "case_label": args.case_label, "supplied_manifest": manifest, "manifest_verified_by_runner": False,
         "cases": cases, "repeats": args.repeats, "extra_body": extra,
         "effective_request_parameters": effective,
         "max_tokens": effective.get("max_tokens"), "temperature": effective.get("temperature"),
         "planned_requests": planned, "planned_correctness_requests": planned_checks,
         "inventory_scope": "benchmark_client_host_not_necessarily_inference_server",
         "timeout_s": args.timeout, "timeout_scope": "socket_inactivity_not_total_run_deadline"}, secret)
    stop = threading.Event()
    def telemetry():
        with (out / "telemetry.jsonl").open("x") as f:
            while True:
                f.write(json.dumps(system_sample()) + "\n")
                f.flush()
                if stop.wait(1):
                    break
    worker = threading.Thread(target=telemetry, daemon=True) if args.telemetry else None
    if worker:
        worker.start()
    records = []
    attempted = 0
    run_status = "running"
    try:
        with (out / "results.jsonl").open("x", encoding="utf-8") as result_file, (out / "events.jsonl").open("x", encoding="utf-8") as event_file:
            for repeat in range(args.repeats):
                for case in cases:
                    rid = f"{repeat + 1}:{case['id']}"
                    attempted += 1
                    r = request_once(url, args.model, case, args, extra, secret, event_file, rid)
                    records.append(r)
                    result_file.write(json.dumps(r, ensure_ascii=False, allow_nan=False) + "\n")
                    result_file.flush()
                    print(json.dumps(redact({"request_id": rid, "elapsed_s": r["elapsed_s"], "done": r["done_marker"],
                                      "correctness": r["correctness_pass"], "correctness_status": r["correctness_status"],
                                      "error": r["error"]}, secret), ensure_ascii=False), flush=True)
                    if not r["transport_complete"]:
                        run_status = "interrupted" if (r["error"] or {}).get("kind") == "interrupted" else "stopped_on_transport_failure"
                        break
                if records and not records[-1]["transport_complete"]:
                    break
        if run_status == "running":
            run_status = "completed"
    except KeyboardInterrupt:
        run_status = "interrupted"
    except Exception:
        run_status = "client_error"
        raise
    finally:
        stop.set()
        if worker:
            worker.join(timeout=3)
        dump(out / "summary.json", summarize(records, planned, attempted, run_status, planned_checks), secret)
    if run_status == "interrupted":
        print("Interrupted. Client disconnected; server cancellation behavior is server-specific.", file=sys.stderr)
        return 130
    return 1 if any(not r["transport_complete"] or r["correctness_status"] in {"failed", "incomplete", "transport_error"}
                    for r in records) else 0


def positive_int(value):
    n = int(value)
    if n <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return n


def positive_float(value):
    n = float(value)
    if not math.isfinite(n) or n <= 0:
        raise argparse.ArgumentTypeError("must be finite and positive")
    return n


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    inv = sub.add_parser("inventory", help="Read-only hardware inventory; no process/env/credential inspection")
    inv.add_argument("--model-dir", default=".")
    inv.add_argument("--output", required=True)
    b = sub.add_parser("run", help="Measure an existing API; default is ONE 32-token arithmetic request")
    b.add_argument("--base-url", default="http://127.0.0.1:8080")
    b.add_argument("--model", required=True, help="Exact alias already served; runner does not load models")
    group = b.add_mutually_exclusive_group()
    group.add_argument("--prompt-file")
    group.add_argument("--cases-file", help="JSONL: id,prompt, optional expected_text or expected_json")
    group.add_argument("--suite", choices=["sanity"], help="Explicitly run all six smoke checks")
    b.add_argument("--repeats", type=positive_int, default=1)
    b.add_argument("--max-tokens", type=positive_int, default=32)
    b.add_argument("--temperature", type=float, default=0.0)
    b.add_argument("--timeout", type=positive_float, default=1200, help="Socket inactivity timeout in seconds, not a total deadline")
    b.add_argument("--api-key-env", help="Read the API key from this environment variable; never log its value")
    b.add_argument("--extra-body", help="JSON object of explicit API parameters; no automatic compatibility fallback")
    b.add_argument("--output-dir", required=True, help="New directory; existing directory is refused")
    b.add_argument("--case-label", default="baseline")
    b.add_argument("--manifest", help="JSON object of model/quantization/engine/settings provenance")
    b.add_argument("--model-dir", default=".", help="Filesystem on which to report available disk space")
    b.add_argument("--telemetry", action="store_true", help="Collect system-wide Linux memory/I/O counters each second")
    s = sub.add_parser("summarize", help="Summarize an existing results.jsonl")
    s.add_argument("results")
    s.add_argument("--output")
    args = parser.parse_args(argv)
    try:
        if args.command == "inventory":
            dump(args.output, inventory(args.model_dir))
            return 0
        if args.command == "run":
            if not math.isfinite(args.temperature) or args.temperature < 0:
                raise ValueError("temperature must be finite and nonnegative")
            return run(args)
        records = [json.loads(line) for line in Path(args.results).read_text().splitlines() if line.strip()]
        parent = Path(args.results).parent
        metadata = json.loads((parent / "manifest.json").read_text()) if (parent / "manifest.json").exists() else {}
        previous = json.loads((parent / "summary.json").read_text()) if (parent / "summary.json").exists() else {}
        if previous.get("recorded_requests", previous.get("request_count")) != len(records):
            previous = {}
        report = summarize(records, metadata.get("planned_requests"), previous.get("attempted_requests"),
                           previous.get("run_status"), metadata.get("planned_correctness_requests"))
        if args.output:
            dump(args.output, report)
        else:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0
    except KeyboardInterrupt:
        print("Interrupted. Client disconnected; server cancellation behavior is server-specific.", file=sys.stderr)
        return 130
    except (OSError, ValueError, TypeError) as exc:
        secret = os.environ.get(getattr(args, "api_key_env", None) or "", "")
        print(redact(f"Error: {exc}", secret), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
