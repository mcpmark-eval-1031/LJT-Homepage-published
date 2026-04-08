# Render Contract — LUFFY TODO File-Set Artifact

**Version:** 1.0.0  
**Repository:** mcpmark-eval-1031/LUFFY  
**Status:** FROZEN  
**Date:** 2026-04-08  
**Scan basis:** `dev` branch — commit `a8b49a8b` (2026-04-06)

---

## 1. Purpose

This contract governs the exact structure, field names, field order,
empty-value representation, normalization rules, and ordering constraints
that every rendering of the **LUFFY TODO file-set artifact** (hereafter "the
artifact") MUST satisfy.

The artifact is a machine-readable JSON document produced by scanning all
`.py` files in the repository for `# TODO` markers and serializing the
extracted items. No rendering may be produced, stored, or reviewed until
this contract is frozen.

---

## 2. Accepted TODO Patterns

A source line MUST match one of the following patterns to qualify as a TODO
item (case-sensitive `TODO`; all other tokens case-insensitive):

| Pattern                     | Example source line                          |
|-----------------------------|----------------------------------------------|
| `# TODO: <text>`            | `# TODO: Add input validation`               |
| `# TODO(<tag>): <text>`     | `# TODO(dev): Implement option handling`     |
| `# TODO - <text>`           | `# TODO - Implement request signing`         |
| `# TODO <text>` (bare)      | `# TODO add support for multi-threading`     |
| `# TODO(<tag>): <text>`     | `# TODO(bugfix): Race condition in …`        |

Lines where `<text>` is absent or blank after stripping MUST be excluded.

---

## 3. Schema Declaration

### 3.1 Top-level Envelope Fields (field order canonical, positional)

| # | Field Name        | JSON Type         | Required | Description |
|---|-------------------|-------------------|----------|-------------|
| 1 | `schema_version`  | `string`          | YES      | Semver of this contract: `"1.0.0"`. |
| 2 | `repository`      | `string`          | YES      | Fully-qualified `owner/repo` slug. |
| 3 | `source_branch`   | `string`          | YES      | Branch from which the scan was performed. |
| 4 | `scanned_at`      | `string` (ISO 8601) | YES    | UTC timestamp of the scan (`YYYY-MM-DDTHH:MM:SSZ`). |
| 5 | `scanned_files`   | `array<string>`   | YES      | Sorted list of root-relative `.py` file paths included in the scan. |
| 6 | `total_items`     | `integer`         | YES      | Total number of TODO items in the artifact (equals `len(items)`). |
| 7 | `items`           | `array`           | YES      | Ordered array of TODO Item Records (see §3.2). |

### 3.2 TODO Item Record Fields (field order canonical, positional)

| # | Field Name      | JSON Type          | Required | Description |
|---|-----------------|--------------------|----------|-------------|
| 1 | `id`            | `integer`          | YES      | 1-based sequential index within the artifact (1 = first item). |
| 2 | `file`          | `string`           | YES      | Root-relative path of the source file, forward slashes, no leading `./`. |
| 3 | `line`          | `integer`          | YES      | 1-based line number where the TODO comment appears. |
| 4 | `tag`           | `string` \| `null` | YES      | Tag extracted from `TODO(tag)` syntax, lower-cased; `null` if absent. |
| 5 | `description`   | `string`           | YES      | Normalized TODO description text (see §4 N-3). |
| 6 | `status`        | `string` (enum)    | YES      | `"open"` for all freshly-scanned items; `"resolved"` only when explicitly closed. |

---

## 4. Empty-Value Policy

| Situation                                        | Representation |
|--------------------------------------------------|----------------|
| `tag` absent from the TODO comment              | `null` (JSON null, NOT empty string `""`) |
| `scanned_files` when no files match             | `[]` (empty JSON array, NOT `null`) |
| `description` cannot be empty                   | Items with empty description after normalization MUST be excluded entirely (not null-valued). |
| Integer fields that equal zero                  | `0` (verbatim integer, NOT `null`) |

**Rule E-1:** An empty string (`""`) MUST NOT appear as any field value.  
**Rule E-2:** No field defined in §3.1 or §3.2 may be omitted from any record.  
**Rule E-3:** `status` MUST always be the string `"open"` or `"resolved"`;
it is never `null`.

---

## 5. Normalization Rules

**Rule N-1 (File Path):** `file` MUST be the root-relative path of the source
file using forward slashes and no leading `./` or `/`.  
Example: `"module_a.py"`, `"tests/test_module_a.py"`, `".python_tmp/setup_env.py"`.

**Rule N-2 (Tag Normalization):** `tag` is extracted from the first parenthesised
token immediately following `TODO`. It MUST be lower-cased.  
Example: `# TODO(Dev): text` → `tag = "dev"`.  
If no parenthesised token is present, `tag = null`.

**Rule N-3 (Description Normalization):** The raw comment text is processed:
1. Strip the leading `#` and any surrounding whitespace.
2. Strip the `TODO` keyword.
3. Strip any `(tag)` group and its following `:` or `-` delimiter and whitespace.
4. Strip any bare `:` or `-` delimiter and following whitespace that immediately
   follows `TODO`.
5. Trim leading/trailing whitespace from the remainder.
6. The first character's case is preserved as-is (do NOT force uppercase or lowercase).

**Rule N-4 (Timestamp Normalization):** `scanned_at` MUST be expressed in UTC
using the `Z` suffix (e.g., `"2026-04-08T18:30:00Z"`).

**Rule N-5 (scanned_files Normalization):** Entries in `scanned_files` MUST be
sorted in ascending lexicographic order (Unicode code-point order on the
original-case path). Hidden directories (e.g., `.python_tmp/`) are included
if their `.py` files were part of the scan.

**Rule N-6 (Status Default):** Items produced by a fresh scan MUST have
`"status": "open"`. The value `"resolved"` may only be applied by a subsequent
review pass; it is never emitted by the scanner itself.

---

## 6. Ordering Constraints

**Rule O-1 (Primary Sort):** TODO Item Records MUST be sorted in ascending
lexicographic order by `file` (case-insensitive; Unicode code-point order on
the lower-cased path).

**Rule O-2 (Secondary Sort):** Within the same `file`, records MUST be sorted
in ascending numeric order by `line`.

**Rule O-3 (id Assignment):** `id` values are assigned **after** sorting.
`id = 1` is assigned to the first record in the sorted output; `id = N` to the
N-th record. `id` values MUST be contiguous and start at `1`.

**Rule O-4 (Stability):** The sort MUST be stable.

**Rule O-5 (Field Order Immutability):** The field order declared in §3.1
(positions 1–7) and §3.2 (positions 1–6) is immutable.

---

## 7. Scan Scope

The canonical scan scope for this repository is **all `.py` files reachable
from the repository root on the scanned branch**, including files in hidden
directories (e.g., `.python_tmp/`). The set of scanned files is recorded
verbatim in `scanned_files`.

---

## 8. Review-Branch Convention

The artifact files MUST be committed to a branch named `review/render-artifact`
branched from the repository's default branch (`main`). The three deliverables:

| File                    | Description |
|-------------------------|-------------|
| `render_contract.md`    | This document (frozen schema). |
| `render_preview.json`   | Contract-conforming JSON artifact. |
| `contract_checklist.md` | Verification checklist. |

---

## 9. Contract Freeze Declaration

> **This contract is FROZEN as of 2026-04-08.**  
> No field names, field positions, empty-value policies, normalization rules,
> or ordering constraints may be altered after this declaration without
> incrementing `schema_version` and re-issuing a new frozen contract.
> `render_preview.json` and `contract_checklist.md` MUST be regenerated
> whenever this contract changes.
