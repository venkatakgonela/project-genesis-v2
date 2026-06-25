from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from project_conductor.cli import main


class RepositoryScannerCliTests(unittest.TestCase):
    def test_cli_outputs_json_scan(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "README.md").write_text("# Fixture\n\n", encoding="utf-8")

            result = subprocess.run(
                [sys.executable, "-m", "project_conductor.cli", "--root", str(root), "--json"],
                check=True,
                capture_output=True,
                text=True,
            )

            payload = json.loads(result.stdout)
            self.assertEqual(payload["artifact_count"], 1)
            self.assertEqual(payload["artifacts"][0]["path"], "README.md")

    def test_cli_outputs_summary(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "README.md").write_text("# Fixture\n\n", encoding="utf-8")
            output = StringIO()

            with redirect_stdout(output):
                exit_code = main(["--root", str(root)])

            self.assertEqual(exit_code, 0)
            self.assertIn("Artifacts discovered: 1", output.getvalue())

    def test_cli_outputs_registry_json(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "README.md").write_text("# Fixture\n\n", encoding="utf-8")

            result = subprocess.run(
                [sys.executable, "-m", "project_conductor.cli", "--root", str(root), "--registry-json"],
                check=True,
                capture_output=True,
                text=True,
            )

            payload = json.loads(result.stdout)
            self.assertEqual(payload["registry_version"], "0.1.0")
            self.assertEqual(payload["source_provider"], "filesystem")


if __name__ == "__main__":
    unittest.main()
