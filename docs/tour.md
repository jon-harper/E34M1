---
title: Tour
summary: E34M1 Modules Tour
authors: Jon Harper
date: 2023-1-26
---

## Overview

E34M1 replaces many of the printed parts from EVA 3, while maintaining compatibility with hotends and extruders. This tour introduces the E34M1 *and* everything else you need to print from EVA 3.

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

### Icons and Terminology

These terms and icons are used throughout the site.

- The :material-printer-3d-nozzle: icon is used to emphasize that a part is 3D printed.
- The :material-cart: shopping cart icon is for example links. *There are no affiliate links on this site.*
- Drive: EVA 3 refers to the extruder, stepper, and mount as the *Drive* module.
- FHCS: flat head cap screw (DIN 7991)
- SHCS: socket head scap screw (DIN 912)
- Voron-style inserts: M3 x 5mm OD x 4mm L heat set inserts
- EVA-style inserts: M3 x 4.6mm OD x 4mm L heat set inserts

## E34M1 Modules

Each E34M1 module comes in multiple varations. These parts are all specific to E34M1.

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-card">

### Front

The Front mounts the hotend, belts, and the front of the Drive module.

<figure markdown>
![front](img/tour/front.png){width="300px"}

[Details and BOM](modules/front.md){.md-button}
</figure>

</div>
<div markdown class="jh-card">
### Top

The top mounts the MGN12H carriage, the X axis endstop, and the back of the Drive module.

<figure markdown>
![top](img/tour/top.png){width="300px"}

[Details and BOM](modules/top.md){.md-button}
</figure>

<div markdown class="jh-grid-container jh-grid-1 jh-link-grid">
</div>
</div>
<div markdown class="jh-card">

### Bottom

The bottom horns are primarily for part cooling and form the lower joint between the Front and Rear Inlet. Some ABL methods (e.g., Beacon, Klicky) mount here.

<figure markdown>
![bottom](img/tour/bottom.png){width="300px"}

[Details and BOM](modules/bottom.md){.md-button}
</figure>
</div>
<div markdown class="jh-card">

### Rear Inlet

Stock EVA 3 has a rear piece here that acts as a belt tensioner. It's unneeded for Mercury One printers, so we moved the cooling inlet forward to save space.

<figure markdown>
![inlet](img/tour/inlet.png){width="300px"}

[Details and BOM](modules/rear.md){.md-button}
</figure>
</div>
<div markdown class="jh-card">

### ABL Side Mount

The side ABL mount is modified from stock EVA. Most ABL methods mount here (e.g., BLTouch and CR Touch).

<figure markdown>
![abl mount](img/tour/abl.png){width="300px"}

[Details and BOM](modules/abl.md){.md-button}
</figure>
</div>
</div>

## Stock EVA Modules

Stock modules have not changed in how they join with other parts. This keeps third party mods compatible while allowing us to make small improvements and fixes to the existing mounting options.

We've assembled lists of known hotend and drive mounts.

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
| [Z Limit Switch Mount](modules/other.md#z-endstop-mount) | Raises the Z endstop for Ender 5 Pro printers. |
| [Toolhead PCB Mounts](modules/pcb_mounts.md) | Mounts for '36 and '42 PCBs for NEMA17 steppers and shrouds to cover them. |

## Related and Contributed Mods

These are related mods not linked elsewhere that may be useful for your build.

| Mod Name | Author | Purpose |
|----------|--------|---------|
| [Klicky Probe Dock for Mercury 1 Zero G](https://www.printables.com/model/386819-klicky-probe-dock-for-mercury-1-zero-g) | [Sir_Wash](https://www.printables.com/social/415185-sir_wash) | Adds a dock for Klicky; works with `klicky_bottom.stl`. |
