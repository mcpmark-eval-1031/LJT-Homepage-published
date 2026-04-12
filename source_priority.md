# Source Priority Rule

## Repository

`mcpmark-eval-1031/LUFFY` — review branch staging for reviewed change set between `dev` and `main`

## Sources Consulted (ranked highest → lowest authority)

| Rank | Source ID | Description |
|------|-----------|-------------|
| 1 | `main-branch-readme` | `README.md` on the `main` branch — the latest committed, maintainer-approved state of the project documentation |
| 2 | `main-csv-message-plan` | `message_plan.csv` on `main` — structured CSV of the full eligible set; explicit column values override prose descriptions |
| 3 | `main-csv-pilot-cohort` | `pilot_cohort.csv` on `main` — committed structured data for the acted-on subset; corroborates message_plan values |
| 4 | `dev-csv-reconciliation` | `path_reconciliation.csv` on `dev` — authoritative mapping of actual file locations (source_path → intended_destination) |
| 5 | `dev-csv-ledger` | `target_ledger.csv` on `dev` — raw TODO inventory derived from scanning source files; authoritative for line-level facts |
| 6 | `main-audit-doc` | `mail_consistency_audit.md` on `main` — derived/summary document; lower authority than structured CSVs |
| 7 | `dev-branch-readme` | `README.md` on `dev` — pre-merge working draft; superseded by the `main` branch version where they differ |
| 8 | `dev-action-preview` | `action_preview.md` on `dev` — planning artifact; describes intended but not yet committed changes |

## Decision Rules Applied

1. **Path format in README.md** (`readme_module_a_path`, `readme_module_b_path`, `readme_todo_path_separator`): The `main` branch README is chosen as the authoritative snapshot because it represents the latest maintainer-committed state (commit `fbe7a13` normalized paths to `src/nebula/` prefix with colon separator). The `dev` branch README and action previews describe an earlier intended format that was superseded.

2. **README TODO section title and format** (`readme_todo_section_title`, `readme_todo_format`): Same rule — `main` branch wins over `dev` branch draft. The `main` branch uses the GitHub-style `- [ ]` checklist format under the heading "Current TODO Items."

3. **Canonical file location** (`module_a_canonical_location`): `dev` path_reconciliation.csv is chosen because it documents the *actual* filesystem layout (files are at repo root). The `main` README's `src/nebula/` prefix is a forward-looking monorepo path reference, not the current physical location.

4. **COLM2026 paper title** (`COLM2026_paper_title`): Both `message_plan.csv` and `pilot_cohort.csv` on `main` agree on "(Title not specified in acceptance email)." The `mail_consistency_audit.md` paraphrase "(title to be confirmed)" is a derived summary; the explicit CSV column value is authoritative.

5. **COMLW2026 deadline status** (`COMLW2026_deadline_status`): The `message_plan.csv` `status` column value "OVERDUE" is a single-token structured label — preferred over embedded inline annotations in the deadline field or free-text rationale prose.
