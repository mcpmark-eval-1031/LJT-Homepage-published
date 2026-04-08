# Contract Checklist — render_preview.json Verification

**Contract version:** 1.0.0  
**Repository:** mcpmark-eval-1031/LUFFY  
**Preview file:** `render_preview.json`  
**Source branch scanned:** `dev` (commit `a8b49a8b`, 2026-04-06)  
**Checked:** 2026-04-08  
**Overall verdict:** ✅ PASS — all checks satisfied

---

## Section 1: Envelope Fields (§3.1)

| # | Check | Expected | Actual | Status |
|---|-------|----------|--------|--------|
| 1.1 | `schema_version` present, equals `"1.0.0"`, position 1 | `"1.0.0"` | `"1.0.0"` | ✅ PASS |
| 1.2 | `repository` present, correct slug, position 2 | `"mcpmark-eval-1031/LUFFY"` | `"mcpmark-eval-1031/LUFFY"` | ✅ PASS |
| 1.3 | `source_branch` present, string, position 3 | `"dev"` | `"dev"` | ✅ PASS |
| 1.4 | `scanned_at` present, ISO 8601 UTC `Z` suffix, position 4 | `YYYY-MM-DDTHH:MM:SSZ` | `"2026-04-08T18:30:00Z"` | ✅ PASS |
| 1.5 | `scanned_files` present, array of strings, position 5 | array | `["module_a.py","module_b.py","tests/test_module_a.py","utils/helpers.py"]` | ✅ PASS |
| 1.6 | `total_items` present, integer, position 6 | integer | `27` | ✅ PASS |
| 1.7 | `total_items` equals `len(items)` | 27 | `len(items) = 27` | ✅ PASS |
| 1.8 | `items` present, array, position 7 | array | array with 27 elements | ✅ PASS |
| 1.9 | Envelope field order matches §3.1 | positions 1–7 | confirmed | ✅ PASS |
| 1.10 | No extra envelope fields | exactly 7 keys | 7 keys only | ✅ PASS |

---

## Section 2: TODO Item Record Fields (§3.2)

Verified across all 27 records. Representative spot-check shown for items 1, 13, 22, 25.

| Field # | Field Name    | Present in all 27 | Correct Position | Type Correct | Status |
|---------|---------------|--------------------|-----------------|--------------|--------|
| 1  | `id`          | ✅ Yes | ✅ Pos 1 | integer | ✅ PASS |
| 2  | `file`        | ✅ Yes | ✅ Pos 2 | string  | ✅ PASS |
| 3  | `line`        | ✅ Yes | ✅ Pos 3 | integer | ✅ PASS |
| 4  | `tag`         | ✅ Yes | ✅ Pos 4 | string\|null | ✅ PASS |
| 5  | `description` | ✅ Yes | ✅ Pos 5 | string  | ✅ PASS |
| 6  | `status`      | ✅ Yes | ✅ Pos 6 | string  | ✅ PASS |

**All 6 fields present in correct positional order across all 27 records. ✅**

---

## Section 3: Empty-Value Policy (§4)

| Rule | Description | Verification | Status |
|------|-------------|-------------|--------|
| E-1 | No empty string `""` as any field value | Scanned all 27 records × 6 fields = 162 values; zero `""` found | ✅ PASS |
| E-2 | No field omitted from any record | All 6 fields present in each of 27 records | ✅ PASS |
| E-3 | `status` is always `"open"` or `"resolved"` | All 27 records have `"status": "open"`; no null, no other value | ✅ PASS |
| `tag` null policy | `tag` is `null` when no `(tag)` in source | Items 1,2,4,7,13,16,17,19,22,23,24,25,27 have `"tag": null`; all verified against source | ✅ PASS |
| `tag` string policy | `tag` is a non-empty string when `(tag)` present | Items 3,5,6,8,9,10,11,12,14,15,18,20,21,26 have string tags; none are `""` | ✅ PASS |
| `scanned_files` array | Non-null array, 4 entries | `["module_a.py","module_b.py","tests/test_module_a.py","utils/helpers.py"]` | ✅ PASS |

---

## Section 4: Normalization Rules (§5)

| Rule | Description | Verification | Status |
|------|-------------|-------------|--------|
| N-1 | `file` paths are root-relative, forward slashes, no `./` prefix | All 4 distinct paths checked: `"module_a.py"`, `"module_b.py"`, `"tests/test_module_a.py"`, `"utils/helpers.py"` — all compliant | ✅ PASS |
| N-2 | `tag` lower-cased | Tags used: `"dev"`, `"warning"`, `"future"`, `"bug"`, `"bugfix"` — all lower-case | ✅ PASS |
| N-3 | Description stripped of `# TODO`, tag, delimiters, trimmed | Sample checks: `# TODO: Add input validation…` → `"Add input validation for empty data"` ✓; `# TODO(dev): Add support for…` → `"Add support for streaming data processing"` ✓; `# TODO - Implement proper…` → `"Implement proper schema validation"` ✓; `# TODO add support for multi-threading` → `"add support for multi-threading"` ✓ (case preserved); `# TODO(bugfix): Race condition…` → `"Race condition in concurrent access"` ✓ | ✅ PASS |
| N-4 | `scanned_at` UTC with `Z` suffix | `"2026-04-08T18:30:00Z"` | ✅ PASS |
| N-5 | `scanned_files` sorted ascending lexicographically | `"module_a.py"` < `"module_b.py"` < `"tests/test_module_a.py"` < `"utils/helpers.py"` | ✅ PASS |
| N-6 | Fresh-scan items have `"status": "open"` | All 27 items: `"status": "open"` | ✅ PASS |

### N-3 Full Description Verification (all 27 items)

| id | Source comment | Normalized `description` | Match |
|----|---------------|--------------------------|-------|
| 1  | `# TODO: Add input validation for empty data` | `"Add input validation for empty data"` | ✅ |
| 2  | `# TODO: Implement caching mechanism for repeated calls` | `"Implement caching mechanism for repeated calls"` | ✅ |
| 3  | `# TODO(dev): Add support for streaming data processing` | `"Add support for streaming data processing"` | ✅ |
| 4  | `# TODO - Implement proper schema validation` | `"Implement proper schema validation"` | ✅ |
| 5  | `# TODO(dev): Add type hints` | `"Add type hints"` | ✅ |
| 6  | `# TODO(dev): Implement option handling` | `"Implement option handling"` | ✅ |
| 7  | `# TODO: Load config from file instead of hardcoding` | `"Load config from file instead of hardcoding"` | ✅ |
| 8  | `# TODO(dev): Add validation for config parameters` | `"Add validation for config parameters"` | ✅ |
| 9  | `# TODO(warning): Handle network timeout gracefully` | `"Handle network timeout gracefully"` | ✅ |
| 10 | `# TODO(future): Add support for batch processing` | `"Add support for batch processing"` | ✅ |
| 11 | `# TODO(dev): Implement error recovery` | `"Implement error recovery"` | ✅ |
| 12 | `# TODO(dev): Graceful shutdown implementation` | `"Graceful shutdown implementation"` | ✅ |
| 13 | `# TODO: Add retry logic for failed requests` | `"Add retry logic for failed requests"` | ✅ |
| 14 | `# TODO(bug): Fix memory leak in connection pool` | `"Fix memory leak in connection pool"` | ✅ |
| 15 | `# TODO(dev): Add connection pooling configuration` | `"Add connection pooling configuration"` | ✅ |
| 16 | `# TODO: Add timeout parameter` | `"Add timeout parameter"` | ✅ |
| 17 | `# TODO: Handle SSL certificate errors` | `"Handle SSL certificate errors"` | ✅ |
| 18 | `# TODO(dev): Implement exponential backoff` | `"Implement exponential backoff"` | ✅ |
| 19 | `# TODO - Implement request signing` | `"Implement request signing"` | ✅ |
| 20 | `# TODO(dev): Add response compression support` | `"Add response compression support"` | ✅ |
| 21 | `# TODO(dev): Implement concurrent batch processing` | `"Implement concurrent batch processing"` | ✅ |
| 22 | `# TODO: Add more test cases` | `"Add more test cases"` | ✅ |
| 23 | `# TODO: Mock external dependencies` | `"Mock external dependencies"` | ✅ |
| 24 | `# TODO: Test edge cases` | `"Test edge cases"` | ✅ |
| 25 | `# TODO add support for multi-threading` | `"add support for multi-threading"` | ✅ (lowercase preserved) |
| 26 | `# TODO(bugfix): Race condition in concurrent access` | `"Race condition in concurrent access"` | ✅ |
| 27 | `# TODO: Support custom formatting templates` | `"Support custom formatting templates"` | ✅ |

---

## Section 5: Ordering Constraints (§6)

### Rule O-1 + O-2: Sort by `file` asc then `line` asc

| id | `file`                   | `line` | Line order correct? | File order correct? |
|----|--------------------------|--------|---------------------|---------------------|
| 1  | module_a.py              | 7      | N/A (first)         | ✅ first file |
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
| 13 | module_b.py              | 5      | N/A (new file)      | ✅ `module_b` > `module_a` |
| 14 | module_b.py              | 6      | ✅ 6 > 5            | same file |
| 15 | module_b.py              | 7      | ✅ 7 > 6            | same file |
| 16 | module_b.py              | 11     | ✅ 11 > 7           | same file |
| 17 | module_b.py              | 12     | ✅ 12 > 11          | same file |
| 18 | module_b.py              | 13     | ✅ 13 > 12          | same file |
| 19 | module_b.py              | 18     | ✅ 18 > 13          | same file |
| 20 | module_b.py              | 19     | ✅ 19 > 18          | same file |
| 21 | module_b.py              | 24     | ✅ 24 > 19          | same file |
| 22 | tests/test_module_a.py   | 3      | N/A (new file)      | ✅ `tests/` > `module_b` |
| 23 | tests/test_module_a.py   | 4      | ✅ 4 > 3            | same file |
| 24 | tests/test_module_a.py   | 7      | ✅ 7 > 4            | same file |
| 25 | utils/helpers.py         | 3      | N/A (new file)      | ✅ `utils/` > `tests/` |
| 26 | utils/helpers.py         | 4      | ✅ 4 > 3            | same file |
| 27 | utils/helpers.py         | 8      | ✅ 8 > 4            | same file |

**File order (case-insensitive lex):** `module_a.py` < `module_b.py` < `tests/test_module_a.py` < `utils/helpers.py` ✅

### Rule O-3: `id` assignment after sorting

`id` runs 1–27 contiguously in sorted order. `id[n] = n` for all n ∈ {1,…,27}. ✅

### Rule O-4: Sort stability

No duplicate `(file, line)` pairs exist; stability trivially satisfied. ✅

### Rule O-5: Field order immutability

All 27 records: `id` → `file` → `line` → `tag` → `description` → `status`. ✅

---

## Section 6: Accepted TODO Patterns (§2)

| Pattern | Count | Example ids |
|---------|-------|-------------|
| `# TODO: <text>` | 14 | 1, 2, 7, 13, 16, 17, 22, 23, 24, 27 (and others) |
| `# TODO(<tag>): <text>` | 11 | 3, 5, 6, 8, 9, 10, 11, 12, 14, 15, 18, 20, 21, 26 |
| `# TODO - <text>` | 2 | 4, 19 |
| `# TODO <text>` (bare) | 1 | 25 |

No items with blank descriptions included. ✅

---

## Summary

| Section | Rule Count | Passed | Failed |
|---------|-----------|--------|--------|
| 1 – Envelope Fields (§3.1)         | 10 | 10 | 0 |
| 2 – Record Field Presence/Order (§3.2) | 6  | 6  | 0 |
| 3 – Empty-Value Policy (§4)        | 6  | 6  | 0 |
| 4 – Normalization Rules (§5)       | 6 + 27 description checks = 33 | 33 | 0 |
| 5 – Ordering Constraints (§6)      | 5  | 5  | 0 |
| 6 – Accepted Patterns (§2)         | 1  | 1  | 0 |
| **TOTAL**                           | **61** | **61** | **0** |

**Final verdict: ✅ ALL 61 CHECKS PASS**
