# Render Contract — Vicent0205/Vicent0205.github.io Content-File Artifact

**Version:** 1.0.0  
**Repository (source):** Vicent0205/Vicent0205.github.io  
**Staging repository:** mcpmark-eval-1031/LUFFY  
**Status:** FROZEN  
**Date:** 2026-04-09  
**Scan basis:** `master` branch — commit `52c3bfd25c5ed59284548f3096932d00213501ae` (2026-03-13)

---

## 1. Purpose

This contract governs the exact structure, field names, field order, empty-value
representation, normalization rules, and ordering constraints that every rendering
of the **personal-website content-file artifact** (hereafter "the artifact") MUST
satisfy.

The artifact is a single machine-readable JSON document produced by extracting and
normalizing content from the following source files in `Vicent0205/Vicent0205.github.io`:

| Source File | Contributes to |
|-------------|----------------|
| `_config.yml` | `site_meta` |
| `_pages/about.md` | `about` |
| `_pages/publications.md` | `publications` (authoritative for content and order) |
| `_bibliography/papers.bib` | `publications` (secondary: `cite_key`, `abbr`, `selected`) |
| `_news/announcement_*.md` | `news` |
| `_data/cv.yml` | `cv` (data) |
| `_pages/cv.md` | `cv.pdf_path`, `cv.cv_format` |

No rendering may be produced, stored, or reviewed until this contract is frozen.

---

## 2. Top-Level Envelope

### 2.1 Field Order (canonical, positional)

| # | Field Name | JSON Type | Required | Description |
|---|------------|-----------|----------|-------------|
| 1 | `schema_version` | `string` | YES | Semver of this contract: `"1.0.0"`. |
| 2 | `repository` | `string` | YES | Source repo slug `"Vicent0205/Vicent0205.github.io"`. |
| 3 | `source_branch` | `string` | YES | Branch from which content was read. |
| 4 | `source_sha` | `string` | YES | Full 40-character commit SHA of HEAD at render time. |
| 5 | `snapshot_at` | `string` (ISO 8601) | YES | UTC timestamp of the snapshot (`YYYY-MM-DDTHH:MM:SSZ`). |
| 6 | `site_meta` | `object` | YES | Site-level settings. See §3. |
| 7 | `about` | `object` | YES | About-page content. See §4. |
| 8 | `publications` | `array` | YES | Ordered publication records. See §5. |
| 9 | `news` | `array` | YES | Ordered news records. See §6. |
| 10 | `cv` | `object` | YES | Curriculum vitae data. See §7. |

**Rule T-1:** Every field in §2.1 MUST be present; none may be omitted.
**Rule T-2:** Field order is immutable; position 1 must precede position 2, and so on.

---

## 3. `site_meta` Object

Source: `_config.yml`

### 3.1 Field Order

| # | Field | Type | Empty value |
|---|-------|------|-------------|
| 1 | `first_name` | `string` | `""` |
| 2 | `middle_name` | `string` | `""` |
| 3 | `last_name` | `string` | `""` |
| 4 | `title` | `string` | `""` |
| 5 | `url` | `string` | `""` |
| 6 | `baseurl` | `string` | `""` |
| 7 | `description` | `string` | `""` |
| 8 | `keywords` | `string` | `""` |
| 9 | `lang` | `string` | `"en"` |

### 3.2 Normalization Rules

**Rule M-1:** All strings are trimmed of leading/trailing whitespace.  
**Rule M-2:** Multi-line YAML block scalars (`>` or `|` notation) are collapsed: each
internal newline is replaced by a single space; the result is then trimmed.  
**Rule M-3:** The YAML value `blank` for `title` (the al-folio default meaning "use full
name") is preserved verbatim as the string `"blank"`. It is never replaced with the
owner's full name.  
**Rule M-4:** An absent YAML key is represented as `""` (empty string), except `lang`
which defaults to `"en"`.

---

## 4. `about` Object

Source: `_pages/about.md`

### 4.1 Field Order

| # | Field | Type | Empty value |
|---|-------|------|-------------|
| 1 | `layout` | `string` | `""` |
| 2 | `permalink` | `string` | `""` |
| 3 | `subtitle` | `string` | `""` |
| 4 | `profile_image` | `string` | `""` |
| 5 | `profile_image_circular` | `boolean` | `false` |
| 6 | `selected_papers` | `boolean` | `false` |
| 7 | `social` | `boolean` | `false` |
| 8 | `announcements_enabled` | `boolean` | `false` |
| 9 | `announcements_scrollable` | `boolean` | `false` |
| 10 | `announcements_limit` | `integer` | `0` |
| 11 | `latest_posts_enabled` | `boolean` | `false` |
| 12 | `bio_text` | `string` | `""` |
| 13 | `scholar_url` | `string` | `""` |
| 14 | `twitter_handle` | `string` | `""` |

### 4.2 Normalization Rules

**Rule A-1:** `bio_text` is the raw Markdown body of `about.md` (everything after the
closing `---` of the front matter). Leading and trailing whitespace of the whole body
are stripped. Paragraph breaks (`\n\n`) are preserved. Inline Markdown (links,
bold, lists) is preserved verbatim.  
**Rule A-2:** `scholar_url` is extracted from the `href` of the first `<a>` tag whose
`href` domain contains `scholar.google.com`. Returned as full URL. If absent, `""`.  
**Rule A-3:** `twitter_handle` is extracted from the `href` of an `<a>` tag pointing to
`twitter.com/` or `x.com/`; the value is the bare handle with no `@` prefix. If
absent, `""`.  
**Rule A-4:** Boolean front-matter keys (`selected_papers`, `social`, etc.) default to
`false` when absent.  
**Rule A-5:** `announcements_limit` is read from `announcements.limit`; `0` if absent.  
**Rule A-6:** `announcements_enabled` is read from `announcements.enabled`; `false` if
absent.  
**Rule A-7:** `announcements_scrollable` is read from `announcements.scrollable`; `false`
if absent.  
**Rule A-8:** `latest_posts_enabled` is read from `latest_posts.enabled`; `false` if
absent.

---

## 5. `publications` Array

Sources: `_pages/publications.md` (authoritative for content and order),
`_bibliography/papers.bib` (secondary for `cite_key`, `abbr`, `selected`).

### 5.1 Publication Record — Field Order

| # | Field | Type | Empty value |
|---|-------|------|-------------|
| 1 | `cite_key` | `string` | `""` |
| 2 | `year` | `integer` | `0` |
| 3 | `title` | `string` | `""` |
| 4 | `authors_raw` | `string` | `""` |
| 5 | `is_first_author` | `boolean` | `false` |
| 6 | `co_first_author` | `boolean` | `false` |
| 7 | `venue` | `string` | `""` |
| 8 | `venue_type` | `string` | `""` |
| 9 | `abbr` | `string` | `""` |
| 10 | `paper_url` | `string` | `""` |
| 11 | `code_url` | `string` | `""` |
| 12 | `selected` | `boolean` | `false` |

### 5.2 Ordering Constraints

Publication records are sorted by the following cascading keys:

1. **Primary:** `year` descending (newest year first).
2. **Secondary:** `is_first_author` descending (`true` before `false`).
3. **Tertiary:** `co_first_author` descending (`true` before `false`).
4. **Quaternary:** Stable source order from `_pages/publications.md` within any
   group where the first three keys are equal (preserves editorial intent).

**Rule O-1:** No two records sharing identical (`year`, `is_first_author`,
`co_first_author`) values may swap their relative order between renderings.  
**Rule O-2:** The positional field order declared in §5.1 is immutable across all 12
fields of every record.

### 5.3 Normalization Rules

**Rule P-1 (`authors_raw`):** Copied verbatim from the author line in `publications.md`,
including `**Name**` bold markers for the site owner and `*` co-first-author superscripts
(e.g., `**Junteng Liu***` denotes first author with co-first flag).  
**Rule P-2 (`is_first_author`):** `true` iff the first `**...**` token in `authors_raw`
matches `Junteng Liu`.  
**Rule P-3 (`co_first_author`):** `true` iff the site-owner's bold name in `authors_raw`
is immediately followed by `*` (without space), e.g. `**Junteng Liu***`.  
**Rule P-4 (`venue`):** The italicized venue string from `publications.md` (between `*`
delimiters), stripped of those delimiters and trimmed. Example: `*NeurIPS 2025*` →
`"NeurIPS 2025"`.  
**Rule P-5 (`venue_type`):** Inferred from `venue` string:
  - `"conference"` — NeurIPS, EMNLP (including Findings), ICML, ACL, ICLR, or similar
    peer-reviewed proceeding.
  - `"preprint"` — `arXiv` appears in the venue string.
  - `"technical_report"` — `Technical Report` appears in the venue string.
  - `"journal"` — a journal name is in the venue string and none of the above match.
**Rule P-6 (`abbr`):** From the BibTeX `abbr` field; `""` when the entry is absent from
`papers.bib`.  
**Rule P-7 (`selected`):** `true` iff the BibTeX entry contains `selected = {true}`;
`false` otherwise or when absent from `papers.bib`.  
**Rule P-8 (`cite_key`):** The BibTeX cite key of the matching entry; `""` when the
publication is not in `papers.bib`.  
**Rule P-9 (`paper_url` / `code_url`):** Extracted from `[Paper](url)` and `[Code](url)`
link syntax in `publications.md`. `""` when the respective link is absent.  
**Rule P-10:** No `null` values anywhere in any publication record.

---

## 6. `news` Array

Source: `_news/announcement_*.md`

### 6.1 News Record — Field Order

| # | Field | Type | Empty value |
|---|-------|------|-------------|
| 1 | `filename` | `string` | `""` |
| 2 | `date` | `string` | `""` |
| 3 | `inline` | `boolean` | `false` |
| 4 | `related_posts` | `boolean` | `false` |
| 5 | `body_markdown` | `string` | `""` |

### 6.2 Ordering Constraints

**Rule N-1:** News records are sorted by `date` **descending** (most recent first).  
**Rule N-2:** When two records share the same `date` value, they are sorted by
`filename` **ascending** (lexicographic, Unicode code-point order) as a deterministic
tie-breaker.

### 6.3 Normalization Rules

**Rule W-1 (`date`):** The `date` YAML front-matter value truncated to `YYYY-MM-DD`;
the time component and timezone offset (`HH:MM:SS+TTTT`) are discarded.  
**Rule W-2 (`filename`):** Basename of the file without directory path, e.g.,
`"announcement_1.md"`.  
**Rule W-3 (`body_markdown`):** Raw Markdown body of the file (content after the
closing `---`) with leading and trailing whitespace stripped; internal line breaks
preserved.  
**Rule W-4:** Boolean front-matter keys default to `false` when absent.  
**Rule W-5:** No `null` values in any news record.

---

## 7. `cv` Object

Sources: `_data/cv.yml` (data), `_pages/cv.md` (front matter: `cv_pdf`).

### 7.1 Top-Level CV Fields — Field Order

| # | Field | Type | Empty value |
|---|-------|------|-------------|
| 1 | `name` | `string` | `""` |
| 2 | `label` | `string` | `""` |
| 3 | `email` | `string` | `""` |
| 4 | `location` | `string` | `""` |
| 5 | `summary` | `string` | `""` |
| 6 | `pdf_path` | `string` | `""` |
| 7 | `social_networks` | `array` | `[]` |
| 8 | `education` | `array` | `[]` |
| 9 | `experience` | `array` | `[]` |
| 10 | `awards` | `array` | `[]` |
| 11 | `skills` | `array` | `[]` |
| 12 | `languages` | `array` | `[]` |

### 7.2 Sub-Record Schemas

**`social_network` record** (field order):

| # | Field | Type | Empty value |
|---|-------|------|-------------|
| 1 | `network` | `string` | `""` |
| 2 | `username` | `string` | `""` |

**`education` record** (field order):

| # | Field | Type | Empty value |
|---|-------|------|-------------|
| 1 | `institution` | `string` | `""` |
| 2 | `location` | `string` | `""` |
| 3 | `area` | `string` | `""` |
| 4 | `study_type` | `string` | `""` |
| 5 | `start_date` | `string` | `""` |
| 6 | `end_date` | `string` | `""` |

**`experience` record** (field order):

| # | Field | Type | Empty value |
|---|-------|------|-------------|
| 1 | `company` | `string` | `""` |
| 2 | `position` | `string` | `""` |
| 3 | `location` | `string` | `""` |
| 4 | `start_date` | `string` | `""` |
| 5 | `end_date` | `string` | `""` |
| 6 | `highlights` | `array<string>` | `[]` |

**`award` record** (field order):

| # | Field | Type | Empty value |
|---|-------|------|-------------|
| 1 | `title` | `string` | `""` |
| 2 | `date` | `string` | `""` |
| 3 | `awarder` | `string` | `""` |

**`skill` record** (field order):

| # | Field | Type | Empty value |
|---|-------|------|-------------|
| 1 | `name` | `string` | `""` |
| 2 | `level` | `string` | `""` |
| 3 | `icon` | `string` | `""` |
| 4 | `keywords` | `array<string>` | `[]` |

**`language` record** (field order):

| # | Field | Type | Empty value |
|---|-------|------|-------------|
| 1 | `name` | `string` | `""` |
| 2 | `summary` | `string` | `""` |

### 7.3 Ordering Constraints

**Rule C-1 (`education`):** Sorted descending by `start_date` (most recent first).  
**Rule C-2 (`experience`):** Sorted descending by `start_date` (most recent first).  
**Rule C-3 (`awards`):** Sorted descending by `date`.  
**Rule C-4 (`social_networks`, `skills`, `languages`):** Preserve YAML source order;
no re-sorting applied.

### 7.4 Normalization Rules

**Rule V-1:** All string values trimmed of whitespace.  
**Rule V-2:** Year-only dates from YAML (e.g., `start_date: 2024`) are serialized as
four-digit strings: `"2024"`.  
**Rule V-3:** Month-precision dates from YAML (e.g., `start_date: 2024-06`) are
serialized as `"YYYY-MM"` strings: `"2024-06"`.  
**Rule V-4:** The literal string `Present` for `end_date` is preserved as `"Present"`.  
**Rule V-5 (`pdf_path`):** Taken from the `cv_pdf` key in `_pages/cv.md` front matter;
`""` if absent.  
**Rule V-6:** No `null` values anywhere in the cv object.

---

## 8. Global Empty-Value Policy

Applies to every section. When a source field is present but blank, null, or absent:

| JSON type | Empty representation |
|-----------|---------------------|
| `string` | `""` |
| `boolean` | `false` |
| `integer` | `0` |
| `array` | `[]` |

**Rule E-1:** `null` MUST NOT appear anywhere in the artifact.  
**Rule E-2:** No field defined in any schema in this contract may be omitted from any
record.  
**Rule E-3:** Empty string `""` is the correct sentinel for absent optional string
fields (not `null`, not the string `"null"`, not `"N/A"`).

---

## 9. Ordering Constraint Summary

| Array | Primary sort | Tie-breaker |
|-------|-------------|-------------|
| `publications` | `year` desc | `is_first_author` desc → `co_first_author` desc → source order |
| `news` | `date` desc | `filename` asc |
| `cv.education` | `start_date` desc | source order |
| `cv.experience` | `start_date` desc | source order |
| `cv.awards` | `date` desc | source order |
| `cv.social_networks` | source order | — |
| `cv.skills` | source order | — |
| `cv.languages` | source order | — |

---

## 10. Review-Branch Convention

The artifact files MUST be committed to a branch named
`review/personal-website-content-render` in `mcpmark-eval-1031/LUFFY`,
branched from `main`. The three deliverables are:

| File | Description |
|------|-------------|
| `render_contract.md` | This document (frozen schema). |
| `render_preview.json` | Contract-conforming JSON artifact. |
| `contract_checklist.md` | Verification checklist. |

---

## 11. Contract Freeze Declaration

> **This contract is FROZEN as of 2026-04-09.**  
> No field names, field positions, empty-value policies, normalization rules,  
> or ordering constraints may be altered after this declaration without  
> incrementing `schema_version` and re-issuing a new frozen contract.  
> `render_preview.json` and `contract_checklist.md` MUST be regenerated  
> whenever this contract changes.
