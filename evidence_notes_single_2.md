# Evidence Notes — Scope Matrix Single-2

**Subproblem:** separating *upstream / template identity* from *destination namespace* when invoking
GitHub fork flows, for the five repositories cited verbatim in the AI-coding-tools playlist descriptions.

| | |
|---|---|
| Review branch | `review/scope-matrix-single-2` (repository root — the established path for this artifact lineage) |
| Full reviewed target set | `scope_matrix_single_2.csv` — **7 data rows × 22 columns** (5 `target` rows + 2 `audited_candidate` rows) |
| Finalized subset | `selected_scope_single_2.json` — **5 entries**, only live-safe values |
| Source priority rule | `github_api_live` > `readme_opening` > `target_set_csv`; `target_set_csv_original_url` never wins canonical routing |
| Policy of record | `review/conflict-resolution:source_priority.md` |
| Reviewed snapshots | 2026-04-08 / 2026-04-09, refreshed 2026-08-09 |
| **Live gate** | **live GitHub REST API, 2026-08-15 (responses observed to ≥ 21:57 UTC), this run** |
| Production branch `main` | untouched |

---

## 0. What each artifact is

The two deliverables are deliberately *not* the same surface.

* **`scope_matrix_single_2.csv` — the full reviewed target set.** One row per reviewed identifier,
  carrying the **reviewed record** (`description`, `license` = the reviewed winners) *plus* the live-gate
  outcome (`description_live_safe`, `license_live_safe`, `fields_live_exact_count`,
  `live_resolved_fields`, `live_gate`). Rows that did **not** make the cut are present with
  `scope_decision = DROP`, and reviewed winners that went stale are still visible here.
* **`selected_scope_single_2.json` — the finalized subset.** Only the 25 `selected=YES` field values,
  and for the two fields whose reviewed winner no longer reproduces, only the **live re-resolved**
  value. No discarded candidate string and no stale reviewed winner is published as a value.

---

## 1. Reconstruction inputs

The reviewed change set is not stored in one place; it was reassembled from artifacts already
committed to this repository and then re-verified live.

| Artifact | Branch | Contribution |
|---|---|---|
| `source_resolution_single_2.csv` (36 rows × 6 cols, 25 `selected=YES`) | `review/source-resolution-single-2` | the per-field candidate matrix and `review_state` / `selected` columns |
| `evidence_notes_single_2.md` | `review/source-resolution-single-2` | the finalized live-safe subset and the live-resolution record |
| `conflict_resolution.csv` (18 contested rows) | `review/conflict-resolution` | contested candidates per repo × field × source |
| `source_priority.md` | `review/conflict-resolution` | three-tier priority policy and per-field winning source |
| `resolved_values.json` (2026-04-09) | `review/conflict-resolution` | machine-readable reviewed choices |
| `target_set.csv` (5 cols) | `review/conflict-resolution` | the playlist-derived `target_set_csv` candidates |
| `target_set.csv` / `target_set.md` (14 cols) | `review/preserve-a-description-listed-repo-even` | membership rules: 5 cited URLs → 5 rows, nothing dropped for being redirected or off-theme |
| `docs/identifier-vs-canonical.md`, `target_set.csv` | `review/separate-identifier-from-canonicalized-identifier-in` | cited-vs-canonical audit, org-rename redirect proof, sibling-repo caution |
| `id_alignment_single_2.csv`, `resolved_mapping_single_2.json` | `review/id-alignment-single-2` | prior scope-annotation schema for this subproblem |

> **Read constraint, stated for the record.** The task-note dump under `/workspace/dumps/workspace/`
> was reachable in this session but empty, so nothing in this document is derived from an unread file.
> Every value below traces either to one of the committed artifacts above or to a live GitHub API
> response obtained in this run.

---

## 2. Scope decisions — all 7 reviewed rows

### 2.1 Target rows (5 / 5 KEEP)

| # | Cited identifier | Canonical identifier | Redirect | Reviewed cands. | Selected | Live-exact | Live-resolved | Decision |
|---|---|---|---|---|---|---|---|---|
| 1 | `openai/codex` | `openai/codex` | no | 7 | 5 | 5 | 0 | **KEEP** |
| 2 | `google-gemini/gemini-cli` | `google-gemini/gemini-cli` | no | 7 | 5 | 5 | 0 | **KEEP** |
| 3 | `QwenLM/Qwen3-Coder` | `QwenLM/Qwen3-Coder` | no | 6 | 5 | 5 | 0 | **KEEP** |
| 4 | `QwenLM/Qwen3-TTS` | `QwenLM/Qwen3-TTS` | no | 7 | 5 | 5 | 0 | **KEEP** |
| 5 | `All-Hands-AI/OpenHands` | `OpenHands/OpenHands` ⚠️ | **yes** | 9 | 5 | 3 | 2 | **KEEP** |
| | | | **totals** | **36** | **25** | **23** | **2** | 5 KEEP |

Nothing is dropped for being redirected (row 5) or off-theme (row 4) — both are explicit membership
rules of this lineage. Repo ids confirmed live: `965415649`, `968197216`, `787368344`, `1138817132`,
`771302083` (owner org id `225919603`).

### 2.2 Audited candidate rows (2 / 2 DROP)

These are identifiers that entered the review and were **excluded**. They are what makes the CSV the
*full* reviewed set rather than a copy of the finalized subset.

* **`All-Hands-AI/OpenHands` — DROP as a canonical target.** Reviewed as a `canonical_owner_repo`
  candidate from tier `target_set_csv_original_url`, `review_state = discarded`. It is *not* a separate
  member of the target set, and it is equally never de-duplicated away: it survives verbatim as the
  cited identifier on row 5. Its one discarded candidate row is already counted inside row 5's nine
  reviewed candidates, so `fields_reviewed_count = 0` here to keep the total at 36.
* **`QwenLM/qwen-code` — DROP as a substitution candidate.** Repo id `1008713177` (created
  2025-06-26, Apache-2.0, *"An open-source AI coding agent that lives in your terminal."*) is a
  **different** repository from `QwenLM/Qwen3-Coder` (repo id `787368344`) and is not a
  canonicalization of it. It is not cited verbatim in any playlist description, so the membership rule
  excludes it. Verified live in this run: two distinct repo ids, two distinct repositories.

---

## 3. Live gate

For each cited identifier the live repository payload was read and compared field-by-field with the
reviewed winner:

```
requested owner/repo == returned full_name   -> identity stable, no redirect
requested owner/repo != returned full_name   -> canonicalized / redirected
reviewed winner == live field value          -> safe to apply live
reviewed winner != live field value          -> stale, must be re-resolved from github_api_live
```

For the one redirected entry the **cited** path was used as the request path. A contents probe on
`All-Hands-AI/OpenHands` returned `200 OK`, while every URL in the response body was rooted at the
renamed namespace:

```
url          https://api.github.com/repos/OpenHands/OpenHands/contents/README.md?ref=main
html_url     https://github.com/OpenHands/OpenHands/blob/main/README.md
download_url https://raw.githubusercontent.com/OpenHands/OpenHands/main/README.md
git_url      https://api.github.com/repos/OpenHands/OpenHands/git/blobs/dca34f6f…
```

Direct live proof that both facts hold at once: the cited path is a still-valid **entry point**, while
the **canonical** identity is `OpenHands/OpenHands`.

### 3.1 Two reviewed winners did not reproduce live

Both belong to `OpenHands/OpenHands`. The priority rule is unchanged — live `github_api_live` is
authoritative — so `selected_scope_single_2.json` publishes the re-resolved value and withholds the
stale one. The stale forms remain visible in `scope_matrix_single_2.csv` as the reviewed record.

| Field | Reviewed winner (2026-04) | Live value (2026-08-15) | Published |
|---|---|---|---|
| `description` | same sentence with the leading `🙌` (U+1F64C) **stripped** — a silent normalisation of the owner-set string | `🙌 OpenHands: AI-Driven Development` | the live form |
| `license` | `Other (NOASSERTION)` — SPDX auto-detection returned no assertion at that snapshot | `MIT` (`license.key = mit`, `spdx_id = MIT`, `name = MIT License`) | `MIT` |

Neither substitution changes a review *decision*: `github_api_live` still beats the `target_set_csv`
paraphrase and the `readme_opening` heading in both cases. `MIT` is published **because the live
authoritative tier says `MIT`**, not because `target_set_csv` happened to claim it too.

### 3.2 Live drift that changes no decision

* The live `OpenHands/OpenHands` `README.md` now opens on the **"Agent Canvas"** product heading, no
  longer "OpenHands: AI-Driven Development". `readme_opening` was already a discarded tier-2 candidate
  for that field, so no finalized value moves. Recorded so a later reviewer is not surprised.
* Stars and releases have moved since the 2026-08-09 target-set refresh (`openai/codex`
  104,938 → 106,116; `google-gemini/gemini-cli` 106,432 → 106,529; `QwenLM/Qwen3-Coder`
  16,776 → 16,788; `QwenLM/Qwen3-TTS` 12,878 → 12,964; `OpenHands/OpenHands` 83,541 → 84,138 with the
  README now referencing `agent-canvas:1.13.0`). Neither `stars` nor `latest_release_tag` is one of the
  five reviewed fields, so they are noted only, never promoted.
* `QwenLM/Qwen3-Coder` still publishes **no** `license` object. `(none detected)` / `null` is reported,
  not back-filled.

---

## 4. Accounting — matrix vs finalized subset

| Dimension | Count | Where |
|---|---|---|
| `scope_matrix` data rows | 7 | `scope_matrix_single_2.csv` |
| ↳ `row_type = target` | 5 | all `scope_decision = KEEP` |
| ↳ `row_type = audited_candidate` | 2 | both `scope_decision = DROP` |
| `selected_scope` entries | 5 | `selected_scope_single_2.json` → `repos` |
| `excluded_from_scope` entries | 2 | `selected_scope_single_2.json` → `excluded_from_scope` |
| Reviewed candidate values | 36 | Σ `fields_reviewed_count` = 7+7+6+7+9+0+0 |
| `selected = YES` values | 25 | Σ `fields_selected_count` = 5 × 5 |
| `selected = NO` values | 11 | 9 discarded description alternatives + 1 legacy routing claim + 1 legacy licence claim |
| Live byte-exact | 23 | Σ `fields_live_exact_count` = 5+5+5+5+3 |
| Live re-resolved | 2 | `OpenHands/OpenHands` → `description`, `license` |
| Values published in the JSON | 25 | 23 byte-exact + 2 re-resolved |
| Discarded candidate strings in the JSON | 0 | — |
| Stale reviewed winners in the JSON | 0 | — |

✅ KEEP rows (5) == `selected_scope` entries (5) == distinct repos with `selected=YES` rows in
`source_resolution_single_2.csv` (5). DROP rows (2) == `excluded_from_scope` entries (2).
Σ `fields_reviewed_count` (36) == data rows of `source_resolution_single_2.csv` (36).

---

## 5. Delivery constraints observed

- Both artifacts are staged on the review branch `review/scope-matrix-single-2`, at the repository
  root — the established path for this artifact lineage.
- The production branch `main` (the published site) is **not** modified, and no published-site path
  (`pages/`, `site_profile.yml`, `.nojekyll`, `publication_*`, `homepage_*`, `memory_*`) is touched.
- **Nothing was applied to any live or upstream repository.** No fork was created, and no description,
  licence or link was written anywhere outside this review branch: the branch only *records* which
  values would be safe to apply.
- Cited identifiers are preserved verbatim; canonical identities are recorded additively, never by
  overwriting the cited path.
- Missing metadata is reported, never invented.
