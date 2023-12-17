---
title: Hotend Mounts
summary: Hotend mounts modified specifically for E34M1
authors: Jon Harper
date: 2023-4-5
prefix: '../'
---

!!! tip
    See [the end of this page](#eva-3-ecosystem-hotends) for compatible third party mounts.

{% import 'format.md' as format with context %}
{% set comp_type='Hotend' -%}

## E34M1 Native Hotends

{% set values = product.sortEntries(product.filterComponents(comp_type).values()) -%}

{% for comp in values -%}
{{ format.variant_entry(comp, prefix) }}
{% endfor -%}

## EVA 3 Ecosystem Hotends

These hotends are third party mounts that use either EVA-style inserts or hex nuts. They may or may not have a bill of materials.

<div markdown class="jh-grid-container jh-grid-2">

<div markdown class="jh-grid-para">

### E3D Revo Micro

- **Author**: [hebijirik](https://www.printables.com/@hebijirik_84624)
- **Inserts/Hex Nuts**: hex nuts

[Link](https://www.printables.com/model/225581-eva-3-revo-micro-hotend/files){.md-button}

</div>
<div markdown class="jh-grid-img">
![revo_micro_image](../img/parts/revo_micro.webp){width="200px"}
</div>
<div markdown class="jh-grid-para">

### E3D V6 & Revo V6

- **Author**: [3DP-MAMSIH](https://www.printables.com/@3DPMAMSIH)
- **Inserts/Hex Nuts**: M3x4.6x4 inserts or hex nuts

[Link](https://www.printables.com/model/201093-eva-30-e3dv6-revo-revo-micro-hotends-mount){.md-button}
</div>
<div markdown class="jh-grid-img">
![E3D V6](../img/parts/e3d_v6.webp){width="200px"}
</div>
</div>
