# Source Identifier vs Canonicalized GitHub Path — Audit Report

## Purpose
This document separates what the tutorial source **named** (verbatim source identifiers)
from what GitHub **currently resolves** to (canonical paths after any redirects or org renames).

---

## The Four Source Identifiers (verbatim, as cited in the tutorial)

```
openai/codex
google-gemini/gemini-cli
QwenLM/Qwen3-Coder
All-Hands-AI/OpenHands
```

---

## Resolution Results

### 1. `openai/codex`
| Field | Value |
|---|---|
| **Tutorial-cited identifier** | `openai/codex` |
| **GitHub redirect?** | **No** |
| **Canonical path** | `openai/codex` |
| **Live URL** | https://github.com/openai/codex |
| **Notes** | Resolves directly. No org rename or redirect detected. |

---

### 2. `google-gemini/gemini-cli`
| Field | Value |
|---|---|
| **Tutorial-cited identifier** | `google-gemini/gemini-cli` |
| **GitHub redirect?** | **No** |
| **Canonical path** | `google-gemini/gemini-cli` |
| **Live URL** | https://github.com/google-gemini/gemini-cli |
| **Notes** | Resolves directly. No org rename or redirect detected. |

---

### 3. `QwenLM/Qwen3-Coder`
| Field | Value |
|---|---|
| **Tutorial-cited identifier** | `QwenLM/Qwen3-Coder` |
| **GitHub redirect?** | **No** |
| **Canonical path** | `QwenLM/Qwen3-Coder` |
| **Live URL** | https://github.com/QwenLM/Qwen3-Coder |
| **Notes** | Resolves directly. No org rename or redirect detected. |

---

### 4. `All-Hands-AI/OpenHands`
| Field | Value |
|---|---|
| **Tutorial-cited identifier** | `All-Hands-AI/OpenHands` |
| **GitHub redirect?** | **YES — org renamed** |
| **Canonical path** | `OpenHands/OpenHands` |
| **Live URL** | https://github.com/OpenHands/OpenHands |
| **Notes** | The GitHub organization was renamed from `All-Hands-AI` to `OpenHands`. The GitHub API transparently redirects all requests for `All-Hands-AI/OpenHands` to `OpenHands/OpenHands`. All `html_url` fields returned by the API reflect the canonical `OpenHands/OpenHands` path. |

---

## Key Finding: Identifier vs Canonical Path

| # | Tutorial Source Identifier | Canonical GitHub Path | Changed? |
|---|---|---|---|
| 1 | `openai/codex` | `openai/codex` | No change |
| 2 | `google-gemini/gemini-cli` | `google-gemini/gemini-cli` | No change |
| 3 | `QwenLM/Qwen3-Coder` | `QwenLM/Qwen3-Coder` | No change |
| 4 | `All-Hands-AI/OpenHands` | `OpenHands/OpenHands` | **Redirected** |

---

## Evidence of Redirect for `All-Hands-AI/OpenHands`

When the GitHub API was queried with `owner=All-Hands-AI, repo=OpenHands`, the response
returned content with all `html_url` fields pointing to:
```
https://github.com/OpenHands/OpenHands/...
```
instead of the expected:
```
https://github.com/All-Hands-AI/OpenHands/...
```

This confirms the `All-Hands-AI` organization was **canonically renamed** to `OpenHands`
on GitHub, and GitHub transparently redirects the old path.

---

## Checklist Confirmation

All four source identifiers preserved verbatim in this document:
- [x] `openai/codex`
- [x] `google-gemini/gemini-cli`
- [x] `QwenLM/Qwen3-Coder`
- [x] `All-Hands-AI/OpenHands`
