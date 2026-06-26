from __future__ import annotations

import unittest
from dataclasses import replace
from pathlib import Path

from project_conductor.registry import build_artifact_registry
from project_conductor.scanner import scan_repository
from project_conductor.state import (
    DETERMINISTIC_GENERATED_AT,
    RepositoryStateBuilder,
    RepositoryStateValidator,
    build_repository_state,
)


FIXTURE_ROOT = Path("tests/fixtures/repository-scanner/basic-repo")
GOLDEN_STATE = Path("tests/fixtures/repository-scanner/expected-repository-state.json")


def _build_fixture_state():
    registry = build_artifact_registry(scan_repository(FIXTURE_ROOT))
    return build_repository_state(registry)


class RepositoryStateTests(unittest.TestCase):
    def test_builds_repository_state_from_artifact_registry(self) -> None:
        state = _build_fixture_state()

        self.assertEqual(state.version.repository_state_version, "0.1.0")
        self.assertEqual(state.version.registry_version, "0.2.0")
        self.assertEqual(state.generator.generated_at, DETERMINISTIC_GENERATED_AT)
        self.assertEqual(state.repository.artifact_count, 2)
        self.assertEqual(state.repository.durable_artifact_count, 1)
        self.assertEqual(state.repository.problem_count, 1)
        self.assertEqual(state.metadata.complete_count, 1)
        self.assertEqual(state.metadata.missing_count, 1)
        self.assertEqual(state.validation_summary.warning_count, 1)
        self.assertTrue(state.validation.valid)

    def test_repository_state_json_matches_golden_output(self) -> None:
        state = _build_fixture_state()

        self.assertEqual(state.to_json(), GOLDEN_STATE.read_text(encoding="utf-8"))

    def test_repository_state_json_is_deterministic(self) -> None:
        registry = build_artifact_registry(scan_repository(FIXTURE_ROOT))

        first = RepositoryStateBuilder().build(registry).to_json()
        second = RepositoryStateBuilder().build(registry).to_json()

        self.assertEqual(first, second)

    def test_repository_state_validator_detects_summary_mismatch(self) -> None:
        state = _build_fixture_state()
        invalid_repository = replace(state.repository, artifact_count=99)
        invalid_state = replace(state, repository=invalid_repository)

        report = RepositoryStateValidator().validate(invalid_state)

        self.assertFalse(report.valid)
        self.assertIn("repository artifact_count does not match artifacts", report.errors)

    def test_repository_state_validator_detects_nondeterministic_artifact_order(self) -> None:
        state = _build_fixture_state()
        invalid_state = replace(state, artifacts=tuple(reversed(state.artifacts)))

        report = RepositoryStateValidator().validate(invalid_state)

        self.assertFalse(report.valid)
        self.assertIn("repository state artifact ordering is not deterministic at 'README.md'", report.errors)


if __name__ == "__main__":
    unittest.main()
