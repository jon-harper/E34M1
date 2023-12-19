---
title: ABL Side Mount
summary: Components for the ABL Side Mount
authors: Jon Harper
date: 2023-4-5
prefix: '../'
---

{% import 'format.md' as format with context %}
{% set comp_type='ABL Side Mount' -%}
{% set values = product.sortEntries(product.filterComponents(comp_type).values()) -%}

The side mount is used by many ABL methods and attaches to the Front. If you use Klicky or Beacon, see the [Bottom Horns](bottom.md) module for mounting options.

{% for comp in values -%}
{{ format.comp_entry(comp, prefix=prefix, img_width="100px") }}

{% endfor -%}