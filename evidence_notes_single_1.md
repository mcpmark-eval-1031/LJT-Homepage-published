# Evidence Notes — Scope Matrix Single-1

**Subproblem:** Namespace-resolution change set for `bugmaker00/Annoy-DataSync`  
(fork of `hkust-nlp/CodeIO`; reviewed commit `120c992`; existence-blocking prerequisite check)  
**Review branch:** `review/scope-matrix-single-1`  
**Companion surface:** `scope_matrix_single_1.csv` (4 rows — 3 KEEP + 1 DROP)  
**Snapshot date:** 2026-04-08  
**Source priority rule:** `P1 live-huggingface > P2 live-github main HEAD > P3 intermediate git snapshots > P4 upstream project`  

---

## Subproblem Context

The reviewed change is commit `120c992` (`chore: update README placeholders for namespaces`)  
pushed to `bugmaker00/Annoy-DataSync` on 2026-04-08. That commit replaced all  
`{hf_namespace}` placeholders with `dongbobo` and all `{github_namespace}` placeholders  
with `bugmaker00` throughout the repository README.

The repository is a fork of `hkust-nlp/CodeIO` (original commits by `lockon-n`, Sep 2025)  
that was forked into `bugmaker00`'s namespace and customised for the Annoy dataset collection.

### Key Evidence Sources

| Source | Label | Queried | Status |
|--------|-------|---------|--------|
| HuggingFace live API | P1 live-huggingface | 2026-04-08 | Confirmed dongbobo/Annoy-PyEdu-Rs and dongbobo/Annoy-PyEdu-Rs-Raw |
| GitHub API (Annoy-DataSync main HEAD) | P2 live-github | 2026-04-08 | Repo exists; commit 120c992 merged; issue #1 open |
| Annoy-DataSync PR#2 | conflict-resolution artifacts | 2026-04-08T22:06:25Z | 38-row conflict_resolution.csv; 14-field resolved_values.json |
| GitHub search (hkust-nlp/CodeIO) | upstream check | 2026-04-08 | 0 results — repo absent |
| GitHub search (bugmaker00 Annoy*) | companion-repo check | 2026-04-08 | 1 result (Annoy-DataSync only) |

---

## Full Scope — All 4 Candidates

### Candidate 1: `bugmaker00/Annoy-DataSync` — KEEP ✅

| Field | Value | Source | Contest |
|-------|-------|--------|---------|
| project_name | Annoy-DataSync | github_api_live | Unchallenged |
| original_url_from_readme | https://github.com/bugmaker00/Annoy-DataSync | github_api_live | Unchallenged |
| canonical_owner_repo | bugmaker00/Annoy-DataSync | github_api_live | Unchallenged |
| description | null | github_api_live | Unchallenged (owner did not set a description) |
| license | null | github_api_live | Unchallenged (no LICENSE file; open issue #1) |
| repo_exists | true | github_api_live | — |
| existence_blocking | NO | — | — |

**scope_decision: KEEP** — Hub repo fully exists and is accessible.

### Candidate 2: `hkust-nlp/CodeIO` — DROP ❌ (EXISTENCE BLOCKING)

| Field | Value | Source | Contest |
|-------|-------|--------|---------|
| repo_exists | false | github_api_live (search: 0 results) | — |
| existence_blocking | YES | — | — |

**scope_decision: DROP** — The upstream fork source does not exist on GitHub at the  
2026-04-08 snapshot. Repository existence is the blocking prerequisite.  
Re-plan required: either locate the repo at an alternate URL or document the upstream as permanently absent.

Fork relationship confirmed indirectly through Annoy-DataSync PR#2 commit log:
- `abde12e` — first update (lockon-n, 2025-09-07 12:57)
- `08667ae` — update: renamed `codeio_*` → `spec_*`, added namespace placeholders
- `272cfc2f` — minor README tweaks
- `120c992` — namespace resolution by bugmaker00 (2026-04-08)

### Candidate 3: `dongbobo/Annoy-PyEdu-Rs-Raw` — KEEP ✅ (HuggingFace)

| Field | Value | Source | Contest |
|-------|-------|--------|---------|
| project_name | Annoy-PyEdu-Rs-Raw | live_huggingface | Unchallenged |
| original_url_from_readme | https://huggingface.co/datasets/dongbobo/Annoy-PyEdu-Rs-Raw | github_api_live_pr2 | Unchallenged |
| canonical_owner_repo | dongbobo/Annoy-PyEdu-Rs-Raw | live_huggingface | Unchallenged (P1+P2 agree; no casing contest) |
| description | Raw Python educational resource dataset (CodeI/O spec_* format) | live_huggingface | Unchallenged |
| license | null | live_huggingface | Unchallenged (no license set; open issue #1) |
| repo_exists | true (on HuggingFace) | live_huggingface | — |
| existence_blocking | NO | — | — |

**scope_decision: KEEP** — Dataset confirmed on HuggingFace.  
⚠️ **Bootstrap failure**: GitHub mirror `bugmaker00/Annoy-PyEdu-Rs-Raw` does not exist.  
Re-plan required for GitHub presence.

### Candidate 4: `dongbobo/Annoy-PyEdu-Rs` — KEEP ✅ (HuggingFace, canonical contested)

| Field | Value | Source | Contest |
|-------|-------|--------|---------|
| project_name | Annoy-PyEdu-Rs | live_huggingface | Unchallenged |
| original_url_from_readme | https://huggingface.co/datasets/dongbobo/Annoy-PyEdu-Rs | github_api_live_pr2 | Unchallenged |
| canonical_owner_repo | dongbobo/Annoy-PyEdu-Rs | live_huggingface | **Contested** — README 120c992 slug casing inconsistency; HF canonical (PyEdu) wins per P1 |
| description | Processed Python educational resource dataset with explanations (spec_* naming; CodeI/O variant) | live_huggingface | Unchallenged |
| license | null | live_huggingface | Unchallenged (no license set; open issue #1) |
| repo_exists | true (on HuggingFace) | live_huggingface | — |
| existence_blocking | NO | — | — |

**scope_decision: KEEP** — Dataset confirmed on HuggingFace.  
**Canonical contest resolved**: README commit 120c992 has two occurrences of `Annoy-Pyedu-Rs`  
(lowercase) and one header badge `Annoy-PyEdu-Rs` (mixed case). HuggingFace live canonical  
is `PyEdu` casing → resolved as `dongbobo/Annoy-PyEdu-Rs`.  
⚠️ **Bootstrap failure**: GitHub mirror `bugmaker00/Annoy-PyEdu-Rs` does not exist.  
Re-plan required for GitHub presence.

---

## Consistency Check

| Dimension | Count | Source |
|-----------|-------|--------|
| scope_matrix rows | 4 | scope_matrix_single_1.csv |
| total_repos_reviewed | 4 | selected_scope_single_1.json _meta |
| KEEP rows (scope_matrix) | 3 | scope_matrix_single_1.csv |
| selected_scope entries | 3 | selected_scope_single_1.json repos |
| DROP rows (scope_matrix) | 1 | scope_matrix_single_1.csv |
| repos_dropped (meta) | 1 | selected_scope_single_1.json _meta |

✅ All dimensions match: scope_matrix (4 rows) == reviewed (4); KEEP (3) == selected (3); DROP (1) == dropped (1).

---

## Blocking Prerequisite Summary

The **repository existence** check blocks `hkust-nlp/CodeIO` from inclusion.  
All other candidates exist on their stated platforms (GitHub or HuggingFace).

Two **bootstrap failures** are documented (GitHub mirrors absent):  
- `bugmaker00/Annoy-PyEdu-Rs-Raw` → HF dataset exists; GitHub repo does not  
- `bugmaker00/Annoy-PyEdu-Rs` → HF dataset exists; GitHub repo does not  

These are re-plan items that do not cause a DROP decision for the HF-level entries,  
but they do mean the full GitHub-side deployment cannot be applied live until the  
GitHub mirrors are created.

---

## Outstanding Items (Not Resolved)

1. **License** — `null` for all 3 KEEP entries; open issue #1 in `bugmaker00/Annoy-DataSync`  
   requesting license clarification for `Annoy-PyEdu-Rs-Raw` and `Annoy-PyEdu-Rs`.
2. **Paper title/ID** — placeholders remain in README post-120c992:  
   `Annoy: This should be a paper Title` / `xxxx.xxxxx` (PR#2 notes these as outstanding).
3. **GitHub mirrors** — `bugmaker00/Annoy-PyEdu-Rs-Raw` and `bugmaker00/Annoy-PyEdu-Rs`  
   need to be created before the full namespace-resolution change can be applied live on GitHub.
