# Source Priority Policy

## Authoritative Source Order

For every field in the AI Coding Tools playlist file set that can be derived
from more than one source, snapshot, or label interpretation, the following
precedence rule applies (highest → lowest):

| Priority | Source ID | Description |
|----------|-----------|-------------|
| 1 | `github_api_live` | Live GitHub REST API `/repos/{owner}/{repo}` snapshot taken at task time (2026-04-08T18:xx UTC). Fields: `description`, `full_name`, `license.spdx_id`. Owner-controlled and always current; canonical ground truth. |
| 2 | `readme_opening` | Opening sentence of the repository's `README.md` on the default branch at the same snapshot. Used only when the API `description` field is absent or ambiguous. |
| 3 | `target_set_csv` | `target_set.csv` committed on `review/preserve-a-description-listed-repo-even` (commit `862c2730`, 2026-04-08). Reconstructed from YouTube playlist descriptions; may contain paraphrased, feature-enriched, or slightly stale values. |
| 3b | `target_set_csv_original_url` | The `Original URL` column of `target_set.csv`, preserved verbatim as listed in the playlist. Superseded by `github_api_live` for canonical routing (e.g. redirected org names). |

## Per-Field Decisions

| Repo | Field | Winning Source | Rationale |
|------|-------|----------------|-----------|
| openai/codex | description | `github_api_live` | API returns the terse, owner-set string ("Lightweight coding agent that runs in your terminal"); target_set paraphrase embeds install details sourced from README |
| google-gemini/gemini-cli | description | `github_api_live` | API sentence aligns with README opening; target_set version adds rate-limit details ("60 req/min") not present in the official API field |
| QwenLM/Qwen3-Coder | description | `github_api_live` | API description is authoritative; target_set framing ("agentic code model family supporting 256K context") is an editorial interpretation incorporating README feature tables |
| QwenLM/Qwen3-TTS | description | `github_api_live` | API description is longer and more precise about capabilities; target_set truncates to capability highlights ("10 languages; sub-100ms latency") only |
| OpenHands/OpenHands | description | `github_api_live` | API is brief but owner-set; target_set embeds redirect note and an unverified SWE-Bench score claim |
| OpenHands/OpenHands | canonical_owner_repo | `github_api_live` | API confirms canonical path `OpenHands/OpenHands` (repo ID 771302083); the playlist URL `All-Hands-AI/OpenHands` is a GitHub redirect that is preserved in the `original_url_from_playlist` field |
| OpenHands/OpenHands | license | `github_api_live` | API SPDX detection returns `NOASSERTION` (Other) at this snapshot; target_set claim of `MIT` is not verified by GitHub's automated license detection |

## Snapshot Provenance

- **github_api_live** captured: 2026-04-08T18:xx UTC (this task run)
- **target_set_csv** authored: 2026-04-08T17:56:57Z (commit `862c2730`)
- **readme_opening** from: default-branch HEAD at same snapshot
