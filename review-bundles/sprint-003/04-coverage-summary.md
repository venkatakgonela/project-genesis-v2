# Sprint 3 Coverage Summary

## Command

```text
PYTHONPATH=src python3 -m trace --count --summary --coverdir /private/tmp/pgv2-trace --module unittest discover -s tests -p 'test_*.py'
```

## Method And Limitation

Coverage was captured with the Python standard library `trace` module to avoid adding dependencies. The full command output includes Python standard library modules; the project-relevant rows are listed below.

## Output

```text
...............
----------------------------------------------------------------------
Ran 15 tests in 0.120s

OK
lines   cov%   module   (path)
    5   100%   project_conductor.__init__   (/Users/kirangonela/code/project-genesis-v2/src/project_conductor/__init__.py)
   39   100%   project_conductor.cli   (/Users/kirangonela/code/project-genesis-v2/src/project_conductor/cli.py)
   28   100%   project_conductor.metadata_contract   (/Users/kirangonela/code/project-genesis-v2/src/project_conductor/metadata_contract.py)
  149   100%   project_conductor.registry   (/Users/kirangonela/code/project-genesis-v2/src/project_conductor/registry.py)
  154   100%   project_conductor.scanner   (/Users/kirangonela/code/project-genesis-v2/src/project_conductor/scanner.py)
    1   100%   project_conductor_tests.__init__   (/Users/kirangonela/code/project-genesis-v2/tests/project_conductor_tests/__init__.py)
   46   100%   project_conductor_tests.test_cli   (/Users/kirangonela/code/project-genesis-v2/tests/project_conductor_tests/test_cli.py)
  107   100%   project_conductor_tests.test_registry   (/Users/kirangonela/code/project-genesis-v2/tests/project_conductor_tests/test_registry.py)
   51   100%   project_conductor_tests.test_scanner   (/Users/kirangonela/code/project-genesis-v2/tests/project_conductor_tests/test_scanner.py)
```
