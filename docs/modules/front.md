---
title: Front
summary: Components for the Front Module
authors: Jon Harper
date: 2023-4-5
prefix: '../'
---

There are three versions of the front module; two mount an accelerometer.

{% import 'format.md' as format with context %}
{% set comp_type='Front' -%}

{% set values = product.sortEntries(product.filterComponents(comp_type).values()) -%}

{% for comp in values -%}
{{ format.comp_entry(comp, prefix) }}
{% endfor -%}