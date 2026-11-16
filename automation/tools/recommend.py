"""Build results/RECOMMENDATION.md: per-use-case Pareto tables from every result bundle.

Quality = mean accuracy over the objective quality subsets the bundle has (zero-shot subsets, see
docs/quality.md). A row is Pareto-optimal for a use case when no other row is at least as good on both
axes and strictly better on one. Rows without quality data appear only in the speed-only tables.
"""
import json
from pathlib import Path

RESULTS = Path("results")
OBJECTIVE = ["gsm8k", "hrm8k-gsm8k", "mmlu-pro", "kmmlu", "humaneval", "tools-ko"]


def load(path: Path) -> dict | None:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def median(values: list[float]) -> float | None:
    vals = sorted(v for v in values if v)
    return vals[len(vals) // 2] if vals else None


def records(run: Path) -> list[dict]:
    path = run / "results.jsonl"
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()] if path.exists() else []


def bundle_metrics(bundle: Path) -> dict:
    runs = bundle / "runs"
    quality = {}
    for name in OBJECTIVE + [n + "-l" for n in OBJECTIVE]:
        s = load(runs / f"quality-{name}" / "summary.json")
        if s and s.get("planned_correctness_requests"):
            quality[name.removesuffix("-l")] = s["correctness_passed"] / s["planned_correctness_requests"]
    single = median([r.get("engine_reported_decode_tokens_per_s") or r.get("end_to_end_completion_tokens_per_s")
                     for k in ("throughput-1", "throughput-2", "throughput-3", "throughput-4", "throughput-5")
                     for r in records(runs / k)])
    aggregate = max([(load(p) or {}).get("aggregate_completion_tokens_per_s") or 0
                     for p in bundle.glob("concurrency*-summary.json")], default=0) or None
    longest = 0
    for ctx in sorted(runs.glob("context-*")):
        s = load(ctx / "summary.json")
        if s and s.get("planned_correctness_requests") and s["correctness_passed"] == s["planned_correctness_requests"]:
            longest = max([longest] + [(r.get("usage") or {}).get("prompt_tokens") or 0 for r in records(ctx)])
    return {"name": bundle.name[11:], "quality": sum(quality.values()) / len(quality) if quality else None,
            "quality_sets": quality, "single": single, "aggregate": aggregate, "longest": longest or None,
            "coding": [quality.get("humaneval"), quality.get("tools-ko")]}


def pareto(rows: list[dict], x: str, y: str) -> set[str]:
    pts = [r for r in rows if r.get(x) and r.get(y) is not None]
    return {r["name"] for r in pts if not any(o[x] >= r[x] and o[y] >= r[y] and (o[x] > r[x] or o[y] > r[y]) for o in pts)}


def table(rows: list[dict], x: str, y: str, x_label: str, y_label: str) -> str:
    best = pareto(rows, x, y)
    pts = sorted((r for r in rows if r.get(x) and r.get(y) is not None), key=lambda r: (-r[y], -r[x]))
    lines = [f"| 결과 | {y_label} | {x_label} | 파레토 최적 |", "|---|---|---|---|"]
    lines += [f"| `{r['name']}` | {fmt(r[y])} | {fmt(r[x])} | {'**예**' if r['name'] in best else ''} |" for r in pts]
    return "\n".join(lines) if pts else "(데이터 없음)"


def fmt(v) -> str:
    return f"{v:.3f}" if isinstance(v, float) and v <= 1 else (f"{v:,.1f}" if isinstance(v, float) else f"{v:,}")


def main() -> None:
    rows = [bundle_metrics(b) for b in sorted(RESULTS.glob("2026-*")) if (b / "runs").exists()]
    for r in rows:
        r["coding_score"] = (sum(v for v in r["coding"] if v is not None) / len([v for v in r["coding"] if v is not None])
                             if any(v is not None for v in r["coding"]) else None)
    q_rows = [r for r in rows if r["quality"] is not None]
    parts = [
        "# 용도별 추천 (자동 생성)",
        "",
        ("`automation/tools/recommend.py`가 결과 폴더에서 계산합니다. 품질은 객관식·수학·코드·툴 호출 부분집합의 평균 정답률"
         "(zero-shot 부분집합, 공식 점수 아님)이고, 문항 수가 100~140개라 약 ±5~9%p 차이는 같은 수준으로 봅니다. "
         "파레토 최적은 두 축 모두에서 더 나은 대안이 없는 조합입니다. 최종 추천은 confirm 프로필(3배 문항, 5회 반복)로 확인한 뒤 확정합니다."),
        "", f"품질 데이터가 있는 결과: {len(q_rows)}개 / 전체 {len(rows)}개", "",
        "## 대화·API 상시 서빙 (품질 × 단일 요청 속도)", "", table(q_rows, "single", "quality", "단일 tok/s", "품질"), "",
        "## 여러 사용자·배치 (품질 × 동시 처리 합계)", "", table(q_rows, "aggregate", "quality", "동시 합계 tok/s", "품질"), "",
        "## 코딩·에이전트 (코드+툴 정답률 × 단일 요청 속도)", "",
        table([r for r in rows if r["coding_score"] is not None], "single", "coding_score", "단일 tok/s", "코드·툴 정답률"), "",
        "## 긴 문서 (정답 낸 최대 입력 × 단일 요청 속도, 품질 무관)", "", table(rows, "single", "longest", "단일 tok/s", "최대 입력 토큰"), "",
        "## 최대 품질 순위", "",
        "| 순위 | 결과 | 품질 | 세트별 정답률 |", "|---|---|---|---|",
        *[f"| {i} | `{r['name']}` | {r['quality']:.3f} | {', '.join(f'{k} {v:.2f}' for k, v in sorted(r['quality_sets'].items()))} |"
          for i, r in enumerate(sorted(q_rows, key=lambda r: -r["quality"]), 1)],
    ]
    (RESULTS / "RECOMMENDATION.md").write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"wrote results/RECOMMENDATION.md ({len(rows)} bundles, {len(q_rows)} with quality)")


if __name__ == "__main__":
    main()
