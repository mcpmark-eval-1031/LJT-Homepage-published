# Contract Checklist — `finalpool-youtube-repo-7` Render Preview

> **Preview branch:** `review/finalpool-youtube-repo-7-contract`  
> **Contract version:** 1.0  
> **Date:** 2026-04-12

This checklist confirms that `render_preview.json` conforms to every rule declared in `render_contract.md`.

---

## A. File-Set Artifact Scope

| # | Rule | Preview Status | Evidence |
|---|------|----------------|----------|
| A.1 | Exactly two files in repo root: `full_scope.csv` and `readback_audit.md` | ✅ PASS | `files` array length == 2; filenames match exactly. |
| A.2 | No extra files in change set | ✅ PASS | Only the two filenames are listed. |
| A.3 | Filenames are case-sensitive | ✅ PASS | Filenames appear in exact casing. |

---

## B. `full_scope.csv` Field Specification

| # | Rule | Preview Status | Evidence |
|---|------|----------------|----------|
| B.1 | Header row contains exactly 14 fields | ✅ PASS | `header` array length == 14. |
| B.2 | Field order is exact (see contract §2.2) | ✅ PASS | Array order: `record_id`, `conference`, `paper_title`, `author_email`, `publication_contact`, `primary_action`, `camera_ready_deadline`, `registration_deadline`, `status`, `priority`, `in_pilot`, `live_action_applied`, `review_verdict`, `source_sha`. |
| B.3 | Exactly 4 data rows | ✅ PASS | `row_count` == 4; `rows` array length == 4. |
| B.4 | No empty cells (use `N/A` for missing) | ✅ PASS | Every JSON object has all 14 keys populated; `N/A` used where applicable. |
| B.5 | `record_id` matches `^[A-Z]+[0-9]{4}$` | ✅ PASS | Values: `COML2026`, `COAI2026`, `COLM2026`, `COMLW2026`. |
| B.6 | `conference` is title-cased, quoted in source CSV | ✅ PASS | Preview values are title-cased with year and type in parentheses. |
| B.7 | `paper_title` uses placeholder when unknown | ✅ PASS | `COLM2026` row contains exactly `(Title not specified in acceptance email)`. |
| B.8 | Email fields are lowercase, no spaces | ✅ PASS | `author_email` and `publication_contact` values conform. |
| B.9 | `status` is uppercase enum | ✅ PASS | Values: `PENDING`, `OVERDUE`. |
| B.10 | `priority` is uppercase enum | ✅ PASS | Values: `HIGH`, `CRITICAL`. |
| B.11 | Booleans are lowercase `true`/`false` | ✅ PASS | `in_pilot` and `live_action_applied` values are `true` or `false`. |
| B.12 | `review_verdict` is lowercase snake_case | ✅ PASS | Values: `deferred`, `pilot_applied`. |
| B.13 | `source_sha` is 40-char lowercase hex | ✅ PASS | All SHA strings are 40 chars and `[0-9a-f]`. |

---

## C. Ordering Constraints

| # | Rule | Preview Status | Evidence |
|---|------|----------------|----------|
| C.1 | Rows sorted ascending by `record_id` | ✅ PASS | `ordering_checks.sorted_by_record_id` == `true`. Sequence: `COAI2026` < `COLM2026` < `COML2026` < `COMLW2026` (lexicographic). |
| C.2 | `record_id` values are unique | ✅ PASS | `ordering_checks.unique_record_ids` == `true`. |
| C.3 | Exactly 2 pilot rows and 2 deferred rows | ✅ PASS | `ordering_checks.pilot_cohort_count` == 2; `ordering_checks.deferred_count` == 2. |
| C.4 | Cohort consistency: `in_pilot`, `live_action_applied`, `review_verdict` align | ✅ PASS | `cohort_consistency.in_pilot_matches_live_action_applied` == `true`; `cohort_consistency.in_pilot_matches_review_verdict` == `true`. |

---

## D. `readback_audit.md` Structural Constraints

| # | Rule | Preview Status | Evidence |
|---|------|----------------|----------|
| D.1 | All 6 required sections are present | ✅ PASS | `required_sections_present` lists all 6 sections. |
| D.2 | Row counts quoted correctly (4 total, 2 pilot, 2 deferred) | ✅ PASS | `row_counts_quoted.total_scope` == 4, `pilot_cohort` == 2, `deferred` == 2. |
| D.3 | Overall verdict is `PASS` | ✅ PASS | `overall_verdict` == `PASS`. |

---

## E. Cross-File Consistency

| # | Rule | Preview Status | Evidence |
|---|------|----------------|----------|
| E.1 | `record_id` values match between CSV and audit | ✅ PASS | `cross_file_consistency.record_ids_match` == `true`. |
| E.2 | `source_sha` references match | ✅ PASS | `cross_file_consistency.source_sha_references_match` == `true`. |
| E.3 | No contradictions | ✅ PASS | `cross_file_consistency.no_contradictions` == `true`. |

---

## Final Verdict

**✅ ALL CHECKS PASS** — `render_preview.json` is a contract-conforming preview of the `finalpool-youtube-repo-7` reviewed change set.
