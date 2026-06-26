# Sprint 4 Coverage Summary

## Command

```text
PYTHONPATH=src python3 -m trace --count --summary --coverdir /private/tmp/pgv2-sprint4-trace --module unittest discover -s tests -p 'test_*.py'
```

## Method And Limitation

Coverage was captured with Python standard library `trace` to avoid adding dependencies. The complete command emits Python standard library rows; project rows are listed below.

## Project Rows

```text
.....................
----------------------------------------------------------------------
Ran 21 tests in 0.203s

OK
lines   cov%   module   (path)
    6   100%   project_conductor.__init__   (/Users/kirangonela/code/project-genesis-v2/src/project_conductor/__init__.py)
   45   100%   project_conductor.cli   (/Users/kirangonela/code/project-genesis-v2/src/project_conductor/cli.py)
   28   100%   project_conductor.metadata_contract   (/Users/kirangonela/code/project-genesis-v2/src/project_conductor/metadata_contract.py)
  149   100%   project_conductor.registry   (/Users/kirangonela/code/project-genesis-v2/src/project_conductor/registry.py)
  154   100%   project_conductor.scanner   (/Users/kirangonela/code/project-genesis-v2/src/project_conductor/scanner.py)
  242   100%   project_conductor.state   (/Users/kirangonela/code/project-genesis-v2/src/project_conductor/state.py)
   59   100%   project_conductor_tests.test_cli   (/Users/kirangonela/code/project-genesis-v2/tests/project_conductor_tests/test_cli.py)
  107   100%   project_conductor_tests.test_registry   (/Users/kirangonela/code/project-genesis-v2/tests/project_conductor_tests/test_registry.py)
   51   100%   project_conductor_tests.test_scanner   (/Users/kirangonela/code/project-genesis-v2/tests/project_conductor_tests/test_scanner.py)
   47   100%   project_conductor_tests.test_state   (/Users/kirangonela/code/project-genesis-v2/tests/project_conductor_tests/test_state.py)
```
