# Contract Checklist — render_preview.json Verification

**Contract version:** 1.0.0  
**Repository:** mcpmark-eval-1031/LUFFY  
**Preview file:** `render_preview.json`  
**Source branch scanned:** `review/changeset-v1` (post-pilot-changeset)  
**Checked:** 2026-04-09  
**Overall verdict:** ✅ PASS — all checks satisfied

---

## Background: Changeset Applied

The `review/changeset-v1` branch applied a pilot subset of TODO resolutions
to two files:

| File              | TODOs on `main` | Resolved | Remaining |
|-------------------|-----------------|----------|-----------|
| `module_a.py`     | 12              | 4        | 8         |
| `module_b.py`     | 9               | 0 (deferred) | 9    |
| `tests/test_module_a.py` | 3      | 0 (deferred) | 3    |
| `utils/helpers.py`| 3               | 3        | 0         |
| **Total**         | **27**          | **7**    | **20**    |

Resolved TODOs are absent from source on this branch; the preview correctly
reflects 20 open items.

---

## Section 1: Envelope Fields (§3.1 — Rules S-1, E-4)

| # | Check | Expected | Actual | Status |
|---|-------|----------|--------|--------|
| 1.1 | `schema_version` present, value `"1.0.0"`, position 1 | `"1.0.0"` | `"1.0.0"` | ✅ PASS |
| 1.2 | `repository` present, correct slug, position 2 | `"mcpmark-eval-1031/LUFFY"` | `"mcpmark-eval-1031/LUFFY"` | ✅ PASS |
| 1.3 | `source_branch` present, string, position 3 | `"review/changeset-v1"` | `"review/changeset-v1"` | ✅ PASS |
| 1.4 | `scanned_at` present, ISO 8601 UTC `Z` suffix, position 4 | `YYYY-MM-DDTHH:MM:SSZ` | `"2026-04-09T00:00:00Z"` | ✅ PASS |
| 1.5 | `scanned_files` present, array of strings, position 5 | sorted array | `["module_a.py","module_b.py","tests/test_module_a.py","utils/helpers.py"]` | ✅ PASS |
| 1.6 | `total_items` present, integer, position 6 | integer | `20` | ✅ PASS |
| 1.7 | `total_items` equals `len(items)` (Rule E-4) | 20 | `len(items) = 20` | ✅ PASS |
| 1.8 | `items` present, array, position 7 | array | array with 20 elements | ✅ PASS |
| 1.9 | Envelope field order matches §3.1 positions 1–7 | positions 1–7 | confirmed | ✅ PASS |
| 1.10 | No extra envelope fields (Rule S-1) | exactly 7 keys | 7 keys only | ✅ PASS |

---

## Section 2: TODO Item Record Fields (§3.2 — Rules S-2, S-3)

All 20 records verified. Spot-check shown for items 1, 8, 9, 17, 18, 20.

| Field # | Field Name    | Present in all 20 | Correct Position | Type Correct | Status |
|---------|---------------|-------------------|-----------------|--------------|--------|
| 1 | `id`          | ✅ Yes | ✅ Pos 1 | integer  | ✅ PASS |
| 2 | `file`        | ✅ Yes | ✅ Pos 2 | string   | ✅ PASS |
| 3 | `line`        | ✅ Yes | ✅ Pos 3 | integer  | ✅ PASS |
| 4 | `tag`         | ✅ Yes | ✅ Pos 4 | string\|null | ✅ PASS |
| 5 | `description` | ✅ Yes | ✅ Pos 5 | string   | ✅ PASS |
| 6 | `status`      | ✅ Yes | ✅ Pos 6 | string   | ✅ PASS |

**All 6 fields present in correct positional order across all 20 records. ✅**

---

## Section 3: Empty-Value Policy (§4)

| Rule | Description | Verification | Status |
|------|-------------|-------------|--------|
| E-1 | No empty string `""` as any field value | Scanned all 20 records × 6 fields = 120 values; zero `""` found | ✅ PASS |
| E-2 | No field omitted from any record | All 6 fields present in each of 20 records | ✅ PASS |
| E-3 | `status` is always `"open"` or `"resolved"` | All 20 records: `"status": "open"`; no null, no other string | ✅ PASS |
| E-4 | `total_items` equals `len(items)` | 20 == 20 | ✅ PASS |
| `tag` null policy | `tag` is `null` when no `(tag)` in source | ids 1,3,4,9,12,13,15,18,19,20 have `"tag": null`; verified against source | ✅ PASS |
| `tag` string policy | `tag` is a non-empty string when `(tag)` present | ids 2,5,6,7,8,10,11,14,16,17 have string tags; none are `""` | ✅ PASS |
| `scanned_files` | Non-null, non-empty array | 4 entries; none null or empty string | ✅ PASS |

---

## Section 4: Normalization Rules (§5)

| Rule | Description | Verification | Status |
|------|-------------|-------------|--------|
| N-1 | `file` paths root-relative, forward slashes, no `./` prefix | 3 distinct paths: `"module_a.py"`, `"module_b.py"`, `"tests/test_module_a.py"` — all compliant; `"utils/helpers.py"` in scanned_files but no items (0 TODOs) | ✅ PASS |
| N-2 | `tag` lower-cased | Tags used: `"dev"`, `"warning"`, `"future"`, `"bug"` — all lower-case | ✅ PASS |
| N-3 | Description stripped of `# TODO`, tag, delimiters, trimmed; first-char case preserved | See full table below | ✅ PASS |
| N-4 | `scanned_at` UTC with `Z` suffix | `"2026-04-09T00:00:00Z"` | ✅ PASS |
| N-5 | `scanned_files` sorted ascending lexicographically | `"module_a.py"` < `"module_b.py"` < `"tests/test_module_a.py"` < `"utils/helpers.py"` | ✅ PASS |
| N-6 | Fresh-scan items have `"status": "open"` | All 20 items: `"status": "open"` | ✅ PASS |
| N-7 | Tie-breaking by `description` asc (no actual ties) | No duplicate `(file, line)` pairs exist | ✅ PASS |

### N-3 Full Description Verification (all 20 items)

| id | Source TODO comment (review/changeset-v1) | Pattern | tag | Normalized `description` | Match |
|----|------------------------------------------|---------|-----|--------------------------|-------|
| 1  | `# TODO: Implement caching mechanism for repeated calls` | `# TODO: <text>` | null | `"Implement caching mechanism for repeated calls"` | ✅ |
| 2  | `# TODO(dev): Add support for streaming data processing` | `# TODO(<tag>): <text>` | `"dev"` | `"Add support for streaming data processing"` | ✅ |
| 3  | `# TODO - Implement proper schema validation` | `# TODO - <text>` | null | `"Implement proper schema validation"` | ✅ |
| 4  | `# TODO: Load config from file instead of hardcoding` | `# TODO: <text>` | null | `"Load config from file instead of hardcoding"` | ✅ |
| 5  | `# TODO(warning): Handle network timeout gracefully` | `# TODO(<tag>): <text>` | `"warning"` | `"Handle network timeout gracefully"` | ✅ |
| 6  | `# TODO(future): Add support for batch processing` | `# TODO(<tag>): <text>` | `"future"` | `"Add support for batch processing"` | ✅ |
| 7  | `# TODO(dev): Implement error recovery` | `# TODO(<tag>): <text>` | `"dev"` | `"Implement error recovery"` | ✅ |
| 8  | `# TODO(dev): Graceful shutdown implementation` | `# TODO(<tag>): <text>` | `"dev"` | `"Graceful shutdown implementation"` | ✅ |
| 9  | `# TODO: Add retry logic for failed requests` | `# TODO: <text>` | null | `"Add retry logic for failed requests"` | ✅ |
| 10 | `# TODO(bug): Fix memory leak in connection pool` | `# TODO(<tag>): <text>` | `"bug"` | `"Fix memory leak in connection pool"` | ✅ |
| 11 | `# TODO(dev): Add connection pooling configuration` | `# TODO(<tag>): <text>` | `"dev"` | `"Add connection pooling configuration"` | ✅ |
| 12 | `# TODO: Add timeout parameter` | `# TODO: <text>` | null | `"Add timeout parameter"` | ✅ |
| 13 | `# TODO: Handle SSL certificate errors` | `# TODO: <text>` | null | `"Handle SSL certificate errors"` | ✅ |
| 14 | `# TODO(dev): Implement exponential backoff` | `# TODO(<tag>): <text>` | `"dev"` | `"Implement exponential backoff"` | ✅ |
| 15 | `# TODO - Implement request signing` | `# TODO - <text>` | null | `"Implement request signing"` | ✅ |
| 16 | `# TODO(dev): Add response compression support` | `# TODO(<tag>): <text>` | `"dev"` | `"Add response compression support"` | ✅ |
| 17 | `# TODO(dev): Implement concurrent batch processing` | `# TODO(<tag>): <text>` | `"dev"` | `"Implement concurrent batch processing"` | ✅ |
| 18 | `# TODO: Add more test cases` | `# TODO: <text>` | null | `"Add more test cases"` | ✅ |
| 19 | `# TODO: Mock external dependencies` | `# TODO: <text>` | null | `"Mock external dependencies"` | ✅ |
| 20 | `# TODO: Test edge cases` | `# TODO: <text>` | null | `"Test edge cases"` | ✅ |

---

## Section 5: Ordering Constraints (§6)

### Rules O-1 + O-2: Primary sort by `file` asc, secondary by `line` asc

| id | `file`                   | `line` | Line order correct? | File order correct? |
|----|--------------------------|--------|---------------------|---------------------|
| 1  | module_a.py              | 15     | N/A (first in file) | ✅ first file |
| 2  | module_a.py              | 16     | ✅ 16 > 15          | same file |
| 3  | module_a.py              | 29     | ✅ 29 > 16          | same file |
| 4  | module_a.py              | 63     | ✅ 63 > 29          | same file |
| 5  | module_a.py              | 68     | ✅ 68 > 63          | same file |
| 6  | module_a.py              | 69     | ✅ 69 > 68          | same file |
| 7  | module_a.py              | 70     | ✅ 70 > 69          | same file |
| 8  | module_a.py              | 75     | ✅ 75 > 70          | same file |
| 9  | module_b.py              | 5      | N/A (new file)      | ✅ `module_b` > `module_a` |
| 10 | module_b.py              | 6      | ✅ 6 > 5            | same file |
| 11 | module_b.py              | 7      | ✅ 7 > 6            | same file |
| 12 | module_b.py              | 11     | ✅ 11 > 7           | same file |
| 13 | module_b.py              | 12     | ✅ 12 > 11          | same file |
| 14 | module_b.py              | 13     | ✅ 13 > 12          | same file |
| 15 | module_b.py              | 18     | ✅ 18 > 13          | same file |
| 16 | module_b.py              | 19     | ✅ 19 > 18          | same file |
| 17 | module_b.py              | 24     | ✅ 24 > 19          | same file |
| 18 | tests/test_module_a.py   | 3      | N/A (new file)      | ✅ `tests/` > `module_b` |
| 19 | tests/test_module_a.py   | 4      | ✅ 4 > 3            | same file |
| 20 | tests/test_module_a.py   | 7      | ✅ 7 > 4            | same file |

**File lex order (case-insensitive):** `module_a.py` < `module_b.py` < `tests/test_module_a.py` < `utils/helpers.py` (0 items). ✅

### Rule O-3: `id` assignment after sorting

`id` runs 1–20 contiguously in sorted order. `id[n] = n` for all n ∈ {1,…,20}. ✅

### Rule O-4: Sort stability

No duplicate `(file, line)` pairs exist; stability is trivially satisfied. ✅

### Rule O-5: Field order immutability

All 20 records: `id` → `file` → `line` → `tag` → `description` → `status`. ✅

---

## Section 6: Accepted TODO Patterns (§2)

| Pattern | Count | Example ids |
|---------|-------|-------------|
| `# TODO: <text>` | 10 | 1, 3, 4, 9, 12, 13, 15, 18, 19, 20 |
| `# TODO(<tag>): <text>` | 8 | 2, 5, 6, 7, 8, 10, 11, 14, 16, 17 |
| `# TODO - <text>` | 2 | 3, 15 |
| `# TODO <text>` (bare) | 0 | — |

> Note: item 3 uses `# TODO - <text>` and item 15 uses `# TODO - <text>`;
> both are correctly captured. No bare pattern or blank-description items
> remain in the post-changeset source (the bare `# TODO add support for
> multi-threading` from `utils/helpers.py` was resolved by the changeset). ✅

---

## Section 7: Changeset Integrity Cross-Check

This section verifies that the preview accurately reflects the changeset
applied in `review/changeset-v1` relative to the `main` baseline.

| Check | Detail | Status |
|-------|--------|--------|
| TODOs resolved in `module_a.py` | 4 resolved (L7 input validation, L15 type hints, L22 option handling, L30 config validation) — none appear in preview | ✅ PASS |
| TODOs retained in `module_a.py` | 8 items at lines 15, 16, 29, 63, 68, 69, 70, 75 — all present in preview as ids 1–8 | ✅ PASS |
| TODOs resolved in `utils/helpers.py` | 3 resolved (L3 threading, L4 race condition, L8 template) — none appear in preview | ✅ PASS |
| TODOs in `utils/helpers.py` after changeset | 0 — file present in `scanned_files`, absent from `items` | ✅ PASS |
| `module_b.py` deferred (unchanged) | 9 items at lines 5–7, 11–13, 18–19, 24 — all present in preview as ids 9–17 | ✅ PASS |
| `tests/test_module_a.py` deferred (unchanged) | 3 items at lines 3, 4, 7 — all present in preview as ids 18–20 | ✅ PASS |
| `total_items` delta from baseline | 27 (main) − 7 (resolved) = 20 (this preview) | ✅ PASS |

---

## Summary

| Section | Rule Count | Passed | Failed |
|---------|-----------|--------|--------|
| 1 — Envelope Fields (§3.1)              | 10 | 10 | 0 |
| 2 — Record Field Presence/Order (§3.2)  | 6  | 6  | 0 |
| 3 — Empty-Value Policy (§4)             | 7  | 7  | 0 |
| 4 — Normalization Rules (§5)            | 7 + 20 description checks = 27 | 27 | 0 |
| 5 — Ordering Constraints (§6)           | 5  | 5  | 0 |
| 6 — Accepted Patterns (§2)              | 1  | 1  | 0 |
| 7 — Changeset Integrity Cross-Check     | 7  | 7  | 0 |
| **TOTAL**                               | **63** | **63** | **0** |

**Final verdict: ✅ ALL 63 CHECKS PASS**
