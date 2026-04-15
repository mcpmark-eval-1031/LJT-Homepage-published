---
layout: archive
title: "Junteng Liu"
author_profile: true
permalink: /
---

{% include base_path %}

I am a first-year PhD candidate at the [HKUST NLP Group](https://nlp.cse.ust.hk/), supervised by [Prof. Junxian He](https://junxianhe.github.io/). I graduated from [Shanghai Jiao Tong University](https://www.sjtu.edu.cn/) (SJTU) in June 2024 with a B.Eng.

## Research Interests

My research focuses on **natural language processing** and **machine learning**. Specific interests include:

* **LLM Reasoning and Reinforcement Learning**
* **Hallucination in Vision-Language Models (VLM)**
* **LLM Truthfulness and Interpretability**

## Publications

See the [Publications](/publications/) page for a full list, or browse below:

{% for post in site.publications reversed %}
{% include archive-single.html %}
{% endfor %}
