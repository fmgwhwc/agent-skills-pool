# S07 regression note

| Behavior / defect | RED | GREEN | Regression |
|---|---|---|---|
| kebab-case skill name + dir match (inspired by validate_r5 name pin) | `python3 -m unittest discover -s tests -v` EXIT=1; 3 FAIL on invalid/empty/Bad_Name | same command EXIT=0; 5 OK | full discover incl. neighbor edges EXIT=0; 7 OK |

Failure reasons at RED matched the missing contract (always-True stub), not setup/ImportError.
Minimal change: regex `^[a-z0-9]+(?:-[a-z0-9]+)*$` + validity gate in `name_matches_dir`.
No unrelated fixture files deleted; production pool/validate_r5 untouched.
