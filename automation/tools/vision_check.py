"""Exact-answer image checks for an OpenAI-compatible server (synthetic PNGs, no external files)."""
import argparse
import base64
import json
import os
import struct
import time
import urllib.request
import zlib
from pathlib import Path

W = H = 96


def png(pixel) -> bytes:
    rows = b"".join(b"\x00" + b"".join(bytes(pixel(x, y)) for x in range(W)) for y in range(H))
    chunk = lambda t, c: struct.pack(">I", len(c)) + t + c + struct.pack(">I", zlib.crc32(t + c))
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", W, H, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(rows)) + chunk(b"IEND", b""))


def squares(x, y):
    boxes = [(10, 10), (40, 50), (70, 15)]
    inside = any(bx <= x < bx + 16 and by <= y < by + 16 for bx, by in boxes)
    return (0, 0, 0) if inside else (255, 255, 255)


CASES = [
    ("solid-red", lambda x, y: (220, 20, 20), "What single color fills this image? Answer with one lowercase English word.", "red"),
    ("split-blue-left", lambda x, y: (20, 40, 220) if x < W // 2 else (20, 200, 40),
     "The image has two halves. Which side is blue, left or right? Answer with one lowercase word.", "left"),
    ("three-squares", squares, "How many black squares are in this image? Answer with only the digit.", "3"),
]


def ask(base: str, model: str, key: str | None, prompt: str, image: bytes, max_tokens: int) -> tuple[dict, float]:
    url = "data:image/png;base64," + base64.b64encode(image).decode()
    body = {"model": model, "max_tokens": max_tokens, "temperature": 0,
            "messages": [{"role": "user", "content": [{"type": "text", "text": prompt},
                                                      {"type": "image_url", "image_url": {"url": url}}]}]}
    headers = {"Content-Type": "application/json", **({"Authorization": f"Bearer {key}"} if key else {})}
    req = urllib.request.Request(base.rstrip("/") + "/v1/chat/completions", json.dumps(body).encode(), headers)
    start = time.time()
    with urllib.request.urlopen(req, timeout=600) as resp:
        return json.load(resp), time.time() - start


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--api-key-env")
    parser.add_argument("--max-tokens", type=int, default=1024)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    key = os.environ.get(args.api_key_env) if args.api_key_env else None
    rows = []
    for case_id, pixel, prompt, expected in CASES:
        try:
            data, elapsed = ask(args.base_url, args.model, key, prompt, png(pixel), args.max_tokens)
            msg = data["choices"][0]["message"]
            answer = (msg.get("content") or "").strip().strip(".").lower()
            rows.append({"case_id": case_id, "expected": expected, "response": answer[:200],
                         "passed": answer == expected, "finish_reason": data["choices"][0].get("finish_reason"),
                         "usage": data.get("usage"), "elapsed_s": round(elapsed, 2), "error": None})
        except (OSError, ValueError, KeyError, IndexError, TypeError) as exc:  # HTTP, JSON and response-shape failures are results
            rows.append({"case_id": case_id, "expected": expected, "passed": False, "error": f"{type(exc).__name__}: {exc}"[:300]})
    summary = {"cases": len(rows), "passed": sum(r["passed"] for r in rows),
               "errors": sum(1 for r in rows if r["error"]), "rows": rows}
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("cases", "passed", "errors")}))


if __name__ == "__main__":
    main()
