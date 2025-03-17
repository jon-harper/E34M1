---
title: Extruder Mounts
summary: Extruder mounts modified for E34M1
authors: Jon Harper
date: 2023-4-19
prefix: '../'
---

!!! tip
    See [the end of this page](#eva-3-ecosystem-drives) for compatible third party mounts.

{% import 'format.md' as format with context %}
{% set comp_type='Drive' -%}

## E34M1 Native Drives

{% set values = product.sortEntries(product.filterComponents(comp_type).values()) -%}

{% for comp in values -%}
{{ format.comp_entry(comp, prefix=prefix, img_width="200px") }}
{% endfor -%}


## EVA 3 Ecosystem Drives

These are mounts from the larger EVA ecosystem that link to external sites.

### Galileo 2 StandAlone

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

- **Author**: [cuiviemen](https://www.printables.com/@cuiviemen_127292)
- **Inserts/Hex Nuts**: M3x4.6x4 inserts

<div markdown class="jh-grid-container jh-grid-1 jh-link-grid">
[Link](https://www.printables.com/model/648710-galileo-2-sa-extruder-for-eva3){ .md-button}
</div>
</div>
<div markdown class="jh-grid-img">
![Galileo 2 StandAlone](../img/parts/drive_g2sa.webp){width="200px"}
</div>
</div>

### Annex Sherpa Micro

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

- **Author**: [Psych0h3ad](https://www.printables.com/@Psych0h3ad_168275)
- **Inserts/Hex Nuts**: M3x4.6x4 inserts

<div markdown class="jh-grid-container jh-grid-1 jh-link-grid">
[Link](https://www.printables.com/model/224597-sherpa-micro-mount-for-eva-3){ .md-button}
</div>
</div>
<div markdown class="jh-grid-img">
![Annex Sherpa Micro](../img/parts/sherpa_micro.webp){width="200px"}
</div>
</div>

### E3D Titan

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

- **Author**: [Chana Kennington](https://www.printables.com/@ChanaKenningt_484474)
- **Inserts/Hex Nuts**: None

<div markdown class="jh-grid-container jh-grid-1 jh-link-grid">
[Link](https://www.printables.com/model/424090-eva3-titan-extruder-mount){ .md-button }
</div>
</div>
<div markdown class="jh-grid-img">
![E3D Titan](../img/parts/titan.webp){width="200px"}
</div>
</div>

### ProtoXtruder 2.0

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

- **Author**: [Ultrazauberer](https://www.printables.com/@Ultrazauberer_772128)
- **Inserts/Hex Nuts**: M3x5x4 inserts

<div markdown class="jh-grid-container jh-grid-1 jh-link-grid">
[Link](https://www.printables.com/model/1142327-eva-30-e34m1-protoxtruder-20-mount){ .md-button }
</div>
</div>
<div markdown class="jh-grid-img">
![ProtoXtruder 2.0 Render](../img/parts/protoxtruder2.webp){width="200px"}
</div>
</div>

### VzBoT3D Vz-HextrudORT Low

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

- **Author**: [Pr20100](https://www.printables.com/@Pr20100)
- **Inserts/Hex Nuts**: M3x4.6x4 inserts or hex nuts

<div markdown class="jh-grid-container jh-grid-1 jh-link-grid">
[Link](https://www.printables.com/model/355751-eva-3-vz-hextrudort-low-extruder-mounting-plate){ .md-button }
</div>
</div>
<div markdown class="jh-grid-img">
![VzBoT3D Vz-HextrudORT Low](../img/parts/hextrudort.webp){width="200px"}
</div>
</div>