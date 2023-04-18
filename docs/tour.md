---
title: Tour
summary: E34M1 Modules Tour
authors: Jon Harper
date: 2023-1-26
---

## Overview

E34M1 replaces many of the printed parts from EVA 3, while maintaining compatibility with others. This tour introduces the E34M1 *and* everything else you need to print from EVA 3.

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-card">
### Core E34M1 Assembly
<figure markdown>
![core](img/tour/core.png){width="300px"}
</figure>
</div>
<div markdown class="jh-card">
### Complete Assembly
<figure markdown>
![complete](img/tour/master.png){width="300px"}
</figure>
</div>
</div>

## E34M1 Core Modules

These are all specific to E34M1.

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-card">

### Front

Numerous parts, including the hotend and belts, attach to the front module.

<figure markdown>
![front](img/tour/front.png){width="300px"}

[Details and BOM](modules/front.md){.md-button}
</figure>

</div>
<div markdown class="jh-card">
### Top

The top mounts the MGN12H carriage, the X axis endstop, and an optional cable guide. A version is available without the cable guide for toolhead PCB users.

<figure markdown>
![top](img/tour/top.png){width="300px"}

[Details and BOM](modules/top.md){.md-button}
</figure>

<div markdown class="jh-grid-container jh-grid-1 jh-link-grid">
</div>
</div>
<div markdown class="jh-card">

### Bottom

The bottom horns are primarily for part cooling. Some ABL methods (e.g., Beacon, Klicky) mount here.

<figure markdown>
![bottom](img/tour/bottom.png){width="300px"}

[Details and BOM](modules/bottom.md){.md-button}
</figure>
</div>
<div markdown class="jh-card">

### Rear Inlet

Stock EVA has a rear piece in this location that acts as a belt tensioner. It is removed in E34M1, with the cooling inlet moved forward and serving in its place.

<figure markdown>
![inlet](img/tour/inlet.png){width="300px"}

[Details and BOM](modules/rear.md){.md-button}
</figure>
</div>
<div markdown class="jh-card">

### ABL Mount

The side ABL mount is modified from stock EVA.

!!! note
    Not all ABL methods use the ABL mount (e.g., Klicky, Beacon).

    See [Related and Contributed Mods](#related-and-contributed-mods) for user-contributed Klicky and Beacon mounts.

<figure markdown>
![abl mount](img/tour/abl.png){width="300px"}

[Details and BOM](modules/abl.md){.md-button}
</figure>
</div>
</div>

## Stock EVA Modules

These components have not changed from EVA. As such, you will need to download the correct parts from the [EVA](https://main.eva-3d.page/) site or elsewhere (e.g., [Printables](https://printables.com)). We've assembled a list of known hotend and drive mounts.

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-card">

### Hotend

This mounts the hotend, cooling fan, and optional shroud.

<figure markdown>
![hotend](img/tour/hotend.png){width="300px"}

[EVA 3 Hotends](compat/hotends.md){.md-button}
</figure>

</div>
<div markdown class="jh-card">

### Drive/Extruder

The drive module attaches the extruder and extruder stepper to the toolhead.

<figure markdown>
![drive](img/tour/drive.png){width="300px"}

[EVA 3 Extruders](compat/drives.md){.md-button}
</figure>

</div>
<div markdown class="jh-card">

### Shroud

All stock shrouds are compatible with E34M1.

<figure markdown>
![shroud](img/tour/shroud.png){width="300px"}

[Stock EVA 3 Shrouds](https://main.eva-3d.page/heat_insert/shrouds/chonkier/){.md-button}

[cuiviemen's Chonky Shrouds with LED Lighting](https://www.printables.com/model/420929-eva-30-chonky-shrouds-with-led-lighting){.md-button}

</figure>

</div>
</div>

## Other E34M1 Components

E34M1 provides several other components that may be useful:

| Component                     | Purpose |
|-------------------------------|---------|
| [Front Intake Duct](modules/other.md#front-intake-duct) | Allows hotend cooling fans to be removed with two (2) screws. |
| [X Axis Stop Block](modules/other.md#x-axis-stop-block) | Bumper for the X axis endstop, adapted from M1.1. |
| [Z Limit Switch Mount](modules/other.md#z-endstop-mount) | Covers the Z endstop PCB. |
| [Toolhead PCB Mounts](modules/pcb_mounts.md) | Mounts for '36 and '42 PCBs for NEMA17 steppers. |
| [Toolhead PCB Shrouds](modules/pcb_shrouds.md) | Shrouds to cover toolhead PCB wiring. |

## Related and Contributed Mods

These are related mods not linked elsewhere that may be useful for your build.

| Mod Name | Author | Purpose |
|----------|--------|---------|
| [Klicky Probe Dock for Mercury 1 Zero G](https://www.printables.com/model/386819-klicky-probe-dock-for-mercury-1-zero-g) | [Sir_Wash](https://www.printables.com/social/415185-sir_wash) | Adds a dock for Klicky; works with `bottom_horns_klicky_fi.stl`. |
