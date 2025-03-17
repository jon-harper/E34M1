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
{{ format.comp_entry(comp, prefix=prefix, img_width="200px") }}
{% endfor -%}

## Third-Party Inlets

These are E34M1 mods hosted on external sites. They may or may not come with a bill of materials.

### 22mm CPAP (18mm ID)

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

- **Author**: [Studmuffin](https://www.printables.com/@Studmuffin_2595396)
- **Inserts/Hex Nuts**: N/A

<div markdown class="jh-grid-container jh-grid-1 jh-link-grid">
[Link](https://www.printables.com/model/1176116-e34m1-18mm-cpap-rear-inlet){ .md-button}
</div>
</div>