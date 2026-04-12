# Render Contract — LUFFY TODO File-Set Artifact

**Version:** 1.0.0  
**Repository:** mcpmark-eval-1031/LUFFY  
**Status:** FROZEN  
**Date:** 2026-04-12  
**Scan basis:** `review/changeset-v2` branch — post-pilot-changeset-v2 snapshot  
**Prior contract:** v1.0.0 (2026-04-09, `review/render-artifact` branch) — schema unchanged; scan basis updated to `review/changeset-v2`.

---

## 1. Purpose

This contract governs the exact structure, field names, field order,
empty-value representation, normalization rules, and ordering constraints
that every rendering of the **LUFFY TODO file-set artifact** (hereafter "the
artifact") MUST satisfy.

The artifact is a machine-readable JSON document produced by scanning all
`.py` files in the canonical scope (§7) for `# TODO` markers and serializing
the extracted items. No rendering may be produced, stored, or reviewed until
this contract is frozen.

> **Contract-first rule:** The schema declared below is frozen before any
> preview JSON is written. `render_preview.json` is derived from this
> contract; the contract is never derived from the preview.

---

## 2. Accepted TODO Patterns

A source line MUST match one of the following patterns to qualify as a TODO
item (case-sensitive `TODO`; all other tokens case-insensitive):

| Pattern                    | Example source line                          |
|----------------------------|----------------------------------------------|
| `# TODO: <text>`           | `# TODO: Add input validation`               |
| `# TODO(<tag>): <text>`    | `# TODO(dev): Implement option handling`     |
| `# TODO - <text>`          | `# TODO - Implement request signing`         |
| `# TODO <text>` (bare)     | `# TODO add support for multi-threading`     |

Lines where `<text>` is absent or blank after stripping MUST be excluded
entirely — they produce no record in the artifact.

---

## 3. Schema Declaration

### 3.1 Top-level Envelope Fields (field order canonical, positional)

| # | Field Name       | JSON Type          | Required | Description |
|---|------------------|--------------------|----------|-------------|
| 1 | `schema_version` | `string`           | YES      | Semver of this contract: `"1.0.0"`. |
| 2 | `repository`     | `string`           | YES      | Fully-qualified `owner/repo` slug. |
| 3 | `source_branch`  | `string`           | YES      | Branch from which the scan was performed. |
| 4 | `scanned_at`     | `string` (ISO 8601)| YES      | UTC timestamp of the scan (`YYYY-MM-DDTHH:MM:SSZ`). |
| 5 | `scanned_files`  | `array<string>`    | YES      | Sorted list of root-relative `.py` file paths included in the scan. |
| 6 | `total_items`    | `integer`          | YES      | Count of TODO Item Records in `items` (equals `len(items)`). |
| 7 | `items`          | `array`            | YES      | Ordered array of TODO Item Records (see §3.2). |

**Rule S-1:** Envelope fields MUST appear in the JSON object in exactly the
order shown (positions 1–7). No additional envelope fields are permitted.

### 3.2 TODO Item Record Fields (field order canonical, positional)

| # | Field Name    | JSON Type           | Required | Description |
|---|---------------|---------------------|----------|-------------|
| 1 | `id`          | `integer`           | YES      | 1-based sequential index assigned after sorting (see §6 Rule O-3). |
| 2 | `file`        | `string`            | YES      | Root-relative path of the source file, forward slashes, no leading `./`. |
| 3 | `line`        | `integer`           | YES      | 1-based line number where the TODO comment appears. |
| 4 | `tag`         | `string` \| `null`  | YES      | Tag extracted from `TODO(tag)` syntax, lower-cased; `null` if absent. |
| 5 | `description` | `string`            | YES      | Normalized TODO description text (see §5 Rule N-3). |
| 6 | `status`      | `string` (enum)     | YES      | `"open"` for fresh-scan items; `"resolved"` only when explicitly closed. |

**Rule S-2:** Item record fields MUST appear in the JSON object in exactly
the order shown (positions 1–6). No additional item fields are permitted.

**Rule S-3:** Every field defined in §3.1 and §3.2 MUST be present in every
record. No field may be omitted.

---

## 4. Empty-Value Policy

| Situation                                        | Representation |
|--------------------------------------------------|----------------|
| `tag` absent from the TODO comment              | `null` (JSON null — NOT empty string `""`) |
| `scanned_files` when no files match             | `[]` (empty JSON array — NOT `null`) |
| `description` normalizes to empty string        | Item MUST be excluded entirely; no null-valued record is emitted. |
| Integer fields that equal zero                  | `0` (verbatim integer — NOT `null`) |

**Rule E-1:** An empty string (`""`) MUST NOT appear as any field value in
any envelope field or item record field.  
**Rule E-2:** No field defined in §3.1 or §3.2 may be omitted from any record.  
**Rule E-3:** `status` MUST always be the string `"open"` or `"resolved"`;
it is never `null` and never any other string.  
**Rule E-4:** `total_items` MUST equal the number of elements in `items`.
Mismatch is a contract violation.

---

## 5. Normalization Rules

**Rule N-1 (File Path):** `file` MUST be the root-relative path using forward
slashes with no leading `./` or `/`.  
Examples: `"module_a.py"`, `"tests/test_module_a.py"`, `"utils/helpers.py"`.

**Rule N-2 (Tag):** `tag` is extracted from the first parenthesised token
immediately following `TODO`. It MUST be lower-cased before storage.  
Example: `# TODO(Dev): text` → `tag = "dev"`.  
If no parenthesised token is present, `tag = null`.

**Rule N-3 (Description):** The raw comment text is normalized as follows:
1. Strip the leading `#` character and all surrounding whitespace.
2. Strip the `TODO` keyword.
3. If present, strip the `(<tag>)` group including the parentheses.
4. Strip any bare `:` or `-` delimiter (and following whitespace) that
   immediately follows `TODO` or the `(<tag>)` group.
5. Trim leading and trailing whitespace from the remainder.
6. Preserve the first character's case as-is (do NOT force upper or lower).

**Rule N-4 (Timestamp):** `scanned_at` MUST be expressed in UTC using the
`Z` suffix (e.g., `"2026-04-12T00:00:00Z"`).

**Rule N-5 (scanned_files Sort):** Entries in `scanned_files` MUST be sorted
in ascending lexicographic order (Unicode code-point order on the original-case
path string).

**Rule N-6 (Status Default):** Items produced by a fresh scan MUST carry
`"status": "open"`. The value `"resolved"` may only be applied by a
subsequent review pass and is never emitted by the scanner itself.

**Rule N-7 (Tie-breaking):** When two TODO items have the same `file` AND
the same `line` (which MUST NOT occur in practice — a single source line
cannot bear two TODO markers), the tie is broken by ascending `description`
lexicographic order. This rule exists for completeness; no actual tie is
expected.

---

## 6. Ordering Constraints

**Rule O-1 (Primary Sort — File):** TODO Item Records MUST be sorted in
ascending lexicographic order by `file` (case-insensitive comparison
performed on the lower-cased path; Unicode code-point order).

**Rule O-2 (Secondary Sort — Line):** Within the same `file`, records MUST
be sorted in ascending numeric order by `line`.

**Rule O-3 (id Assignment):** `id` values are assigned **after** sorting.
`id = 1` is assigned to the first record in the sorted output; `id = N` to
the N-th record. IDs MUST be contiguous integers starting at `1`.

**Rule O-4 (Stability):** The sort MUST be stable (equal keys preserve
original discovery order).

**Rule O-5 (Field Order Immutability):** The field orders declared in §3.1
(positions 1–7) and §3.2 (positions 1–6) are immutable. They MUST NOT be
altered without incrementing `schema_version`.

---

## 7. Scan Scope

The canonical scan scope for this repository is **all `.py` files reachable
from the repository root on the scanned branch**, using the branch as checked
out at the moment of the scan.

The four application-code paths are the canonical scope for this rendering cycle:

1. `module_a.py`
2. `module_b.py`
3. `tests/test_module_a.py`
4. `utils/helpers.py`

### Changeset-v2 Scope Summary

| File                     | blob SHA (changeset-v2)   | TODOs on `main` | Resolved | Remaining |
|--------------------------|---------------------------|-----------------|----------|-----------|
| `module_a.py`            | `83c055ab` (unchanged)    | 12              | 0        | 12        |
| `module_b.py`            | `ae56b089` (changed)      | 9               | 4        | 5         |
| `tests/test_module_a.py` | `5c41895d` (unchanged)    | 3               | 0        | 3         |
| `utils/helpers.py`       | `3e4017ac` (unchanged)    | 3               | 0        | 3         |
| **Total**                |                           | **27**          | **4**    | **23**    |

**Pilot scope:** Only `module_b.py` received changes in this changeset.  
**Deferred:** `module_a.py`, `tests/test_module_a.py`, `utils/helpers.py` carry their unmodified `main` blobs.

---

## 8. Blank and Tie Representation Summary

| Field | When value is absent / indeterminate | Representation |
|-------|--------------------------------------|----------------|
| `tag` | No `(tag)` token in source line — includes bare `# TODO <text>` pattern | `null` |
| `description` | Empty after normalization | Record excluded (not null) |
| `scanned_files` | No `.py` files found | `[]` |
| `total_items` | Zero qualifying items | `0` |
| `status` | Never absent | `"open"` or `"resolved"` only |
| Tie on `(file, line)` | Identical coordinates | Break by `description` asc |

---

## 9. Review-Branch Convention

The artifact files MUST be committed to a branch named with the prefix
`review/`. The three deliverables that constitute a complete render package:

| File                    | Description |
|-------------------------|-------------|
| `render_contract.md`    | This document (frozen schema). |
| `render_preview.json`   | Contract-conforming JSON artifact. |
| `contract_checklist.md` | Line-by-line verification checklist. |

For this rendering cycle the target branch is
`review/personal-website-construct-finalpool-11`,
branched from `review/changeset-v2` (HEAD commit `57459b7f`).

---

## 10. Contract Freeze Declaration

> **This contract is FROZEN as of 2026-04-12.**  
> No field names, field positions, empty-value policies, normalization rules,
> or ordering constraints may be altered after this declaration without
> incrementing `schema_version` and re-issuing a new frozen contract.
> `render_preview.json` and `contract_checklist.md` MUST be regenerated
> whenever this contract changes.
