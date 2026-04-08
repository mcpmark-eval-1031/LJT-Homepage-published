# Borderline Cases — `review/sync-todo-to-readme`

**Repository**: `mcpmark-eval-1031/LUFFY`  
**Review branch**: `review/sync-todo-to-readme`  
**Snapshot commit**: `fbe7a135c8220ddbc2d633367d4cdaeb42087c78` (main)  
**Audit source**: `boundary_review.csv` rows with `decision = DROP`  
**Reference**: `full_scope.csv`, `cross_source_matrix.csv`, `normalized_selection.json`, `readback_audit.md`

---

## Purpose

This document explains the **closest-rejected cases**: candidate file sets (or individual TODO
entries within the kept set) that came nearest to crossing the inclusion boundary in either
direction. For each case the exact rule that settled the decision is stated and the live evidence
that distinguishes it from the kept set is provided.

---

## Case 1 — `.python_tmp/setup_env.py` *(closest rejected file — PRIMARY borderline case)*

| Attribute | Value |
|-----------|-------|
| **File** | `.python_tmp/setup_env.py` |
| **Decision** | **DROP** |
| **Decisive rule** | `hidden_tooling_directory_excluded` |
| **TODO candidates found** | 38 |
| **Duplicates canonical content** | YES |

### Why it was nearly included

A naive full-tree `grep -rn "TODO"` over all Python files in the repository will match
38 lines in `.python_tmp/setup_env.py` (lines 22–80 and 132–197) that look identical in
syntax to real development TODOs:

```python
# TODO: Add input validation for empty data        (line 22, and again at line 132)
# TODO(warning): Handle network timeout gracefully (line 42, and again at line 160)
# TODO(bug): Fix memory leak in connection pool    (line 51, and again at line 179)
```

The **`dev` branch README confirms that this mistake was actually made**: it lists all
65 entries — 38 from `.python_tmp/setup_env.py` followed by the 27 canonical entries.
This is direct empirical evidence that the file sits at the exact edge of the scan boundary.

### Why it was rejected

`.python_tmp/setup_env.py` is an **agent scaffolding script** that programmatically
creates the entire project. Its TODO lines fall into two groups:

| Lines | Source | Nature |
|-------|--------|--------|
| 22–80 (17 entries) | Inside Python string literals (`files = {'module_a.py': '''…'''`, etc.) | Partial/early-version copies of the source file TODOs embedded as string content in the `files` dict |
| 132–197 (21 entries) | Inside `dev_module_a` / `dev_module_b` string variables | Full copies of canonical TODO texts used to write the dev-branch versions of module_a.py and module_b.py |

These are **source-code templates**, not developer tasks filed against `setup_env.py` itself.
Running `grep TODO .python_tmp/setup_env.py` finds them only because the string literals
contain the `# TODO` prefix verbatim; the comments belong logically to the files they
describe, not to the scaffolding script.

Three additional factors seal the rejection:

1. **Hidden directory convention**: `.python_tmp/` begins with a dot, indicating a
   tool-specific scratch directory (analogous to `.github/`, `.cache/`, etc.).
   Production TODO scans conventionally skip hidden directories.

2. **All content is duplicated**: Every TODO text in `setup_env.py` already appears under
   its correct coordinate in the canonical 27-entry set. Including `setup_env.py` would
   produce 38 duplicate checklist entries with incorrect `setup_env.py:NNN` coordinates.

3. **Consistency check fails**: `normalized_selection.json` _meta records
   `"total_todos": 27` and `"consistency_check": "cross_source_matrix rows (27) ==
   normalized_selection entries (27) == README TODO count (27) == source scan count (27)"`.
   Adding 38 setup_env entries would break this 27-entry consistency invariant.

**Boundary statement**: The inclusion boundary is drawn at the `.python_tmp/` directory
level — ALL files under that directory are excluded regardless of their TODO content.
`setup_env.py` is the only file in `.python_tmp/` that carries actual TODO markers; the
other five files (`check_files.py`, `git_check.py`, `list_workspace.py`, `push_again.py`,
`reinit_git.py`) have zero TODO comments and are dropped by the same directory-level rule.

---

## Case 2 — `module_a.py:36` — `TODO(future)` tag *(closest near-miss within the kept set)*

| Attribute | Value |
|-----------|-------|
| **Canonical coordinate** | `module_a.py:36` |
| **Decision** | **KEEP** (included in final README) |
| **Tag** | `future` |
| **TODO text** | `Add support for batch processing` |
| **Path contested** | YES (erroneous `src/nebula/module_a.py:36` in main README) |

### Why it was borderline

The `TODO(future)` tag signals a **long-term / aspirational** item rather than an
immediately actionable task. A strict "actionable-only" filter could have excluded it
on the grounds that future-labelled items belong in a roadmap document rather than a
current-sprint TODO checklist.

### Why it was kept

The scope rule for `review/sync-todo-to-readme` is **coordinate normalisation only**:
the review corrects path prefixes; it does not apply a tag-severity filter to exclude
entries. All 27 entries in `full_scope.csv` are included in scope regardless of tag
(`plain`, `dev`, `warning`, `future`, `bug`, `bugfix`). Tag-based triage is out of scope
for this review pass.

Furthermore, `normalized_selection.json` explicitly lists `module_a.py:36` with
`resolution: "scan_result"` and includes it in the final 27-entry set. `readback_audit.md`
row 10 confirms `✅ MATCH`.

---

## Case 3 — `module_a.py:35` — `TODO(warning)` tag *(second near-miss within the kept set)*

| Attribute | Value |
|-----------|-------|
| **Canonical coordinate** | `module_a.py:35` |
| **Decision** | **KEEP** |
| **Tag** | `warning` |
| **TODO text** | `Handle network timeout gracefully` |
| **Path contested** | YES (erroneous `src/nebula/module_a.py:35` in main README) |

### Why it was borderline

The `TODO(warning)` tag implies a **severity classification** — this item represents a
potential reliability hazard. One might argue that severity-classified items deserve a
separate tracking mechanism (e.g., a bug tracker or a `WARNINGS.md`) rather than a
standard checklist alongside low-priority refactors.

### Why it was kept

Same reasoning as Case 2: the review's scope is limited to path-coordinate normalisation.
The `warning` tag does not trigger any exclusion rule in `full_scope.csv` or
`normalized_selection.json`. `readback_audit.md` row 9 confirms `✅ MATCH`.

---

## Case 4 — `module_b.py:6` — `TODO(bug)` tag *(third near-miss within the kept set)*

| Attribute | Value |
|-----------|-------|
| **Canonical coordinate** | `module_b.py:6` |
| **Decision** | **KEEP** |
| **Tag** | `bug` |
| **TODO text** | `Fix memory leak in connection pool` |
| **Path contested** | YES (erroneous `src/nebula/module_b.py:6` in main README) |

### Why it was borderline

A `TODO(bug)` item (memory leak) might be considered more urgent than a routine
refactor and could warrant its own issue in the bug tracker rather than a README
checklist entry. A reviewers' policy of "bugs → issue tracker only" would have excluded it.

### Why it was kept

Again, the review applies only the `scan_result > readme_coordinate` rule; no
tag-severity exclusion policy exists for this review pass. `readback_audit.md` row 14
confirms `✅ MATCH`. The `cross_source_matrix.csv` records it as `resolution=scan_result`
with `path_contested=YES, coordinate_match=NO`.

---

## Summary Table

| Case | Candidate | Decision | Rule that decided | Near-miss reason |
|------|-----------|----------|-------------------|------------------|
| 1 | `.python_tmp/setup_env.py` | **DROP** | `hidden_tooling_directory_excluded` | 38 real-looking TODOs; dev branch mistakenly included them; decisive factor: string-literal embedding + hidden dir |
| 2 | `module_a.py:36` | **KEEP** | `scan_result_over_readme_coordinate` (no tag filter) | `TODO(future)` tag raises question of actionability; kept because scope = coordinate normalisation only |
| 3 | `module_a.py:35` | **KEEP** | `scan_result_over_readme_coordinate` (no tag filter) | `TODO(warning)` tag could justify separate severity tracking; kept by same reasoning |
| 4 | `module_b.py:6`  | **KEEP** | `scan_result_over_readme_coordinate` (no tag filter) | `TODO(bug)` tag might warrant issue-tracker-only policy; kept by same reasoning |

---

## Inclusion Boundary Statement

The boundary enforced in `review/sync-todo-to-readme` has two orthogonal components:

1. **File-scope boundary** (coarse): Include only Python files under `repo_root/`,
   `tests/`, and `utils/`. Exclude all files under `.python_tmp/` (agent tooling).
   This boundary eliminates 38 artifact-duplicate TODO candidates from `setup_env.py`.

2. **Coordinate-form boundary** (fine): For each included entry, use the
   `scan_coordinate` (source-scan result) as the authoritative path. The
   `readme_coordinate` form is dropped when it carries an erroneous `src/nebula/`
   directory prefix introduced by commit `fbe7a135`. This corrects 21 of the 27
   kept entries.

Both boundaries are explicit in `full_scope.csv` (`resolution` column) and
`normalized_selection.json` (`_meta.source_rule`).
