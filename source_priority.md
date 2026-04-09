# Source Priority Policy

## Authoritative Source Order

For every field in the AI Coding Tools playlist file set that can be derived
from more than one source, snapshot, or label interpretation, the following
precedence rule applies (highest → lowest):

| Priority | Source ID | Description |
|----------|-----------|-------------|
| 1 | `github_api_live` | Live GitHub REST API `/repos/{owner}/{repo}` snapshot taken at task time (2026-04-09T00:xx UTC). Fields: `description`, `full_name`, `license.spdx_id`. Owner-controlled and always current; canonical ground truth. |
| 2 | `readme_opening` | Opening sentence (or heading) of the repository's `README.md` on the default branch at the same snapshot. Used only when the API `description` field is absent or ambiguous. |
| 3 | `target_set_csv` | `target_set.csv` committed on `review/conflict-resolution`. Reconstructed from YouTube playlist descriptions; may contain paraphrased, feature-enriched, or slightly stale values. |
| 3b | `target_set_csv_original_url` | The `Original URL` column of `target_set.csv`, preserved verbatim as listed in the playlist. Superseded by `github_api_live` for canonical routing (e.g. redirected org names). |

## Rationale

`github_api_live` wins because it is the owner-set, machine-readable field served
directly from GitHub's API at the moment of this task run. It is the shortest
path to what the repo author considers their canonical description.

`readme_opening` is the next most reliable signal: it reflects what the author
wrote at the top of their README and is nearly always consistent with the API
description. It is used as a tiebreaker or fallback when the API field is blank.

`target_set_csv` is derived from YouTube playlist copy-paste descriptions and
may embed installation details, rate-limit numbers, benchmark scores, or
editorial framing that is not part of the canonical repo metadata.

## Per-Field Decisions

| Repo | Field | Winning Source | Rationale |
|------|-------|----------------|-----------|
| openai/codex | description | `github_api_live` | API returns terse, owner-set string; `target_set_csv` embeds install instructions sourced from README; `readme_opening` is longer but agrees in substance |
| google-gemini/gemini-cli | description | `github_api_live` | API sentence aligns with README opening; `target_set_csv` adds rate-limit details ("60 req/min") not in the official description field |
| QwenLM/Qwen3-Coder | description | `github_api_live` | API description is authoritative; `target_set_csv` is an editorial interpretation incorporating README feature tables (256K context, 358 languages) |
| QwenLM/Qwen3-TTS | description | `github_api_live` | API description is the most complete and precise; `readme_opening` is a restatement; `target_set_csv` truncates to feature highlights only |
| OpenHands/OpenHands | description | `github_api_live` | API is brief but owner-set; `target_set_csv` embeds redirect note and an unverified SWE-Bench score claim; `readme_opening` heading agrees with API |
| OpenHands/OpenHands | canonical_owner_repo | `github_api_live` | API confirms canonical path `OpenHands/OpenHands` (repo ID 771302083); the playlist URL `All-Hands-AI/OpenHands` is a GitHub redirect preserved in `original_url_from_playlist` |
| OpenHands/OpenHands | license | `github_api_live` | API SPDX detection returns `NOASSERTION` at this snapshot; `target_set_csv` claim of `MIT` is not verified by GitHub's automated license detection |

## Snapshot Provenance

- **github_api_live** captured: 2026-04-09T00:xx UTC (this task run)
- **target_set_csv** authored: 2026-04-08T17:56:57Z (commit `862c2730` on `review/preserve-a-description-listed-repo-even`)
- **readme_opening** from: default-branch HEAD at same snapshot
- **Policy file committed before** `resolved_values.json` to ensure traceability
