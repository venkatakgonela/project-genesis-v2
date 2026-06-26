# Sprint 3 Validation Report

## Command

```text
PYTHONPATH=src python3 -c 'import json; from pathlib import Path; from project_conductor.scanner import scan_repository; from project_conductor.registry import build_artifact_registry; registry = build_artifact_registry(scan_repository(Path("tests/fixtures/repository-scanner/basic-repo"))); print(json.dumps(registry.validation.to_dict(), indent=2, sort_keys=True))'
```

## Output

```json
{
  "errors": [],
  "valid": true,
  "warnings": [
    "artifact 'docs/no-metadata.md' metadata_status is missing"
  ]
}
```

## Negative Validation Coverage

The test suite includes negative cases for duplicate artifact IDs, invalid metadata status, missing `metadata:` prefix for metadata-backed artifacts, and metadata-free artifacts incorrectly marked durable.
