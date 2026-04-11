# Borderline Cases — `finalpool-personal-website-construct_9`

**Review branch:** `review/personal-website-construct-finalpool-9`  
**Base branch:** `review/personal-website-construct-8` (commit `e9c1314`)  
**Subject pair:** `bugmaker00/My-Homepage` ← `academicpages/academicpages.github.io`  
**Boundary table:** `boundary_review.csv`  
**Kept subset:** `kept_subset.json` (13 files)  

This document explains the four rows in `boundary_review.csv` whose decision was
non-obvious — either the closest files to the KEEP/DROP boundary or a file kept
by a rule so narrow that the rationale requires elaboration.

---

## §1 — `.python_tmp/setup_env.py` (6106 B) — Closest DROP near-miss

| Attribute | Value |
|-----------|-------|
| **Decision** | DROP |
| **Origin branch** | `main` |
| **Blob SHA** | `d07e6701e7153651b34f0b28dd0341fdab40f7e3` |
| **Size** | 6106 bytes |

### Why it looked like a KEEP candidate

`setup_env.py` is the largest file in the `.python_tmp/` group and the only one
whose content is non-trivially informative: it contains the verbatim source text
of `module_a.py`, `module_b.py`, `utils/helpers.py`, and `tests/test_module_a.py`
as Python string literals, and it programmatically creates `git init`, `git add`,
and `git commit` operations. A reviewer skimming only size and content density
could mistake it for a documentation artefact that explains the repository's
genesis.

### Why it was dropped

The decisive rule is **tooling-scaffold exclusion**: `setup_env.py` is the
script that bootstrapped the repository; it is upstream infrastructure whose
purpose was exhausted when the initial commit was created. Specifically:

1. **Absent from session-8 `full_scope.csv`** — the established scope catalogue
   (11 files, all verified MATCH) does not include any `.python_tmp/` file.
   Session-8 explicitly accepted the source-base files that `setup_env.py` wrote,
   but not the writer itself.
2. **Not cross-referenced in any review artefact** — `conflict_resolution.csv`,
   `source_priority.md`, `resolved_values.json`, `review_table_pair_1.csv`, and
   `decision_summary_pair_1.md` contain zero references to `setup_env.py` or the
   `.python_tmp/` directory.
3. **Self-liquidating purpose** — the script's value was realised at bootstrap
   time. Retaining it in the reviewed change set would document a scaffolding
   operation, not the review findings.
4. **Operational, not analytical** — the content is imperative (subprocess calls,
   file writes) rather than evidence-preserving (field values, source priorities,
   audit results). The correct artefacts to consult for the repository genesis are
   the accepted source-base files themselves.

**Inclusion would require:** an explicit cross-reference from a review artefact OR
a session rule that bootstrapping scripts are in scope (there is none).

---

## §2 — `dev/README.md` (2308 B) — Superseded alternative README

| Attribute | Value |
|-----------|-------|
| **Decision** | DROP |
| **Origin branch** | `dev` |
| **Blob SHA** | `b716d0d44db6039b43422fc1aa5c2df83ce3f977` |
| **Size** | 2308 bytes |

### Why it looked like a KEEP candidate

The `dev` branch `README.md` is 197 bytes larger than the `main` branch version
(2308 B vs 2111 B). Its additional content includes:

- A complete **tabular** rendering of all 27 TODO items (file_path / line_number / task columns)
- A **FIXME list** section (empty, but explicitly present)
- A **Python Backlog Snapshot** section with per-file TODO and FIXME counts and
  a `last refreshed: 2026-04-10 19:06 UTC` timestamp

Someone comparing the two READMEs could argue the `dev` version is more
information-rich and should supplement or replace the `main` version in scope.

### Why it was dropped

1. **Superseded by an accepted copy** — `main/README.md` (SHA `14b4e0cc`) is
   already a KEEP entry in `kept_subset.json`. Two versions of the same file from
   different branches cannot both be in the reviewed change set without a merge
   or explicit versioning scheme; the `main` version is the correct one because it
   carries the path-normalization fix.
2. **Path-normalization mismatch** — the `dev` README uses bare module paths
   (`module_a.py:7`) rather than `src/nebula/module_a.py:7`. The path-normalization
   fix was committed to `main` in commit `fbe7a13` specifically to correct this.
   Accepting the `dev` version would re-introduce the very error that `fbe7a13`
   resolved.
3. **Wrong workflow context** — the embedded timestamp `2026-04-10 19:06 UTC`
   places this file's generation 24 hours after the finalpool review pass
   (`2026-04-09`). It belongs to a subsequent `dev`-branch TODO/FIXME inventory
   workflow, not to the personal-website-construct fork-pair review.
4. **Not referenced in any finalpool artefact** — no entry in
   `conflict_resolution.csv`, `source_priority.md`, or `resolved_values.json`
   cites the `dev` README.

**Inclusion would require:** the `dev` version to carry the corrected
`src/nebula/` paths AND the `main` version to be retired from scope.

---

## §3 — `dev/target_ledger.csv` (2493 B) — Highest-quality dev artefact; path-normalization mismatch

| Attribute | Value |
|-----------|-------|
| **Decision** | DROP |
| **Origin branch** | `dev` |
| **Blob SHA** | `72ab383acba5e8d460983823a650ed2952e0f229` |
| **Size** | 2493 bytes |

### Why it looked like a KEEP candidate

`target_ledger.csv` is the highest-quality artefact in the `dev` branch:

- **27 rows** — one per TODO comment, matching the complete README checklist
- **Four columns:** `path` / `line` / `raw_marker` (verbatim comment text) / `description`
- **`raw_marker` column** captures the exact tag form used (e.g.
  `# TODO(warning): Handle network timeout gracefully` vs
  `# TODO: Add input validation for empty data`) — information not present in any
  accepted artefact
- All row values have been independently verified against the source files in this
  session (every description string matches `README.md` and the source files verbatim)

A case could be made that `target_ledger.csv` complements `full_scope.csv` by
providing TODO-level provenance that no accepted artefact currently documents.

### Why it was dropped

1. **Path-normalization mismatch** — paths use bare form (`module_a.py`, not
   `src/nebula/module_a.py`). This is the same defect corrected by commit `fbe7a13`
   and present in `dev/README.md` (§2 above). Accepting a file with pre-normalization
   paths would create a scope inconsistency.
2. **Dev-branch workflow context** — the file was generated by the dev-branch
   TODO/FIXME inventory workflow, not by the personal-website-construct fork-pair
   review workflow. Its provenance is orthogonal to the review question (upstream
   template identity and bootstrap status).
3. **Not referenced in any finalpool artefact** — zero mentions in
   `conflict_resolution.csv`, `source_priority.md`, `resolved_values.json`,
   `review_table_pair_1.csv`, or `decision_summary_pair_1.md`.
4. **Not in session-8 `full_scope.csv`** — the established scope catalogue does not
   include this file; adding it now would expand the scope without a corresponding
   review pass.

**Inclusion would require:** path correction to `src/nebula/` prefix AND an explicit
cross-reference from a finalpool artefact OR a new review session that expands the
scope to include TODO-provenance ledgers.

---

## §4 — `.gitignore` (14 B) — Marginal KEEP; smallest file; session-8 continuity rule

| Attribute | Value |
|-----------|-------|
| **Decision** | KEEP (marginal) |
| **Origin branch** | `main` |
| **Blob SHA** | `a81974ffd1df871c137252f8927315638ac36310` |
| **Size** | 14 bytes |

### Why it looked like a DROP candidate

With only 14 bytes of content (`.github_token\n`), `.gitignore` contains no TODO
comments, no review findings, no field values, and no analytical output. It is the
smallest file in the entire candidate set and its sole function is to prevent a
credential file from being committed. A reviewer scanning by file size or analytical
content would naturally question its inclusion.

### Why it was kept

1. **Session-8 continuity rule** — `.gitignore` was explicitly included in
   `session-8 full_scope.csv` (row 11: blob SHA `a81974ff` / 14 B / `source-base`
   / `staged_on_review_8=YES`) and verified MATCH by `readback_audit.md`. The
   session-8 acceptance constitutes a prior scope decision that carries forward
   unless a specific DROP rule is triggered.
2. **No DROP rule triggered** — `.gitignore` is not a tooling scaffold (§1 rule),
   not a wrong-context artefact (§2/§3 rule), and not superseded by an already-
   accepted copy. The only available DROP criteria do not apply.
3. **Credential protection is a legitimate project-base concern** — the content
   `.github_token\n` protects a live API credential from accidental version
   tracking. Its presence in the repository is intentional and its acceptance into
   the scope is consistent with including all project-base files that belong to
   `main`.

**Exclusion would require:** an explicit scope-narrowing rule that restricts
source-base files to those containing TODO comments — no such rule has been adopted
in any prior session artefact.

---

## Summary Table

| § | Candidate | Size | Decision | Swing factor |
|---|-----------|-----:|----------|-------------|
| 1 | `.python_tmp/setup_env.py` | 6106 B | **DROP** | Largest scaffold file; absent from session-8 scope; no review cross-reference despite high information density |
| 2 | `dev/README.md` | 2308 B | **DROP** | Richer format than accepted `main` version but carries uncorrected bare paths and wrong workflow timestamp |
| 3 | `dev/target_ledger.csv` | 2493 B | **DROP** | Highest-quality dev artefact (raw_marker column); disqualified by pre-normalization paths and orthogonal workflow provenance |
| 4 | `.gitignore` | 14 B | **KEEP** | Smallest kept file; marginal content; retained under session-8 continuity rule + credential-protection rationale |
