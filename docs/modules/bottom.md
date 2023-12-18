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

Several versions of the bottom horns are available for E34M1. Which version you should use depends on your hotend and your ABL method. See the [Compatibility](../guide.md#bottom-horns) page for a breakdown table.

{% for comp in values -%}
{{ format.comp_entry(comp, prefix, img_width="200px") }}
{% endfor -%}