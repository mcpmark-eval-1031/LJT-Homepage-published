# Live Re-Enactment — Source Resolution Single-2

Independent live re-verification of the reviewed change set, run against the live
GitHub API on **2026-08-22 UTC**. It confirms that the finalized subset in
`evidence_notes_single_2.md` reproduces live; no value decided by the review is stale
as of this run.

**Subproblem:** separate *upstream / template identity* from *destination namespace*
for the five repositories cited verbatim in the AI-coding-tools playlist descriptions.
**Review branch:** `review/source-resolution-single-2`
**Source-priority rule (unchanged):** `github_api_live` > `readme_opening` > `target_set_csv`;
`target_set_csv_original_url` never wins canonical routing.

---

## 1. Cited identifiers vs canonical identity (5 of 5)

| # | Cited URL (verbatim from playlist) | Live `full_name` | Redirect | Repo id |
|---|---|---|---|---|
| 1 | `https://github.com/openai/codex` | `openai/codex` | none | 965415649 |
| 2 | `https://github.com/google-gemini/gemini-cli` | `google-gemini/gemini-cli` | none | 968197216 |
| 3 | `https://github.com/QwenLM/Qwen3-Coder` | `QwenLM/Qwen3-Coder` | none | 787368344 |
| 4 | `https://github.com/QwenLM/Qwen3-TTS` | `QwenLM/Qwen3-TTS` | none | 1138817132 |
| 5 | `https://github.com/All-Hands-AI/OpenHands` | `OpenHands/OpenHands` | **YES** (org rename) | 771302083 |

Four of five cited paths resolve to themselves (`full_name` == cited identifier).
The fifth is the fork-identity case: `All-Hands-AI` was renamed to `OpenHands`, and the
cited path is a still-valid `200 OK` entry point whose every response URL is rooted at the
canonical namespace `OpenHands/OpenHands`.

---

## 2. Fields re-probed live (all reproduce, byte-exact against the reviewed winners)

| Canonical repo | description (live) | license (live) |
|---|---|---|
| `openai/codex` | Lightweight coding agent that runs in your terminal | Apache-2.0 |
| `google-gemini/gemini-cli` | An open-source AI agent that brings the power of Gemini directly into your terminal. | Apache-2.0 |
| `QwenLM/Qwen3-Coder` | Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team. | none detected (no license object) |
| `QwenLM/Qwen3-TTS` | Qwen3-TTS is an open-source series of TTS models developed by the Qwen team at Alibaba Cloud, supporting stable, expressive, and streaming speech generation, free-form voice design, and vivid voice cloning. | Apache-2.0 |
| `OpenHands/OpenHands` | 🙌 OpenHands: AI-Driven Development | MIT |

---

## 3. Sub-probe results for the central case (`OpenHands/OpenHands`)

- **Identity:** requested `All-Hands-AI/OpenHands`, returned `full_name = OpenHands/OpenHands`
  (`owner.login = OpenHands`, repo id `771302083`) → canonical routing confirmed.
- **Description:** the live owner-set string carries the leading **🙌 (U+1F64C)**. This is the
  byte-exact live-safe value; the emoji-stripped form survives only in the CSV as the
  *reviewed record* (`evidence_notes_single_2.md` §3.1).
- **License:** live SPDX reports `MIT` (`license.key = mit`, `spdx_id = MIT`, `name = MIT License`).
  The reviewed `Other (NOASSERTION)` winner was licence-detection drift and is correctly
  withheld from the live-safe subset (`evidence_notes_single_2.md` §3.2). Independent
  corroboration: the canonical repo's licence file and the `api-evangelist/openhands` mirror
  both state MIT.

---

## 4. Sibling-repo caution

`QwenLM/qwen-code` is a **different** repository and is not substituted for
`QwenLM/Qwen3-Coder`. `QwenLM/Qwen3-TTS` is a speech-synthesis project, not a coding agent;
it is retained because it is cited verbatim in a playlist description (flagged, not dropped).

---

## 5. Non-reviewed fields noted, not promoted

Star counts and `latest_release_tag` drift between snapshots (e.g. `codex` stars 106,396 →
111,627; `gemini-cli` 106,535 → 106,608; `OpenHands` 84,261 → 84,746) and `OpenHands` latest
release is `v1.13.0`. None of these are among the five reviewed fields, so no finalized value
moves.

---

## 6. Conclusion

- 4 of 5 cited identifiers resolve as cited; 1 (`All-Hands-AI/OpenHands`) canonicalizes to
  `OpenHands/OpenHands` while remaining a valid entry point.
- Every finalized value in `evidence_notes_single_2.md` §2 reproduces live as of 2026-08-22.
- No discarded candidate is safe to apply; no invented value; no cited identifier rewritten.
- The reviewed change set is reproduced live → the `evidence_notes_single_2.md` finalized
  subset is **safe to apply live as written**.

## 7. Artifact lineage referenced

`source_resolution_single_2.csv` (full reviewed target set, this branch) ·
`evidence_notes_single_2.md` (finalized subset) · `target_set.csv` / `target_set.md`
(branch `review/preserve-a-description-listed-repo-even`) · `review/conflict-resolution`
(`conflict_resolution.csv`, `source_priority.md`, `resolved_values.json`) ·
`review/separate-identifier-from-canonicalized-identifier-in`
(`docs/identifier-vs-canonical.md`, org-rename redirect audit).
