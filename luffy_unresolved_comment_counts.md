# LUFFY Unresolved Comment Counts

Unresolved `TODO` / `FIXME` comments found in the LUFFY project's Python sources on the `dev` branch.

## Totals

| Tag | Count |
|-------|-------|
| TODO | 27 |
| FIXME | 0 |

- **Total TODO: 27**
- **Total FIXME: 0**
- **Total unresolved comments: 27**

## Per-file breakdown

| File | TODO | FIXME |
|------|------|-------|
| `module_a.py` | 12 | 0 |
| `module_b.py` | 9 | 0 |
| `tests/test_module_a.py` | 3 | 0 |
| `utils/helpers.py` | 3 | 0 |

## Scope note

The requested scan target was a `luffy/` directory. No `luffy/` directory exists on the `dev` branch (nor on any other branch of this repository) — this repository *is* the LUFFY project, and its Python sources live at the repository root. The scan therefore covered every tracked `.py` file in the project tree:

- `module_a.py`
- `module_b.py`
- `tests/test_module_a.py`
- `utils/helpers.py`

Paths in `luffy_unresolved_comments.json` are recorded as real repository-relative paths so that they resolve correctly. The scratch `.python_tmp/` tooling scripts are excluded: their `TODO` strings are string literals inside a generator template, not real code comments.
