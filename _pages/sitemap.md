---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
---

{% include base_path %}

## Pages

* [Home]({{ base_path }}/)
* [About]({{ base_path }}/about/)
* [Publications]({{ base_path }}/publications/)
* [CV]({{ base_path }}/cv/)

## Publications

{% for post in site.publications %}
* [{{ post.title }}]({{ base_path }}{{ post.url }})
{% endfor %}
