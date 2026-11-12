"""Disk-budget boundary tests; no hardware, network or model is used."""
import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "preflight", Path(__file__).resolve().parents[1] / "benchmarks" / "preflight.py")
preflight = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(preflight)


def catalog(size=594_000_000_000, preparation=0):
    return {"schema_version": "1.0", "constraints": {"storage_nominal_bytes": 1_000_000_000_000},
            "candidates": [{"id": "candidate", "name": "Test model",
                            "checkpoint_bytes_estimate": size,
                            "additional_preparation_bytes_estimate": preparation,
                            "checkpoint_revision": None, "gb10_evidence": "unverified",
                            "excluded_from_current_scope": False}]}


def inventory(free=800_000_000_000, total=1_000_000_000_000):
    return {"disk": {"total_bytes": total, "free_bytes": free, "checked_path": "/models"},
            "memory": {"meminfo_kib": {"MemTotal": 128 * 1024 ** 2, "MemAvailable": 80 * 1024 ** 2}}}


class PreflightTests(unittest.TestCase):
    def test_one_tb_cannot_hold_1611_gb_even_if_free_unknown(self):
        result = preflight.assess(inventory(None), catalog(1_611_000_000_000), "candidate")
        self.assertIs(result["storage_fit"], False)
        self.assertIs(result["ready_to_run"], False)
        self.assertIn("checkpoint_exceeds_nominal_storage_scope", result["reasons"])

    def test_binary_reserve_boundary_and_decimal_model_size(self):
        required = 594_000_000_000 + 64 * 1024 ** 3
        result = preflight.assess(inventory(required), catalog(), "candidate")
        self.assertIs(result["storage_fit"], True)
        self.assertEqual(result["budget"]["estimated_remaining_after_budget_bytes"], 0)
        self.assertEqual(result["budget"]["checkpoint_estimate"]["GB_decimal"], 594)
        result = preflight.assess(inventory(required - 1), catalog(), "candidate")
        self.assertIs(result["storage_fit"], False)

    def test_unknown_preparation_does_not_promote_storage_fit(self):
        result = preflight.assess(inventory(), catalog(preparation=None), "candidate")
        self.assertIsNone(result["storage_fit"])
        self.assertIs(result["lower_bound_fits_current_free_space"], True)
        self.assertIsNone(result["budget"]["required_estimate"])
        self.assertIsNone(result["ready_to_run"])
        override = preflight.assess(inventory(), catalog(preparation=None), "candidate", temporary_gib=0)
        self.assertIs(override["storage_fit"], True)
        self.assertEqual(override["budget"]["preparation_source"], "explicit_cli_override")

    def test_unknown_free_space_is_not_success(self):
        result = preflight.assess(inventory(None), catalog(), "candidate")
        self.assertIsNone(result["storage_fit"])
        self.assertIn("filesystem_free_space_unknown", result["reasons"])

    def test_fit_does_not_claim_ram_fit_or_runtime_readiness(self):
        result = preflight.assess(inventory(), catalog(), "candidate")
        self.assertIs(result["storage_fit"], True)
        self.assertIsNone(result["ready_to_run"])
        self.assertIsNone(result["memory_observed"]["model_ram_fit"])
        self.assertEqual(result["memory_observed"]["physical_total"]["GiB_binary"], 128)
        self.assertIn("checkpoint_revision_not_pinned", result["reasons"])

    def test_small_free_space_fails_even_when_preparation_unknown(self):
        result = preflight.assess(inventory(200_000_000_000), catalog(preparation=None), "candidate")
        self.assertIs(result["storage_fit"], False)
        self.assertIs(result["lower_bound_fits_current_free_space"], False)

    def test_invalid_inventory_and_duplicate_candidate_are_rejected(self):
        with self.assertRaises(ValueError):
            preflight.assess(inventory(2_000_000_000_000), catalog(), "candidate")
        with self.assertRaises(ValueError):
            preflight.assess({"memory": ["invalid"]}, catalog(), "candidate")
        c = catalog()
        c["candidates"].append(c["candidates"][0].copy())
        with self.assertRaises(ValueError):
            preflight.assess(inventory(), c, "candidate")

    def test_cli_refuses_overwrite_and_unknown_is_exit_three(self):
        with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            root = Path(tmp)
            (root / "inventory.json").write_text(json.dumps(inventory()))
            (root / "models.json").write_text(json.dumps(catalog(preparation=None)))
            args = ["--inventory", str(root / "inventory.json"), "--catalog", str(root / "models.json"),
                    "--candidate", "candidate", "--output", str(root / "result.json")]
            self.assertEqual(preflight.main(args), 3)
            first = (root / "result.json").read_text()
            self.assertEqual(preflight.main(args), 2)
            self.assertEqual((root / "result.json").read_text(), first)


if __name__ == "__main__":
    unittest.main()
