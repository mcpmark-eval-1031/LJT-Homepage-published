# Evidence Notes — Source Resolution Single-2

**Subproblem:** Upstream template identity from destination namespace when invoking
GitHub fork flows (AI coding tools playlist, 5 repos).  
**Review branch:** `review/source-resolution-single-2-reconstructed`  
**Baseline reconstructed:** `review/source-resolution-single-2` @ `efc9f33e` (2026-04-08)  
**Companion surface:** `source_resolution_single_2.csv` (34 rows — 25 selected + 9 non-selected)  
**Original snapshot date:** 2026-04-08 · **Live re-verification:** 2026-08-09  
**Source priority rule:** `github_api_live` > `readme_opening` > `target_set_csv`  
*(Policy documented in `review/conflict-resolution:source_priority.md`)*

---

## Scope of This Document

This file is the **live-safe subset** of the review surface. It reproduces **only**
the rows carrying `selected = YES` in `source_resolution_single_2.csv` — i.e. the
values that may be applied to a live surface without further adjudication.

Non-selected candidates (9 rows) are deliberately **not restated here**; they remain
only on the full review surface, referenced by `(repo, field, source)` counts in the
Consistency Check below. Unchallenged fields (single candidate, no conflict) are
listed without rationale; contested fields are annotated with the winning rationale.

---

## Finalized Values — Safe to Apply Live

### 1. `openai/codex`  *(repo ID 965415649 — live-confirmed)*

| Field | Finalized Value | Source | Note |
|---|---|---|---|
| project_name | Codex CLI | target_set_csv | Unchallenged |
| original_url_from_playlist | https://github.com/openai/codex | target_set_csv | Unchallenged; no redirect |
| canonical_owner_repo | openai/codex | github_api_live | Unchallenged; direct resolution |
| description | Lightweight coding agent that runs in your terminal | github_api_live | **Contested** — wins over the target_set_csv paraphrase (adds install details not present in the owner-set API field) and over readme_opening (longer restatement, agrees in substance) |
| license | Apache-2.0 | github_api_live | Unchallenged; SPDX `Apache-2.0` re-confirmed 2026-08-09 |

### 2. `google-gemini/gemini-cli`  *(repo ID 968197216 — live-confirmed)*

| Field | Finalized Value | Source | Note |
|---|---|---|---|
| project_name | Gemini CLI | target_set_csv | Unchallenged |
| original_url_from_playlist | https://github.com/google-gemini/gemini-cli | target_set_csv | Unchallenged; no redirect |
| canonical_owner_repo | google-gemini/gemini-cli | github_api_live | Unchallenged; direct resolution |
| description | An open-source AI agent that brings the power of Gemini directly into your terminal. | github_api_live | **Contested** — wins over the target_set_csv variant (embeds a "60 req/min" rate-limit and context-window detail absent from the owner-set field) and over readme_opening |
| license | Apache-2.0 | github_api_live | Unchallenged; SPDX `Apache-2.0` re-confirmed 2026-08-09 |

### 3. `QwenLM/Qwen3-Coder`  *(repo ID 787368344 — live-confirmed)*

| Field | Finalized Value | Source | Note |
|---|---|---|---|
| project_name | Qwen3-Coder | target_set_csv | Unchallenged |
| original_url_from_playlist | https://github.com/QwenLM/Qwen3-Coder | target_set_csv | Unchallenged; no redirect |
| canonical_owner_repo | QwenLM/Qwen3-Coder | github_api_live | Unchallenged; direct resolution |
| description | Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team. | github_api_live | **Contested** — wins over the target_set_csv editorial summary (incorporates README feature tables: 256K context, 358 languages, size variants) |
| license | (none detected) | github_api_live | Unchallenged; GitHub returns **no** `license` object for this repo — null at 2026-04-08 and still null at 2026-08-09. Do **not** substitute a README-inferred license. |

### 4. `QwenLM/Qwen3-TTS`  *(repo ID 1138817132 — live-confirmed)*

| Field | Finalized Value | Source | Note |
|---|---|---|---|
| project_name | Qwen3-TTS | target_set_csv | Unchallenged |
| original_url_from_playlist | https://github.com/QwenLM/Qwen3-TTS | target_set_csv | Unchallenged; no redirect |
| canonical_owner_repo | QwenLM/Qwen3-TTS | github_api_live | Unchallenged; direct resolution |
| description | Qwen3-TTS is an open-source series of TTS models developed by the Qwen team at Alibaba Cloud, supporting stable, expressive, and streaming speech generation, free-form voice design, and vivid voice cloning. | github_api_live | **Contested** — wins over the target_set_csv capability summary (truncates to highlights only) |
| license | Apache-2.0 | github_api_live | Unchallenged; SPDX `Apache-2.0` re-confirmed 2026-08-09 |

### 5. `OpenHands/OpenHands` ⚠️ Fork-Identity Resolution  *(repo ID 771302083 — live-confirmed)*

The playlist listed this repository as `All-Hands-AI/OpenHands`. The GitHub
organization was **renamed** `All-Hands-AI` → `OpenHands`, and GitHub transparently
redirects API and web requests for the old path to the canonical path
`OpenHands/OpenHands`. This is the central *upstream-template-identity* case for the
subproblem: the destination namespace in the playlist is **not** the canonical
upstream identity, yet it must still be preserved verbatim as the source-listed
identifier.

| Field | Finalized Value | Source | Note |
|---|---|---|---|
| project_name | OpenHands | target_set_csv | Unchallenged |
| original_url_from_playlist | https://github.com/All-Hands-AI/OpenHands | target_set_csv | **Preserved verbatim** — the source-listed identifier *before* redirect; never rewritten to the canonical path |
| canonical_owner_repo | OpenHands/OpenHands | github_api_live | **Contested** — API resolves the canonical path (repo ID 771302083); `All-Hands-AI/OpenHands` is the pre-rename destination namespace and is retained only in `original_url_from_playlist`. Redirect re-confirmed active 2026-08-09. |
| description | 🙌 OpenHands: AI-Driven Development | github_api_live | **Contested** — wins over the target_set_csv variant (embeds an unverified SWE-Bench score and a redirect note). Value **refreshed on the live pass**: the owner-set API string carries a leading 🙌 emoji; apply the emoji form. |
| license | MIT | github_api_live | **Contested** — resolved on the live pass. GitHub SPDX detection now returns `MIT` for the repository `LICENSE` blob (it returned `NOASSERTION` at the 2026-04-08 snapshot). `github_api_live` remains the selected authority. |

---

## Live Re-Verification Delta (2026-04-08 → 2026-08-09)

| Repo | Field | Baseline value (`efc9f33e`) | Live value (2026-08-09) | Action |
|---|---|---|---|---|
| openai/codex | all 5 fields | — | identical | Re-confirmed, no change |
| google-gemini/gemini-cli | all 5 fields | — | identical | Re-confirmed, no change |
| QwenLM/Qwen3-Coder | all 5 fields | — | identical (license still null) | Re-confirmed, no change |
| QwenLM/Qwen3-TTS | all 5 fields | — | identical | Re-confirmed, no change |
| OpenHands/OpenHands | description | `OpenHands: AI-Driven Development` | `🙌 OpenHands: AI-Driven Development` | **Refreshed** to the owner-set string |
| OpenHands/OpenHands | license | `Other (NOASSERTION)` | `MIT` | **Refreshed**; SPDX detection now resolves the LICENSE blob |
| OpenHands/OpenHands | canonical redirect | active | active | Re-confirmed (`All-Hands-AI/OpenHands` → `OpenHands/OpenHands`) |

**Effect on the review surface:** none structurally. The `(repo, field, source)`
triples and the winner/discarded assignment are unchanged; only two candidate
*values* were refreshed in place, so the surface remains **34 rows / 25 selected**.

**Note on the retired `license` conflict.** The `target_set_csv` license candidate
for `OpenHands/OpenHands` (`MIT`) is no longer in *value* conflict with live GitHub.
Its row stays `selected = NO` because `github_api_live` is the selected authority for
the field under the priority policy — one selected row per `(repo, field)` — not
because the value is now wrong.

---

## Consistency Check

| Repo | Finalized rows (this doc) | selected=YES rows (CSV) |
|---|---|---|
| openai/codex | 5 | 5 |
| google-gemini/gemini-cli | 5 | 5 |
| QwenLM/Qwen3-Coder | 5 | 5 |
| QwenLM/Qwen3-TTS | 5 | 5 |
| OpenHands/OpenHands | 5 | 5 |
| **Total** | **25** | **25** |

**Non-selected rows withheld from this document (9):**

| Repo | Field | Non-selected sources |
|---|---|---|
| openai/codex | description | target_set_csv, readme_opening |
| google-gemini/gemini-cli | description | target_set_csv, readme_opening |
| QwenLM/Qwen3-Coder | description | target_set_csv |
| QwenLM/Qwen3-TTS | description | target_set_csv |
| OpenHands/OpenHands | canonical_owner_repo | target_set_csv_original_url |
| OpenHands/OpenHands | description | target_set_csv |
| OpenHands/OpenHands | license | target_set_csv |

**Grand total CSV rows:** 34 (25 selected + 9 non-selected)

---

## Evidence Trail

| Artifact | Branch | Commit | Purpose |
|---|---|---|---|
| `target_set.csv` / `target_set.md` | `review/preserve-a-description-listed-repo-even` | `862c2730` | Original reconstructed playlist targets (5 repos) |
| `docs/identifier-vs-canonical.md` | `review/separate-identifier-from-canonicalized-identifier-in` | `084d3e91` | Org-rename redirect audit (All-Hands-AI → OpenHands) |
| `conflict_resolution.csv` | `review/conflict-resolution` | `f822ac68` | Per-field candidate matrix (18 contested candidate rows) |
| `source_priority.md` | `review/conflict-resolution` | `dacc25f6` | Three-tier priority policy |
| `resolved_values.json` | `review/conflict-resolution` | `6dccb745` | Machine-readable final choices (2026-04-09) |
| `source_resolution_single_2.csv` | `review/source-resolution-single-2` | `efc9f33e` | Baseline 34-row review surface (2026-04-08) |
| `scope_matrix_single_2.csv` / `selected_scope_single_2.json` | `review/scope-matrix-single-2` | `eacf2abd` | Downstream scope review (5 KEEP / 0 DROP) |
| `id_alignment_single_2.csv` / `resolved_mapping_single_2.json` | `review/id-alignment-single-2` | `c3f53ce5` | Downstream identity alignment; first recorded the owner-set emoji description |
| `source_resolution_single_2.csv` | `review/source-resolution-single-2-reconstructed` | *(this commit)* | Reconstructed full review surface, live-verified 2026-08-09 |
| `evidence_notes_single_2.md` | `review/source-resolution-single-2-reconstructed` | *(this commit)* | Finalized live-safe values — 25 selected rows (this document) |

### Apply-Live Guardrails

1. **Never** rewrite `original_url_from_playlist` to the canonical path — the
   pre-rename identifier is itself a reviewed value.
2. **Never** backfill `QwenLM/Qwen3-Coder.license`; GitHub reports no license object
   and `(none detected)` is the reviewed value.
3. `OpenHands/OpenHands.description` must be applied **with** the leading 🙌 emoji;
   stripping it reintroduces the superseded 2026-04-08 value.
4. `OpenHands/OpenHands.license` is `MIT` **as of the live pass only**; SPDX detection
   has flipped once already (NOASSERTION → MIT), so re-verify before any future apply.
5. Descriptions are owner-set API strings; do not merge in README or playlist prose.
