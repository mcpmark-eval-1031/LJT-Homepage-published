# Source Priority Policy — `finalpool-youtube-repo-7`

## Authoritative Source Order

For every field in the reviewed change set (`full_scope.csv` and `readback_audit.md`)
that can be derived from more than one source, snapshot, or label interpretation,
the following precedence rule applies (highest → lowest):

| Priority | Source ID | Description |
|----------|-----------|-------------|
| 1 | `pr_branch_file` | The actual file content on the review branch `review/finalpool-youtube-repo-7` (commit `e0880e9f...`). This is the reviewed and staged artifact; it reflects the final intent of the review. |
| 2 | `main_source_file` | The ground-truth source files on `main` (`message_plan.csv`, `pilot_cohort.csv`, `mail_consistency_audit.md`). These provide the canonical upstream data from which the review set is derived. |
| 3 | `pr_description` | The PR #4 description body and tables (`task notes`). These are human-readable summaries that may abbreviate, paraphrase, or omit detail for brevity. |
| 4 | `readback_audit_summary` | Inline summary tables inside `readback_audit.md` (e.g., the condensed "Full Scope Verification" table). These are secondary renderings of the primary data and may truncate values. |

## Rationale

`pr_branch_file` wins because it is the committed, reviewed artifact. When the reviewer
intentionally simplified a value (e.g., reducing the registration deadline note from
"N/A (already registered — upgrade needed)" to "N/A"), that simplification is part
of the approved change set.

`main_source_file` is the next authority. It is used when the PR branch file is
absent or when a derived field (like `source_sha`) could legitimately point to
more than one upstream file. In those cases we select the source that most
specifically describes the record's action state (`pilot_cohort.csv` for pilot
records, `message_plan.csv` for deferred records).

`pr_description` and `readback_audit_summary` are treated as presentation-layer
artifacts. They are allowed to use ellipsis ("…"), omit parenthetical qualifiers,
or rephrase actions, but they do not override the canonical field values in the
committed CSV.

## Snapshot Provenance

- **pr_branch_file** captured: 2026-04-12 (PR #4 head `e0880e9f...`)
- **main_source_file** captured: 2026-04-12 (main branch HEAD `47d693ad...`)
- **pr_description** captured: 2026-04-12 (PR #4 body)
- **Policy committed on**: `review/finalpool-youtube-repo-7-resolved`
