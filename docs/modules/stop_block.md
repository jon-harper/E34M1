---
title: X Axis Stop Blocks
summary: Options for triggering the X endstop.
authors: Jon Harper
date: 2023-5-3
prefix: '../'
---

{% import 'format.md' as format with context %}
{% set comp_type='X Stop Block' -%}
{% set values = product.sortEntries(product.filterComponents(comp_type).values()) -%}

Stop blocks are bumpers for the X endstop (or toolhead if using sensorless homing). Several options are available based on your needs.

{% for comp in values -%}
{{ format.comp_entry(comp, prefix=prefix, img_width="200px") }}

{% endfor -%}
