---
title: Bottom Horns
summary: Components for the Bottom Horns Module
authors: Jon Harper
date: 2023-4-5
prefix: '../'
---

{% import 'format.md' as format with context %}
{% set comp_type='Bottom Horns' -%}
{% set values = product.sortEntries(product.filterComponents(comp_type).values()) -%}

Your duct should match the length of your hotend. If you are using Beacon or Klicky, choose
the appropriate variant for that ABL method.

See the Intro Guide's [compatibility](../guide.md#bottom-horns) section for more information and
a table of hotends and ducts.

{% for comp in values -%}
{{ format.comp_entry(comp, prefix=prefix, img_width="200px") }}
{% endfor -%}