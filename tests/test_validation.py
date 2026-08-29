"""Smoke tests for local runners that discover Python unittest tests."""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class ValidationTests(unittest.TestCase):
    def run_script(self, name: str, *args: str) -> None:
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / name), *args],
            cwd=ROOT,
            check=True,
        )

    def test_package_contract(self) -> None:
        self.run_script("build_release.py", "--check")

    def test_acceptance_contract(self) -> None:
        self.run_script("validate_acceptance.py")


if __name__ == "__main__":
    unittest.main()
