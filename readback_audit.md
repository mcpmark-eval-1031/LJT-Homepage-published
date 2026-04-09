# Readback Audit — `review/sync-todo-to-readme`

**Repository**: `mcpmark-eval-1031/LUFFY`  
**Review branch**: `review/sync-todo-to-readme`  
**Base snapshot commit**: `fbe7a135c8220ddbc2d633367d4cdaeb42087c78` (main)  
**Audit generated**: 2026-04-09T03:34:12Z  
**Source of truth**: `full_scope.csv` (canonical TODO coordinates derived from source scan)

---

## Summary

| Metric | Count |
|--------|-------|
| Total TODOs in scope | 27 |
| Path-contested entries corrected (`src/nebula/` prefix stripped) | 21 |
| Path-unchallenged entries (already correct) | 6 |
| README lines matching `canonical_coordinate` | 27 |
| README lines NOT matching `canonical_coordinate` | 0 |

**Result: All 27 entries PASS. Live README is in full agreement with `full_scope.csv`.**

---

## Correction Applied

Commit `fbe7a135` on `main` introduced a spurious `src/nebula/` directory prefix for the  
21 entries sourced from `module_a.py` and `module_b.py`. Those files reside at the  
**monorepo root**, not under `src/nebula/`. The `review/sync-todo-to-readme` branch strips the  
erroneous prefix and restores root-relative coordinates consistent with the source scan.

**Rule applied**: `scan_result > readme_coordinate`  
(Source-file scan is authoritative; README coordinate is the derived artefact.)

---

## Line-by-line Audit

| # | full_scope.csv `canonical_coordinate` | README (live) coordinate | Match | Note |
|---|---------------------------------------|--------------------------|-------|------|
|   1 | `module_a.py:7` | `module_a.py:7` | ✅ MATCH | corrected from erroneous `src/nebula/module_a.py:7` |
|   2 | `module_a.py:8` | `module_a.py:8` | ✅ MATCH | corrected from erroneous `src/nebula/module_a.py:8` |
|   3 | `module_a.py:9` | `module_a.py:9` | ✅ MATCH | corrected from erroneous `src/nebula/module_a.py:9` |
|   4 | `module_a.py:14` | `module_a.py:14` | ✅ MATCH | corrected from erroneous `src/nebula/module_a.py:14` |
|   5 | `module_a.py:15` | `module_a.py:15` | ✅ MATCH | corrected from erroneous `src/nebula/module_a.py:15` |
|   6 | `module_a.py:22` | `module_a.py:22` | ✅ MATCH | corrected from erroneous `src/nebula/module_a.py:22` |
|   7 | `module_a.py:29` | `module_a.py:29` | ✅ MATCH | corrected from erroneous `src/nebula/module_a.py:29` |
|   8 | `module_a.py:30` | `module_a.py:30` | ✅ MATCH | corrected from erroneous `src/nebula/module_a.py:30` |
|   9 | `module_a.py:35` | `module_a.py:35` | ✅ MATCH | corrected from erroneous `src/nebula/module_a.py:35` |
|  10 | `module_a.py:36` | `module_a.py:36` | ✅ MATCH | corrected from erroneous `src/nebula/module_a.py:36` |
|  11 | `module_a.py:37` | `module_a.py:37` | ✅ MATCH | corrected from erroneous `src/nebula/module_a.py:37` |
|  12 | `module_a.py:41` | `module_a.py:41` | ✅ MATCH | corrected from erroneous `src/nebula/module_a.py:41` |
|  13 | `module_b.py:5` | `module_b.py:5` | ✅ MATCH | corrected from erroneous `src/nebula/module_b.py:5` |
|  14 | `module_b.py:6` | `module_b.py:6` | ✅ MATCH | corrected from erroneous `src/nebula/module_b.py:6` |
|  15 | `module_b.py:7` | `module_b.py:7` | ✅ MATCH | corrected from erroneous `src/nebula/module_b.py:7` |
|  16 | `module_b.py:11` | `module_b.py:11` | ✅ MATCH | corrected from erroneous `src/nebula/module_b.py:11` |
|  17 | `module_b.py:12` | `module_b.py:12` | ✅ MATCH | corrected from erroneous `src/nebula/module_b.py:12` |
|  18 | `module_b.py:13` | `module_b.py:13` | ✅ MATCH | corrected from erroneous `src/nebula/module_b.py:13` |
|  19 | `module_b.py:18` | `module_b.py:18` | ✅ MATCH | corrected from erroneous `src/nebula/module_b.py:18` |
|  20 | `module_b.py:19` | `module_b.py:19` | ✅ MATCH | corrected from erroneous `src/nebula/module_b.py:19` |
|  21 | `module_b.py:24` | `module_b.py:24` | ✅ MATCH | corrected from erroneous `src/nebula/module_b.py:24` |
|  22 | `tests/test_module_a.py:3` | `tests/test_module_a.py:3` | ✅ MATCH | unchallenged |
|  23 | `tests/test_module_a.py:4` | `tests/test_module_a.py:4` | ✅ MATCH | unchallenged |
|  24 | `tests/test_module_a.py:7` | `tests/test_module_a.py:7` | ✅ MATCH | unchallenged |
|  25 | `utils/helpers.py:3` | `utils/helpers.py:3` | ✅ MATCH | unchallenged |
|  26 | `utils/helpers.py:4` | `utils/helpers.py:4` | ✅ MATCH | unchallenged |
|  27 | `utils/helpers.py:8` | `utils/helpers.py:8` | ✅ MATCH | unchallenged |

---

## Files in Reviewed Scope

| File | TODOs scanned | Path contested? |
|------|--------------|------------------|
| `module_a.py` | 12 | YES — all 12 carried erroneous `src/nebula/` prefix |
| `module_b.py` | 9 | YES — all 9 carried erroneous `src/nebula/` prefix |
| `tests/test_module_a.py` | 3 | NO |
| `utils/helpers.py` | 3 | NO |
| **Total** | **27** | **21 contested, 6 unchallenged** |

---

## Verification Procedure

To reproduce this audit independently:

```bash
# 1. Clone or fetch the repo
git fetch origin review/sync-todo-to-readme

# 2. Scan TODOs from source
grep -rn "TODO" module_a.py module_b.py tests/test_module_a.py utils/helpers.py

# 3. Compare with README checklist on this branch
grep '- \[ \]' README.md

# 4. Confirm all README coordinates match scan coordinates
#    (no entry should begin with src/nebula/)
grep 'src/nebula' README.md && echo "FAIL" || echo "PASS"
```

Expected output of step 4: `PASS` (no `src/nebula/` occurrences in README).
