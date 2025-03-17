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
{{ format.comp_entry(comp, prefix=prefix, img_width="200px") }}
{% endfor -%}

## Third-Party Hotends

These hotends are third-party mounts. They may use either hex nuts or heat set inserts, and may or may not include a bill of materials.

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

### E3D Revo Micro

- **Author**: [hebijirik](https://www.printables.com/@hebijirik_84624)
- **Inserts/Hex Nuts**: hex nuts

[Files](https://www.printables.com/model/225581-eva-3-revo-micro-hotend/files){ .md-button }

</div>
<div markdown class="jh-grid-img">
![revo_micro_image](../img/parts/revo_micro.webp){width="200px"}
</div>
<div markdown class="jh-grid-para">

### E3D V6 & Revo V6 

- **Author**: [3DP-MAMSIH](https://www.printables.com/@3DPMAMSIH)
- **Inserts/Hex Nuts**: M3x4.6x4 inserts or hex nuts

[Files](https://www.printables.com/model/201093-eva-30-e3dv6-revo-revo-micro-hotends-mount){ .md-button }

</div>
<div markdown class="jh-grid-img">
![E3D V6](../img/parts/e3d_v6.webp){width="200px"}
</div>
<div markdown class="jh-grid-para">

### Mellow NF-Crazy

- **Author**: [Lascoose](https://www.printables.com/@Lascoose)
- **Inserts/Hex Nuts**: M3x4.6x4 inserts

[Files](https://www.printables.com/model/316658-eva-30-nf-crazy-hotend){ .md-button }

</div>
<div markdown class="jh-grid-img">
![Mellow NF-Crazy](../img/parts/mellow_nf_crazy.webp){width="200px"}
</div>

<div markdown class="jh-grid-para">

### TriangleLabs Dragon Ace

- **Author**: [SuperHKA](https://www.printables.com/@SuperHKA_2872552)
- **Inserts/Hex Nuts**: M3x5x4 inserts

[Files](https://www.printables.com/model/1181970-dragon-ace-mount-for-e34m1){ .md-button }

### TriangleLabs TZ V6

- **Author**: [Ultrazauberer](https://www.printables.com/@Ultrazauberer_772128)
- **Inserts/Hex Nuts**: M3x5x4 inserts

[Files](https://www.printables.com/model/1227780-eva-30-e34m1-v6-tz20-hotend-mount){ .md-button }

- **Author**: [Raniel Endrino](https://www.printables.com/@RanielEndrino_310348)
- **Inserts/Hex Nuts**: M3x5x4 inserts

[Files](https://www.printables.com/model/666511-e34m1-tz2-hotend-mount-for-zerog-mercury-one1){ .md-button }

</div>
