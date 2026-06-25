from __future__ import annotations

import unittest
from pathlib import Path

from project_conductor.registry import RegistryArtifact, build_artifact_registry, validate_registry_artifacts
from project_conductor.scanner import scan_repository


FIXTURE_ROOT = Path("tests/fixtures/repository-scanner/basic-repo")
GOLDEN_REGISTRY = Path("tests/fixtures/repository-scanner/expected-artifact-registry.json")


class ArtifactRegistryTests(unittest.TestCase):
    def test_builds_registry_from_repository_scan(self) -> None:
        registry = build_artifact_registry(scan_repository(FIXTURE_ROOT))

        self.assertEqual(registry.artifact_count, 2)
        self.assertTrue(registry.validation.valid)
        self.assertEqual([artifact.path for artifact in registry.artifacts], ["README.md", "docs/no-metadata.md"])
        self.assertEqual(registry.artifacts[0].artifact_id, "FIXTURE-001")
        self.assertEqual(registry.artifacts[0].metadata_status, "complete")
        self.assertEqual(registry.artifacts[1].artifact_id, "PATH-ce3a89079780")
        self.assertEqual(registry.artifacts[1].metadata_status, "missing")
        self.assertEqual(registry.artifacts[1].source_provider, "filesystem")

    def test_registry_json_matches_golden_output(self) -> None:
        registry = build_artifact_registry(scan_repository(FIXTURE_ROOT))

        self.assertEqual(registry.to_json(), GOLDEN_REGISTRY.read_text(encoding="utf-8"))

    def test_validation_detects_duplicate_ids(self) -> None:
        artifact = RegistryArtifact(
            artifact_id="DUPLICATE",
            path="a.md",
            artifact_type="repository",
            title="A",
            hash="hash-a",
            metadata_status="complete",
            metadata_id="DUPLICATE",
            problems=(),
            source_provider="filesystem",
        )
        duplicate = RegistryArtifact(
            artifact_id="DUPLICATE",
            path="b.md",
            artifact_type="repository",
            title="B",
            hash="hash-b",
            metadata_status="complete",
            metadata_id="DUPLICATE",
            problems=(),
            source_provider="filesystem",
        )

        report = validate_registry_artifacts((artifact, duplicate))

        self.assertFalse(report.valid)
        self.assertIn("duplicate artifact_id", report.errors[0])


if __name__ == "__main__":
    unittest.main()

