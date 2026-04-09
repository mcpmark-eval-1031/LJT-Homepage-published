# Dry-Run Preview — Dataset License Issue (finalpool-dataset-license-issue_11)

**Repository**: `mcpmark-eval-1031/LUFFY`  
**Review branch**: `review/dataset-license-issue-finalpool`  
**Base snapshot commit**: `fbe7a135c8220ddbc2d633367d4cdaeb42087c78` (main)  
**Issue resolved**: `bugmaker00/Annoy-DataSync#1` — "License info. needed"  
**Snapshot date**: 2026-04-09  
**Source of truth**: `full_scope.csv` (2 rows)  

---

## Background

The Annoy-DataSync project references two HuggingFace datasets:

| Dataset | HF URL |
|---------|--------|
| `dongbobo/Annoy-PyEdu-Rs-Raw` | https://huggingface.co/datasets/dongbobo/Annoy-PyEdu-Rs-Raw |
| `dongbobo/Annoy-PyEdu-Rs` | https://huggingface.co/datasets/dongbobo/Annoy-PyEdu-Rs |

Both datasets are adopted from the **HuggingFaceTB/smollm-corpus** `python-edu` subset,
which is licensed under **ODC-By 1.0** (Open Data Commons Attribution License).  
The companion metadata dataset `dongbobo/annoy-license-metadata` documents the
required license as `odc-by` for both.  
Neither dataset currently has a YAML frontmatter block with the `license` field set,
leaving the HuggingFace Hub unable to surface the license on each dataset card.

Open issue tracking this gap: `bugmaker00/Annoy-DataSync#1` — filed 2026-04-09.

---

## Row-by-Row Action Preview

### Row 1 — `dongbobo/Annoy-PyEdu-Rs-Raw / README.md`
**platform**: HUGGINGFACE  
**pilot_subset**: YES  
**change_applied**: applied (pilot)

| Before | After |
|--------|-------|
| No YAML frontmatter; README begins with `# Annoy: This should be a paper Title` | YAML frontmatter prepended: `---\nlicense: odc-by\n---` followed by the existing body |

**Exact diff (unified format)**:
```diff
--- a/README.md
+++ b/README.md
@@ -1,3 +1,6 @@
+---
+license: odc-by
+---
 # Annoy: This should be a paper Title
 
 <p align="left">
```

**Rationale**:  
- Upstream source: `HuggingFaceTB/smollm-corpus` (python-edu subset) — ODC-By 1.0.  
- `dongbobo/annoy-license-metadata` explicitly maps `Annoy-PyEdu-Rs-Raw → odc-by`.  
- No existing frontmatter — clean prepend; zero body changes.  
- Resolves `bugmaker00/Annoy-DataSync#1` for this dataset.

---

### Row 2 — `dongbobo/Annoy-PyEdu-Rs / README.md`
**platform**: HUGGINGFACE  
**pilot_subset**: NO  
**change_applied**: pending (deferred)

| Before | After (if applied) |
|--------|--------------------|
| No YAML frontmatter; README begins with `# Annoy: This should be a paper Title` | YAML frontmatter prepended: `---\nlicense: odc-by\n---` followed by the existing body |

**Exact diff (unified format, would-be)**:
```diff
--- a/README.md
+++ b/README.md
@@ -1,3 +1,6 @@
+---
+license: odc-by
+---
 # Annoy: This should be a paper Title
 
 <p align="left">
```

**Rationale**:  
- Identical upstream provenance as Row 1.  
- `dongbobo/annoy-license-metadata` maps `Annoy-PyEdu-Rs → odc-by`.  
- Deferred to second pass after pilot Row 1 is confirmed successful.  
- Will complete resolution of `bugmaker00/Annoy-DataSync#1`.

---

## Summary Table

| Row | HF Repo | File | Action | Pilot? | Status |
|-----|---------|------|--------|--------|--------|
| 1 | `dongbobo/Annoy-PyEdu-Rs-Raw` | README.md | Prepend `license: odc-by` YAML frontmatter | YES | applied |
| 2 | `dongbobo/Annoy-PyEdu-Rs` | README.md | Prepend `license: odc-by` YAML frontmatter | NO | pending |

**Total files in scope**: 2  
**Pilot subset**: 1 (Row 1 only)  
**Deferred**: 1 (Row 2)  
