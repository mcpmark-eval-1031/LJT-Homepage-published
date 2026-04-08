# Evidence Notes — Source Resolution Single-2

**Subproblem:** Upstream template identity from destination namespace when
invoking GitHub fork flows (AI coding tools playlist, 5 repos).  
**Review branch:** `review/source-resolution-single-2`  
**Companion surface:** `source_resolution_single_2.csv` (34 rows, all candidates + review states)  
**Snapshot date:** 2026-04-08  
**Source priority rule:** `github_api_live` > `readme_opening` > `target_set_csv`  
*(Policy documented in `review/conflict-resolution:source_priority.md`)*

---

## Finalized Values — Safe to Apply Live

Only rows with `selected = YES` are reproduced here. Unchallenged fields
(single candidate, no conflict) are listed without rationale. Contested
fields are annotated.

### 1. `openai/codex`

| Field | Finalized Value | Source | Note |
|---|---|---|---|
| project_name | Codex CLI | target_set_csv | Unchallenged |
| original_url_from_playlist | https://github.com/openai/codex | target_set_csv | Unchallenged; no redirect |
| canonical_owner_repo | openai/codex | github_api_live | Unchallenged; direct resolution |
| description | Lightweight coding agent that runs in your terminal | github_api_live | **Contested** — wins over target_set_csv paraphrase (adds install details not in owner-set field) and readme_opening (slightly different phrasing) |
| license | Apache-2.0 | github_api_live | Unchallenged |

### 2. `google-gemini/gemini-cli`

| Field | Finalized Value | Source | Note |
|---|---|---|---|
| project_name | Gemini CLI | target_set_csv | Unchallenged |
| original_url_from_playlist | https://github.com/google-gemini/gemini-cli | target_set_csv | Unchallenged; no redirect |
| canonical_owner_repo | google-gemini/gemini-cli | github_api_live | Unchallenged; direct resolution |
| description | An open-source AI agent that brings the power of Gemini directly into your terminal. | github_api_live | **Contested** — wins over target_set_csv paraphrase (embeds "60 req/min" rate-limit detail absent from the owner-set API field) and readme_opening |
| license | Apache-2.0 | github_api_live | Unchallenged |

### 3. `QwenLM/Qwen3-Coder`

| Field | Finalized Value | Source | Note |
|---|---|---|---|
| project_name | Qwen3-Coder | target_set_csv | Unchallenged |
| original_url_from_playlist | https://github.com/QwenLM/Qwen3-Coder | target_set_csv | Unchallenged; no redirect |
| canonical_owner_repo | QwenLM/Qwen3-Coder | github_api_live | Unchallenged; direct resolution |
| description | Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team. | github_api_live | **Contested** — wins over target_set_csv paraphrase (editorial interpretation incorporating README feature tables; not the owner-set API string) |
| license | (none detected) | github_api_live | Unchallenged; GitHub SPDX detection returned null at this snapshot |

### 4. `QwenLM/Qwen3-TTS`

| Field | Finalized Value | Source | Note |
|---|---|---|---|
| project_name | Qwen3-TTS | target_set_csv | Unchallenged |
| original_url_from_playlist | https://github.com/QwenLM/Qwen3-TTS | target_set_csv | Unchallenged; no redirect |
| canonical_owner_repo | QwenLM/Qwen3-TTS | github_api_live | Unchallenged; direct resolution |
| description | Qwen3-TTS is an open-source series of TTS models developed by the Qwen team at Alibaba Cloud, supporting stable, expressive, and streaming speech generation, free-form voice design, and vivid voice cloning. | github_api_live | **Contested** — wins over target_set_csv summary (truncates to capability highlights only) |
| license | Apache-2.0 | github_api_live | Unchallenged |

### 5. `OpenHands/OpenHands` ⚠️ Fork-Identity Resolution

The playlist listed this repository as `All-Hands-AI/OpenHands`.
The GitHub organization was **renamed** from `All-Hands-AI` to `OpenHands`.
GitHub transparently redirects all API and web requests for the old path
to the canonical path `OpenHands/OpenHands` (repo ID 771302083).
This is the central *upstream-template-identity* case for this subproblem.

| Field | Finalized Value | Source | Note |
|---|---|---|---|
| project_name | OpenHands | target_set_csv | Unchallenged |
| original_url_from_playlist | https://github.com/All-Hands-AI/OpenHands | target_set_csv | **Preserved verbatim** — the source-listed identifier before redirect |
| canonical_owner_repo | OpenHands/OpenHands | github_api_live | **Contested** — `github_api_live` confirms canonical path (repo ID 771302083); `All-Hands-AI/OpenHands` is the pre-rename destination namespace, preserved in `original_url_from_playlist` only |
| description | OpenHands: AI-Driven Development | github_api_live | **Contested** — wins over target_set_csv which embeds unverified SWE-Bench score and redirect note |
| license | Other (NOASSERTION) | github_api_live | **Contested** — target_set_csv claimed MIT; GitHub SPDX automated detection returns NOASSERTION at this snapshot; github_api_live is authoritative |

---

## Consistency Check

The table below confirms that the winner count in this document matches
the `selected=YES` count in `source_resolution_single_2.csv`.

| Repo | Winner rows (this doc) | selected=YES rows (CSV) |
|---|---|---|
| openai/codex | 5 | 5 |
| google-gemini/gemini-cli | 5 | 5 |
| QwenLM/Qwen3-Coder | 5 | 5 |
| QwenLM/Qwen3-TTS | 5 | 5 |
| OpenHands/OpenHands | 5 | 5 |
| **Total** | **25** | **25** |

---

## Evidence Trail

| Artifact | Branch | Commit | Purpose |
|---|---|---|---|
| `target_set.csv` / `target_set.md` | `review/preserve-a-description-listed-repo-even` | `862c2730` | Original reconstructed playlist targets |
| `docs/identifier-vs-canonical.md` | `review/separate-identifier-from-canonicalized-identifier-in` | `084d3e91` | Org-rename redirect audit (All-Hands-AI → OpenHands) |
| `conflict_resolution.csv` | `review/conflict-resolution` | `f822ac68` | Per-field candidate matrix (16 contested rows) |
| `source_priority.md` | `review/conflict-resolution` | `dacc25f6` | Three-tier priority policy |
| `resolved_values.json` | `review/conflict-resolution` | `6dccb745` | Machine-readable final choices |
| `source_resolution_single_2.csv` | `review/source-resolution-single-2` | *(this commit)* | Full 34-row review surface (this subproblem) |
| `evidence_notes_single_2.md` | `review/source-resolution-single-2` | *(this commit)* | Finalized live-safe values (this document) |
