# Sprint 4 Performance Summary

## Command

```text
PYTHONPATH=src python3 -c 'import time; from pathlib import Path; from project_conductor.registry import build_artifact_registry; from project_conductor.scanner import scan_repository; from project_conductor.state import build_repository_state; registry = build_artifact_registry(scan_repository(Path("tests/fixtures/repository-scanner/basic-repo"))); start = time.perf_counter(); iterations = 1000; payload = None
for _ in range(iterations):
    payload = build_repository_state(registry).to_json()
elapsed = time.perf_counter() - start
print("iterations:", iterations)
print("total_seconds:", format(elapsed, ".6f"))
print("average_milliseconds:", format((elapsed / iterations) * 1000, ".6f"))
print("last_payload_bytes:", len(payload.encode("utf-8")))'
```

## Output

```text
iterations: 1000
total_seconds: 0.066457
average_milliseconds: 0.066457
last_payload_bytes: 2489
```
