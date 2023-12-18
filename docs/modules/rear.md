---
title: Rear Inlet
summary: Components for the Rear Module
authors: Jon Harper
date: 2023-4-5
prefix: '../'
---

{% import 'format.md' as format with context %}
{% set comp_type='Rear Inlet' -%}
{% set values = product.sortEntries(product.filterComponents(comp_type).values()) -%}

The rear module acts as a part cooling fan inlet. Use the single 5015 inlet if you
are unsure which is best.

{% for comp in values -%}
{{ format.comp_entry(comp, prefix, img_width="200px") }}
{% endfor -%}