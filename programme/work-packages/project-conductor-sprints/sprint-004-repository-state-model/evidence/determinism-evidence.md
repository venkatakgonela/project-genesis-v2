# Sprint 4 Determinism Evidence

## Command

```text
PYTHONPATH=src python3 -c 'from pathlib import Path; from project_conductor.registry import build_artifact_registry; from project_conductor.scanner import scan_repository; from project_conductor.state import build_repository_state; registry = build_artifact_registry(scan_repository(Path("tests/fixtures/repository-scanner/basic-repo"))); first = build_repository_state(registry).to_json(); second = build_repository_state(registry).to_json(); print("outputs_equal:", first == second); print("bytes:", len(first.encode("utf-8")))'
```

## Output

```text
outputs_equal: True
bytes: 2489
```
