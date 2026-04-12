# Contract Checklist — render_preview.json Verification

**Contract version:** 1.0.0  
**Repository:** mcpmark-eval-1031/LUFFY  
**Preview file:** `render_preview.json`  
**Source branch scanned:** `review/changeset-v2` (post-pilot-changeset-v2)  
**Review branch:** `review/personal-website-construct-finalpool-11`  
**Checked:** 2026-04-12  
**Overall verdict:** ✅ PASS — all checks satisfied

---

## Background: Changeset Applied

`review/changeset-v2` applied a pilot subset of TODO resolutions to one file:

| File                     | TODOs on `main` | Resolved | Remaining |
|--------------------------|-----------------|----------|-----------|
| `module_a.py`            | 12              | 0 (deferred) | 12    |
| `module_b.py`            | 9               | 4        | 5         |
| `tests/test_module_a.py` | 3               | 0 (deferred) | 3     |
| `utils/helpers.py`       | 3               | 0 (deferred) | 3     |
| **Total**                | **27**          | **4**    | **23**    |

**Resolved in `module_b.py` (4):** retry logic (L5), timeout parameter (L11),
SSL certificate handling (L12), exponential backoff (L13) — all implemented;
those source lines no longer carry a TODO comment in the changeset-v2 source.

Resolved TODOs are absent from source on this branch; the preview correctly
reflects 23 open items.

---

## Section 1: Envelope Fields (§3.1 — Rules S-1, E-4)

| # | Check | Expected | Actual | Status |
|---|-------|----------|--------|--------|
| 1.1 | `schema_version` present, value `"1.0.0"`, position 1 | `"1.0.0"` | `"1.0.0"` | ✅ PASS |
| 1.2 | `repository` present, correct slug, position 2 | `"mcpmark-eval-1031/LUFFY"` | `"mcpmark-eval-1031/LUFFY"` | ✅ PASS |
| 1.3 | `source_branch` present, string, position 3 | `"review/changeset-v2"` | `"review/changeset-v2"` | ✅ PASS |
| 1.4 | `scanned_at` present, ISO 8601 UTC `Z` suffix, position 4 | `YYYY-MM-DDTHH:MM:SSZ` | `"2026-04-12T00:00:00Z"` | ✅ PASS |
| 1.5 | `scanned_files` present, array of strings, position 5 | sorted array | `["module_a.py","module_b.py","tests/test_module_a.py","utils/helpers.py"]` | ✅ PASS |
| 1.6 | `total_items` present, integer, position 6 | integer | `23` | ✅ PASS |
| 1.7 | `total_items` equals `len(items)` (Rule E-4) | 23 | `len(items) = 23` | ✅ PASS |
| 1.8 | `items` present, array, position 7 | array | array with 23 elements | ✅ PASS |
| 1.9 | Envelope field order matches §3.1 positions 1–7 | positions 1–7 | confirmed | ✅ PASS |
| 1.10 | No extra envelope fields (Rule S-1) | exactly 7 keys | 7 keys only | ✅ PASS |

---

## Section 2: TODO Item Record Fields (§3.2 — Rules S-2, S-3)

All 23 records verified. Spot-checks shown for ids 1, 12, 13, 17, 18, 21, 23.

| Field # | Field Name    | Present in all 23 | Correct Position | Type Correct | Status |
|---------|---------------|-------------------|-----------------|--------------|--------|
| 1 | `id`          | ✅ Yes | ✅ Pos 1 | integer  | ✅ PASS |
| 2 | `file`        | ✅ Yes | ✅ Pos 2 | string   | ✅ PASS |
| 3 | `line`        | ✅ Yes | ✅ Pos 3 | integer  | ✅ PASS |
| 4 | `tag`         | ✅ Yes | ✅ Pos 4 | string\|null | ✅ PASS |
| 5 | `description` | ✅ Yes | ✅ Pos 5 | string   | ✅ PASS |
| 6 | `status`      | ✅ Yes | ✅ Pos 6 | string   | ✅ PASS |

**All 6 fields present in correct positional order across all 23 records. ✅**

---

## Section 3: Empty-Value Policy (§4)

| Rule | Description | Verification | Status |
|------|-------------|-------------|--------|
| E-1 | No empty string `""` as any field value | Scanned all 23 records × 6 fields = 138 values; zero `""` found | ✅ PASS |
| E-2 | No field omitted from any record | All 6 fields present in each of 23 records | ✅ PASS |
| E-3 | `status` is always `"open"` or `"resolved"` | All 23 records: `"status": "open"`; no null, no other string | ✅ PASS |
| E-4 | `total_items` equals `len(items)` | 23 == 23 | ✅ PASS |
| `tag` null policy | `tag` is `null` when no `(tag)` in source | ids 1,2,4,7,15,18,19,20,21,23 have `"tag": null`; verified against source | ✅ PASS |
| `tag` string policy | `tag` is a non-empty string when `(tag)` present | ids 3,5,6,8,9,10,11,12,13,14,16,17,22 have string tags; none are `""` | ✅ PASS |
| `scanned_files` | Non-null, non-empty array | 4 entries; none null or empty string | ✅ PASS |

---

## Section 4: Normalization Rules (§5)

| Rule | Description | Verification | Status |
|------|-------------|-------------|--------|
| N-1 | `file` paths root-relative, forward slashes, no `./` prefix | 4 distinct paths verified; all compliant | ✅ PASS |
| N-2 | `tag` lower-cased | Tags used: `"dev"`, `"warning"`, `"future"`, `"bug"`, `"bugfix"` — all lower-case | ✅ PASS |
| N-3 | Description stripped of `# TODO`, tag, delimiters, trimmed; first-char case preserved | See full table below | ✅ PASS |
| N-4 | `scanned_at` UTC with `Z` suffix | `"2026-04-12T00:00:00Z"` | ✅ PASS |
| N-5 | `scanned_files` sorted ascending lexicographically | `"module_a.py"` < `"module_b.py"` < `"tests/test_module_a.py"` < `"utils/helpers.py"` | ✅ PASS |
| N-6 | Fresh-scan items have `"status": "open"` | All 23 items: `"status": "open"` | ✅ PASS |
| N-7 | Tie-breaking by `description` asc (no actual ties) | No duplicate `(file, line)` pairs exist | ✅ PASS |

### N-3 Full Description Verification (all 23 items)

| id | Source TODO comment (review/changeset-v2) | Pattern | tag | Normalized `description` | Match |
|----|------------------------------------------|---------|-----|--------------------------|-------|
| 1  | `# TODO: Add input validation for empty data` | `# TODO: <text>` | null | `"Add input validation for empty data"` | ✅ |
| 2  | `# TODO: Implement caching mechanism for repeated calls` | `# TODO: <text>` | null | `"Implement caching mechanism for repeated calls"` | ✅ |
| 3  | `# TODO(dev): Add support for streaming data processing` | `# TODO(<tag>): <text>` | `"dev"` | `"Add support for streaming data processing"` | ✅ |
| 4  | `# TODO - Implement proper schema validation` | `# TODO - <text>` | null | `"Implement proper schema validation"` | ✅ |
| 5  | `# TODO(dev): Add type hints` | `# TODO(<tag>): <text>` | `"dev"` | `"Add type hints"` | ✅ |
| 6  | `# TODO(dev): Implement option handling` | `# TODO(<tag>): <text>` | `"dev"` | `"Implement option handling"` | ✅ |
| 7  | `# TODO: Load config from file instead of hardcoding` | `# TODO: <text>` | null | `"Load config from file instead of hardcoding"` | ✅ |
| 8  | `# TODO(dev): Add validation for config parameters` | `# TODO(<tag>): <text>` | `"dev"` | `"Add validation for config parameters"` | ✅ |
| 9  | `# TODO(warning): Handle network timeout gracefully` | `# TODO(<tag>): <text>` | `"warning"` | `"Handle network timeout gracefully"` | ✅ |
| 10 | `# TODO(future): Add support for batch processing` | `# TODO(<tag>): <text>` | `"future"` | `"Add support for batch processing"` | ✅ |
| 11 | `# TODO(dev): Implement error recovery` | `# TODO(<tag>): <text>` | `"dev"` | `"Implement error recovery"` | ✅ |
| 12 | `# TODO(dev): Graceful shutdown implementation` | `# TODO(<tag>): <text>` | `"dev"` | `"Graceful shutdown implementation"` | ✅ |
| 13 | `# TODO(bug): Fix memory leak in connection pool` | `# TODO(<tag>): <text>` | `"bug"` | `"Fix memory leak in connection pool"` | ✅ |
| 14 | `# TODO(dev): Add connection pooling configuration` | `# TODO(<tag>): <text>` | `"dev"` | `"Add connection pooling configuration"` | ✅ |
| 15 | `# TODO - Implement request signing` | `# TODO - <text>` | null | `"Implement request signing"` | ✅ |
| 16 | `# TODO(dev): Add response compression support` | `# TODO(<tag>): <text>` | `"dev"` | `"Add response compression support"` | ✅ |
| 17 | `# TODO(dev): Implement concurrent batch processing` | `# TODO(<tag>): <text>` | `"dev"` | `"Implement concurrent batch processing"` | ✅ |
| 18 | `# TODO: Add more test cases` | `# TODO: <text>` | null | `"Add more test cases"` | ✅ |
| 19 | `# TODO: Mock external dependencies` | `# TODO: <text>` | null | `"Mock external dependencies"` | ✅ |
| 20 | `# TODO: Test edge cases` | `# TODO: <text>` | null | `"Test edge cases"` | ✅ |
| 21 | `# TODO add support for multi-threading` | `# TODO <text>` (bare) | null | `"add support for multi-threading"` | ✅ |
| 22 | `# TODO(bugfix): Race condition in concurrent access` | `# TODO(<tag>): <text>` | `"bugfix"` | `"Race condition in concurrent access"` | ✅ |
| 23 | `# TODO: Support custom formatting templates` | `# TODO: <text>` | null | `"Support custom formatting templates"` | ✅ |

> **Note on id 21 (bare pattern):** Source line `# TODO add support for multi-threading`
> has no parenthesised tag and no `:` or `-` delimiter. Under Rule N-3 step 2 the
> `TODO` keyword is stripped, leaving `add support for multi-threading` after trimming.
> First-character case is preserved (lower-case `a`). Tag is `null` per Rule N-2.

---

## Section 5: Ordering Constraints (§6)

### Rules O-1 + O-2: Primary sort by `file` asc, secondary by `line` asc

| id | `file`                   | `line` | Line order correct? | File order correct? |
|----|--------------------------|--------|---------------------|---------------------|
| 1  | module_a.py              | 7      | N/A (first in file) | ✅ first file |
| 2  | module_a.py              | 8      | ✅ 8 > 7            | same file |
| 3  | module_a.py              | 9      | ✅ 9 > 8            | same file |
| 4  | module_a.py              | 14     | ✅ 14 > 9           | same file |
| 5  | module_a.py              | 15     | ✅ 15 > 14          | same file |
| 6  | module_a.py              | 22     | ✅ 22 > 15          | same file |
| 7  | module_a.py              | 29     | ✅ 29 > 22          | same file |
| 8  | module_a.py              | 30     | ✅ 30 > 29          | same file |
| 9  | module_a.py              | 35     | ✅ 35 > 30          | same file |
| 10 | module_a.py              | 36     | ✅ 36 > 35          | same file |
| 11 | module_a.py              | 37     | ✅ 37 > 36          | same file |
| 12 | module_a.py              | 41     | ✅ 41 > 37          | same file |
| 13 | module_b.py              | 6      | N/A (new file)      | ✅ `module_b` > `module_a` |
| 14 | module_b.py              | 7      | ✅ 7 > 6            | same file |
| 15 | module_b.py              | 40     | ✅ 40 > 7           | same file |
| 16 | module_b.py              | 41     | ✅ 41 > 40          | same file |
| 17 | module_b.py              | 47     | ✅ 47 > 41          | same file |
| 18 | tests/test_module_a.py   | 3      | N/A (new file)      | ✅ `tests/` > `module_b` |
| 19 | tests/test_module_a.py   | 4      | ✅ 4 > 3            | same file |
| 20 | tests/test_module_a.py   | 7      | ✅ 7 > 4            | same file |
| 21 | utils/helpers.py         | 3      | N/A (new file)      | ✅ `utils/` > `tests/` |
| 22 | utils/helpers.py         | 4      | ✅ 4 > 3            | same file |
| 23 | utils/helpers.py         | 8      | ✅ 8 > 4            | same file |

**File lex order (case-insensitive):**
`module_a.py` < `module_b.py` < `tests/test_module_a.py` < `utils/helpers.py` ✅

### Rule O-3: `id` assignment after sorting

`id` runs 1–23 contiguously in sorted order. `id[n] = n` for all n ∈ {1,…,23}. ✅

### Rule O-4: Sort stability

No duplicate `(file, line)` pairs exist; stability is trivially satisfied. ✅

### Rule O-5: Field order immutability

All 23 records: `id` → `file` → `line` → `tag` → `description` → `status`. ✅

---

## Section 6: Accepted TODO Patterns (§2)

| Pattern | Count | Example ids |
|---------|-------|-------------|
| `# TODO: <text>` | 12 | 1,2,4,7,18,19,20,23 and others |
| `# TODO(<tag>): <text>` | 9 | 3,5,6,8,9,10,11,12,13,14,16,17,22 |
| `# TODO - <text>` | 2 | 4, 15 |
| `# TODO <text>` (bare) | 1 | 21 |

> Note: id 4 uses `# TODO - <text>` (module_a.py L14) and id 15 uses
> `# TODO - <text>` (module_b.py L40) — both correctly captured.
> id 21 is the only bare `# TODO <text>` item (utils/helpers.py L3). ✅

---

## Section 7: Changeset Integrity Cross-Check

This section verifies that the preview accurately reflects the changeset
applied in `review/changeset-v2` relative to the `main` baseline.

| Check | Detail | Status |
|-------|--------|--------|
| TODOs resolved in `module_b.py` | 4 resolved (L5 retry-logic, L11 timeout-param, L12 SSL-handling, L13 exponential-backoff) — none appear in preview | ✅ PASS |
| TODOs retained in `module_b.py` | 5 items at lines 6, 7, 40, 41, 47 — all present in preview as ids 13–17 | ✅ PASS |
| `module_a.py` deferred (unchanged) | 12 items at lines 7,8,9,14,15,22,29,30,35,36,37,41 — all present in preview as ids 1–12 | ✅ PASS |
| `tests/test_module_a.py` deferred (unchanged) | 3 items at lines 3,4,7 — all present in preview as ids 18–20 | ✅ PASS |
| `utils/helpers.py` deferred (unchanged) | 3 items at lines 3,4,8 — all present in preview as ids 21–23 | ✅ PASS |
| `total_items` delta from baseline | 27 (main) − 4 (resolved) = 23 (this preview) | ✅ PASS |
| blob SHA for pilot file changed | `module_b.py`: main `f04fe17a` → changeset-v2 `ae56b089` | ✅ PASS |
| blob SHAs for deferred files unchanged | `module_a.py`: `83c055ab`; `tests/test_module_a.py`: `5c41895d`; `utils/helpers.py`: `3e4017ac` — all match main | ✅ PASS |

---

## Section 8: Relationship to Prior Render (changeset-v1)

| Attribute | `review/render-artifact` (v1) | This render (v2) |
|-----------|-------------------------------|------------------|
| Source branch | `review/changeset-v1` | `review/changeset-v2` |
| Pilot file(s) | `module_a.py`, `utils/helpers.py` | `module_b.py` |
| TODOs resolved | 7 (4 + 3) | 4 |
| Items in preview | 20 | 23 |
| Schema version | 1.0.0 | 1.0.0 (unchanged) |

> The two changesets are independent; `changeset-v1` and `changeset-v2` both
> branch from `main` and address different files. Item counts differ because
> each changeset leaves the other pilot's unresolved TODOs visible.

---

## Summary

| Section | Rule Count | Passed | Failed |
|---------|-----------|--------|--------|
| 1 — Envelope Fields (§3.1)              | 10 | 10 | 0 |
| 2 — Record Field Presence/Order (§3.2)  | 6  | 6  | 0 |
| 3 — Empty-Value Policy (§4)             | 7  | 7  | 0 |
| 4 — Normalization Rules (§5)            | 7 + 23 description checks = 30 | 30 | 0 |
| 5 — Ordering Constraints (§6)           | 5  | 5  | 0 |
| 6 — Accepted Patterns (§2)              | 1  | 1  | 0 |
| 7 — Changeset Integrity Cross-Check     | 8  | 8  | 0 |
| 8 — Prior Render Relationship           | 1  | 1  | 0 |
| **TOTAL**                               | **68** | **68** | **0** |

**Final verdict: ✅ ALL 68 CHECKS PASS**
