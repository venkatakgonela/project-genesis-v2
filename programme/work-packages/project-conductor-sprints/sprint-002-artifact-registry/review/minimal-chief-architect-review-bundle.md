# Minimal Chief Architect Review Bundle

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S2-REV-MINIMAL |
| Title | Minimal Chief Architect Review Bundle |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-009 |
| Related ADRs | ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-009 |
| Tags | review, minimal, chief-architect |
| Review Date | 2026-07-02 |

## 1. Current Sprint Objective

Implement Sprint 2 only: the Artifact Registry Model.

Convert `RepositoryScan` output from Repository Discovery Capability, Filesystem Provider into deterministic `ArtifactRegistry` entries that include path, type, title, hash, metadata status, problems, source provider, stable artifact ID, validation report, and deterministic JSON export.

## 2. Architecture Decisions Touched

| Decision Area | Status |
| --- | --- |
| ADR-DRAFT-014 Artifact Metadata and Registry Format | Used current Markdown metadata `ID` when present; no metadata migration. |
| ADR-DRAFT-015 Artifact State and Index Strategy | Added in-memory registry model and deterministic JSON export only. |
| DCF-002 Artifact Registry Decision | Followed hybrid strategy: scanner output becomes normalized registry data. |
| DCF-003 Repository State Engine Decision | Consumed filesystem provider output; no Git enrichment, database, or persistence. |

No ADRs were approved or modified.

## 3. Files Changed

Focused current-sprint files only:

```text
.gitignore
src/project_conductor/__init__.py
src/project_conductor/cli.py
src/project_conductor/registry.py
tests/project_conductor_tests/test_cli.py
tests/project_conductor_tests/test_registry.py
tests/fixtures/repository-scanner/expected-artifact-registry.json
programme/work-packages/WP-009-deterministic-project-conductor-mvp-sprint-2-artifact-registry.md
programme/work-packages/project-conductor-sprints/sprint-002-artifact-registry/
prompts/2026-06-25-wp-009-deterministic-project-conductor-mvp-sprint-2.md
```

Sprint 1 docs were also terminology-updated to say: Repository Discovery Capability, Filesystem Provider.

## 4. Git Diff Patch

Focused patch for implementation, tests, golden output, and hygiene only:

```diff
diff --git a/.gitignore b/.gitignore
index d38a4bd..80695d0 100644
--- a/.gitignore
+++ b/.gitignore
@@ -1,4 +1,6 @@
-.DS_Store
+*.DS_Store
+__MACOSX/
+**/__MACOSX/
 .idea/
 .vscode/
 
@@ -12,10 +14,12 @@ tmp/
 
 # Language and tool caches kept out until implementation begins.
 __pycache__/
+**/__pycache__/
 .pytest_cache/
 .ruff_cache/
 .mypy_cache/
 node_modules/
 .venv/
+**/.venv/
 venv/
-
+**/venv/
diff --git a/src/project_conductor/__init__.py b/src/project_conductor/__init__.py
--- a/src/project_conductor/__init__.py
+++ b/src/project_conductor/__init__.py
@@
-"""Deterministic Project Conductor Sprint 1 scanner."""
+"""Deterministic Project Conductor implementation slices."""
+
+from project_conductor.registry import (
+    ArtifactRegistry,
+    RegistryArtifact,
+    RegistryValidationReport,
+    build_artifact_registry,
+    validate_registry_artifacts,
+)
@@
     "Artifact",
+    "ArtifactRegistry",
@@
+    "RegistryArtifact",
+    "RegistryValidationReport",
     "ScanProblem",
+    "build_artifact_registry",
     "scan_repository",
+    "validate_registry_artifacts",
 ]
diff --git a/src/project_conductor/cli.py b/src/project_conductor/cli.py
--- a/src/project_conductor/cli.py
+++ b/src/project_conductor/cli.py
@@
-from project_conductor.scanner import RepositoryScanError, scan_repository
+from project_conductor.registry import build_artifact_registry
+from project_conductor.scanner import RepositoryScanError, scan_repository
@@
     parser.add_argument(
         "--json",
         action="store_true",
         help="Print the scan representation as JSON instead of a short summary.",
     )
+    parser.add_argument(
+        "--registry-json",
+        action="store_true",
+        help="Print the Artifact Registry representation as deterministic JSON.",
+    )
@@
-    if args.json:
+    if args.registry_json:
+        registry = build_artifact_registry(scan)
+        sys.stdout.write(registry.to_json())
+        return 0
+
+    if args.json:
         json.dump(scan.to_dict(), sys.stdout, indent=2, sort_keys=True)
         sys.stdout.write("\n")
diff --git a/src/project_conductor/registry.py b/src/project_conductor/registry.py
new file mode 100644
--- /dev/null
+++ b/src/project_conductor/registry.py
@@
+"""Artifact Registry Model for Project Conductor Sprint 2."""
+
+from __future__ import annotations
+
+import hashlib
+import json
+from dataclasses import dataclass
+from typing import Dict, Iterable, List, Optional, Sequence, Tuple
+
+from project_conductor.scanner import Artifact, RepositoryScan, ScanProblem
+
+REGISTRY_VERSION = "0.1.0"
+DEFAULT_SOURCE_PROVIDER = "filesystem"
+VALID_METADATA_STATUSES = frozenset({"complete", "incomplete", "missing"})
+
+@dataclass(frozen=True)
+class RegistryArtifact:
+    """A normalized artifact entry for deterministic registry consumers."""
+
+    artifact_id: str
+    path: str
+    artifact_type: str
+    title: Optional[str]
+    hash: str
+    metadata_status: str
+    metadata_id: Optional[str]
+    problems: Tuple[str, ...]
+    source_provider: str
+
+    def to_dict(self) -> Dict[str, object]:
+        return {
+            "artifact_id": self.artifact_id,
+            "path": self.path,
+            "type": self.artifact_type,
+            "title": self.title,
+            "hash": self.hash,
+            "metadata_status": self.metadata_status,
+            "metadata_id": self.metadata_id,
+            "problems": list(self.problems),
+            "source_provider": self.source_provider,
+        }
+
+@dataclass(frozen=True)
+class RegistryValidationReport:
+    """Validation result for an artifact registry structure."""
+
+    valid: bool
+    errors: Tuple[str, ...] = ()
+    warnings: Tuple[str, ...] = ()
+
+    def to_dict(self) -> Dict[str, object]:
+        return {"valid": self.valid, "errors": list(self.errors), "warnings": list(self.warnings)}
+
+@dataclass(frozen=True)
+class ArtifactRegistry:
+    """Deterministic Artifact Registry representation."""
+
+    registry_version: str
+    source_provider: str
+    artifacts: Tuple[RegistryArtifact, ...]
+    validation: RegistryValidationReport
+
+    @property
+    def artifact_count(self) -> int:
+        return len(self.artifacts)
+
+    def to_dict(self) -> Dict[str, object]:
+        return {
+            "registry_version": self.registry_version,
+            "source_provider": self.source_provider,
+            "artifact_count": self.artifact_count,
+            "validation": self.validation.to_dict(),
+            "artifacts": [artifact.to_dict() for artifact in self.artifacts],
+        }
+
+    def to_json(self) -> str:
+        return json.dumps(self.to_dict(), indent=2, sort_keys=True) + "\n"
+
+def build_artifact_registry(scan: RepositoryScan, *, source_provider: str = DEFAULT_SOURCE_PROVIDER) -> ArtifactRegistry:
+    """Convert a RepositoryScan into a deterministic ArtifactRegistry."""
+
+    artifacts = tuple(
+        sorted(
+            (_to_registry_artifact(artifact, source_provider=source_provider) for artifact in scan.artifacts),
+            key=lambda artifact: artifact.path,
+        )
+    )
+    validation = validate_registry_artifacts(artifacts, source_provider=source_provider)
+    return ArtifactRegistry(REGISTRY_VERSION, source_provider, artifacts, validation)
+
+def validate_registry_artifacts(
+    artifacts: Sequence[RegistryArtifact], *, source_provider: str = DEFAULT_SOURCE_PROVIDER
+) -> RegistryValidationReport:
+    """Validate deterministic registry structure without running quality gates."""
+
+    errors: List[str] = []
+    warnings: List[str] = []
+    seen_ids: Dict[str, str] = {}
+    previous_path = ""
+
+    for index, artifact in enumerate(artifacts):
+        if not artifact.artifact_id:
+            errors.append(f"artifact at index {index} has empty artifact_id")
+        elif artifact.artifact_id in seen_ids:
+            errors.append(
+                f"duplicate artifact_id {artifact.artifact_id!r} for {seen_ids[artifact.artifact_id]!r} and {artifact.path!r}"
+            )
+        else:
+            seen_ids[artifact.artifact_id] = artifact.path
+        if not artifact.path:
+            errors.append(f"artifact {artifact.artifact_id!r} has empty path")
+        if artifact.path < previous_path:
+            errors.append(f"artifact registry ordering is not deterministic at {artifact.path!r}")
+        previous_path = artifact.path
+        if not artifact.artifact_type:
+            errors.append(f"artifact {artifact.path!r} has empty type")
+        if not artifact.hash:
+            errors.append(f"artifact {artifact.path!r} has empty hash")
+        if artifact.metadata_status not in VALID_METADATA_STATUSES:
+            errors.append(f"artifact {artifact.path!r} has invalid metadata_status {artifact.metadata_status!r}")
+        if artifact.source_provider != source_provider:
+            errors.append(
+                f"artifact {artifact.path!r} source_provider {artifact.source_provider!r} does not match registry provider"
+            )
+        if artifact.metadata_status != "complete":
+            warnings.append(f"artifact {artifact.path!r} metadata_status is {artifact.metadata_status}")
+
+    return RegistryValidationReport(valid=not errors, errors=tuple(errors), warnings=tuple(warnings))
+
+def _to_registry_artifact(artifact: Artifact, *, source_provider: str) -> RegistryArtifact:
+    metadata_id = _metadata_id(artifact)
+    return RegistryArtifact(
+        artifact_id=_stable_artifact_id(artifact),
+        path=artifact.path,
+        artifact_type=artifact.artifact_type,
+        title=artifact.title,
+        hash=artifact.sha256,
+        metadata_status=_metadata_status(artifact),
+        metadata_id=metadata_id,
+        problems=_problem_messages(artifact.problems),
+        source_provider=source_provider,
+    )
+
+def _metadata_id(artifact: Artifact) -> Optional[str]:
+    if artifact.metadata is None:
+        return None
+    value = artifact.metadata.fields.get("ID")
+    if not value or value == "TODO":
+        return None
+    return value
+
+def _stable_artifact_id(artifact: Artifact) -> str:
+    metadata_id = _metadata_id(artifact)
+    if metadata_id:
+        return metadata_id
+    path_digest = hashlib.sha1(artifact.path.encode("utf-8")).hexdigest()[:12]
+    return f"PATH-{path_digest}"
+
+def _metadata_status(artifact: Artifact) -> str:
+    if artifact.metadata is None:
+        return "missing"
+    if artifact.metadata.has_required_fields:
+        return "complete"
+    return "incomplete"
+
+def _problem_messages(problems: Iterable[ScanProblem]) -> Tuple[str, ...]:
+    return tuple(problem.message for problem in problems)
diff --git a/tests/project_conductor_tests/test_cli.py b/tests/project_conductor_tests/test_cli.py
--- a/tests/project_conductor_tests/test_cli.py
+++ b/tests/project_conductor_tests/test_cli.py
@@
+    def test_cli_outputs_registry_json(self) -> None:
+        with tempfile.TemporaryDirectory() as temp_dir:
+            root = Path(temp_dir)
+            (root / "README.md").write_text("# Fixture\n\n", encoding="utf-8")
+
+            result = subprocess.run(
+                [sys.executable, "-m", "project_conductor.cli", "--root", str(root), "--registry-json"],
+                check=True,
+                capture_output=True,
+                text=True,
+            )
+
+            payload = json.loads(result.stdout)
+            self.assertEqual(payload["registry_version"], "0.1.0")
+            self.assertEqual(payload["source_provider"], "filesystem")
diff --git a/tests/project_conductor_tests/test_registry.py b/tests/project_conductor_tests/test_registry.py
new file mode 100644
--- /dev/null
+++ b/tests/project_conductor_tests/test_registry.py
@@
+from __future__ import annotations
+
+import unittest
+from pathlib import Path
+
+from project_conductor.registry import RegistryArtifact, build_artifact_registry, validate_registry_artifacts
+from project_conductor.scanner import scan_repository
+
+FIXTURE_ROOT = Path("tests/fixtures/repository-scanner/basic-repo")
+GOLDEN_REGISTRY = Path("tests/fixtures/repository-scanner/expected-artifact-registry.json")
+
+class ArtifactRegistryTests(unittest.TestCase):
+    def test_builds_registry_from_repository_scan(self) -> None:
+        registry = build_artifact_registry(scan_repository(FIXTURE_ROOT))
+        self.assertEqual(registry.artifact_count, 2)
+        self.assertTrue(registry.validation.valid)
+        self.assertEqual([artifact.path for artifact in registry.artifacts], ["README.md", "docs/no-metadata.md"])
+        self.assertEqual(registry.artifacts[0].artifact_id, "FIXTURE-001")
+        self.assertEqual(registry.artifacts[1].artifact_id, "PATH-ce3a89079780")
+        self.assertEqual(registry.artifacts[1].metadata_status, "missing")
+        self.assertEqual(registry.artifacts[1].source_provider, "filesystem")
+
+    def test_registry_json_matches_golden_output(self) -> None:
+        registry = build_artifact_registry(scan_repository(FIXTURE_ROOT))
+        self.assertEqual(registry.to_json(), GOLDEN_REGISTRY.read_text(encoding="utf-8"))
+
+    def test_validation_detects_duplicate_ids(self) -> None:
+        artifact = RegistryArtifact("DUPLICATE", "a.md", "repository", "A", "hash-a", "complete", "DUPLICATE", (), "filesystem")
+        duplicate = RegistryArtifact("DUPLICATE", "b.md", "repository", "B", "hash-b", "complete", "DUPLICATE", (), "filesystem")
+        report = validate_registry_artifacts((artifact, duplicate))
+        self.assertFalse(report.valid)
+        self.assertIn("duplicate artifact_id", report.errors[0])
diff --git a/tests/fixtures/repository-scanner/expected-artifact-registry.json b/tests/fixtures/repository-scanner/expected-artifact-registry.json
new file mode 100644
--- /dev/null
+++ b/tests/fixtures/repository-scanner/expected-artifact-registry.json
@@
+{
+  "artifact_count": 2,
+  "artifacts": [
+    {
+      "artifact_id": "FIXTURE-001",
+      "hash": "ce66feadc5372b565dfd32e002ae98c7788c5ec223d02b1a000af444cf998242",
+      "metadata_id": "FIXTURE-001",
+      "metadata_status": "complete",
+      "path": "README.md",
+      "problems": [],
+      "source_provider": "filesystem",
+      "title": "Fixture Repository",
+      "type": "repository"
+    },
+    {
+      "artifact_id": "PATH-ce3a89079780",
+      "hash": "b47ab94694f21363850d9da2c618e9798f7562b9c2bb00b3ba5d8430d852cccf",
+      "metadata_id": null,
+      "metadata_status": "missing",
+      "path": "docs/no-metadata.md",
+      "problems": ["metadata section not found"],
+      "source_provider": "filesystem",
+      "title": "No Metadata",
+      "type": "documentation"
+    }
+  ],
+  "registry_version": "0.1.0",
+  "source_provider": "filesystem",
+  "validation": {
+    "errors": [],
+    "valid": true,
+    "warnings": ["artifact 'docs/no-metadata.md' metadata_status is missing"]
+  }
+}
```

## 5. Test Results

```text
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py'

...........
----------------------------------------------------------------------
Ran 11 tests in 0.121s

OK
```

uv path also passed:

```text
UV_CACHE_DIR=/private/tmp/project-genesis-v2-uv-cache PYTHONPATH=src uv run --no-sync python -m unittest discover -s tests -p 'test_*.py'

Ran 11 tests in 0.069s
OK
```

## 6. Coverage Summary

Python standard-library `trace` executed-line summary:

| Module | Lines | Coverage |
| --- | ---: | ---: |
| `project_conductor.__init__` | 4 | 100% |
| `project_conductor.cli` | 39 | 100% |
| `project_conductor.registry` | 128 | 100% |
| `project_conductor.scanner` | 154 | 100% |
| `project_conductor_tests.test_cli` | 45 | 100% |
| `project_conductor_tests.test_registry` | 46 | 100% |
| `project_conductor_tests.test_scanner` | 51 | 100% |

Coverage caveat: `trace` is executed-line coverage, not branch coverage.

## 7. Evidence Summary

| Evidence | Result |
| --- | --- |
| Hygiene cleanup | Verified no `.venv`, `.DS_Store`, `__MACOSX`, or `__pycache__` remained after final cleanup. |
| Registry fixture execution | 2 artifacts, source provider `filesystem`, validation valid, 1 warning for intentionally metadata-free fixture artifact. |
| Golden output | `ArtifactRegistry.to_json()` matches `tests/fixtures/repository-scanner/expected-artifact-registry.json`. |
| Forbidden scope scan | No forbidden implementation terms found in `src`, `tests`, or `pyproject.toml`. |
| Persistence boundary | No registry files are generated by runtime; JSON export is command output only. |

## 8. Known Limitations

- Metadata-free artifacts receive path-derived IDs, so moving a metadata-free file changes its generated ID.
- Registry validation is structural only; it is not a quality gate.
- Registry export is not persisted as generated repository state.
- Duplicate artifact IDs are detected but not remediated.
- No Git enrichment, database, quality gate workflow, or link/dependency validation exists.

## 9. Open Questions

1. Should metadata-free artifacts remain in the registry with generated path IDs, or should future persisted registries include only metadata-bearing durable artifacts?
2. Should `artifact_id` use raw metadata IDs, or should metadata-backed IDs be namespaced in the registry?
3. Should the registry schema become an explicit versioned schema artifact before persisted registry output is introduced?
4. Should the next sprint persist generated registry JSON, or harden the metadata contract first?
5. Should validation warnings remain embedded in registry output, or become a separate validation report artifact later?

## 10. Suggested Next Decision

Decide whether Sprint 3 should:

```text
Persist generated Artifact Registry JSON
```

or:

```text
Define and harden the metadata contract/schema before persistence
```

Recommended decision: harden the metadata contract/schema first, then persist generated registry output after the Chief Architect approves which artifact classes belong in the durable registry.

