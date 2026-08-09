# Source Identifier vs Canonicalized GitHub Path — Audit Report

## Purpose
Separate what the tutorial descriptions **named** (verbatim source identifiers) from what
GitHub **currently resolves** to (canonical `owner/repo` paths after any redirect, org
rename, or repository transfer).

Machine-readable companion: **`target_set.csv`** at the repository root — 4 data rows,
one per cited identifier, with `source_identifier` and `canonical_identifier` held in
separate columns.

- **Snapshot / re-verification date:** 2026-08-09 (live GitHub REST API)
- **Authority order:** `github_api_live` > `readme_opening` > tutorial description text
  (policy inherited from `review/conflict-resolution:source_priority.md`)

---

## The Four Source Identifiers (verbatim, as cited in the tutorial descriptions)

```
openai/codex
google-gemini/gemini-cli
QwenLM/Qwen3-Coder
All-Hands-AI/OpenHands
```

Nothing is dropped, merged, or silently rewritten: 4 cited identifiers → 4 rows.

---

## Method

For each cited identifier, `GET /repos/{owner}/{repo}` was called with the **cited**
owner/repo. GitHub answers a stale path with the **canonical** payload, so comparing the
requested path against the returned `full_name` / `owner.login` / `html_url` is direct
proof of whether a redirect or canonicalization is in effect.

```
requested path == returned full_name   ->  no redirect
requested path != returned full_name   ->  redirected / canonicalized
```

---

## Resolution Results

### 1. `openai/codex` — no change
| Field | Value |
|---|---|
| **Tutorial-cited identifier** | `openai/codex` |
| **Redirects / canonicalizes?** | **No** |
| **Canonical identifier** (`full_name`) | `openai/codex` |
| **Live URL** (`html_url`) | https://github.com/openai/codex |
| **Repo id** | 965415649 |
| **Owner** | `openai` (org id 14957082) |
| **Live description** | Lightweight coding agent that runs in your terminal |
| **License (SPDX)** | Apache-2.0 |
| **Default branch** | `main` |

---

### 2. `google-gemini/gemini-cli` — no change
| Field | Value |
|---|---|
| **Tutorial-cited identifier** | `google-gemini/gemini-cli` |
| **Redirects / canonicalizes?** | **No** |
| **Canonical identifier** (`full_name`) | `google-gemini/gemini-cli` |
| **Live URL** (`html_url`) | https://github.com/google-gemini/gemini-cli |
| **Repo id** | 968197216 |
| **Owner** | `google-gemini` (org id 161781182) |
| **Live description** | An open-source AI agent that brings the power of Gemini directly into your terminal. |
| **License (SPDX)** | Apache-2.0 |
| **Default branch** | `main` |

---

### 3. `QwenLM/Qwen3-Coder` — no change
| Field | Value |
|---|---|
| **Tutorial-cited identifier** | `QwenLM/Qwen3-Coder` |
| **Redirects / canonicalizes?** | **No** |
| **Canonical identifier** (`full_name`) | `QwenLM/Qwen3-Coder` |
| **Live URL** (`html_url`) | https://github.com/QwenLM/Qwen3-Coder |
| **Repo id** | 787368344 |
| **Owner** | `QwenLM` (org id 141221163) |
| **Live description** | Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team. |
| **License (SPDX)** | *(null — GitHub SPDX detection reports no license at this snapshot)* |
| **Default branch** | `main` |

> Sibling-repo caution: `QwenLM/qwen-code` is a **different** repository (the Qwen coding
> CLI). It is *not* a canonicalization of `QwenLM/Qwen3-Coder`, and must not be
> substituted for it in the target set.

---

### 4. `All-Hands-AI/OpenHands` — ⚠️ canonicalized
| Field | Value |
|---|---|
| **Tutorial-cited identifier** | `All-Hands-AI/OpenHands` |
| **Redirects / canonicalizes?** | **YES** |
| **Canonical identifier** (`full_name`) | `OpenHands/OpenHands` |
| **Live URL** (`html_url`) | https://github.com/OpenHands/OpenHands |
| **Repo id** | 771302083 |
| **Owner** | `OpenHands` (org id 225919603) |
| **Live description** | 🙌 OpenHands: AI-Driven Development |
| **License (SPDX)** | MIT |
| **Default branch** | `main` |

---

## Key Finding: identifier vs canonicalized identifier

| # | Tutorial source identifier | Canonical identifier | Changed? |
|---|---|---|---|
| 1 | `openai/codex` | `openai/codex` | No change |
| 2 | `google-gemini/gemini-cli` | `google-gemini/gemini-cli` | No change |
| 3 | `QwenLM/Qwen3-Coder` | `QwenLM/Qwen3-Coder` | No change |
| 4 | `All-Hands-AI/OpenHands` | `OpenHands/OpenHands` | **Redirected / canonicalized** |

**1 of 4** cited identifiers no longer matches its canonical path; the other 3 resolve as-is.

---

## Evidence of Redirect for `All-Hands-AI/OpenHands`

Requesting the **cited** path returns the **canonical** payload:

```
GET https://api.github.com/repos/All-Hands-AI/OpenHands   -> 200 OK
  "id":        771302083
  "full_name": "OpenHands/OpenHands"                 # <- not All-Hands-AI/OpenHands
  "html_url":  "https://github.com/OpenHands/OpenHands"
  "owner":     { "login": "OpenHands", "id": 225919603 }
```

Corroborated by a `git` object-level probe: `GET /repos/All-Hands-AI/OpenHands/commits/main`
returns `html_url: https://github.com/OpenHands/OpenHands/commit/<sha>`.

Cross-check on the legacy namespace:

```
GET https://api.github.com/orgs/All-Hands-AI        -> 200 OK (id 169105795, 5 public repos)
GET https://api.github.com/orgs/All-Hands-AI/repos  -> SWE-bench, openhands-resolver,
                                                       swe-bench.github.io, pr-eval-results,
                                                       docker-python-nodejs
                                                       (all archived; no "OpenHands" repo)
```

Interpretation: as part of the All-Hands-AI → OpenHands rebrand, the repository moved out
of the `All-Hands-AI` namespace into the `OpenHands` organization. Both facts hold and are
non-contradictory — the cited identifier remains a *valid entry point* (GitHub redirects
it), while the *canonical* identifier is `OpenHands/OpenHands`.

Drift note: at the earlier 2026-04 snapshot GitHub's SPDX detection reported
`NOASSERTION` for this repo; the live snapshot now reports `MIT`. The canonical path is
unchanged between the two snapshots.

---

## Why the two identifiers stay in separate columns

`target_set.csv` deliberately carries both:

- **`source_identifier`** — preserved **verbatim** as cited in the tutorial descriptions, so
  the citation stays auditable and the tutorial text can still be matched literally.
- **`canonical_owner` / `canonical_repo` / `canonical_identifier` / `github_html_url`** — the
  live, owner-set canonical routing, safe to use for API calls, links, and dedup keys.

Collapsing them would either (a) rewrite history by silently replacing what the tutorial
actually said, or (b) freeze a path that keeps drifting as orgs are renamed and repos are
transferred. Keeping both makes the single changed row explicit instead of invisible.

---

## Checklist Confirmation

All four source identifiers preserved verbatim, each with a live-verified canonical identifier:

- [x] `openai/codex` → `openai/codex`
- [x] `google-gemini/gemini-cli` → `google-gemini/gemini-cli`
- [x] `QwenLM/Qwen3-Coder` → `QwenLM/Qwen3-Coder`
- [x] `All-Hands-AI/OpenHands` → `OpenHands/OpenHands` (redirect)

Row-count check: 4 cited identifiers → 4 data rows in `target_set.csv` (+ 1 header).

---

## Delivery Constraints Observed

- All changes staged on the review branch
  `review/separate-identifier-from-canonicalized-identifier-in`.
- The production branch (`main`, the published-site branch) is **not** modified, and no
  published-site path (`pages/`, `site_profile.yml`, `.nojekyll`, `publication_*`) is touched.
- `target_set.csv` is written at the repository root — the established path for this
  artifact in this review lineage — rather than at a new or alternate path.
