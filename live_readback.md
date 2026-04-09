# Live Readback — `review/dataset-license-issue-finalpool`

**Repository**: `mcpmark-eval-1031/LUFFY`  
**Review branch**: `review/dataset-license-issue-finalpool`  
**Base snapshot commit**: `fbe7a135c8220ddbc2d633367d4cdaeb42087c78` (main)  
**Planning commit**: `aba51e99e2d2db3ae78e0cb2870a5c82c848365f`  
**Readback generated**: 2026-04-09  
**Source of truth**: `full_scope.csv` / `pilot_scope.csv`  

---

## Purpose

This document confirms that the live HuggingFace state for the **pilot row** in
`pilot_scope.csv` matches the change described in `dry_run_preview.md`,  
and that the **deferred row** remains untouched.

---

## Summary

| Metric | Value |
|--------|-------|
| Total files in reviewed scope | 2 |
| Pilot subset (change_applied=applied) | 1 |
| Deferred (change_applied=pending) | 1 |
| License fixes applied | 1 |
| Live-state checks passing | 2 / 2 |

**Result: Pilot row PASS. Deferred row PASS (unchanged). Live state is in full agreement with `full_scope.csv`.**

---

## File-by-File Readback

### Row 1 — `dongbobo/Annoy-PyEdu-Rs-Raw / README.md` — Pilot subset ✅

| Field | full_scope.csv (plan) | Live HF state | Match? |
|-------|-----------------------|---------------|--------|
| `current_license` | null | null (pre-change) | n/a |
| `required_license` | odc-by | odc-by | ✅ PASS |
| `change_applied` | applied | applied | ✅ PASS |
| YAML frontmatter present | YES (after) | YES | ✅ PASS |
| `license: odc-by` in frontmatter | YES | YES | ✅ PASS |
| Body content unchanged | YES | YES (body identical to pre-change) | ✅ PASS |

**Live README first 5 lines (verified by live fetch)**:
```
---
license: odc-by
---
# Annoy: This should be a paper Title

```

**Commit applied to HF dataset**: `fix: add license: odc-by YAML frontmatter (resolves bugmaker00/Annoy-DataSync#1)`  
**HF dataset URL**: https://huggingface.co/datasets/dongbobo/Annoy-PyEdu-Rs-Raw  
**Verification URL**: https://huggingface.co/datasets/dongbobo/Annoy-PyEdu-Rs-Raw/raw/main/README.md

---

### Row 2 — `dongbobo/Annoy-PyEdu-Rs / README.md` — Deferred (pending) ✅

| Field | full_scope.csv (plan) | Live HF state | Match? |
|-------|-----------------------|---------------|--------|
| `change_applied` | pending | pending (no change applied) | ✅ PASS |
| YAML frontmatter present | NO (before) | NO | ✅ PASS |
| `license: odc-by` in frontmatter | NO (deferred) | NO | ✅ PASS |
| Body content unchanged | YES (no touch) | YES | ✅ PASS |

**Live README first line (verified by live fetch)**:  
`# Annoy: This should be a paper Title`  
No YAML frontmatter block present — consistent with `pending` status.

---

## Scope Completeness Check

```
full_scope.csv rows : 2
Files readback      : 2
Difference          : 0  ← complete
```

| Row | HF Repo | File | plan_status | live_status | readback_verdict |
|-----|---------|------|-------------|-------------|-----------------|
| 1 | `dongbobo/Annoy-PyEdu-Rs-Raw` | README.md | applied | applied | ✅ PASS |
| 2 | `dongbobo/Annoy-PyEdu-Rs` | README.md | pending | pending | ✅ PASS |

**All 2 rows PASS. Live HuggingFace state is consistent with `full_scope.csv`.**

---

## Issue Tracking

- **`bugmaker00/Annoy-DataSync#1`** — "License info. needed"
  - Status: **partially resolved** — `Annoy-PyEdu-Rs-Raw` now carries `license: odc-by`
  - Remaining: `Annoy-PyEdu-Rs` (Row 2, deferred) needs the same fix in the second pass

---

## Verification Steps

```bash
# 1. Confirm pilot dataset README has odc-by frontmatter
curl -sL https://huggingface.co/datasets/dongbobo/Annoy-PyEdu-Rs-Raw/raw/main/README.md \
  | head -4
# Expected:
#   ---
#   license: odc-by
#   ---
#   # Annoy: This should be a paper Title

# 2. Confirm deferred dataset README has no frontmatter yet
curl -sL https://huggingface.co/datasets/dongbobo/Annoy-PyEdu-Rs/raw/main/README.md \
  | head -2
# Expected:
#   # Annoy: This should be a paper Title
```
