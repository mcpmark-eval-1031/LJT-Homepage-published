# Render Contract — `finalpool-youtube-repo-7` Reviewed Change Set

> **Version:** 1.0  
> **Artifact:** `finalpool-youtube-repo-7` camera-ready email triage & pilot cohort review  
> **Branch:** `review/finalpool-youtube-repo-7-contract`  
> **Generated:** 2026-04-12 UTC (reconstructed)

---

## 1. File-Set Artifact Scope

The final file-set artifact for this reviewed change set consists of **exactly two files** located in the repository root:

| # | Filename | Role | Encoding |
|---|----------|------|----------|
| 1 | `full_scope.csv` | Canonical structured data (source of truth) | UTF-8, no BOM, LF line endings |
| 2 | `readback_audit.md` | Human-readable audit report | UTF-8, no BOM, LF line endings |

**Constraints:**
- No additional files may be added to the reviewed change set.
- Filenames are case-sensitive and must match exactly.
- Both files must be present in the same directory (repository root).

---

## 2. `full_scope.csv` — Field Specification

### 2.1 Structure

- **Format:** RFC 4180-compliant CSV.
- **Header:** Exactly one header row. Fields are separated by commas (`,`).
- **Quoting:** Fields containing commas, double quotes, or line breaks must be enclosed in double quotes (`"`). Embedded double quotes are escaped by doubling (`""`).
- **Rows:** Exactly **4 data rows** (plus the header row = 5 total lines).
- **Line endings:** Unix-style LF (`\n`). No trailing blank lines.

### 2.2 Field Order (Exact)

The header row must contain the following 14 fields in this exact order:

1. `record_id`
2. `conference`
3. `paper_title`
4. `author_email`
5. `publication_contact`
6. `primary_action`
7. `camera_ready_deadline`
8. `registration_deadline`
9. `status`
10. `priority`
11. `in_pilot`
12. `live_action_applied`
13. `review_verdict`
14. `source_sha`

### 2.3 Empty-Value Policy

- **No cell may be truly empty** (zero-length between delimiters is prohibited).
- Missing or not-applicable values must be represented by the literal string `N/A` (uppercase, no spaces).
- Boolean fields must never be empty; they must be exactly `true` or `false` (lowercase).
- `source_sha` must be a non-empty 40-character lowercase hexadecimal string.

### 2.4 Normalization Rules

| Field | Normalization Rule |
|-------|-------------------|
| `record_id` | Uppercase alphanumeric, no spaces. Pattern: `^[A-Z]+[0-9]{4}$`. Example: `COML2026`. |
| `conference` | Title-cased descriptive string with year and conference type in parentheses. Must be double-quoted in CSV because it contains commas. |
| `paper_title` | Free-form string, double-quoted in CSV. If the title is unknown, use exactly `(Title not specified in acceptance email)`. |
| `author_email` | Valid email format, lowercase, no spaces, not quoted. |
| `publication_contact` | Valid email format, lowercase, no spaces, not quoted. |
| `primary_action` | Sentence-case descriptive string. Must be double-quoted in CSV because it contains commas. |
| `camera_ready_deadline` | `YYYY-MM-DD` or `YYYY-MM-DD (QUALIFIER)`. If a qualifier is present, the field must be double-quoted. Qualifier text is preserved as-is (case-sensitive). |
| `registration_deadline` | Same as `camera_ready_deadline`, or the literal `N/A`. |
| `status` | Uppercase enum. Allowed values: `PENDING`, `OVERDUE`. (Extensible set; values must be uppercase.) |
| `priority` | Uppercase enum. Allowed values: `HIGH`, `CRITICAL`. |
| `in_pilot` | Lowercase boolean. Allowed values: `true`, `false`. |
| `live_action_applied` | Lowercase boolean. Allowed values: `true`, `false`. |
| `review_verdict` | Lowercase snake_case enum. Allowed values: `deferred`, `pilot_applied`. |
| `source_sha` | 40-character lowercase hexadecimal SHA-1 string. Example: `5f47a60c1b13c5293d92427fa5fb858c038b0823`. |

### 2.5 Ordering Constraints

- **Row order:** Data rows must be sorted in **strict ascending lexicographic order** by `record_id`.
- **Uniqueness:** `record_id` values must be unique across all rows.
- **Cohort consistency:** The set of rows where `in_pilot == "true"` must be exactly the same set where `live_action_applied == "true"` and `review_verdict == "pilot_applied"`. No row may have a partial match (e.g., `in_pilot=true` with `review_verdict=deferred`).
- **Cardinality:** Exactly 2 rows must have `in_pilot=true` (pilot cohort), and exactly 2 rows must have `in_pilot=false` (deferred).

---

## 3. `readback_audit.md` — Structural Constraints

- **Format:** GitHub-flavored Markdown.
- **Line endings:** Unix-style LF (`\n`).
- **Required sections:** The document must contain, at minimum, the following top-level sections (identified by `##` headings):
  1. `Repository Identification`
  2. ``Full Scope Verification (`full_scope.csv`)``
  3. `Live State Readback`
  4. `Pilot Cohort Workflow — Applied Actions`
  5. `Cross-Validation Summary`
  6. `Deferred Actions (Non-Pilot, Full-Rollout Candidates)`
- **Data fidelity:** All `record_id`, `priority`, `in_pilot`, and `review_verdict` values mentioned in the audit tables must match the corresponding values in `full_scope.csv` exactly.
- **Counts:** The audit must state that the total scope is 4 rows, pilot cohort is 2 rows, and deferred is 2 rows.

---

## 4. Cross-File Consistency

- `readback_audit.md` must reference the same `record_id` values present in `full_scope.csv`.
- The `source_sha` values in `full_scope.csv` must correspond to the SHAs listed in the `Live State Readback` table of `readback_audit.md`.
- No contradictions may exist between the CSV data and the audit narrative.
