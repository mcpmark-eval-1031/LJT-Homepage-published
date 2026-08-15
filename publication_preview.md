# Publication preview — new entries for Junteng Liu's homepage

**Site:** `mcpmark-eval-1031/LJT-Homepage` @ `master` (academicpages / Jekyll).
**Owner:** Junteng Liu — PhD candidate, HKUST NLP Group.
**Companion file:** `publication_fields.csv` (one row per target paper, all parsed fields).

## The style these entries are written in

Read from the site itself, not assumed:

| Surface | File | What it defines |
|---|---|---|
| Collection | `_config.yml` → `collections.publications` | one Markdown file per paper in `_publications/`, permalink `/publications/:path/` |
| Categories | `_config.yml` → `publication_category` | `books`, `manuscripts` (*Journal Articles*), `conferences` (*Conference Papers*), `preprints` (*Preprints*) |
| Listing page | `_pages/publications.html` | groups by category in the order above, `{% for post in site.publications reversed %}` inside each group |
| Item renderer | `_includes/archive-single.html` | prints `Published in <i>{{ post.venue }}</i>, {{ post.date \| date: "%Y" }}`, then the excerpt, then `Recommended citation: {{ post.citation }}` and a `Download Paper` link when `paperurl` is set |
| Existing entries | `_publications/*.md` | front matter `title, collection, category, permalink, excerpt, date, venue, codeurl, citation`; body `**Authors:** …` / `**Venue:** …` / `[Code](…)` |

Every entry below keeps that exact shape. File names follow the collection's `YYYY-MM-DD-<slug>.md` convention and the permalinks keep the site's existing `/publication/<year>-<slug>` form so no published link breaks.

**Target papers:** the six papers of the publication set, newest first.

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

[Code](https://github.com/MiniMax-AI/SynLogic)
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

[Code](https://github.com/hkust-nlp/Vision4Chart)
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

[Code](https://github.com/hkust-nlp/ceval)
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

[Code](https://github.com/hkust-nlp/PEM_composition)
```

---

## B. How they come out on `/publications/`

`_pages/publications.html` walks `publication_category` in `_config.yml` order and reverses each group, so the page reads:

### Conference Papers

> **SynLogic: Synthesizing Verifiable Reasoning Data at Scale for Learning Logical Reasoning and Beyond**
> Published in *NeurIPS 2025*, 2025
> Synthesizing verifiable reasoning data at scale for learning logical reasoning and beyond
> Recommended citation: Junteng Liu, Yuanxiang Fan, Zhuo Jiang, Han Ding, Yongyi Hu, Chi Zhang, Yiqi Shi, Shitong Weng, Aili Chen, Shiqi Chen, Yunan Huang, Mozhi Zhang, Pengyu Zhao, Junjie Yan, Junxian He. (2025). "SynLogic: …" *NeurIPS 2025*. — Download Paper

> **On the Universal Truthfulness Hyperplane Inside LLMs**
> Published in *EMNLP 2024*, 2024 — Download Paper

> **In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation**
> Published in *ICML 2024*, 2024 — Download Paper

> **Composing Parameter-Efficient Modules with Arithmetic Operations**
> Published in *NeurIPS 2023*, 2023 — Download Paper

> **C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models**
> Published in *NeurIPS 2023*, 2023 — Download Paper

### Preprints

> **On the Perception Bottleneck of VLMs for Chart Understanding**
> Published in *arXiv preprint*, 2025 — Download Paper

*(The two 2023-12-01 papers share a date, so Jekyll breaks the tie on file name and `reversed` puts `composing-modules` ahead of `c-eval`. Every other position is a pure date ordering. "Conference Papers" precedes "Preprints" because that is the order the categories are declared in `_config.yml`.)*

---

## C. Same six entries in the about-page list style

`_pages/about.md` lists publications grouped by year, numbered, with the site owner in bold:

```markdown
## Publications

### 2025

1. **SynLogic: Synthesizing Verifiable Reasoning Data at Scale for Learning Logical Reasoning and Beyond**  
   **Junteng Liu**, Yuanxiang Fan, Zhuo Jiang, Han Ding, Yongyi Hu, Chi Zhang, Yiqi Shi, Shitong Weng, Aili Chen, Shiqi Chen, Yunan Huang, Mozhi Zhang, Pengyu Zhao, Junjie Yan, Junxian He  
   *NeurIPS 2025*  
   [Paper](https://arxiv.org/abs/2505.19641) | [Code](https://github.com/MiniMax-AI/SynLogic)

2. **On the Perception Bottleneck of VLMs for Chart Understanding**  
   **Junteng Liu**, Weihao Zeng, Xiwen Zhang, Yijun Wang, Zifei Shan, Junxian He  
   *arXiv preprint, 2025*  
   [Paper](https://arxiv.org/abs/2503.18435) | [Code](https://github.com/hkust-nlp/Vision4Chart)

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
   [Paper](https://arxiv.org/abs/2305.08322) | [Code](https://github.com/hkust-nlp/ceval)

6. **Composing Parameter-Efficient Modules with Arithmetic Operations**  
   Jinghan Zhang, Shiqi Chen, **Junteng Liu**, Junxian He  
   *Advances in Neural Information Processing Systems (NeurIPS 2023)*  
   [Paper](https://arxiv.org/abs/2306.14870) | [Code](https://github.com/hkust-nlp/PEM_composition)
```

---

## D. `publication_fields.csv` ↔ preview consistency check

| # | slug | `category` | `date` / year | `venue` | `paperurl` (arXiv id) | `codeurl` | authors | owner position |
|---|---|---|---|---|---|---|---|---|
| 1 | synlogic | conferences | 2025-12-01 / 2025 | NeurIPS 2025 | 2505.19641 | MiniMax-AI/SynLogic | 15 | 1st |
| 2 | vlm-chart | preprints | 2025-03-01 / 2025 | arXiv preprint | 2503.18435 | hkust-nlp/Vision4Chart | 6 | 1st |
| 3 | universal-truthfulness-hyperplane | conferences | 2024-12-01 / 2024 | EMNLP 2024 | 2407.08582 | hkust-nlp/Universal_Truthfulness_Hyperplane | 4 | 1st |
| 4 | in-context-sharpness-alerts | conferences | 2024-07-01 / 2024 | ICML 2024 | 2403.01548 | hkust-nlp/Activation_Decoding | 7 | 3rd |
| 5 | c-eval | conferences | 2023-12-01 / 2023 | NeurIPS 2023 | 2305.08322 | hkust-nlp/ceval | 13 | 7th |
| 6 | composing-modules | conferences | 2023-12-01 / 2023 | NeurIPS 2023 | 2306.14870 | hkust-nlp/PEM_composition | 4 | 3rd |

All six rows agree with the entries in section A: same title, same author order, same category, same date, same venue, same URLs. Every `category` value is one of the four declared in `_config.yml`.

---

## E. Provenance and conventions

**1. Where each field was read.** Titles and author orders come from each paper's official BibTeX; venues, arXiv ids and code URLs were re-read from the repositories in this session:

| Paper | Repository | Evidence |
|---|---|---|
| SynLogic | `MiniMax-AI/SynLogic` | BibTeX `liu2025synlogic`, `eprint 2505.19641`, `cs.AI`; description "[NeurIPS 2025] The official repo of SynLogic …"; dataset `MiniMaxAI/SynLogic` |
| Perception Bottleneck | `hkust-nlp/Vision4Chart` | BibTeX `liu2025perceptionbottleneckvlmschart`, `eprint 2503.18435`, `cs.CV`; "Released Resources" → dataset `Junteng/Vision4Chart` |
| Universal Truthfulness Hyperplane | `hkust-nlp/Universal_Truthfulness_Hyperplane` | BibTeX `liu2024universal`, `arXiv:2407.08582`; News "accepted by EMNLP 2024" |
| In-Context Sharpness | `hkust-nlp/Activation_Decoding` | BibTeX `chen2024incontext`, `arxiv.org/abs/2403.01548`; description "… (ICML 2024)" |
| C-Eval | `hkust-nlp/ceval` | Paper link `arxiv.org/abs/2305.08322`; News "[2023.10.26] C-Eval has been accepted to NeurIPS 2023"; BibTeX `huang2023ceval` |
| Composing PEMs | `hkust-nlp/PEM_composition` | News "accepted to NeurIPS 2023"; paper link `arxiv.org/abs/2306.14870`; BibTeX `zhang2023composing` |

**2. `date` rule.** The `date` field only drives the file name and the reverse-chronological order. Peer-reviewed papers use the venue month (NeurIPS → December, EMNLP → the site's existing December value, ICML → July); the preprint uses its arXiv posting month (2503 → March 2025). The day is always `01`, matching every entry already in the collection.

**3. `category`.** `conferences` for the five papers with a confirmed venue, `preprints` for the one paper that claims no venue anywhere in its repository. `manuscripts` and `books` are unused — nothing in this set is a journal article or a book.

**4. Excerpts and citation shape are the site's, unchanged.** Each `excerpt` is the string the site already carries for that paper, and each `citation` follows the dominant site pattern `Authors. (Year). "Title." <i>Venue</i>.`

**5. Differences from what is on the site today — all evidence-backed, none cosmetic.**

| Paper | Field | Currently on the site | New entry | Why |
|---|---|---|---|---|
| SynLogic | `venue` / `category` | `arXiv preprint` / `preprints` | `NeurIPS 2025` / `conferences` | The official repo's description states "[NeurIPS 2025] The official repo of SynLogic …" |
| SynLogic | file name | `2025-06-08-synlogic.md` | `2025-12-01-synlogic.md` | The current name contradicts the file's own `date: 2025-03-01`; the new name matches the new venue date |
| SynLogic | `codeurl` | `github.com/Vicent0205/SynLogic` | `github.com/MiniMax-AI/SynLogic` | See note 6 |
| Perception Bottleneck | file name | `2025-06-08-vlm-chart.md` | `2025-03-01-vlm-chart.md` | The current name contradicts the file's own `date: 2025-03-01`; the new name matches it and the arXiv id `2503.*` |
| Perception Bottleneck | `codeurl` | `github.com/Vicent0205/Vision4Chart` | `github.com/hkust-nlp/Vision4Chart` | See note 6 |
| Universal Truthfulness | `codeurl` | `github.com/Vicent0205/Universal_Truthfulness_Hyperplane` | `github.com/hkust-nlp/Universal_Truthfulness_Hyperplane` | See note 6 |
| In-Context Sharpness, C-Eval, Composing PEMs | `codeurl` | *(absent)* | `hkust-nlp/Activation_Decoding`, `hkust-nlp/ceval`, `hkust-nlp/PEM_composition` | Each repo's README identifies itself as that paper's official implementation |
| all six | `paperurl` | *(absent)* | arXiv abstract URL | `_includes/archive-single.html` already renders `paperurl` as a "Download Paper" link; the ids come from the official BibTeX |

**6. Why the `Vicent0205/*` code links were replaced.** The three code URLs on the site point at `Vicent0205/SynLogic`, `Vicent0205/Vision4Chart` and `Vicent0205/Universal_Truthfulness_Hyperplane`. A repository listing for that account returns 9 repositories and none of them is any of those three, so those paths carry no repository of their own. The URLs used above are the repositories that actually hold the code and that each paper's own BibTeX/README points to.

**7. Nothing was invented.** No abstract, teaser image, slides URL, BibTeX file, award or venue was added beyond what the sources above state. Fields with no evidence are simply absent: no `dataurl` for the Universal Truthfulness Hyperplane or the In-Context Sharpness papers (their repos publish none), and no venue for the Perception Bottleneck paper.
