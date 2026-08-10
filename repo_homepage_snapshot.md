# Current homepage snapshot

- Captured: 2026-08-10
- Source repository: `mcpmark-eval-1031/LJT-Homepage` (branch `master`)
- Homepage body: `_pages/about.md` (permalink `/`)
- Author profile card rendered next to the homepage: `author:` block of `_config.yml`, mirrored in `_data/authors.yml`
- Header navigation (`_data/navigation.yml`): only `Publications` -> `/publications/`; there is no Teaching, Talks, Portfolio or CV link

---

## Author profile card (`_config.yml` -> `author`, `_data/authors.yml`)

| key | value rendered on the homepage |
| --- | --- |
| `avatar` | `profile.png` |
| `name` | Junteng Liu |
| `bio` | First-year PhD candidate at HKUST NLP Group. Research focuses on natural language processing and machine learning, with interests in LLM Reasoning and Reinforcement Learning, Hallucination in Vision-Language Models (VLM), and LLM truthfulness and Interpretability. |
| `location` | Hong Kong |
| `employer` | HKUST NLP Group |
| `email` | jliugi@connect.ust.hk |
| `googlescholar` | https://scholar.google.com/citations?hl=en&user=tbK9jl4AAAAJ&view_op=list_works&sortby=pubdate |
| `github` | Vicent0205 |
| `twitter` | junteng88716710 |

---

## Homepage body (`_pages/about.md`)

# Junteng Liu

I am a first-year PhD candidate at the **HKUST NLP Group**, supervised by Professor Junxian He. I graduated from **Shanghai Jiao Tong University (SJTU)** in June 2024. My research focuses on natural language processing and machine learning.

## Research Interests

- LLM Reasoning and Reinforcement Learning
- Hallucination in Vision-Language Models (VLM)
- LLM truthfulness and Interpretability

## Skills

- Natural Language Processing
- Machine Learning
- LLM Reasoning and Reinforcement Learning
- Hallucination in Vision-Language Models (VLM)
- LLM truthfulness and Interpretability

## Academic Background

- **Ph.D. in Computer Science** (2024-Present) - Hong Kong University of Science and Technology (HKUST)
  Advisor: Professor Junxian He

- **B.Eng.** (2020-2024) - Shanghai Jiao Tong University (SJTU)
  Awarded Zhiyuan Honor Scholarship

## Research Experience

**PhD Candidate** | HKUST NLP Group
*2024 - Present*
Advisor: Professor Junxian He

**Research Intern** | MINIMAX
*February 2025 - Present*

**Research Intern** | Tencent WXG
*June 2024 - September 2024*
Advisor: Zifei Shan

**Research Intern** | Shanghai AI Lab
*June 2023 - December 2023*
Advisor: Prof. Yu Cheng

## Publications

### 2025

1. **SynLogic: Synthesizing Verifiable Reasoning Data at Scale for Learning Logical Reasoning and Beyond** (arXiv preprint, 2025)
2. **On the Perception Bottleneck of VLMs for Chart Understanding** (arXiv preprint, 2025)

### 2024

3. **On the Universal Truthfulness Hyperplane Inside LLMs** (Proceedings of EMNLP 2024)
4. **In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation** (Proceedings of ICML 2024)

### 2023

5. **C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models** (NeurIPS 2023)
6. **Composing Parameter-Efficient Modules with Arithmetic Operations** (NeurIPS 2023)

(Each entry additionally renders its full author list and, for four of the six papers, a `[Code]` link.)

## Honors & Awards

- Zhiyuan Honor Scholarship, Shanghai Jiao Tong University

## Contact

- **Email:** [jliugi@connect.ust.hk](mailto:jliugi@connect.ust.hk)
- **GitHub:** [Vicent0205](https://github.com/Vicent0205)
- **Google Scholar:** [Profile](https://scholar.google.com/citations?hl=en&user=tbK9jl4AAAAJ&view_op=list_works&sortby=pubdate)
- **X (Twitter):** [@junteng88716710](https://x.com/junteng88716710)

---

## Field presence detected in this snapshot

| requested field | present on homepage? | where |
| --- | --- | --- |
| advisor | yes | intro paragraph; Academic Background; Research Experience |
| affiliation | yes | intro paragraph; `author.employer` |
| awards | yes | "Honors & Awards"; "Awarded Zhiyuan Honor Scholarship" under the B.Eng. entry |
| education | yes | "Academic Background" |
| email | yes | Contact; `author.email` |
| github | yes | Contact; `author.github` |
| google_scholar | yes | Contact; `author.googlescholar` |
| name | yes | page title; `author.name` |
| phone | no | - |
| portrait_url | yes | `author.avatar` = `profile.png` (`_config.yml` and `_data/authors.yml`) |
| publications | yes | "Publications" |
| research_experience | yes | "Research Experience" |
| research_interests | yes | "Research Interests" |
| service | no | - |
| short_bio | yes | intro paragraph; `author.bio` |
| teaching | no | - (`_pages/teaching.html` is an empty archive page and is not linked from the navigation) |
| title | yes | intro paragraph; Research Experience |
| twitter | yes | Contact; `author.twitter` |

### Homepage content that is not one of the requested fields

- A "Skills" section listing `Natural Language Processing`, `Machine Learning` and a duplicate of the three research interests.
- `author.location` = `Hong Kong` on the profile card.
