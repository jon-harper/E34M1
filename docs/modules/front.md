---
title: Front
summary: Components for the Front Module
authors: Jon Harper
date: 2023-4-5
prefix: '../'
---

The Front module serves several purposes:

- The Top, Rear, and Bottom Horns are screwed into the Front, much like building on a foundation.
- The belts secure at each side of the Front.
- The Hotend and Drive modules both attach to it.
- The ABL Side Mount, if needed, goes on the left side.
- Lastly, it can mount an accelerometer.

{% import 'format.md' as format with context %}
{% set comp_type='Front' -%}

{% set values = product.sortEntries(product.filterComponents(comp_type).values()) -%}

{% for comp in values -%}
{{ format.comp_entry(comp, img_width="200px", prefix=prefix) }}
{% endfor -%}