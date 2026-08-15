# Evidence Notes — Source Resolution (single_2)

**This document is the finalized, live-safe subset — not the review surface.**
`source_resolution_single_2.csv`, committed alongside it, is the *full reviewed target set*:
every candidate value for every field, winners and discards alike. This file is its
complement and carries **only** the finalized values that were re-probed against the live
GitHub REST API in this run and reproduce there — i.e. only what would be safe to apply
live. No discarded candidate string is reproduced here, and nothing that failed the live
gate is published as a value.

| | |
|---|---|
| Subproblem | separating *upstream / template identity* from *destination namespace* for the five repositories cited verbatim in the AI-coding-tools playlist descriptions |
| Review branch | `review/source-resolution-single-2` (repository root — the established path for this artifact lineage) |
| Full review surface | `source_resolution_single_2.csv` — 36 data rows × 6 columns, 25 rows `selected=YES` |
| This document | finalized subset + live-resolved values only |
| Source priority rule (unchanged) | `github_api_live` > `readme_opening` > `target_set_csv`; `target_set_csv_original_url` never wins canonical routing |
| Policy of record | `review/conflict-resolution:source_priority.md` |
| Live gate | GitHub REST API, **2026-08-15 (≥ 15:25 UTC)**, this run |
| Production branch `main` | untouched |

---

## 0. Inputs that were actually readable in this session

The reviewed change set is not stored in one place; it was reassembled from the artifacts
already committed to this repository, then re-verified live.

| Artifact | Branch | Contribution to the reconstruction |
|---|---|---|
| `target_set.csv` (5 cols) | `review/conflict-resolution` | the playlist-derived target set: `Original URL`, `Original Repo`, `Canonical Owner/Repo`, `Project Name`, `Description` → the `target_set_csv` candidates |
| `conflict_resolution.csv` | `review/conflict-resolution` | the 18 contested candidate rows (per repo × field × source) |
| `source_priority.md` | `review/conflict-resolution` | the three-tier priority policy and the per-field winning source |
| `resolved_values.json` | `review/conflict-resolution` | the machine-readable reviewed choices (2026-04-09 snapshot) |
| `target_set.csv` / `target_set.md` (14 cols) | `review/preserve-a-description-listed-repo-even` | membership rules: 5 cited URLs → 5 rows; nothing dropped for being off-theme or redirected |
| `docs/identifier-vs-canonical.md`, `target_set.csv` | `review/separate-identifier-from-canonicalized-identifier-in` | cited-identifier vs canonical-identifier audit and the org-rename redirect proof |

> **Read constraint, stated for the record.** The task-note dump under
> `/workspace/dumps/workspace/` is not reachable from any MCP server exposed in this
> session (no filesystem, shell or browser tool is available), so nothing in this document
> is derived from an unread file. Every value below traces either to one of the committed
> artifacts above or to a live GitHub API response obtained in this run.

---

## 1. Two snapshots are in play

| Snapshot | Taken | Role |
|---|---|---|
| Reviewed change set | 2026-04-08 → 2026-04-09, refreshed 2026-08-09 | produced the `review_state` / `selected` columns of the CSV |
| **Live re-verification** | **2026-08-15, this run** | the gate for “safe to apply live”; nothing enters this document without passing it |

The CSV stays faithful to the **reviewed** record. This document is the *filtered* surface.

### Live re-verification method

For each cited identifier the live repository object was read and compared field-by-field
with the reviewed winner:

```
requested owner/repo  ==  returned full_name   ->  identity stable, no redirect
requested owner/repo  !=  returned full_name   ->  canonicalized / redirected
reviewed winner       ==  live field value     ->  safe to apply live
reviewed winner       !=  live field value     ->  stale, must be re-resolved
```

For the one redirected entry the **cited** path was used as the request path:
`GET /repos/All-Hands-AI/OpenHands/contents/README.md` returned `200 OK`, but every URL in
the response body was rooted at the renamed namespace:

```
url          https://api.github.com/repos/OpenHands/OpenHands/contents/README.md?ref=main
html_url     https://github.com/OpenHands/OpenHands/blob/main/README.md
download_url https://raw.githubusercontent.com/OpenHands/OpenHands/main/README.md
git_url      https://api.github.com/repos/OpenHands/OpenHands/git/blobs/dca34f6f…
```

Direct live proof that both facts hold at once: the cited path is a still-valid **entry
point**, while the **canonical** identity is `OpenHands/OpenHands`.

---

## 2. Finalized values — safe to apply live

Only `selected=YES` rows appear below (25 of 36). “unchallenged” = single candidate, no
conflict; “contested” = the winner of a multi-candidate field.

### 2.1 `openai/codex` — repo id `965415649`, default branch `main`

| Field | Finalized value | Source | State | Live re-verify |
|---|---|---|---|---|
| project_name | Codex CLI | target_set_csv | unchallenged | n/a — editorial label, not an API field |
| original_url_from_playlist | `https://github.com/openai/codex` | target_set_csv | unchallenged | cited path resolves directly, no redirect ✅ |
| canonical_owner_repo | `openai/codex` | github_api_live | unchallenged | `full_name` matches the cited path ✅ |
| description | Lightweight coding agent that runs in your terminal | github_api_live | **contested → winner** | byte-exact ✅ |
| license | Apache-2.0 | github_api_live | unchallenged | `license.spdx_id = Apache-2.0` ✅ |

*Contested field:* `description`. The owner-set API string beats the playlist paraphrase
(which injects install channels) and the README opening (which restates it at greater
length).

### 2.2 `google-gemini/gemini-cli` — repo id `968197216`, default branch `main`

| Field | Finalized value | Source | State | Live re-verify |
|---|---|---|---|---|
| project_name | Gemini CLI | target_set_csv | unchallenged | n/a — editorial label |
| original_url_from_playlist | `https://github.com/google-gemini/gemini-cli` | target_set_csv | unchallenged | cited path resolves directly, no redirect ✅ |
| canonical_owner_repo | `google-gemini/gemini-cli` | github_api_live | unchallenged | `full_name` matches ✅ |
| description | An open-source AI agent that brings the power of Gemini directly into your terminal. | github_api_live | **contested → winner** | byte-exact ✅ |
| license | Apache-2.0 | github_api_live | unchallenged | `license.spdx_id = Apache-2.0` ✅ |

*Contested field:* `description`. The playlist paraphrase embeds quota and context-window
figures that are not part of the owner-set field; rejected.

### 2.3 `QwenLM/Qwen3-Coder` — repo id `787368344`, default branch `main`

| Field | Finalized value | Source | State | Live re-verify |
|---|---|---|---|---|
| project_name | Qwen3-Coder | target_set_csv | unchallenged | n/a — editorial label |
| original_url_from_playlist | `https://github.com/QwenLM/Qwen3-Coder` | target_set_csv | unchallenged | cited path resolves directly, no redirect ✅ |
| canonical_owner_repo | `QwenLM/Qwen3-Coder` | github_api_live | unchallenged | `full_name` matches ✅ |
| description | Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team. | github_api_live | **contested → winner** | byte-exact ✅ |
| license | (none detected) | github_api_live | unchallenged | live payload carries **no** `license` object at all ✅ — reported, not invented |

*Sibling-repo caution (carried forward):* `QwenLM/qwen-code` is a **different** repository
and must never be substituted for `QwenLM/Qwen3-Coder`.

### 2.4 `QwenLM/Qwen3-TTS` — repo id `1138817132`, default branch `main`

| Field | Finalized value | Source | State | Live re-verify |
|---|---|---|---|---|
| project_name | Qwen3-TTS | target_set_csv | unchallenged | n/a — editorial label |
| original_url_from_playlist | `https://github.com/QwenLM/Qwen3-TTS` | target_set_csv | unchallenged | cited path resolves directly, no redirect ✅ |
| canonical_owner_repo | `QwenLM/Qwen3-TTS` | github_api_live | unchallenged | `full_name` matches ✅ |
| description | Qwen3-TTS is an open-source series of TTS models developed by the Qwen team at Alibaba Cloud, supporting stable, expressive, and streaming speech generation, free-form voice design, and vivid voice cloning. | github_api_live | **contested → winner** | byte-exact ✅ |
| license | Apache-2.0 | github_api_live | unchallenged | `license.spdx_id = Apache-2.0` ✅ |

*Retained on purpose:* this is a speech-synthesis project, not a coding agent. It is cited
verbatim in a playlist description, so a theme filter must not drop it.

### 2.5 `OpenHands/OpenHands` — repo id `771302083`, owner org id `225919603`, default branch `main` ⚠️ fork-identity case

The central *upstream-template identity vs. destination namespace* row. The playlist cites
`All-Hands-AI/OpenHands`; the organisation was renamed and the repository now lives at
`OpenHands/OpenHands`. Both facts hold simultaneously — see §1.

| Field | Finalized value | Source | State | Live re-verify |
|---|---|---|---|---|
| project_name | OpenHands | target_set_csv | unchallenged | n/a — editorial label |
| original_url_from_playlist | `https://github.com/All-Hands-AI/OpenHands` | target_set_csv | unchallenged | **preserved verbatim** — never overwritten with the canonical path; live probe of this exact path returns `200 OK` ✅ |
| canonical_owner_repo | `OpenHands/OpenHands` | github_api_live | **contested → winner** | `full_name`, `owner.login` and every response URL rooted here ✅ |
| description | `🙌 OpenHands: AI-Driven Development` | github_api_live | **contested → winner (re-resolved)** | ⚠️ see §3.1 — leading `🙌` (U+1F64C) restored from live |
| license | `MIT` | github_api_live | **contested → winner (re-resolved)** | ⚠️ see §3.2 — reviewed winner was stale |

---

## 3. Live-resolved substitutions

Two reviewed winners did **not** reproduce live. The priority rule is unchanged — the live
`github_api_live` value is authoritative — so the value published in §2.5 is the
re-resolved one, and the stale form is withheld from this document. It remains visible in
`source_resolution_single_2.csv` as the reviewed record.

### 3.1 `OpenHands/OpenHands` → `description`

| | |
|---|---|
| Reviewed winner (2026-04) | the same sentence with the leading `🙌` (U+1F64C) **stripped** — a silent normalisation of the owner-set string; withheld here |
| Live owner-set value (2026-08-15) | `🙌 OpenHands: AI-Driven Development` |
| **Resolved / live-safe** | `🙌 OpenHands: AI-Driven Development` |

Applying the reviewed form live would rewrite the owner's own description, so the
byte-exact live form is published instead. Substance is unchanged, so the review *decision*
(`github_api_live` beats the playlist paraphrase and the README heading) still stands —
only the string was refreshed.

### 3.2 `OpenHands/OpenHands` → `license`

| | |
|---|---|
| Reviewed winner (2026-04) | `Other (NOASSERTION)` — GitHub SPDX auto-detection returned no assertion at that snapshot; **not safe to apply live**, withheld |
| Live SPDX value (2026-08-15) | `MIT` (`license.key = mit`, `license.spdx_id = MIT`, `license.name = MIT License`) |
| **Resolved / live-safe** | `MIT` |

This is licence-*detection* drift, not a policy change: GitHub's detector now recognises
the repository's licence file. The playlist-derived `target_set_csv` happened to claim
`MIT` too, but `MIT` is published here **because live `github_api_live` says `MIT`** — the
tier order is untouched, only the snapshot moved.

---

## 4. Deliberately excluded from this document

| Excluded | Count | Why |
|---|---|---|
| `selected=NO` candidate values (playlist paraphrases, README openings, the legacy routing claim) | 11 | discarded in review; reproducing them here would blur the “finalized subset” contract. They stay in `source_resolution_single_2.csv`. |
| The two stale reviewed winners (§3) | 2 | they do not reproduce live, so they are not safe to apply |
| Any invented value for a field GitHub does not publish | 0 | `QwenLM/Qwen3-Coder` has no licence object; `(none detected)` is reported rather than back-filled |
| Any rewrite of a cited identifier | 0 | cited paths are preserved verbatim; canonical identities are additive |

### Known live drift that changes no decision

- The live `OpenHands/OpenHands` `README.md` now opens on the **“Agent Canvas”** product
  heading, no longer “OpenHands: AI-Driven Development”. `readme_opening` was already a
  discarded tier-2 candidate for that field, so no finalized value moves. Recorded so a
  later reviewer is not surprised.
- `OpenHands/OpenHands` latest release is now `v1.13.0` (published 2026-08-13), up from
  `v1.12.0` in the 2026-08-09 target set. `latest_release_tag` is not one of the five
  reviewed fields, so it is noted only, not promoted.

---

## 5. Accounting — CSV vs. this document

| Repo | `selected=YES` rows in CSV | Finalized rows here | Live byte-exact | Live-resolved (§3) |
|---|---|---|---|---|
| `openai/codex` | 5 | 5 | 5 | 0 |
| `google-gemini/gemini-cli` | 5 | 5 | 5 | 0 |
| `QwenLM/Qwen3-Coder` | 5 | 5 | 5 | 0 |
| `QwenLM/Qwen3-TTS` | 5 | 5 | 5 | 0 |
| `OpenHands/OpenHands` | 5 | 5 | 3 | 2 |
| **Total** | **25** | **25** | **23** | **2** |

CSV row accounting: **36 data rows** = **18 contested** candidate rows (one-for-one with
`review/conflict-resolution:conflict_resolution.csv`) + **18 unchallenged**
single-candidate rows. `selected=YES` = 25 = 5 fields × 5 repos. `selected=NO` = 11 = 9
discarded description alternatives + 1 discarded legacy routing claim + 1 discarded licence
claim.

Identifier accounting: 5 cited URLs → 5 repos, nothing dropped, nothing added; 1 of 5
cited identifiers is canonicalized (`All-Hands-AI/OpenHands` → `OpenHands/OpenHands`), the
other 4 resolve as cited.

---

## 6. Delivery constraints observed

- Both artifacts are staged on the review branch `review/source-resolution-single-2`, at
  the repository root — the established path for this artifact lineage.
- The production branch `main` (the published site) is **not** modified, and no
  published-site path (`pages/`, `site_profile.yml`, `.nojekyll`, `publication_*`,
  `homepage_*`, `memory_*`) is touched.
- **Nothing was applied to any live or upstream repository.** No fork was created, no
  description, licence or link was written anywhere outside this review branch: the branch
  only *records* which values would be safe to apply.
- Cited identifiers are preserved verbatim; canonical identities are recorded additively,
  never by overwriting the cited path.
- Missing metadata is reported, never invented.
