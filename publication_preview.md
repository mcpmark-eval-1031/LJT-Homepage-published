# Publication preview — new entries for the LJT homepage

**Owner / site subject:** Junteng Liu (LJT) — PhD candidate, HKUST NLP Group (`site_profile.yml`).

**Site and publication style used as the rendering reference**

| Surface | Path | Style |
|---|---|---|
| Site source (academicpages) | branch `LJT-Homepage` → `_publications/*.md`, listed by `_pages/publications.html` and `index.md` | one Markdown file per paper, `YYYY-MM-DD-<slug>.md`, YAML front matter (`layout, title, collection, category, permalink, citation, excerpt, date, venue, paperurl`) + short body with `**Authors:**` and `**Links:**` |
| Published site | branch `main` → `pages/publications.md` | flat reverse-chronological bullet list: `- <Title> (<Year>)` |

**Target papers:** the 6 papers of the publication set (see `publication_fields.csv`, newest first).

---

## A. New entries in the site's `_publications/` style (primary)

### 1. `_publications/2025-12-01-synlogic.md`

```markdown
---
layout: single
title: "SynLogic: Synthesizing Verifiable Reasoning Data at Scale for Learning Logical Reasoning and Beyond"
collection: publications
category: conferences
permalink: /publication/2025-12-01-synlogic
citation: >-
  Liu, Junteng, Yuanxiang Fan, Zhuo Jiang, Han Ding, Yongyi Hu, Chi Zhang, Yiqi Shi, Shitong Weng, Aili Chen, Shiqi Chen, Yunan Huang, Mozhi Zhang, Pengyu Zhao, Junjie Yan, and Junxian He. (2025). "SynLogic: Synthesizing Verifiable Reasoning Data at Scale for Learning Logical Reasoning and Beyond." NeurIPS 2025. arXiv:2505.19641.
excerpt: "A data synthesis framework that generates verifiable logical reasoning data at scale across 35 tasks with controllable difficulty."
date: 2025-12-01
venue: 'NeurIPS 2025'
paperurl: 'https://arxiv.org/abs/2505.19641'
---

SynLogic is a logical-reasoning data synthesis framework: it covers 35 distinct reasoning tasks (Sudoku, Game of 24, Cipher, Arrow Maze, ...), supports controllable difficulty, and every instance is checkable by rule-based verifiers, which makes the data directly usable for reinforcement learning.

**Authors:** **Junteng Liu**, Yuanxiang Fan, Zhuo Jiang, Han Ding, Yongyi Hu, Chi Zhang, Yiqi Shi, Shitong Weng, Aili Chen, Shiqi Chen, Yunan Huang, Mozhi Zhang, Pengyu Zhao, Junjie Yan, Junxian He

**Links:**
- [arXiv](https://arxiv.org/abs/2505.19641)
- [Code](https://github.com/MiniMax-AI/SynLogic)
- [Data](https://huggingface.co/datasets/MiniMaxAI/SynLogic)
```

### 2. `_publications/2025-03-01-perception-bottleneck-vlms-chart.md`

```markdown
---
layout: single
title: "On the Perception Bottleneck of VLMs for Chart Understanding"
collection: publications
category: manuscripts
permalink: /publication/2025-03-01-perception-bottleneck-vlms-chart
citation: >-
  Liu, Junteng, Weihao Zeng, Xiwen Zhang, Yijun Wang, Zifei Shan, and Junxian He. (2025). "On the Perception Bottleneck of VLMs for Chart Understanding." arXiv preprint arXiv:2503.18435.
excerpt: "Isolates visual perception - rather than reasoning - as a key bottleneck of vision-language models on chart understanding."
date: 2025-03-01
venue: 'arXiv preprint'
paperurl: 'https://arxiv.org/abs/2503.18435'
---

We analyse where vision-language models break down on chart questions and show that the vision encoder is a major bottleneck. The study covers CLIP training with hard-negative captions, CLIP evaluation on chart datasets, and LLaVA training/evaluation on FigureQA, DVQA, PlotQA, ChartQA, ChartBench, ChartX and MathVista.

**Authors:** **Junteng Liu**, Weihao Zeng, Xiwen Zhang, Yijun Wang, Zifei Shan, Junxian He

**Links:**
- [arXiv](https://arxiv.org/abs/2503.18435)
- [Code](https://github.com/hkust-nlp/Vision4Chart)
- [Data](https://huggingface.co/datasets/Junteng/Vision4Chart)
```

### 3. `_publications/2024-11-01-universal-truthfulness-hyperplane.md`

```markdown
---
layout: single
title: "On the Universal Truthfulness Hyperplane Inside LLMs"
collection: publications
category: conferences
permalink: /publication/2024-11-01-universal-truthfulness-hyperplane
citation: >-
  Liu, Junteng, Shiqi Chen, Yu Cheng, and Junxian He. (2024). "On the Universal Truthfulness Hyperplane Inside LLMs." EMNLP 2024. arXiv:2407.08582.
excerpt: "Probes trained on diverse datasets give positive evidence for a single, universal truthfulness hyperplane inside LLMs."
date: 2024-11-01
venue: 'EMNLP 2024'
paperurl: 'https://arxiv.org/abs/2407.08582'
---

We examine whether a universal truthfulness hyperplane exists inside a model by designing and training a probe on diverse datasets. The approach substantially improves over existing results and conveys positive signals for the existence of such a hyperplane.

**Authors:** **Junteng Liu**, Shiqi Chen, Yu Cheng, Junxian He

**Links:**
- [arXiv](https://arxiv.org/abs/2407.08582)
- [Code](https://github.com/hkust-nlp/Universal_Truthfulness_Hyperplane)
```

### 4. `_publications/2024-07-01-in-context-sharpness.md`

```markdown
---
layout: single
title: "In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation"
collection: publications
category: conferences
permalink: /publication/2024-07-01-in-context-sharpness
citation: >-
  Chen, Shiqi, Miao Xiong, Junteng Liu, Zhengxuan Wu, Teng Xiao, Siyang Gao, and Junxian He. (2024). "In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation." ICML 2024. arXiv:2403.01548.
excerpt: "Correct generations show sharper in-context activations; an entropy-based sharpness signal is folded into decoding to reduce hallucination."
date: 2024-07-01
venue: 'ICML 2024'
paperurl: 'https://arxiv.org/abs/2403.01548'
---

Correct generations tend to have sharper context activations in the hidden states of in-context tokens than incorrect ones. We quantify this sharpness with an entropy-based metric and use it to adjust the next-token distribution during decoding, improving factuality.

**Authors:** Shiqi Chen, Miao Xiong, **Junteng Liu**, Zhengxuan Wu, Teng Xiao, Siyang Gao, Junxian He

**Links:**
- [arXiv](https://arxiv.org/abs/2403.01548)
- [Code](https://github.com/hkust-nlp/Activation_Decoding)
```

### 5. `_publications/2023-12-01-c-eval.md`

```markdown
---
layout: single
title: "C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models"
collection: publications
category: conferences
permalink: /publication/2023-12-01-c-eval
citation: >-
  Huang, Yuzhen, Yuzhuo Bai, Zhihao Zhu, Junlei Zhang, Jinghan Zhang, Tangjun Su, Junteng Liu, Chuancheng Lv, Yikai Zhang, Jiayi Lei, Yao Fu, Maosong Sun, and Junxian He. (2023). "C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models." NeurIPS 2023, Datasets and Benchmarks Track. arXiv:2305.08322.
excerpt: "A multi-level, multi-discipline Chinese evaluation suite for foundation models."
date: 2023-12-01
venue: 'NeurIPS 2023'
paperurl: 'https://arxiv.org/abs/2305.08322'
---

C-Eval is a comprehensive Chinese evaluation suite for foundation models, spanning multiple difficulty levels and disciplines.

**Authors:** Yuzhen Huang, Yuzhuo Bai, Zhihao Zhu, Junlei Zhang, Jinghan Zhang, Tangjun Su, **Junteng Liu**, Chuancheng Lv, Yikai Zhang, Jiayi Lei, Yao Fu, Maosong Sun, Junxian He

**Links:**
- [arXiv](https://arxiv.org/abs/2305.08322)
- [Code](https://github.com/hkust-nlp/ceval)
```

### 6. `_publications/2023-12-01-composing-parameter-efficient-modules.md`

```markdown
---
layout: single
title: "Composing Parameter-Efficient Modules with Arithmetic Operations"
collection: publications
category: conferences
permalink: /publication/2023-12-01-composing-parameter-efficient-modules
citation: >-
  Zhang, Jinghan, Shiqi Chen, Junteng Liu, and Junxian He. (2023). "Composing Parameter-Efficient Modules with Arithmetic Operations." NeurIPS 2023. arXiv:2306.14870.
excerpt: "Training-free composition of parameter-efficient modules through linear arithmetic operations in weight space."
date: 2023-12-01
venue: 'NeurIPS 2023'
paperurl: 'https://arxiv.org/abs/2306.14870'
---

We define addition and negation operators over parameter-efficient modules and compose them by linear arithmetic in weight space, with no additional training. Applications include distribution generalization, multi-tasking, unlearning, domain transfer, and detoxifying Alpaca-LoRA.

**Authors:** Jinghan Zhang, Shiqi Chen, **Junteng Liu**, Junxian He

**Links:**
- [arXiv](https://arxiv.org/abs/2306.14870)
- [Code](https://github.com/hkust-nlp/PEM_composition)
- [Data](https://huggingface.co/datasets/jinghan23/DatasetofPEMCompostition)
```

---

## B. Same entries in the published-site list style (`pages/publications.md`)

```markdown
# Publications

- SynLogic: Synthesizing Verifiable Reasoning Data at Scale for Learning Logical Reasoning and Beyond (2025)
- On the Perception Bottleneck of VLMs for Chart Understanding (2025)
- On the Universal Truthfulness Hyperplane Inside LLMs (2024)
- In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation (2024)
- C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models (2023)
- Composing Parameter-Efficient Modules with Arithmetic Operations (2023)
```

---

## C. `publication_fields.csv` <-> preview consistency check

| # | title | venue_abbr / `venue` | year / `date` | paper_url / `paperurl` | code_url | bold_author | match |
|---|---|---|---|---|---|---|---|
| 1 | SynLogic: Synthesizing Verifiable Reasoning Data at Scale ... | NeurIPS 2025 | 2025 / 2025-12-01 | arxiv.org/abs/2505.19641 | MiniMax-AI/SynLogic | **Junteng Liu** (1st) | OK |
| 2 | On the Perception Bottleneck of VLMs for Chart Understanding | arXiv preprint | 2025 / 2025-03-01 | arxiv.org/abs/2503.18435 | hkust-nlp/Vision4Chart | **Junteng Liu** (1st) | OK |
| 3 | On the Universal Truthfulness Hyperplane Inside LLMs | EMNLP 2024 | 2024 / 2024-11-01 | arxiv.org/abs/2407.08582 | hkust-nlp/Universal_Truthfulness_Hyperplane | **Junteng Liu** (1st) | OK |
| 4 | In-Context Sharpness as Alerts ... | ICML 2024 | 2024 / 2024-07-01 | arxiv.org/abs/2403.01548 | hkust-nlp/Activation_Decoding | **Junteng Liu** (3rd) | OK |
| 5 | C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite ... | NeurIPS 2023 | 2023 / 2023-12-01 | arxiv.org/abs/2305.08322 | hkust-nlp/ceval | **Junteng Liu** (7th) | OK |
| 6 | Composing Parameter-Efficient Modules with Arithmetic Operations | NeurIPS 2023 | 2023 / 2023-12-01 | arxiv.org/abs/2306.14870 | hkust-nlp/PEM_composition | **Junteng Liu** (3rd) | OK |

---

## D. Conventions and provenance

1. **Author order** is verbatim from each paper's official BibTeX; the site owner (**Junteng Liu**) is bolded, matching the site's author-highlighting convention.
2. **`date` rule** (used only for file naming and reverse-chronological ordering): venue month for peer-reviewed papers (NeurIPS -> December, EMNLP -> November, ICML -> July), arXiv posting month for the preprint; day is pinned to `01`.
3. **`category`**: `conferences` for peer-reviewed venue papers, `manuscripts` for the arXiv preprint (switch to a dedicated `preprints` category if `_config.yml` defines one).
4. **Verified in-environment** (official repositories reachable from GitHub):
   - `MiniMax-AI/SynLogic` - BibTeX `eprint 2505.19641`, description "[NeurIPS 2025] The official repo of SynLogic ..."
   - `hkust-nlp/Vision4Chart` - BibTeX `eprint 2503.18435`, dataset/model links
   - `hkust-nlp/Universal_Truthfulness_Hyperplane` - BibTeX `arXiv:2407.08582`, News: accepted by EMNLP 2024
   - `hkust-nlp/Activation_Decoding` - BibTeX + description: ICML 2024, `arXiv:2403.01548`
   - `hkust-nlp/PEM_composition` - BibTeX + News: NeurIPS 2023, `arXiv:2306.14870`
   - `hkust-nlp/ceval` - description: "Official github repo for C-Eval ... [NeurIPS 2023]"
5. **Corrections vs. what was previously on the site**: the earlier `_publications` entries carried two wrong `paperurl` values - SynLogic (`arXiv:2502.11026`) and Universal Truthfulness Hyperplane (`arXiv:2412.04268`) - and pointed SynLogic's code at `Vicent0205/SynLogic`. The verified values are `arXiv:2505.19641` / `arXiv:2407.08582` and `github.com/MiniMax-AI/SynLogic`. SynLogic's venue is also now known (NeurIPS 2025) rather than "arXiv preprint".
6. **Single unverified field**: C-Eval's arXiv id (`2305.08322`) comes from the public record and could not be re-confirmed from a repository file in this environment; it is flagged in the `field_source` column of `publication_fields.csv`.
