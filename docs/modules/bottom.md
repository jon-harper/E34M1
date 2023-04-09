---
title: Bottom Horns
summary: Components for the Bottom Horns Module
authors: Jon Harper
date: 2023-4-5
---

Several versions of the bottom horns are available for E34M1. Which version you should use depends on your hotend and your ABL method. See [the Compatibility page](../compat/index.md#bottom-horns) for details.

This page is divided into two sections for standard-length hotends and Volcano/UHF hotends.

## Standard Hotend Bottom Horns

### Dual Horns
<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

**Bill of Materials**

| Parts     | Qty |
|-----------|-----|
| [:material-printer-3d-nozzle: `stock_bottom.stl`][bottom_horns]     | 1 |
| Heat Set Insert, M3x5x4   | 1 |

**Origin**: EVA 3

</div>
<div markdown class="jh-grid-img">
![bottom_illustration](../img/parts/bottom_horns.png){ width=256px}
</div>
</div>

??? note "Heat Set Inserts"
    ![bottom_illustration](../img/inserts/bottom.png){ width=256px}

### Dual Horns for Klicky

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

**Bill of Materials**

| Parts     | Qty |
|-----------|-----|
| [:material-printer-3d-nozzle: `klicky_bottom.stl`][bottom_klicky]     | 1 |
| Heat Set Insert, M3x5x4   | 1 |

**Origin**: EVA 3, [Klicky Probe](https://github.com/jlas1/Klicky-Probe)

!!! note
    The additional materials required for the Klicky probe wiring and magnets are beyond the scope of this documentation.

??? note "Heat Set Inserts"
    ![bottom_illustration](../img/inserts/bottom_klicky.png){ width=256px}

</div>
<div markdown class="jh-grid-img">
![bottom_illustration](../img/parts/bottom_horns_klicky.png){ width=256px}
</div>
</div>

### Dual Horns for Beacon

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

**Bill of Materials**

| Parts     | Qty |
|-----------|-----|
| [:material-printer-3d-nozzle: `beacon_bottom.stl`][bottom_beacon]     | 1 | 
| Heat Set Insert, M3x5x4   | 3 |
| Low-Profile Beacon Kit    | 1 |

**Origin**: [Beacon 3D mount solution for E34M1 - EVA 3 for Mercury One](https://www.printables.com/model/438193-beacon-3d-mount-solution-for-e34m1-eva-3-for-mercu) by [cuiviemen](https://www.printables.com/@cuiviemen_127292)

!!! note
    You will need to remove (or not install) the Molex Sherlock connector for the Beacon PCB and solder your wires directly to the PCB. See [cuiviemen](https://www.printables.com/@cuiviemen_127292)'s [original Beacon mod](https://www.printables.com/model/438193-beacon-3d-mount-solution-for-e34m1-eva-3-for-mercu) for a Rear Intake that helps with wire routing.

    The kit should include the ultra-low-profile M3 screws needed to attach the Beacon.

??? note "Heat Set Inserts"
    ![bottom_illustration](../img/inserts/bottom_beacon.png){ width=256px}

</div>
<div markdown class="jh-grid-img">
![bottom_illustration](../img/parts/bottom_beacon.png){ width=256px}
</div>
</div>

### Trihorns

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

**Bill of Materials**

| Parts     | Qty |
|-----------|-----|
| [:material-printer-3d-nozzle: `bottom_horns_fi.stl`][bottom_horns]     | 1 |
| Heat Set Insert, M3x5x4   | 1 |

??? note "Heat Set Inserts"
    ![bottom_illustration](../img/inserts/bottom_trihorn.png){ width=256px}

</div>
<div markdown class="jh-grid-img">
![bottom_illustration](../img/parts/bottom_trihorns.png){ width=256px}
</div>
</div>

### Trihorns for Klicky

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

**Bill of Materials**

| Parts     | Qty |
|-----------|-----|
| [:material-printer-3d-nozzle: `klicky_bottom_trihorn.stl`][bottom_klicky_trihorn]     | 1 |
| Heat Set Insert, M3x5x4   | 1 |

**Origin**: EVA 3, [Klicky Probe](https://github.com/jlas1/Klicky-Probe)

!!! note
    The additional materials required for the Klicky probe wiring and magnets are beyond the scope of this documentation.

??? note "Heat Set Inserts"
    ![bottom_illustration](../img/inserts/bottom_trihorn_klicky.png){ width=256px}

</div>
<div markdown class="jh-grid-img">
![bottom_illustration](../img/parts/bottom_klicky_trihorns.png){ width=256px}
</div>
</div>

## Volcano/UHF Bottom Horns

Volcano bottom horn support is limited. The EVA 3 source file contains gemeotry errors and must be modified as a mesh.

### Dual Horns for Beacon

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

**Bill of Materials**

| Parts     | Qty |
|-----------|-----|
| [:material-printer-3d-nozzle: `beacon_bottom_uhf.stl`][bottom_beacon_uhf]     | 1 |
| Heat Set Insert, M3x5x4   | 3 |
| Low-Profile Beacon Kit    | 1 |

**Origin**: [EVA3.0 Phaetus Rapido UHF/Volcano +Beacon for Mercury One.1 by ZERO G](https://www.printables.com/model/428524-eva30-phaetus-rapido-uhfvolcano-beacon-for-mercury) by [Psych0h3ad](https://www.printables.com/@Psych0h3ad_168275)

!!! note
    See [cuiviemen](https://www.printables.com/@cuiviemen_127292)'s [original Beacon mod](https://www.printables.com/model/438193-beacon-3d-mount-solution-for-e34m1-eva-3-for-mercu) for a Rear Intake that helps with wire routing.

    The kit should include the ultra-low-profile M3 screws needed to attach the Beacon.

??? note "Heat Set Inserts"
    ![bottom_illustration](../img/inserts/bottom_beacon_uhf.png){ width=256px}
</div>
<div markdown class="jh-grid-img">
![bottom_illustration](../img/parts/bottom_beacon_uhf.png){ width=256px}
</div>
</div>