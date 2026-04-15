---
layout: single
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

## Education

* **Ph.D. in Computer Science** (2024–Present)
  * Hong Kong University of Science and Technology (HKUST)
  * HKUST NLP Group, supervised by [Prof. Junxian He](https://junxianhe.github.io/)

* **B.Eng. in Computer Science** (2020–2024)
  * Shanghai Jiao Tong University (SJTU)
  * Graduated June 2024
  * Received Zhiyuan Honor Scholarship

## Work Experience

* **Research Intern** at MINIMAX (February 2025 – Present)
* **Research Intern** at Tencent WXG (June 2024 – September 2024)
  * Advisor: Zifei Shan
* **Research Intern** at Shanghai AI Lab (June 2023 – December 2023)
  * Advisor: Prof. Yu Cheng

## Research Interests

* LLM Reasoning and Reinforcement Learning
* Hallucination in Vision-Language Models (VLM)
* LLM Truthfulness and Interpretability

## Skills

* **Programming Languages:** Python, C/C++, JavaScript
* **Frameworks & Libraries:** PyTorch, HuggingFace Transformers, JAX, vLLM
* **Tools & Platforms:** Git, Linux, Docker, Weights & Biases, AWS
* **Languages:** Chinese (native), English (fluent)

## Awards

* Zhiyuan Honor Scholarship, Shanghai Jiao Tong University

## Publications

{% for post in site.publications reversed %}
{% include archive-single-cv.html %}
{% endfor %}

## Service and Leadership

* Active contributor to open-source NLP research
