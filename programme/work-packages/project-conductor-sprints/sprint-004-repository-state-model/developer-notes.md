# Sprint 4 Developer Notes

## Run Tests

```text
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py'
```

## Export Repository State

```text
PYTHONPATH=src python3 -m project_conductor.cli --root tests/fixtures/repository-scanner/basic-repo --state-json
```

## Design Guardrail

Do not add persistence, Git, branch, diff, quality gate, AI, agent, or application logic to `project_conductor.state`.
