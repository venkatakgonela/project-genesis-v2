from __future__ import annotations

import unittest
from pathlib import Path

from project_conductor.metadata_contract import default_metadata_contract
from project_conductor.registry import RegistryArtifact, build_artifact_registry, validate_registry_artifacts
from project_conductor.scanner import scan_repository


FIXTURE_ROOT = Path("tests/fixtures/repository-scanner/basic-repo")
GOLDEN_REGISTRY = Path("tests/fixtures/repository-scanner/expected-artifact-registry.json")


class ArtifactRegistryTests(unittest.TestCase):
    def test_builds_registry_from_repository_scan(self) -> None:
        registry = build_artifact_registry(scan_repository(FIXTURE_ROOT))

        self.assertEqual(registry.artifact_count, 2)
        self.assertEqual(registry.registry_version, "0.2.0")
        self.assertEqual(registry.registry_schema_version, "1.0.0")
        self.assertEqual(registry.metadata_contract_version, "1.0.0")
        self.assertTrue(registry.validation.valid)
        self.assertEqual([artifact.path for artifact in registry.artifacts], ["README.md", "docs/no-metadata.md"])
        self.assertEqual(registry.artifacts[0].artifact_id, "metadata:FIXTURE-001")
        self.assertEqual(registry.artifacts[0].metadata_id, "FIXTURE-001")
        self.assertEqual(registry.artifacts[0].metadata_status, "complete")
        self.assertTrue(registry.artifacts[0].durable)
        self.assertEqual(registry.artifacts[1].artifact_id, "path:ce3a89079780")
        self.assertEqual(registry.artifacts[1].metadata_status, "missing")
        self.assertFalse(registry.artifacts[1].durable)
        self.assertEqual(registry.artifacts[1].source_provider, "filesystem")

    def test_registry_json_matches_golden_output(self) -> None:
        registry = build_artifact_registry(scan_repository(FIXTURE_ROOT))

        self.assertEqual(registry.to_json(), GOLDEN_REGISTRY.read_text(encoding="utf-8"))

    def test_validation_detects_duplicate_ids(self) -> None:
        artifact = RegistryArtifact(
            artifact_id="metadata:DUPLICATE",
            path="a.md",
            artifact_type="repository",
            title="A",
            hash="hash-a",
            metadata_status="complete",
            metadata_id="DUPLICATE",
            durable=True,
            problems=(),
            source_provider="filesystem",
        )
        duplicate = RegistryArtifact(
            artifact_id="metadata:DUPLICATE",
            path="b.md",
            artifact_type="repository",
            title="B",
            hash="hash-b",
            metadata_status="complete",
            metadata_id="DUPLICATE",
            durable=True,
            problems=(),
            source_provider="filesystem",
        )

        report = validate_registry_artifacts((artifact, duplicate))

        self.assertFalse(report.valid)
        self.assertIn("duplicate artifact_id", report.errors[0])

    def test_validation_detects_invalid_metadata_status(self) -> None:
        artifact = RegistryArtifact(
            artifact_id="metadata:BAD-001",
            path="bad.md",
            artifact_type="documentation",
            title="Bad",
            hash="hash-bad",
            metadata_status="invalid",
            metadata_id="BAD-001",
            durable=True,
            problems=(),
            source_provider="filesystem",
        )

        report = validate_registry_artifacts((artifact,))

        self.assertFalse(report.valid)
        self.assertIn("invalid metadata_status", report.errors[0])

    def test_validation_detects_unprefixed_metadata_artifact_id(self) -> None:
        artifact = RegistryArtifact(
            artifact_id="BAD-001",
            path="bad.md",
            artifact_type="documentation",
            title="Bad",
            hash="hash-bad",
            metadata_status="complete",
            metadata_id="BAD-001",
            durable=True,
            problems=(),
            source_provider="filesystem",
        )

        report = validate_registry_artifacts((artifact,))

        self.assertFalse(report.valid)
        self.assertIn("metadata-backed artifact_id must start with 'metadata:'", report.errors[0])

    def test_validation_rejects_metadata_free_durable_artifact(self) -> None:
        artifact = RegistryArtifact(
            artifact_id="path:abc123",
            path="readme.md",
            artifact_type="documentation",
            title="Readme",
            hash="hash-readme",
            metadata_status="missing",
            metadata_id=None,
            durable=True,
            problems=("metadata section not found",),
            source_provider="filesystem",
        )

        report = validate_registry_artifacts((artifact,))

        self.assertFalse(report.valid)
        self.assertIn("cannot be durable without metadata", report.errors[0])

    def test_metadata_contract_exposes_required_and_optional_fields(self) -> None:
        contract = default_metadata_contract()

        self.assertEqual(contract.version, "1.0.0")
        self.assertIn("ID", contract.required_fields)
        self.assertIn("Schema Version", contract.optional_fields)
        self.assertIn("complete", contract.allowed_metadata_statuses)
        self.assertIn("work-package", contract.durable_registry_authority_types)


if __name__ == "__main__":
    unittest.main()
