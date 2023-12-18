---
title: Visual Tour
summary: E34M1 Modules Tour
authors: Jon Harper
date: 2023-1-26
---

## Overview

E34M1 replaces most of stock EVA 3 but is still compatible with stock hotends, extruders, and shrouds. This tour introduces E34M1 and the larger EVA 3 ecosystem.

<div markdown class="grid">
<div markdown class="card">

**Core E34M1 Assembly**
<figure markdown>
![core](img/tour/core.webp){width="300px"}
</figure>
</div>
<div markdown class="card">
**Complete Assembly**
<figure markdown>
![complete](img/tour/master.webp){width="300px"}
</figure>
</div>
</div>

## Core Modules

Each E34M1 module comes in multiple varations. These parts are all specific to E34M1.

<div markdown class="grid">
<div markdown class="card">

### [Front](modules/front.md)

The Front mounts the hotend, belts, and the front of the Drive module.

<figure markdown>
[![front](img/tour/front.webp){width="300px"}](modules/front.md)
</figure>

</div>
<div markdown class="card">

### [Top](modules/top.md)

The top mounts the MGN12H carriage, the X axis endstop, and the back of the Drive module. It has an optional attachment point for an umbilical cable guide.

<figure markdown>
[![top](img/tour/top.webp){width="300px"}](modules/top.md)
</figure>

</div>
<div markdown class="card">

### [Bottom Horns](modules/bottom.md)

The bottom horns are primarily for part cooling and form the lower joint between the Front and Rear Inlet. Some ABL methods (e.g., Beacon, Klicky) mount here.

<figure markdown>
[![bottom](img/tour/bottom.webp){width="300px"}](modules/bottom.md)
</figure>
</div>
<div markdown class="card">

### [Rear Inlet](modules/rear.md)

Stock EVA 3 has a rear piece here that acts as a belt tensioner. It's unneeded for Mercury One printers, so we moved the cooling inlet forward to save space.

<figure markdown>
[![inlet](img/tour/inlet.webp){width="300px"}](modules/rear.md)
</figure>
</div>
<div markdown class="card">

### [ABL Side Mounts](modules/abl.md)

The side ABL mount is significantly different from stock EVA. Most ABL methods mount here (e.g., BLTouch and CR Touch).

<figure markdown>
[![abl mount](img/tour/abl.webp){width="300px"}](modules/abl.md)
</figure>
</div>
</div>

## EVA-Compatible Modules

Compared to stock EVA 3, these modules have not changed in how they join with other parts. This keeps third party mods compatible while allowing us to make small improvements and fixes.

<div markdown class="grid">
<div markdown class="card">

### [EVA 3 Hotends](modules/hotend.md)

The hotend module mounts the hotend, cooling fan, and an optional shroud.

<figure markdown>
[![hotend](img/tour/hotend.webp){width="300px"}](modules/hotend.md)
</figure>

</div>
<div markdown class="card">

### [EVA 3 Drives/Extruders](modules/drive.md)

The drive module attaches the extruder and extruder stepper to the toolhead.

<figure markdown>
[![drive](img/tour/drive.webp){width="300px"}](modules/drive.md)
</figure>

</div>
<div markdown class="card">

### Shroud

All stock shrouds are compatible with E34M1.

<figure markdown>
![shroud](img/tour/shroud.webp){width="300px"}
</figure>
- [Stock EVA 3 Shrouds](https://main.eva-3d.page/heat_insert/shrouds/chonkier/)
- [cuiviemen's Chonky Shrouds with LED Lighting](https://www.printables.com/model/420929-eva-30-chonky-shrouds-with-led-lighting)
</div>
</div>

## Other E34M1 Components

E34M1 provides several other components that may be useful:

| Component                     | Purpose |
|-------------------------------|---------|
| [X Axis Stop Blocks](modules/stop_block.md) | Bumpers for the X axis endstop. |
| [Z Limit Switch Mount](modules/other.md#z-endstop-mount) | Raises the Z endstop for Ender 5 Pro printers. |
| [NEMA17 PCB Mounts](modules/pcb_mounts.md) | (Deprecated) NEMA17 steppers mounts for toolhead PCBs and shrouds to cover them. |

## Additional Mods

### Klicky Docks

These are related mods not linked elsewhere that may be useful for your build.

| Mod Name | Author | Purpose |
|----------|--------|---------|
| [Klicky Probe Dock for Mercury 1 Zero G](https://www.printables.com/model/386819-klicky-probe-dock-for-mercury-1-zero-g) | [Sir_Wash](https://www.printables.com/social/415185-sir_wash) | Adds a dock for Klicky; works with `klicky_bottom.stl`. |
| [Ender 5/Mercury One Klicky Probe Dock](https://www.printables.com/model/595738-ender-5mercury-one-klicky-probe-dock) | [jonspaceharper](https://www.printables.com/@jonspaceharper) | Uses M3 instead of M5 screws and provides enough adjustment for regular and UHF hotends. |

### Filament Sensors

Multi-material printing often requires a filament sensor at the toolhead. There are two known third-party mods for this using different detection methods; note that these do not function as runout sensors (they are after the extruder).

- [Inductive Sensor](https://www.printables.com/model/239026-eva-3-toolhead-sensor) by [Dutchwoody](https://www.printables.com/@Dutchwoody)
- [Microswitch and Ball Bearing](https://www.printables.com/model/442650-eva-3-toolhead-sensor-mechanical-and-reliable) by [Guy](https://www.printables.com/@Guy_258839)