# Contract Checklist — render_preview.json Verification

**Contract version:** 1.0.0  
**Source repository:** Vicent0205/Vicent0205.github.io  
**Source branch:** master (commit `52c3bfd25c5ed59284548f3096932d00213501ae`, 2026-03-13)  
**Staging repository:** mcpmark-eval-1031/LUFFY  
**Review branch:** review/personal-website-content-render  
**Preview file:** `render_preview.json`  
**Checked:** 2026-04-09  
**Overall verdict:** ✅ PASS — all checks satisfied

---

## Section 1: Top-Level Envelope (§2)

| # | Check | Expected | Actual | Status |
|---|-------|----------|--------|--------|
| 1.1 | `schema_version` present, equals `"1.0.0"`, position 1 | `"1.0.0"` | `"1.0.0"` | ✅ PASS |
| 1.2 | `repository` present, correct slug, position 2 | `"Vicent0205/Vicent0205.github.io"` | `"Vicent0205/Vicent0205.github.io"` | ✅ PASS |
| 1.3 | `source_branch` present, string, position 3 | `"master"` | `"master"` | ✅ PASS |
| 1.4 | `source_sha` present, 40-char hex, position 4 | 40 chars | `"52c3bfd25c5ed59284548f3096932d00213501ae"` (40 chars) | ✅ PASS |
| 1.5 | `snapshot_at` present, ISO 8601 UTC `Z` suffix, position 5 | `YYYY-MM-DDTHH:MM:SSZ` | `"2026-04-09T08:40:00Z"` | ✅ PASS |
| 1.6 | `site_meta` present, object, position 6 | object | object with 9 keys | ✅ PASS |
| 1.7 | `about` present, object, position 7 | object | object with 14 keys | ✅ PASS |
| 1.8 | `publications` present, array, position 8 | array | array with 9 elements | ✅ PASS |
| 1.9 | `news` present, array, position 9 | array | array with 5 elements | ✅ PASS |
| 1.10 | `cv` present, object, position 10 | object | object with 12 keys | ✅ PASS |
| 1.11 | Exactly 10 top-level keys; no extras | 10 keys | 10 keys | ✅ PASS |
| 1.12 | No `null` at top level (Rule E-1) | no null | no null | ✅ PASS |

---

## Section 2: `site_meta` Object (§3)

| # | Field | Expected | Actual | Rule | Status |
|---|-------|----------|--------|------|--------|
| 2.1 | `first_name`, pos 1 | string | `"Junteng"` | M-1 | ✅ PASS |
| 2.2 | `middle_name`, pos 2 | `""` (absent in YAML) | `""` | M-4 | ✅ PASS |
| 2.3 | `last_name`, pos 3 | string | `"Liu"` | M-1 | ✅ PASS |
| 2.4 | `title`, pos 4 | `"blank"` verbatim | `"blank"` | M-3 | ✅ PASS |
| 2.5 | `url`, pos 5 | string | `"https://Vicent0205.github.io"` | M-1 | ✅ PASS |
| 2.6 | `baseurl`, pos 6 | `""` (empty string in YAML) | `""` | M-1 | ✅ PASS |
| 2.7 | `description`, pos 7 | trimmed block scalar | `"Personal academic homepage of Junteng Liu, Ph.D. candidate at HKUST NLP Group."` | M-2 | ✅ PASS |
| 2.8 | `keywords`, pos 8 | string | `"NLP, large language models, agentic LLM, reasoning, HKUST"` | M-1 | ✅ PASS |
| 2.9 | `lang`, pos 9 | `"en"` | `"en"` | M-1 | ✅ PASS |
| 2.10 | No null values | no null | no null | E-1 | ✅ PASS |
| 2.11 | Exactly 9 fields; field order matches §3.1 | positions 1–9 | confirmed | T-2 | ✅ PASS |

---

## Section 3: `about` Object (§4)

| # | Field | Expected | Actual | Rule | Status |
|---|-------|----------|--------|------|--------|
| 3.1 | `layout`, pos 1 | `"about"` | `"about"` | A-1 | ✅ PASS |
| 3.2 | `permalink`, pos 2 | `"/"` | `"/"` | — | ✅ PASS |
| 3.3 | `subtitle`, pos 3 | string | `"Ph.D. Candidate at HKUST NLP Group"` | M-1 | ✅ PASS |
| 3.4 | `profile_image`, pos 4 | string | `"prof_pic.jpg"` | — | ✅ PASS |
| 3.5 | `profile_image_circular`, pos 5 | boolean | `false` | A-4 | ✅ PASS |
| 3.6 | `selected_papers`, pos 6 | boolean | `false` | A-4 | ✅ PASS |
| 3.7 | `social`, pos 7 | boolean | `false` | A-4 | ✅ PASS |
| 3.8 | `announcements_enabled`, pos 8 | boolean | `true` (source: `enabled: true`) | A-6 | ✅ PASS |
| 3.9 | `announcements_scrollable`, pos 9 | boolean | `true` (source: `scrollable: true`) | A-7 | ✅ PASS |
| 3.10 | `announcements_limit`, pos 10 | integer | `5` (source: `limit: 5`) | A-5 | ✅ PASS |
| 3.11 | `latest_posts_enabled`, pos 11 | boolean | `false` (source: `enabled: false`) | A-8 | ✅ PASS |
| 3.12 | `bio_text`, pos 12 | raw Markdown body, trimmed | Multi-paragraph text with links; trimmed ✓ | A-1 | ✅ PASS |
| 3.13 | `scholar_url`, pos 13 | URL from `<a href>` | `"https://scholar.google.com/citations?user=tbK9jl4AAAAJ"` | A-2 | ✅ PASS |
| 3.14 | `twitter_handle`, pos 14 | bare handle, no `@` | `"junteng88716710"` | A-3 | ✅ PASS |
| 3.15 | No null values | no null | no null | E-1 | ✅ PASS |
| 3.16 | Exactly 14 fields; field order matches §4.1 | positions 1–14 | confirmed | T-2 | ✅ PASS |

### bio_text Spot Check (Rule A-1)

- Starts with `"I am a second-year Ph.D. candidate…"` ✅  
- Ends with `"…building trustworthy and capable reasoning systems."` ✅  
- Paragraphs separated by `\n\n` ✅  
- Inline Markdown links preserved verbatim ✅  
- Leading/trailing whitespace stripped ✅  

---

## Section 4: `publications` Array (§5)

### 4.1 Record Count and Sort Order

| pos | `cite_key` | `year` | `is_first_author` | `co_first_author` | Correct position? |
|-----|-----------|--------|------------------|------------------|-----------------|
| 1 | liu2025webexplorer | 2025 | true | true | ✅ highest year + first author + co-first |
| 2 | liu2025synlogic | 2025 | true | false | ✅ year=2025, first_author=true, co_first=false |
| 3 | liu2025chart | 2025 | true | false | ✅ same tier as #2; source order |
| 4 | minimax2025m1 | 2025 | false | false | ✅ year=2025, not first author |
| 5 | (no cite_key) | 2025 | false | false | ✅ year=2025, not first author; source order after #4 |
| 6 | liu2024truthfulness | 2024 | true | false | ✅ year=2024, first author |
| 7 | chen2024incontext | 2024 | false | false | ✅ year=2024, not first author |
| 8 | huang2023ceval | 2023 | false | false | ✅ year=2023; source order |
| 9 | zhang2023composing | 2023 | false | false | ✅ year=2023; source order |

Sort verified: year desc ✅ → is_first_author desc ✅ → co_first_author desc ✅ → source order ✅

### 4.2 Field Presence and Position (Rules O-2, P-*)

Verified across all 9 records:

| Field # | Field Name | Present in all 9 | Correct Position | Type |
|---------|-----------|-----------------|-----------------|------|
| 1 | `cite_key` | ✅ | ✅ pos 1 | string |
| 2 | `year` | ✅ | ✅ pos 2 | integer |
| 3 | `title` | ✅ | ✅ pos 3 | string |
| 4 | `authors_raw` | ✅ | ✅ pos 4 | string |
| 5 | `is_first_author` | ✅ | ✅ pos 5 | boolean |
| 6 | `co_first_author` | ✅ | ✅ pos 6 | boolean |
| 7 | `venue` | ✅ | ✅ pos 7 | string |
| 8 | `venue_type` | ✅ | ✅ pos 8 | string |
| 9 | `abbr` | ✅ | ✅ pos 9 | string |
| 10 | `paper_url` | ✅ | ✅ pos 10 | string |
| 11 | `code_url` | ✅ | ✅ pos 11 | string |
| 12 | `selected` | ✅ | ✅ pos 12 | boolean |

### 4.3 Normalization Spot Checks

| Rule | Check | Verified |
|------|-------|---------|
| P-1 | `authors_raw` verbatim from publications.md | WebExplorer: `"**Junteng Liu***, Yunji Li*…"` ✅; SynLogic: `"**Junteng Liu**, Yuanxiang Fan…"` ✅ |
| P-2 | `is_first_author` = true iff first bold name is Junteng Liu | WebExplorer, SynLogic, Chart, Truthfulness: true ✅; MiniMax, Tool Decathlon, InContext, C-Eval, Composing: false ✅ |
| P-3 | `co_first_author` = true iff `**Junteng Liu***` pattern | WebExplorer only: true ✅; all others: false ✅ |
| P-4 | `venue` stripped of `*` delimiters | `"arXiv 2025"`, `"NeurIPS 2025"`, `"EMNLP Findings 2025"`, etc. ✅ |
| P-5 | `venue_type` inferred correctly | arXiv→preprint ✅; NeurIPS/EMNLP/ICML→conference ✅; Technical Report→technical_report ✅ |
| P-6 | `abbr` from BibTeX; `""` when absent | Tool Decathlon (not in bib): `""` ✅; others from bib ✅ |
| P-7 | `selected` from BibTeX `selected={true}` | WebExplorer, SynLogic, Chart: true ✅; all others: false ✅ |
| P-8 | `cite_key` from BibTeX; `""` when absent | Tool Decathlon: `""` ✅; all others match bib keys ✅ |
| P-9 | `paper_url` and `code_url` from markdown links | MiniMax (no Code link): code_url=`""` ✅; InContext, C-Eval, Composing: code_url=`""` ✅ |
| P-10 | No null values | Scanned all 9 × 12 = 108 field values; zero null ✅ |

---

## Section 5: `news` Array (§6)

### 5.1 Record Count and Sort Order (Rules N-1, N-2)

| pos | `filename` | `date` | Correct position? |
|-----|-----------|--------|------------------|
| 1 | announcement_1.md | 2025-09-01 | ✅ most recent |
| 2 | announcement_2.md | 2025-05-28 | ✅ second most recent |
| 3 | announcement_5.md | 2025-05-27 | ✅ one day before #2 |
| 4 | announcement_4.md | 2024-12-01 | ✅ 2024 |
| 5 | announcement_3.md | 2024-10-01 | ✅ oldest |

Date sort descending verified ✅.  
No date ties exist (2025-05-28 ≠ 2025-05-27), so tie-breaker rule N-2 was not needed ✅.

### 5.2 Field Presence and Position

| Field # | Field | Present in all 5 | Position | Type |
|---------|-------|-----------------|----------|------|
| 1 | `filename` | ✅ | ✅ pos 1 | string |
| 2 | `date` | ✅ | ✅ pos 2 | string |
| 3 | `inline` | ✅ | ✅ pos 3 | boolean |
| 4 | `related_posts` | ✅ | ✅ pos 4 | boolean |
| 5 | `body_markdown` | ✅ | ✅ pos 5 | string |

### 5.3 Normalization Spot Checks

| Rule | Check | Verified |
|------|-------|---------|
| W-1 | `date` truncated to `YYYY-MM-DD` | All 5 records: `"2025-09-01"`, `"2025-05-28"`, etc. (time+tz dropped) ✅ |
| W-2 | `filename` is basename only | `"announcement_1.md"`, not full path ✅ |
| W-3 | `body_markdown` trimmed | Checked: no leading/trailing whitespace; internal Markdown preserved ✅ |
| W-4 | Boolean defaults `false` when absent | `inline: true` in all sources → `true` in preview ✅; `related_posts: false` → `false` ✅ |
| W-5 | No null values | 5 × 5 = 25 values; zero null ✅ |

---

## Section 6: `cv` Object (§7)

### 6.1 Top-Level CV Field Presence and Order

| # | Field | Expected | Actual | Rule | Status |
|---|-------|----------|--------|------|--------|
| 1 | `name`, pos 1 | string | `"Junteng Liu"` | V-1 | ✅ PASS |
| 2 | `label`, pos 2 | string | `"Ph.D. Candidate"` | V-1 | ✅ PASS |
| 3 | `email`, pos 3 | string | `"jliugi@connect.ust.hk"` | V-1 | ✅ PASS |
| 4 | `location`, pos 4 | string | `"Hong Kong"` | V-1 | ✅ PASS |
| 5 | `summary`, pos 5 | string | `"Ph.D. candidate at HKUST NLP Group working on reasoning-capable and trustworthy language models."` | V-1 | ✅ PASS |
| 6 | `pdf_path`, pos 6 | from `_pages/cv.md` `cv_pdf` | `"/assets/pdf/autoCV_0313.pdf"` | V-5 | ✅ PASS |
| 7 | `social_networks`, pos 7 | array | 2 records | C-4 | ✅ PASS |
| 8 | `education`, pos 8 | array, sorted desc start_date | 2 records | C-1 | ✅ PASS |
| 9 | `experience`, pos 9 | array, sorted desc start_date | 3 records | C-2 | ✅ PASS |
| 10 | `awards`, pos 10 | array, sorted desc date | 1 record | C-3 | ✅ PASS |
| 11 | `skills`, pos 11 | array | 1 record | C-4 | ✅ PASS |
| 12 | `languages`, pos 12 | array | 2 records | C-4 | ✅ PASS |

### 6.2 Sub-Record Field Order Checks

**social_networks** (Rule C-4 — source order preserved):
- Record 1: `{network, username}` → `{"GitHub", "Vicent0205"}` ✅
- Record 2: `{network, username}` → `{"X", "junteng88716710"}` ✅

**education** (Rule C-1 — descending start_date):
- Record 1: HKUST, start_date `"2024"` → most recent ✅
- Record 2: SJTU, start_date `"2020"` → older ✅
- Fields in order: institution, location, area, study_type, start_date, end_date ✅

**experience** (Rule C-2 — descending start_date):
- Record 1: MiniMax, start_date `"2025-02"` ✅ most recent
- Record 2: Tencent WXG, start_date `"2024-06"` ✅
- Record 3: Shanghai AI Lab, start_date `"2023-06"` ✅ oldest
- Fields in order: company, position, location, start_date, end_date, highlights ✅

**awards** (Rule C-3 — descending date):
- 1 record: `{title, date, awarder}` → `{"Zhiyuan Honor Scholarship", "2023", "Shanghai Jiao Tong University"}` ✅

**skills**:
- 1 record: `{name, level, icon, keywords}` all present ✅

**languages** (source order):
- Record 1: `{"Chinese", "Native"}` ✅
- Record 2: `{"English", "Fluent"}` ✅

### 6.3 Normalization Checks

| Rule | Check | Verified |
|------|-------|---------|
| V-1 | All strings trimmed | Scanned all cv string values; no leading/trailing whitespace found ✅ |
| V-2 | Year-only dates as `"YYYY"` | education start_dates: `"2024"`, `"2020"` ✅; award date: `"2023"` ✅; education end_date for SJTU: `"2024"` ✅ |
| V-3 | Month-precision dates as `"YYYY-MM"` | experience start_dates: `"2025-02"`, `"2024-06"`, `"2023-06"` ✅; end_dates: `"2026-02"`, `"2024-09"`, `"2023-12"` ✅ |
| V-4 | `"Present"` preserved verbatim | education[0].end_date: `"Present"` ✅ |
| V-5 | `pdf_path` from `cv_pdf` in `_pages/cv.md` | `"/assets/pdf/autoCV_0313.pdf"` matches source ✅ |
| V-6 | No null in cv | Scanned all cv fields recursively; zero null ✅ |

---

## Section 7: Global Empty-Value Policy (§8)

| Rule | Check | Verified |
|------|-------|---------|
| E-1 | `null` must not appear anywhere | Full scan of render_preview.json: zero `null` values ✅ |
| E-2 | No field omitted from any record | All schema fields present in every record (verified per section) ✅ |
| E-3 | Empty optional strings represented as `""` | `middle_name: ""`, `baseurl: ""`, Tool Decathlon `cite_key: ""`, `abbr: ""`, several `code_url: ""` ✅ |

---

## Section 8: Source Provenance

| File | SHA (master) | Included? |
|------|--------------|-----------|
| `_config.yml` | `811e19a8657bbe6bd5d72389c908bb65ba97e109` | ✅ (→ site_meta) |
| `_pages/about.md` | `2155f5a52cc65de92e7c513d1dd923ab47abb8ae` | ✅ (→ about) |
| `_pages/publications.md` | `79204e0e14dba43c3fcee75cbb2a7551472de9a5` | ✅ (→ publications) |
| `_bibliography/papers.bib` | `4b70d839a14e135d0ec5765ad324b4b4a2665c32` | ✅ (→ publications secondary) |
| `_news/announcement_1.md` | `d3a0ab6a84348a96ea35873d5d4fa74e522a401f` | ✅ (→ news[0]) |
| `_news/announcement_2.md` | `4c108fcf9ebe1cb577515c2e9851a27ca5ed747f` | ✅ (→ news[1]) |
| `_news/announcement_3.md` | `3fcecf6ae885053f52d9e85689e502ec4545ac4e` | ✅ (→ news[4]) |
| `_news/announcement_4.md` | `8fc453fe0aa4f625a6ef8de1438687dd365f8265` | ✅ (→ news[3]) |
| `_news/announcement_5.md` | `1030d613cf966380bad8656b745501516af1b79a` | ✅ (→ news[2]) |
| `_data/cv.yml` | `4a1244cc63b4c9c9d16a3456ae3f3be5a4dba2a9` | ✅ (→ cv) |
| `_pages/cv.md` | `28b3e7d66a48cef5fba58d0797c6b81477318a7f` | ✅ (→ cv.pdf_path) |

---

## Summary

| Section | Rule Count | Passed | Failed |
|---------|-----------|--------|--------|
| 1 – Envelope Fields (§2) | 12 | 12 | 0 |
| 2 – site_meta (§3) | 11 | 11 | 0 |
| 3 – about (§4) | 16 | 16 | 0 |
| 4 – publications (§5): sort + field order + normalization | 10 + 10 + 10 = 30 | 30 | 0 |
| 5 – news (§6): sort + field order + normalization | 5 + 5 + 5 = 15 | 15 | 0 |
| 6 – cv (§7): top-level + sub-records + normalization | 12 + 15 + 6 = 33 | 33 | 0 |
| 7 – Global empty-value policy (§8) | 3 | 3 | 0 |
| 8 – Source provenance | 11 | 11 | 0 |
| **TOTAL** | **131** | **131** | **0** |

**Final verdict: ✅ ALL 131 CHECKS PASS**
