---
title: Front
summary: Components for the Front Module
authors: Jon Harper
date: 2023-4-5
prefix: '../'
---

The Front module acts as a keystone or centerpiece:

- The Top, Rear, and Bottom Horns anchor to the Front, along with the hotend and some ABL methods;
- Both belts attach to the sides of the Front;
- Half of the drive module mounts above the hotend; and
- Some configurations also mount an accelerometer.

{% import 'format.md' as format with context %}
{% set comp_type='Front' -%}

{% set values = product.sortEntries(product.filterComponents(comp_type).values()) -%}

{% for comp in values -%}
{{ format.comp_entry(comp, img_width="200px", prefix=prefix) }}
{% endfor -%}