# Evidence Notes — Source Resolution (single_2)

**Subproblem.** Separating *upstream / template identity* from *destination
namespace* when a GitHub fork flow is invoked against the repositories cited in
the AI-coding-tools playlist descriptions (5 repos).

| | |
|---|---|
| Review branch | `review/source-resolution-single-2` |
| Full review surface | `source_resolution_single_2.csv` — 36 candidate rows × 6 columns, 25 rows `selected=YES` |
| This document | **only** the finalized subset / resolved values that re-verify against live GitHub and are therefore safe to apply live |
| Source priority rule | `github_api_live` > `readme_opening` > `target_set_csv` (`target_set_csv_original_url` never wins routing) |
| Policy of record | `review/conflict-resolution:source_priority.md` |

### Two snapshots are in play

| Snapshot | Taken | Role |
|---|---|---|
| Reviewed change set | 2026-04-08 → 2026-04-09 | produced the `review_state` / `selected` columns in the CSV |
| **Live re-verification** | **2026-08-15 (this run)** | the gate for “safe to apply live” — nothing enters this document without it |

The CSV is deliberately faithful to the **reviewed** target set: it keeps every
candidate, including discarded ones and including a winner that has since gone
stale. This document is the opposite — it is the *filtered* surface and carries
only values that a live apply would reproduce.

---

## 1. Live re-verification method

For each cited identifier the live repository object was read and compared
field-by-field with the reviewed winner:

```
requested owner/repo  ==  returned full_name   ->  identity stable, no redirect
requested owner/repo  !=  returned full_name   ->  canonicalized / redirected
reviewed winner       ==  live field value     ->  safe to apply live
reviewed winner       !=  live field value     ->  stale, must be re-resolved
```

Fork-identity probe for the one redirected entry: the **cited** path
`All-Hands-AI/OpenHands` was used to read `README.md`. GitHub answered `200 OK`
but every URL in the response body (`url`, `html_url`, `download_url`,
`git_url`) was rooted at `OpenHands/OpenHands` — direct live proof that the
cited path is a still-valid *entry point* whose *canonical* identity is the
renamed namespace.

---

## 2. Finalized values — safe to apply live

Only `selected=YES` rows appear below. “Unchallenged” = single candidate, no
conflict. Live column records the outcome of §1.

### 2.1 `openai/codex` — repo id `965415649`

| Field | Finalized value | Source | Live re-verify |
|---|---|---|---|
| project_name | Codex CLI | target_set_csv | n/a — editorial label, not an API field |
| original_url_from_playlist | `https://github.com/openai/codex` | target_set_csv | resolves directly, no redirect |
| canonical_owner_repo | `openai/codex` | github_api_live | `full_name` matches ✅ |
| description | Lightweight coding agent that runs in your terminal | github_api_live | byte-exact ✅ |
| license | Apache-2.0 | github_api_live | `license.spdx_id = Apache-2.0` ✅ |

*Contested field:* `description`. The owner-set API string wins over the
playlist paraphrase (which injects install channels) and over the README
opening (which restates it at greater length).

### 2.2 `google-gemini/gemini-cli` — repo id `968197216`

| Field | Finalized value | Source | Live re-verify |
|---|---|---|---|
| project_name | Gemini CLI | target_set_csv | n/a — editorial label |
| original_url_from_playlist | `https://github.com/google-gemini/gemini-cli` | target_set_csv | resolves directly, no redirect |
| canonical_owner_repo | `google-gemini/gemini-cli` | github_api_live | `full_name` matches ✅ |
| description | An open-source AI agent that brings the power of Gemini directly into your terminal. | github_api_live | byte-exact ✅ |
| license | Apache-2.0 | github_api_live | `license.spdx_id = Apache-2.0` ✅ |

*Contested field:* `description`. The playlist paraphrase embeds quota and
context-window figures that are not part of the owner-set field; rejected.

### 2.3 `QwenLM/Qwen3-Coder` — repo id `787368344`

| Field | Finalized value | Source | Live re-verify |
|---|---|---|---|
| project_name | Qwen3-Coder | target_set_csv | n/a — editorial label |
| original_url_from_playlist | `https://github.com/QwenLM/Qwen3-Coder` | target_set_csv | resolves directly, no redirect |
| canonical_owner_repo | `QwenLM/Qwen3-Coder` | github_api_live | `full_name` matches ✅ |
| description | Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team. | github_api_live | byte-exact ✅ |
| license | (none detected) | github_api_live | live payload carries **no** `license` object ✅ — reported, not invented |

*Sibling-repo caution (carried forward):* `QwenLM/qwen-code` is a different
repository and must never be substituted for `QwenLM/Qwen3-Coder`.

### 2.4 `QwenLM/Qwen3-TTS` — repo id `1138817132`

| Field | Finalized value | Source | Live re-verify |
|---|---|---|---|
| project_name | Qwen3-TTS | target_set_csv | n/a — editorial label |
| original_url_from_playlist | `https://github.com/QwenLM/Qwen3-TTS` | target_set_csv | resolves directly, no redirect |
| canonical_owner_repo | `QwenLM/Qwen3-TTS` | github_api_live | `full_name` matches ✅ |
| description | Qwen3-TTS is an open-source series of TTS models developed by the Qwen team at Alibaba Cloud, supporting stable, expressive, and streaming speech generation, free-form voice design, and vivid voice cloning. | github_api_live | byte-exact ✅ |
| license | Apache-2.0 | github_api_live | `license.spdx_id = Apache-2.0` ✅ |

*Retained on purpose:* this is a speech-synthesis project, not a coding agent.
It is cited verbatim in a playlist description, so a theme filter must not drop
it.

### 2.5 `OpenHands/OpenHands` — repo id `771302083` ⚠️ fork-identity case

This is the central *upstream-template-identity vs. destination-namespace* row.
The playlist cites `All-Hands-AI/OpenHands`; the organisation was renamed to
`OpenHands` and the repository now lives at `OpenHands/OpenHands`
(owner org id `225919603`). Both facts hold simultaneously: the cited path is a
valid entry point, the canonical path is the renamed one.

| Field | Finalized value | Source | Live re-verify |
|---|---|---|---|
| project_name | OpenHands | target_set_csv | n/a — editorial label |
| original_url_from_playlist | `https://github.com/All-Hands-AI/OpenHands` | target_set_csv | **preserved verbatim** — never overwritten with the canonical path; live probe of this exact path returns `200 OK` |
| canonical_owner_repo | `OpenHands/OpenHands` | github_api_live | `full_name` + all response URLs rooted here ✅ |
| description | `🙌 OpenHands: AI-Driven Development` | github_api_live | ⚠️ see §3.1 — leading `🙌` (U+1F64C) restored from live |
| license | `MIT` | github_api_live | ⚠️ see §3.2 — reviewed winner was stale |

---

## 3. Live-resolved substitutions

Two reviewed winners did **not** reproduce live. Under the unchanged priority
rule the live API value is authoritative, so the value published above is the
re-resolved one and the stale string is withheld from this document (it stays
visible in the CSV as the reviewed record).

### 3.1 `OpenHands/OpenHands` → `description`

| | |
|---|---|
| Reviewed winner (2026-04) | `OpenHands: AI-Driven Development` |
| Live owner-set value (2026-08-15) | `🙌 OpenHands: AI-Driven Development` |
| Resolved / live-safe | `🙌 OpenHands: AI-Driven Development` |

The reviewed winner had the leading emoji stripped — a silent normalisation of
the owner-set string. Applying it live would rewrite the owner's description.
The byte-exact live form is published instead. Substance is unchanged, so the
review decision (`github_api_live` beats the playlist paraphrase and the README
heading) still stands.

### 3.2 `OpenHands/OpenHands` → `license`

| | |
|---|---|
| Reviewed winner (2026-04) | `Other (NOASSERTION)` — GitHub SPDX auto-detection returned no assertion |
| Live SPDX value (2026-08-15) | `MIT` (`license.key = mit`, `license.spdx_id = MIT`) |
| Resolved / live-safe | `MIT` |

This is licence-detection drift, not a policy change: GitHub's automated
detector now recognises the repository's licence file. The `MIT` value the
playlist-derived `target_set_csv` originally claimed was correct in substance,
but it is published here because **live `github_api_live` says `MIT`** — the
priority order is untouched, only the snapshot moved. `Other (NOASSERTION)` is
therefore *not* safe to apply live and is excluded from this document.

---

## 4. Consistency check

| Repo | `selected=YES` rows in CSV | Finalized rows here | Live byte-exact | Live-resolved (§3) |
|---|---|---|---|---|
| `openai/codex` | 5 | 5 | 5 | 0 |
| `google-gemini/gemini-cli` | 5 | 5 | 5 | 0 |
| `QwenLM/Qwen3-Coder` | 5 | 5 | 5 | 0 |
| `QwenLM/Qwen3-TTS` | 5 | 5 | 5 | 0 |
| `OpenHands/OpenHands` | 5 | 5 | 3 | 2 |
| **Total** | **25** | **25** | **23** | **2** |

CSV row accounting: 36 data rows = 18 contested candidates (matching
`review/conflict-resolution:conflict_resolution.csv`) + 18 unchallenged
single-candidate rows. 25 `YES` = 5 fields × 5 repos; 11 `NO` = 9 discarded
description/canonical/licence alternatives + 2 discarded routing/licence claims.

Known drift **not** promoted into any value: the live `OpenHands/OpenHands`
README now opens on the “Agent Canvas” product heading rather than
“OpenHands: AI-Driven Development”. `readme_opening` was already a discarded
tier-2 candidate for that field, so the drift changes no decision — it is
recorded here only so a later reviewer is not surprised by it.

---

## 5. Evidence trail

| Artifact | Branch | Purpose |
|---|---|---|
| `target_set.csv` / `target_set.md` | `review/preserve-a-description-listed-repo-even` | reconstructed playlist target set (5 cited URLs → 5 rows) |
| `docs/identifier-vs-canonical.md` | `review/separate-identifier-from-canonicalized-identifier-in` | cited-vs-canonical identifier audit, org-rename redirect proof |
| `conflict_resolution.csv` | `review/conflict-resolution` | per-field candidate matrix (18 contested rows) |
| `source_priority.md` | `review/conflict-resolution` | three-tier source priority policy |
| `resolved_values.json` | `review/conflict-resolution` | machine-readable reviewed choices |
| `source_resolution_single_2.csv` | `review/source-resolution-single-2` | full reviewed target set (this commit) |
| `evidence_notes_single_2.md` | `review/source-resolution-single-2` | finalized live-safe values (this document) |

---

## 6. Delivery constraints observed

- Both artifacts are staged on the review branch
  `review/source-resolution-single-2`, at the repository root — the established
  path for this artifact lineage.
- The production branch `main` (the published site) is **not** modified, and no
  published-site path (`pages/`, `site_profile.yml`, `.nojekyll`,
  `publication_*`, `homepage_*`) is touched.
- Nothing is applied to any live/upstream repository by this change: the branch
  only *records* which values would be safe to apply.
- Cited identifiers are preserved verbatim; canonical identities are recorded
  additively, never by overwriting the cited path.
