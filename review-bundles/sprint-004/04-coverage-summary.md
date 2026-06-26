# Sprint 4 Coverage Summary

Coverage was captured with Python standard library `trace`.

```text
PYTHONPATH=src python3 -m trace --count --summary --coverdir /private/tmp/pgv2-sprint4-trace --module unittest discover -s tests -p 'test_*.py'
```

```text
Ran 21 tests in 0.203s
OK
project_conductor.__init__   100%
project_conductor.cli   100%
project_conductor.metadata_contract   100%
project_conductor.registry   100%
project_conductor.scanner   100%
project_conductor.state   100%
project_conductor_tests.test_cli   100%
project_conductor_tests.test_registry   100%
project_conductor_tests.test_scanner   100%
project_conductor_tests.test_state   100%
```
