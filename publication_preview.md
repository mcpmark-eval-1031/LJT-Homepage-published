# Publication preview — new `_publications/` entries for Junteng Liu's homepage

- **Site of record:** `mcpmark-eval-1031/LJT-Homepage` @ `master` (academicpages / Jekyll)
- **Owner:** Junteng Liu — first-year PhD candidate, HKUST NLP Group
- **Companion file:** `publication_fields.csv` — one row per target paper, 24 parsed fields
- **Target papers:** the six papers of the site's publication set, newest first

---

## 0. The style these entries are written in

Read off the site itself, not assumed:

| Surface | File | What it fixes |
|---|---|---|
| Collection | `_config.yml` → `collections.publications` | one Markdown file per paper in `_publications/`, `output: true`, permalink `/:collection/:path/` |
| Categories | `_config.yml` → `publication_category` | `books` → *Books*, `manuscripts` → *Journal Articles*, `conferences` → *Conference Papers*, `preprints` → *Preprints* |
| Listing page | `_pages/publications.html` | walks `site.publication_category` in declaration order, and inside each category `{% for post in site.publications reversed %}` |
| Item renderer | `_includes/archive-single.html` | prints `Published in <i>{{ post.venue }}</i>, {{ post.date \| date: "%Y" }}`, then `post.excerpt`, then `Recommended citation: {{ post.citation }}` and a `Download Paper` link whenever `paperurl` is set |
| File naming | `markdown_generator/publications.py` | `YYYY-MM-DD-<url_slug>.md`, permalink `/publication/<…>` |
| Existing entries | `_publications/*.md` | front matter `title, collection, category, permalink, excerpt, date, venue, codeurl, citation`; body `**Authors:** …` / `**Venue:** …` / `[Code](…)` |

Two consequences worth stating, because they shape every entry below:

1. `archive-single.html` renders only `paperurl`, `slidesurl` and `bibtexurl` as links — **not** `codeurl`. The site therefore carries `codeurl` in the front matter *and* repeats it as a `[Code](…)` link in the body. Both are kept.
2. `date` is not display metadata: it drives the file name, the `%Y` shown after the venue, and the position in the reversed listing.

File names follow the collection's `YYYY-MM-DD-<slug>.md` convention and the permalinks keep the site's existing `/publication/<year>-<slug>` form, so no already-published link breaks.

---

## A. New `_publications/` entries

### 1. `_publications/2025-12-01-synlogic.md`

```markdown
---
title: "SynLogic: Synthesizing Verifiable Reasoning Data at Scale for Learning Logical Reasoning and Beyond"
collection: publications
category: conferences
permalink: /publication/2025-synlogic
excerpt: 'Synthesizing verifiable reasoning data at scale for learning logical reasoning and beyond'
date: 2025-12-01
venue: 'NeurIPS 2025'
paperurl: 'https://arxiv.org/abs/2505.19641'
codeurl: 'https://github.com/MiniMax-AI/SynLogic'
citation: 'Junteng Liu, Yuanxiang Fan, Zhuo Jiang, Han Ding, Yongyi Hu, Chi Zhang, Yiqi Shi, Shitong Weng, Aili Chen, Shiqi Chen, Yunan Huang, Mozhi Zhang, Pengyu Zhao, Junjie Yan, Junxian He. (2025). "SynLogic: Synthesizing Verifiable Reasoning Data at Scale for Learning Logical Reasoning and Beyond." <i>NeurIPS 2025</i>.'
---

**Authors:** Junteng Liu, Yuanxiang Fan, Zhuo Jiang, Han Ding, Yongyi Hu, Chi Zhang, Yiqi Shi, Shitong Weng, Aili Chen, Shiqi Chen, Yunan Huang, Mozhi Zhang, Pengyu Zhao, Junjie Yan, Junxian He

**Venue:** NeurIPS 2025

[Code](https://github.com/MiniMax-AI/SynLogic) | [Data](https://huggingface.co/datasets/MiniMaxAI/SynLogic)
```

### 2. `_publications/2025-03-01-vlm-chart.md`

```markdown
---
title: "On the Perception Bottleneck of VLMs for Chart Understanding"
collection: publications
category: preprints
permalink: /publication/2025-vlm-chart
excerpt: 'On the perception bottleneck of vision-language models for chart understanding'
date: 2025-03-01
venue: 'arXiv preprint'
paperurl: 'https://arxiv.org/abs/2503.18435'
codeurl: 'https://github.com/hkust-nlp/Vision4Chart'
citation: 'Junteng Liu, Weihao Zeng, Xiwen Zhang, Yijun Wang, Zifei Shan, Junxian He. (2025). "On the Perception Bottleneck of VLMs for Chart Understanding." <i>arXiv preprint</i>.'
---

**Authors:** Junteng Liu, Weihao Zeng, Xiwen Zhang, Yijun Wang, Zifei Shan, Junxian He

**Venue:** arXiv preprint, 2025

[Code](https://github.com/hkust-nlp/Vision4Chart) | [Data](https://huggingface.co/datasets/Junteng/Vision4Chart)
```

### 3. `_publications/2024-12-01-universal-truthfulness-hyperplane.md`

```markdown
---
title: "On the Universal Truthfulness Hyperplane Inside LLMs"
collection: publications
category: conferences
permalink: /publication/2024-universal-truthfulness-hyperplane
excerpt: 'On the universal truthfulness hyperplane inside LLMs'
date: 2024-12-01
venue: 'EMNLP 2024'
paperurl: 'https://arxiv.org/abs/2407.08582'
codeurl: 'https://github.com/hkust-nlp/Universal_Truthfulness_Hyperplane'
citation: 'Junteng Liu, Shiqi Chen, Yu Cheng, Junxian He. (2024). "On the Universal Truthfulness Hyperplane Inside LLMs." <i>EMNLP 2024</i>.'
---

**Authors:** Junteng Liu, Shiqi Chen, Yu Cheng, Junxian He

**Venue:** EMNLP 2024

[Code](https://github.com/hkust-nlp/Universal_Truthfulness_Hyperplane)
```

### 4. `_publications/2024-07-01-in-context-sharpness-alerts.md`

```markdown
---
title: "In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation"
collection: publications
category: conferences
permalink: /publication/2024-in-context-sharpness-alerts
excerpt: 'In-context sharpness as alerts: an inner representation perspective for hallucination mitigation'
date: 2024-07-01
venue: 'ICML 2024'
paperurl: 'https://arxiv.org/abs/2403.01548'
codeurl: 'https://github.com/hkust-nlp/Activation_Decoding'
citation: 'Shiqi Chen, Miao Xiong, Junteng Liu, Zhengxuan Wu, Teng Xiao, Siyang Gao, Junxian He. (2024). "In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation." <i>ICML 2024</i>.'
---

**Authors:** Shiqi Chen, Miao Xiong, Junteng Liu, Zhengxuan Wu, Teng Xiao, Siyang Gao, Junxian He

**Venue:** ICML 2024

[Code](https://github.com/hkust-nlp/Activation_Decoding)
```

### 5. `_publications/2023-12-01-c-eval.md`

```markdown
---
title: "C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models"
collection: publications
category: conferences
permalink: /publication/2023-c-eval
excerpt: 'A multi-level multi-discipline Chinese evaluation suite for foundation models'
date: 2023-12-01
venue: 'NeurIPS 2023'
paperurl: 'https://arxiv.org/abs/2305.08322'
codeurl: 'https://github.com/hkust-nlp/ceval'
citation: 'Yuzhen Huang, Yuzhuo Bai, Zhihao Zhu, Junlei Zhang, Jinghan Zhang, Tangjun Su, Junteng Liu, Chuancheng Lv, Yikai Zhang, Jiayi Lei, Yao Fu, Maosong Sun, Junxian He. (2023). "C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models." <i>NeurIPS 2023</i>.'
---

**Authors:** Yuzhen Huang, Yuzhuo Bai, Zhihao Zhu, Junlei Zhang, Jinghan Zhang, Tangjun Su, Junteng Liu, Chuancheng Lv, Yikai Zhang, Jiayi Lei, Yao Fu, Maosong Sun, Junxian He

**Venue:** NeurIPS 2023

[Code](https://github.com/hkust-nlp/ceval) | [Data](https://huggingface.co/datasets/ceval/ceval-exam)
```

### 6. `_publications/2023-12-01-composing-modules.md`

```markdown
---
title: "Composing Parameter-Efficient Modules with Arithmetic Operations"
collection: publications
category: conferences
permalink: /publication/2023-composing-modules
excerpt: 'Composing parameter-efficient modules with arithmetic operations'
date: 2023-12-01
venue: 'NeurIPS 2023'
paperurl: 'https://arxiv.org/abs/2306.14870'
codeurl: 'https://github.com/hkust-nlp/PEM_composition'
citation: 'Jinghan Zhang, Shiqi Chen, Junteng Liu, Junxian He. (2023). "Composing Parameter-Efficient Modules with Arithmetic Operations." <i>NeurIPS 2023</i>.'
---

**Authors:** Jinghan Zhang, Shiqi Chen, Junteng Liu, Junxian He

**Venue:** NeurIPS 2023

[Code](https://github.com/hkust-nlp/PEM_composition) | [Data](https://huggingface.co/datasets/jinghan23/DatasetofPEMCompostition)
```

---

## B. How they come out on `/publications/`

`_pages/publications.html` walks `publication_category` in `_config.yml` order (`books`, `manuscripts`, `conferences`, `preprints`), skips categories with no posts, and reverses each group. Nothing in this set is a book or a journal article, so the page reads:

### Conference Papers

> **SynLogic: Synthesizing Verifiable Reasoning Data at Scale for Learning Logical Reasoning and Beyond**
> Published in *NeurIPS 2025*, 2025
> Synthesizing verifiable reasoning data at scale for learning logical reasoning and beyond
> Recommended citation: Junteng Liu, Yuanxiang Fan, Zhuo Jiang, Han Ding, Yongyi Hu, Chi Zhang, Yiqi Shi, Shitong Weng, Aili Chen, Shiqi Chen, Yunan Huang, Mozhi Zhang, Pengyu Zhao, Junjie Yan, Junxian He. (2025). "SynLogic: Synthesizing Verifiable Reasoning Data at Scale for Learning Logical Reasoning and Beyond." *NeurIPS 2025*.
> [Download Paper](https://arxiv.org/abs/2505.19641)

> **On the Universal Truthfulness Hyperplane Inside LLMs**
> Published in *EMNLP 2024*, 2024
> On the universal truthfulness hyperplane inside LLMs
> Recommended citation: Junteng Liu, Shiqi Chen, Yu Cheng, Junxian He. (2024). "On the Universal Truthfulness Hyperplane Inside LLMs." *EMNLP 2024*.
> [Download Paper](https://arxiv.org/abs/2407.08582)

> **In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation**
> Published in *ICML 2024*, 2024
> In-context sharpness as alerts: an inner representation perspective for hallucination mitigation
> Recommended citation: Shiqi Chen, Miao Xiong, Junteng Liu, Zhengxuan Wu, Teng Xiao, Siyang Gao, Junxian He. (2024). "In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation." *ICML 2024*.
> [Download Paper](https://arxiv.org/abs/2403.01548)

> **Composing Parameter-Efficient Modules with Arithmetic Operations**
> Published in *NeurIPS 2023*, 2023
> Composing parameter-efficient modules with arithmetic operations
> Recommended citation: Jinghan Zhang, Shiqi Chen, Junteng Liu, Junxian He. (2023). "Composing Parameter-Efficient Modules with Arithmetic Operations." *NeurIPS 2023*.
> [Download Paper](https://arxiv.org/abs/2306.14870)

> **C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models**
> Published in *NeurIPS 2023*, 2023
> A multi-level multi-discipline Chinese evaluation suite for foundation models
> Recommended citation: Yuzhen Huang, Yuzhuo Bai, Zhihao Zhu, Junlei Zhang, Jinghan Zhang, Tangjun Su, Junteng Liu, Chuancheng Lv, Yikai Zhang, Jiayi Lei, Yao Fu, Maosong Sun, Junxian He. (2023). "C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models." *NeurIPS 2023*.
> [Download Paper](https://arxiv.org/abs/2305.08322)

### Preprints

> **On the Perception Bottleneck of VLMs for Chart Understanding**
> Published in *arXiv preprint*, 2025
> On the perception bottleneck of vision-language models for chart understanding
> Recommended citation: Junteng Liu, Weihao Zeng, Xiwen Zhang, Yijun Wang, Zifei Shan, Junxian He. (2025). "On the Perception Bottleneck of VLMs for Chart Understanding." *arXiv preprint*.
> [Download Paper](https://arxiv.org/abs/2503.18435)

*Ordering notes.* Every position above is a pure reverse-chronological `date` ordering, except the two papers that share `2023-12-01`: Jekyll breaks that tie on the document path, so ascending order is `2023-12-01-c-eval.md` then `2023-12-01-composing-modules.md`, and `reversed` puts **composing-modules ahead of c-eval**. "Conference Papers" precedes "Preprints" because that is the order the two categories are declared in `_config.yml`, not because of any date.

*Link notes.* `Download Paper` appears for all six because each entry now sets `paperurl`; `read_more` is `"disabled"` in `_config.yml`, so the excerpt is rendered in full with no "Read more" tail. The `[Code]` / `[Data]` links live in the entry body (the individual `/publications/<file>/` page), not in this listing, because `archive-single.html` has no `codeurl` branch.

---

## C. Same six entries in the about-page list style

`_pages/about.md` lists publications grouped by year, numbered, with the site owner's name in bold:

```markdown
## Publications

### 2025

1. **SynLogic: Synthesizing Verifiable Reasoning Data at Scale for Learning Logical Reasoning and Beyond**  
   **Junteng Liu**, Yuanxiang Fan, Zhuo Jiang, Han Ding, Yongyi Hu, Chi Zhang, Yiqi Shi, Shitong Weng, Aili Chen, Shiqi Chen, Yunan Huang, Mozhi Zhang, Pengyu Zhao, Junjie Yan, Junxian He  
   *NeurIPS 2025*  
   [Paper](https://arxiv.org/abs/2505.19641) | [Code](https://github.com/MiniMax-AI/SynLogic) | [Data](https://huggingface.co/datasets/MiniMaxAI/SynLogic)

2. **On the Perception Bottleneck of VLMs for Chart Understanding**  
   **Junteng Liu**, Weihao Zeng, Xiwen Zhang, Yijun Wang, Zifei Shan, Junxian He  
   *arXiv preprint, 2025*  
   [Paper](https://arxiv.org/abs/2503.18435) | [Code](https://github.com/hkust-nlp/Vision4Chart) | [Data](https://huggingface.co/datasets/Junteng/Vision4Chart)

### 2024

3. **On the Universal Truthfulness Hyperplane Inside LLMs**  
   **Junteng Liu**, Shiqi Chen, Yu Cheng, Junxian He  
   *Proceedings of EMNLP 2024*  
   [Paper](https://arxiv.org/abs/2407.08582) | [Code](https://github.com/hkust-nlp/Universal_Truthfulness_Hyperplane)

4. **In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation**  
   Shiqi Chen, Miao Xiong, **Junteng Liu**, Zhengxuan Wu, Teng Xiao, Siyang Gao, Junxian He  
   *Proceedings of ICML 2024*  
   [Paper](https://arxiv.org/abs/2403.01548) | [Code](https://github.com/hkust-nlp/Activation_Decoding)

### 2023

5. **C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models**  
   Yuzhen Huang, Yuzhuo Bai, Zhihao Zhu, Junlei Zhang, Jinghan Zhang, Tangjun Su, **Junteng Liu**, Chuancheng Lv, Yikai Zhang, Jiayi Lei, Yao Fu, Maosong Sun, Junxian He  
   *Advances in Neural Information Processing Systems (NeurIPS 2023)*  
   [Paper](https://arxiv.org/abs/2305.08322) | [Code](https://github.com/hkust-nlp/ceval) | [Data](https://huggingface.co/datasets/ceval/ceval-exam)

6. **Composing Parameter-Efficient Modules with Arithmetic Operations**  
   Jinghan Zhang, Shiqi Chen, **Junteng Liu**, Junxian He  
   *Advances in Neural Information Processing Systems (NeurIPS 2023)*  
   [Paper](https://arxiv.org/abs/2306.14870) | [Code](https://github.com/hkust-nlp/PEM_composition) | [Data](https://huggingface.co/datasets/jinghan23/DatasetofPEMCompostition)
```

The about page's existing per-year headings, numbering, bolding of *Junteng Liu* and the `*Proceedings of …*` / `*Advances in …*` venue wording are all kept exactly as the page already has them; only the SynLogic venue line and the link lists change.

---

## D. `publication_fields.csv` ↔ preview consistency check

| # | `slug` | `category` | `date` / `year` | `venue` | `arxiv_id` → `paperurl` | `codeurl` | `dataurl` | authors | owner position |
|---|---|---|---|---|---|---|---|---|---|
| 1 | synlogic | conferences | 2025-12-01 / 2025 | NeurIPS 2025 | 2505.19641 | MiniMax-AI/SynLogic | MiniMaxAI/SynLogic | 15 | 1st |
| 2 | vlm-chart | preprints | 2025-03-01 / 2025 | arXiv preprint | 2503.18435 | hkust-nlp/Vision4Chart | Junteng/Vision4Chart | 6 | 1st |
| 3 | universal-truthfulness-hyperplane | conferences | 2024-12-01 / 2024 | EMNLP 2024 | 2407.08582 | hkust-nlp/Universal_Truthfulness_Hyperplane | *(none)* | 4 | 1st |
| 4 | in-context-sharpness-alerts | conferences | 2024-07-01 / 2024 | ICML 2024 | 2403.01548 | hkust-nlp/Activation_Decoding | *(none)* | 7 | 3rd |
| 5 | c-eval | conferences | 2023-12-01 / 2023 | NeurIPS 2023 | 2305.08322 | hkust-nlp/ceval | ceval/ceval-exam | 13 | 7th |
| 6 | composing-modules | conferences | 2023-12-01 / 2023 | NeurIPS 2023 | 2306.14870 | hkust-nlp/PEM_composition | jinghan23/DatasetofPEMCompostition | 4 | 3rd |

All six CSV rows agree with the entries in section A: same title, same author order, same `collection`, same `category`, same `date`, same `venue`, same URLs, same `permalink`, same `excerpt`. Every `category` value is one of the four declared in `_config.yml`, and every `filename` matches the `YYYY-MM-DD-<slug>.md` convention with the row's own `date`.

---

## E. Provenance and conventions

### E.1 Where each field was read

Titles and author orders come from each paper's own BibTeX; venues, arXiv ids, code and data URLs were re-read from the repositories in this session:

| Paper | Repository | Evidence used |
|---|---|---|
| SynLogic | `MiniMax-AI/SynLogic` | BibTeX `@misc{liu2025synlogic}`, `eprint 2505.19641`, `primaryClass cs.AI`; repo description "[NeurIPS 2025] The official repo of SynLogic: …"; README Resources table → dataset `MiniMaxAI/SynLogic` |
| Perception Bottleneck | `hkust-nlp/Vision4Chart` | BibTeX `@misc{liu2025perceptionbottleneckvlmschart}`, `eprint 2503.18435`, `primaryClass cs.CV`; README "Released Resources" → dataset `Junteng/Vision4Chart`; description names no venue |
| Universal Truthfulness Hyperplane | `hkust-nlp/Universal_Truthfulness_Hyperplane` | BibTeX `@article{liu2024universal}`, `arXiv preprint arXiv:2407.08582`; README News "Our paper is accepted by EMNLP 2024!"; description "… (EMNLP 2024)" |
| In-Context Sharpness | `hkust-nlp/Activation_Decoding` | BibTeX `@inproceedings{chen2024incontext}`, `url https://arxiv.org/abs/2403.01548`; description "… (ICML 2024)" |
| C-Eval | `hkust-nlp/ceval` | README Paper link `arxiv.org/abs/2305.08322`; News "[2023.10.26] C-Eval has been accepted to NeurIPS 2023"; BibTeX `@inproceedings{huang2023ceval}`; Hugging Face link `ceval/ceval-exam` |
| Composing PEMs | `hkust-nlp/PEM_composition` | README News "Our paper has been accepted to NeurIPS 2023"; paper link `arxiv.org/abs/2306.14870` (also the repo homepage); BibTeX `@inproceedings{zhang2023composing}`; "Instruction Datasets" link `jinghan23/DatasetofPEMCompostition` |

`venue_full` in the CSV is the standard long form of the acronym already in `venue` — for the two NeurIPS papers it is literally the `booktitle` their own BibTeX uses (*Advances in Neural Information Processing Systems*).

### E.2 The `date` rule

`date` only drives the file name, the `%Y` after the venue, and the reversed order. Peer-reviewed papers use the venue month (NeurIPS → December, EMNLP → the December value the site already carries, ICML → July); the one preprint uses its arXiv posting month (`2503.*` → March 2025). The day is always `01`, matching every entry already in the collection.

### E.3 `category`

`conferences` for the five papers with a venue confirmed by their own repository, `preprints` for the one paper that claims no venue anywhere. `books` and `manuscripts` stay unused — nothing in this set is a book or a journal article.

### E.4 Excerpts, permalinks and citation shape are the site's, unchanged

Each `excerpt` is the string the site already carries for that paper and each `permalink` is the site's existing one, so no published URL moves. Each `citation` follows the site's dominant pattern `Authors. (Year). "Title." <i>Venue</i>.` — the pattern used by four of the six current files; the two preprint files omit the `<i>…</i>` and are brought into line.

### E.5 Differences from what is on the site today

All evidence-backed; none cosmetic.

| Paper | Field | Currently on the site | New entry | Why |
|---|---|---|---|---|
| SynLogic | `venue` / `category` | `arXiv preprint` / `preprints` | `NeurIPS 2025` / `conferences` | The official repo's description states "[NeurIPS 2025] The official repo of SynLogic: …" |
| SynLogic | file name | `2025-06-08-synlogic.md` | `2025-12-01-synlogic.md` | The current name contradicts the file's own `date: 2025-03-01`; the new name matches the new NeurIPS date |
| SynLogic | `codeurl` | `github.com/Vicent0205/SynLogic` | `github.com/MiniMax-AI/SynLogic` | See E.6 |
| Perception Bottleneck | file name | `2025-06-08-vlm-chart.md` | `2025-03-01-vlm-chart.md` | The current name contradicts the file's own `date: 2025-03-01`; the new name matches it and the arXiv id `2503.*` |
| Perception Bottleneck | `codeurl` | `github.com/Vicent0205/Vision4Chart` | `github.com/hkust-nlp/Vision4Chart` | See E.6 |
| Universal Truthfulness | `codeurl` | `github.com/Vicent0205/Universal_Truthfulness_Hyperplane` | `github.com/hkust-nlp/Universal_Truthfulness_Hyperplane` | See E.6 |
| In-Context Sharpness, C-Eval, Composing PEMs | `codeurl` | *(absent)* | `hkust-nlp/Activation_Decoding`, `hkust-nlp/ceval`, `hkust-nlp/PEM_composition` | Each README identifies its repository as that paper's official implementation |
| all six | `paperurl` | *(absent)* | arXiv abstract URL | `archive-single.html` already renders `paperurl` as a "Download Paper" link; the ids come from the papers' own BibTeX |
| SynLogic, Perception Bottleneck, C-Eval, Composing PEMs | body `[Data]` link | *(absent)* | Hugging Face dataset URL | Published in each repository's own README |

### E.6 Why the `Vicent0205/*` code links were replaced

The site publishes `codeurl` values under `github.com/Vicent0205/{SynLogic, Vision4Chart, Universal_Truthfulness_Hyperplane}`. A repository listing for that account returns **9 repositories** — `sjtuoj`, `Vicent0205.github.io`, `digtalImageLab`, `dsp_lab`, `nlp`, `socket-programming`, `61c-proj1`, `Pattern-Recognition`, `gkc_lab` — and none of those three. Those paths therefore hold no repository. The URLs used above are the repositories that actually contain the code and that each paper's own README/BibTeX points to. This is recorded per row in the CSV's `field_source` column.

### E.7 Nothing was invented

No abstract, teaser image, `slidesurl`, `bibtexurl`, award, DOI or venue was added beyond what the sources above state. Fields with no evidence are simply left empty: `dataurl` is blank for the Universal Truthfulness Hyperplane and In-Context Sharpness rows because those repositories publish no dataset, and no venue is claimed for the Perception Bottleneck paper.
