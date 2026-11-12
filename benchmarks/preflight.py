#!/usr/bin/env python3
"""Read-only disk-budget check from a saved inventory and model catalog.

No downloads, model loading, cache deletion, or configuration changes occur.
Only --output writes a new JSON file. A storage pass never proves RAM fit or
runtime support. Exit codes: 0 estimated budget fits, 1 cannot fit/out of scope,
3 insufficient information, 2 invalid input or output error.
"""
import argparse
import json
import sys
from decimal import Decimal, InvalidOperation, ROUND_CEILING
from pathlib import Path

GIB = 1024 ** 3


def nonnegative_decimal(text):
    try:
        value = Decimal(str(text))
    except InvalidOperation as exc:
        raise argparse.ArgumentTypeError("must be a finite nonnegative number") from exc
    if not value.is_finite() or value < 0:
        raise argparse.ArgumentTypeError("must be a finite nonnegative number")
    return value


def gib_bytes(value):
    return int((nonnegative_decimal(value) * GIB).to_integral_value(rounding=ROUND_CEILING))


def byte_count(value):
    return value if isinstance(value, int) and not isinstance(value, bool) and value >= 0 else None


def sizes(value):
    if value is None:
        return None
    return {"bytes": value, "GB_decimal": round(value / 1_000_000_000, 6),
            "GiB_binary": round(value / GIB, 6)}


def assess(inventory, catalog, candidate_id, reserve_gib=Decimal(64), temporary_gib=None):
    if not isinstance(inventory, dict) or not isinstance(catalog, dict):
        raise ValueError("inventory and catalog must be JSON objects")
    candidates = catalog.get("candidates")
    if not isinstance(candidates, list):
        raise ValueError("catalog.candidates must be an array")
    matches = [c for c in candidates if isinstance(c, dict) and c.get("id") == candidate_id]
    if len(matches) != 1:
        raise ValueError("candidate id must match exactly one catalog entry")
    candidate = matches[0]
    disk = inventory.get("disk") or {}
    memory_block = inventory.get("memory") or {}
    if not isinstance(memory_block, dict):
        raise ValueError("inventory.memory must be an object")
    memory = memory_block.get("meminfo_kib") or {}
    constraints = catalog.get("constraints") or {}
    if not all(isinstance(v, dict) for v in (disk, memory, constraints)):
        raise ValueError("inventory disk/memory and catalog constraints must be objects")
    free = byte_count(disk.get("free_bytes"))
    total = byte_count(disk.get("total_bytes"))
    nominal = byte_count(constraints.get("storage_nominal_bytes"))
    checkpoint = byte_count(candidate.get("checkpoint_bytes_estimate"))
    preparation = (gib_bytes(temporary_gib) if temporary_gib is not None
                   else byte_count(candidate.get("additional_preparation_bytes_estimate")))
    reserve = gib_bytes(reserve_gib)
    if free is not None and total is not None and free > total:
        raise ValueError("inventory free_bytes exceeds total_bytes")
    lower_bound = checkpoint + reserve + (preparation or 0) if checkpoint is not None else None
    known_budget = lower_bound if checkpoint is not None and preparation is not None else None
    reasons = []
    lower_bound_fits = None
    storage_fit = None
    if checkpoint is None:
        reasons.append("checkpoint_size_unknown")
    elif nominal is not None and checkpoint > nominal:
        storage_fit = False
        reasons.append("checkpoint_exceeds_nominal_storage_scope")
    elif nominal is not None and lower_bound > nominal:
        storage_fit = False
        reasons.append("minimum_budget_exceeds_nominal_storage_scope")
    elif total is not None and lower_bound > total:
        storage_fit = False
        reasons.append("minimum_required_space_exceeds_filesystem_capacity")
    elif free is not None:
        lower_bound_fits = lower_bound <= free
        if not lower_bound_fits:
            storage_fit = False
            reasons.append("insufficient_free_space_even_for_minimum_budget")
        elif preparation is not None:
            storage_fit = True
            reasons.append("estimated_storage_budget_fits_current_free_space")
    else:
        reasons.append("filesystem_free_space_unknown")
    if preparation is None:
        reasons.append("additional_preparation_space_unknown_lower_bound_only")
    excluded = candidate.get("excluded_from_current_scope") is True
    if excluded:
        reasons.append("candidate_excluded_from_current_scope")
    if not candidate.get("checkpoint_revision"):
        reasons.append("checkpoint_revision_not_pinned")
    mem_total = byte_count(memory.get("MemTotal"))
    mem_available = byte_count(memory.get("MemAvailable"))
    if mem_total is None:
        reasons.append("physical_memory_inventory_unknown")
    reasons.extend(["ram_fit_not_estimated", "runtime_not_validated_on_this_device"])
    return {
        "schema_version": "1.0",
        "check_type": "offline_storage_budget_estimate",
        "candidate": {"id": candidate_id, "name": candidate.get("name"),
                      "checkpoint_revision": candidate.get("checkpoint_revision"),
                      "gb10_evidence": candidate.get("gb10_evidence"),
                      "excluded_from_current_scope": excluded},
        "storage_fit": storage_fit,
        "lower_bound_fits_current_free_space": lower_bound_fits,
        "ready_to_run": False if storage_fit is False or excluded else None,
        "reasons": reasons,
        "disk": {"checked_path": disk.get("checked_path"),
                 "filesystem_total": sizes(total), "filesystem_free": sizes(free),
                 "scope_nominal_capacity": sizes(nominal)},
        "budget": {"checkpoint_estimate": sizes(checkpoint),
                   "additional_preparation_estimate": sizes(preparation),
                   "preparation_source": "explicit_cli_override" if temporary_gib is not None else "catalog",
                   "planning_reserve": sizes(reserve),
                   "required_lower_bound": sizes(lower_bound),
                   "required_estimate": sizes(known_budget),
                   "estimated_remaining_after_budget_bytes": free - known_budget
                   if free is not None and known_budget is not None else None},
        "memory_observed": {"physical_total": sizes(mem_total * 1024) if mem_total is not None else None,
                            "available_at_capture": sizes(mem_available * 1024) if mem_available is not None else None,
                            "model_ram_fit": None},
        "notes": [
            "A full new checkpoint download is budgeted; existing partial files are not credited.",
            "GB is decimal; GiB is binary. Catalog file sizes may be estimates.",
            "The 64 GiB default reserve is a planning policy, not a hardware requirement.",
            "Unknown preparation space means only a lower bound has been checked.",
            "A storage pass does not validate RAM, kernel support, output quality or model readiness.",
            "Inventory describes the host where it was collected, not necessarily the model server.",
            "No files were downloaded or removed and no model/service settings were changed."
        ]
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", required=True, help="Saved inventory JSON from the GB10")
    parser.add_argument("--catalog", default="configs/models.json")
    parser.add_argument("--candidate", required=True)
    parser.add_argument("--reserve-gib", type=nonnegative_decimal, default=Decimal(64))
    parser.add_argument("--temporary-gib", type=nonnegative_decimal,
                        help="Explicit additional peak preparation space; omitted uses catalog or unknown")
    parser.add_argument("--output", help="Optional new JSON output path; existing files are refused")
    args = parser.parse_args(argv)
    try:
        inventory = json.loads(Path(args.inventory).read_text(encoding="utf-8"))
        catalog = json.loads(Path(args.catalog).read_text(encoding="utf-8"))
        result = assess(inventory, catalog, args.candidate, args.reserve_gib, args.temporary_gib)
        rendered = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
        if args.output:
            with Path(args.output).open("x", encoding="utf-8") as f:
                f.write(rendered)
        print(rendered, end="")
        if result["candidate"]["excluded_from_current_scope"] or result["storage_fit"] is False:
            return 1
        return 0 if result["storage_fit"] is True else 3
    except (OSError, ValueError, TypeError, argparse.ArgumentTypeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
