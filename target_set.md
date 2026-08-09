# Playlist Target Set — Reconstructed

The playlist descriptions supply exactly five verbatim project URLs. This document (and
`target_set.csv`) reconstruct the **intended target set**: one row per description-listed
project, enriched with metadata probed live from the GitHub REST API.

- Snapshot taken: **2026-08-09 ~18:56 UTC**
- Source of truth for membership: the **playlist descriptions** (verbatim URLs)
- Source of truth for metadata: **live GitHub API** (`GET /repos/{owner}/{repo}`, `.../releases/latest`)
- Rows in the target set: **5 / 5** (nothing dropped, nothing added)

## Target set

| # | Original URL (verbatim) | Listed owner/repo | Resolved owner/repo | Redirect? | Language | License | Default branch | Stars | Latest release |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `https://github.com/openai/codex` | `openai/codex` | `openai/codex` | no | Rust | Apache-2.0 | `main` | 104,938 | `rust-v0.147.0` |
| 2 | `https://github.com/google-gemini/gemini-cli` | `google-gemini/gemini-cli` | `google-gemini/gemini-cli` | no | TypeScript | Apache-2.0 | `main` | 106,432 | `v0.54.4` |
| 3 | `https://github.com/QwenLM/Qwen3-Coder` | `QwenLM/Qwen3-Coder` | `QwenLM/Qwen3-Coder` | no | Python | none detected | `main` | 16,776 | none |
| 4 | `https://github.com/QwenLM/Qwen3-TTS` | `QwenLM/Qwen3-TTS` | `QwenLM/Qwen3-TTS` | no | Python | Apache-2.0 | `main` | 12,878 | none |
| 5 | `https://github.com/All-Hands-AI/OpenHands` | `All-Hands-AI/OpenHands` | `OpenHands/OpenHands` ⚠️ | **yes** | TypeScript | MIT | `main` | 83,541 | `v1.12.0` |

Live descriptions (as returned by the API):

1. `openai/codex` — Lightweight coding agent that runs in your terminal
2. `google-gemini/gemini-cli` — An open-source AI agent that brings the power of Gemini directly into your terminal.
3. `QwenLM/Qwen3-Coder` — Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team.
4. `QwenLM/Qwen3-TTS` — Qwen3-TTS is an open-source series of TTS models developed by the Qwen team at Alibaba Cloud, supporting stable, expressive, and streaming speech generation, free-form voice design, and vivid voice cloning.
5. `All-Hands-AI/OpenHands` → `OpenHands/OpenHands` — 🙌 OpenHands: AI-Driven Development

## Reconstruction rules applied

1. **Membership is defined by the descriptions.** Every URL that appears verbatim in a
   playlist description becomes exactly one row. Five URLs in, five rows out.
2. **A description-listed repo is preserved even when the live lookup disagrees with the
   listed path.** `All-Hands-AI/OpenHands` has been transferred and GitHub now serves it as
   `OpenHands/OpenHands`. The row is kept, the listed path stays byte-for-byte in
   `original_url` / `listed_owner_repo`, and the canonical path is recorded *additively* in
   `resolved_owner_repo` with `redirect_detected = yes`. The listed path is never overwritten
   and the entry is never de-duplicated away.
3. **A description-listed repo is preserved even when it is off-theme.** `QwenLM/Qwen3-TTS`
   is a speech-synthesis project, not a coding agent, so a theme-based filter would discard
   it. It is listed in a description, therefore it stays in the target set (flagged in
   `notes` instead of being dropped).
4. **Missing metadata is reported, not invented.** `QwenLM/Qwen3-Coder` has no license
   detected by the API (`license = null`) and neither Qwen repository has a published
   release, so those cells read `none` rather than being guessed or back-filled.
5. **No silent normalisation.** Owner/repo casing (`QwenLM`, `All-Hands-AI`, `OpenHands`) is
   kept exactly as published; URLs are not rewritten to `www`/`.git`/trailing-slash variants.

## Verbatim URL check

All five URLs appear below exactly as given in the playlist descriptions:

1. `https://github.com/openai/codex`
2. `https://github.com/google-gemini/gemini-cli`
3. `https://github.com/QwenLM/Qwen3-Coder`
4. `https://github.com/QwenLM/Qwen3-TTS`
5. `https://github.com/All-Hands-AI/OpenHands`

## Delivery

| Item | Value |
|---|---|
| Machine-readable target set | `target_set.csv` (14 columns, 5 data rows, UTF-8) |
| Human-readable summary | `target_set.md` (this file) |
| Branch | `review/preserve-a-description-listed-repo-even` |
| Production branch (`main`) | untouched — no production file path was modified |

The changes are delivered on the review branch above so they can be inspected before any
promotion; `main` and the existing published file paths are deliberately left unchanged.
