from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from project_conductor.scanner import RepositoryScanError, scan_repository


METADATA = """## Metadata

| Field | Value |
| --- | --- |
| ID | TEST-001 |
| Title | Test Artifact |
| Version | 0.1.0 |
| Status | Draft |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | None |
| Related ADRs | ADR-001 |
| Related Work Packages | WP-008 |
| Tags | test |
| Review Date | 2026-07-02 |
"""


class RepositoryScannerTests(unittest.TestCase):
    def test_discovers_markdown_artifacts_with_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            artifact_path = root / "programme" / "work-packages" / "WP-TEST.md"
            artifact_path.parent.mkdir(parents=True)
            artifact_path.write_text(f"# Test Artifact\n\n{METADATA}\n## Body\n\nContent.\n", encoding="utf-8")

            scan = scan_repository(root)

            self.assertEqual(len(scan.artifacts), 1)
            artifact = scan.artifacts[0]
            self.assertEqual(artifact.path, "programme/work-packages/WP-TEST.md")
            self.assertEqual(artifact.artifact_type, "work-package")
            self.assertEqual(artifact.title, "Test Artifact")
            self.assertTrue(artifact.has_metadata)
            self.assertEqual(artifact.metadata.fields["ID"], "TEST-001")
            self.assertEqual(artifact.problems, ())

    def test_scan_order_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "b").mkdir()
            (root / "a").mkdir()
            (root / "b" / "two.md").write_text("# Two\n\n", encoding="utf-8")
            (root / "a" / "one.md").write_text("# One\n\n", encoding="utf-8")

            scan = scan_repository(root)

            self.assertEqual([artifact.path for artifact in scan.artifacts], ["a/one.md", "b/two.md"])

    def test_excludes_git_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / ".git").mkdir()
            (root / ".git" / "ignored.md").write_text("# Ignored\n", encoding="utf-8")
            (root / "README.md").write_text("# Included\n", encoding="utf-8")

            scan = scan_repository(root)

            self.assertEqual([artifact.path for artifact in scan.artifacts], ["README.md"])

    def test_reports_missing_metadata_without_failing_scan(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "README.md").write_text("# Missing Metadata\n\nBody.\n", encoding="utf-8")

            scan = scan_repository(root)

            self.assertEqual(len(scan.artifacts), 1)
            self.assertEqual(len(scan.problems), 1)
            self.assertEqual(scan.problems[0].message, "metadata section not found")

    def test_rejects_missing_root(self) -> None:
        with self.assertRaises(RepositoryScanError):
            scan_repository(Path("/definitely/not/a/project/genesis/repository"))


if __name__ == "__main__":
    unittest.main()

