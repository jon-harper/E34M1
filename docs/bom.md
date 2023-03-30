---
title: Bill of Materials
summary: Materials for each E34M1 part
authors: Jon Harper
date: 2023-1-26
hide: navigation
---

This page contains a bill of materials for each EVA "module".

!!! note
    - All heat set inserts are "Voron-style" (M3x5x4) instead of the thinner "EVA-style" (M3x4.6x4).

## Core E34M1 Assembly

The core assembly contains four modules:

- [Universal Front](#universal-front)
- [Top with Endstop](#top-piece-with-endstop)
- [Bottom Horns](#bottom-horns)
- [Rear Cooling Inlet](#cooling-inlet)

There is no longer a back piece as in EVA 3; it is removed in this mod. The part cooling inlet is modified to serve in its place.

### Universal Front

There are two version of the universal front:

1. Stock Front: Mounts an ADXL345 input shaper (stock EVA 3)
2. PIS Front: Mounts a FYSETC portable input shaper

=== "Stock Front"
    <div markdown class="jh-grid-container jh-grid-2">
    <div markdown class="jh-grid-para">
    
    | Parts     | Qty | Notes |
    |-----------|-----|-------|
    | [:material-printer-3d-nozzle: `universal_front_fi.stl`][front]  | 1 | |
    | [:material-printer-3d-nozzle: `belt_grabber.stl`][belt_grabber] | 2 | |
    | Screw, M3-0.5 x 6mm       | 4 | May substitute with 8mm. |
    | Screw, M3-0.5 x 40mm      | 4 | |
    | Heat Set Insert, M3x5x4   | 14 |

    If using an accelerometer, add:

    - ADXL345 (x1)
    - Screw, M3-0.5 x 8mm (x2)

    </div>
    <div markdown class="jh-grid-img">
    ![front_illustration](img/parts/front_universal.png){ width=256px}
    </div>
    </div>

=== "PIS Front"
    <div markdown class="jh-grid-container jh-grid-2">
    <div markdown class="jh-grid-para">

    | Parts     | Qty | Notes |
    |-----------|-----|-------|
    | [:material-printer-3d-nozzle: `universal_front_pis_fi.stl`][front_pis]  | 1 | |
    | [:material-printer-3d-nozzle: `belt_grabber.stl`][belt_grabber] | 2 | |
    | Screw, M3-0.5 x 6mm       | 4 | May substitute with 8mm. |
    | Screw, M3-0.5 x 8mm       | 2 | |
    | Heat Set Insert, M3x5x4   | 16 |
    | FYSETC Portable Input Shaper | 1 |

    </div>
    <div markdown class="jh-grid-img">
    ![front_illustration](img/parts/front_universal_pis.png){ width=256px}
    </div>
    </div>

### Top with Endstop

1. Top with Endstop: Top piece modified for M1 with a cable guide.
2. PCB Mount Top: Top piece for PCB mount users without a cable guide. See [PCB Mount](#pcb-mount).

=== "Top with Endstop"
    <div markdown class="jh-grid-container jh-grid-2">
    <div markdown class="jh-grid-para">

    | Parts     | Qty | Notes |
    |-----------|-----|-------|
    | [:material-printer-3d-nozzle: `top_endstop_mgn12h.stl`][top] | 1 | |
    | [:material-printer-3d-nozzle: `cable_guide.stl`][cable_guide] | 1 | |
    | Horizontal limit switch  | 1 | |
    | Screw, M3-0.5 x 6mm      | 2 | May substitute 8mm. |
    | Screw, M3-0.5 x 8mm      | 6 | |
    | Heat Set Insert, M3x5x4  | 6 | |

    </div>
    <div markdown class="jh-grid-img">
    ![top_illustration](img/parts/top_endstop_mgn12h.png){ width=256px}
    </div>
    </div>

=== "PCB Mount Top"
    <div markdown class="jh-grid-container jh-grid-2">
    <div markdown class="jh-grid-para">

    | Parts     | Qty | Notes |
    |-----------|-----|-------|
    | [:material-printer-3d-nozzle: `top_endstop_mgn12h_pcb.stl`][top_pcb] | 1 | |
    | Horizontal limit switch  | 1 | |
    | Screw, M3-0.5 x 8mm      | 6 | |
    | Heat Set Insert, M3x5x4  | 4 | |

    </div>
    <div markdown class="jh-grid-img">
    ![top_illustration](img/parts/top_endstop_mgn12h_pcb.png){ width=256px}
    </div>
    </div>

### Bottom Horns

Two versions are available with E34M1:

1. Stock Bottom Horns: Modified version of the stock EVA 3 bottom.
2. Klicky Bottom Horns: Like the above, but with support for Klicky.

[Additional options are available as mods.](tour.md#related-and-contributed-mods)

=== "Stock Bottom Horns"
    <div markdown class="jh-grid-container jh-grid-2">
    <div markdown class="jh-grid-para">

    | Parts     | Qty | Notes |
    |-----------|-----|-------|
    | [:material-printer-3d-nozzle: `bottom_horns_fi.stl`][bottom_horns]     | 1 | |
    | Heat Set Insert, M3x5x4   | 1 | |

    </div>
    <div markdown class="jh-grid-img">
    ![bottom_illustration](img/parts/bottom_horns.png){ width=256px}
    </div>
    </div>

=== "Klicky Bottom Horns"
    <div markdown class="jh-grid-container jh-grid-2">
    <div markdown class="jh-grid-para">

    | Parts     | Qty | Notes |
    |-----------|-----|-------|
    | [:material-printer-3d-nozzle: `bottom_horns_klicky_fi.stl`][bottom_klicky]     | 1 | |
    | Heat Set Insert, M3x5x4   | 1 | |

    !!! note
        The additional materials required for the Klicky probe wiring and magnets are beyond the scope of this documentation.

    </div>
    <div markdown class="jh-grid-img">
    <!-- ![bottom_illustration](img/parts/bottom_horns.png){ width=256px} -->
    </div>
    </div>

### Rear Cooling Inlet

Two versions are available with E34M1:

1. Low-Profile Cooling Inlet: Modified stock 5015 inlet with lower height.
2. Low-Profile Sideways Cooling Inlet: Low-height sideways mount for a 5015 part fan.

There are [mods available](tour.md#related-and-contributed-mods) to use stock EVA 3 intakes with E34M1, as well.

=== "Low-Profile Cooling Inlet"
    <div markdown class="jh-grid-container jh-grid-2">
    <div markdown class="jh-grid-para">

    | Parts     | Qty | Notes |
    |-----------|-----|-------|
    | [:material-printer-3d-nozzle: `5015_inlet_fi.stl`][5015_inlet] | 1 | |
    | Screw, M3-0.5 x 6mm       | 1 | May substitue 8mm. |
    | Screw, M3-0.5 x 20mm      | 1 | |
    | Screw, M3-0.5 x 45mm      | 4 | |
    | Heat Set Insert, M3x5x4   | 1 | |

    </div>
    <div markdown class="jh-grid-img">
    ![inlet_illustration](img/parts/5015_inlet.png){ width=256px}
    </div>
    </div>

=== "Low-Profile Sideways Cooling Inlet"
    <div markdown class="jh-grid-container jh-grid-2">
    <div markdown class="jh-grid-para">

    | Parts     | Qty | Notes |
    |-----------|-----|-------|
    | [:material-printer-3d-nozzle: `5015_sideways_inlet_fi.stl`][5015_sideways_inlet] | 1 | |
    | Screw, M3-0.5 x 6mm       | 1 | May substitue 8mm. |
    | Screw, M3-0.5 x 20mm      | 1 | |
    | Screw, M3-0.5 x 45mm      | 4 | |
    | Heat Set Insert, M3x5x4   | 1 | |

    </div>
    <div markdown class="jh-grid-img">
    ![inlet_illustration](img/parts/5015_sideways_inlet.png){ width=256px}
    </div>
    </div>

## Other Parts

### ABL

The ABL mount point offers support for several ABL/hotend combinations:

1. BLTouch
2. BLTouch for Volcano hotends
3. CR Touch (non-Volcano)
4. CR Touch Volcano support is available through [this mod](https://www.printables.com/model/434179-eva3-uhf-cr-touch).

=== "BLTouch"
    <div markdown class="jh-grid-container jh-grid-2">
    <div markdown class="jh-grid-para">

    | Parts     | Qty | Notes |
    |-----------|-----|-------|
    | [:material-printer-3d-nozzle: `bl_touch_mount.stl`][bltouch_mount] | 1 | |
    | Hex Nut, M3               | 2 | |
    | Screw, M3-0.5 x 6mm       | 2 | May substitute 8mm. |
    | Screw, M3-0.5 x 8mm       | 2 | |

    </div>
    <div markdown class="jh-grid-img">
    ![bltouch_illustration](img/parts/bltouch_mount.png){ width=100px }
    </div>
    </div>
=== "BLTouch Volcano"
    <div markdown class="jh-grid-container jh-grid-2">
    <div markdown class="jh-grid-para">

    | Parts     | Qty | Notes |
    |-----------|-----|-------|
    | [:material-printer-3d-nozzle: `bl_touch_volcano_mount.stl`][bltouch_volcano] | 1 | |
    | Hex Nut, M3               | 2 | |
    | Screw, M3-0.5 x 6mm       | 2 | May substitute 8mm. |
    | Screw, M3-0.5 x 8mm       | 2 | |

    </div>
    <div markdown class="jh-grid-img">
    <!-- ![bltouch_illustration](img/parts/bltouch_mount.png){ width=100px } -->
    </div>
    </div>
=== "CR Touch"
    <div markdown class="jh-grid-container jh-grid-2">
    <div markdown class="jh-grid-para">

    | Parts     | Qty | Notes |
    |-----------|-----|-------|
    | [:material-printer-3d-nozzle: `cr_touch_mount.stl`][crtouch_mount] | 1 | |
    | Heat Set Insert, M3x5x4   | 2 | |
    | Screw, M3-0.5 x 8mm       | 4 | |

    </div>
    <div markdown class="jh-grid-img">
    <!-- ![bltouch_illustration](img/parts/bltouch_mount.png){ width=100px } -->
    </div>
    </div>

### Front Intake Duct

Hotend cooling fans may be attached using an intake duct that allows two (2) screws to remove the fan instead of four (4). The BOM below is for a 4010 fan with the duct.

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

| Parts     | Qty | Notes |
|-----------|-----|-------|
| [:material-printer-3d-nozzle: `front_intake_duct.stl`][front_intake]  | 1 | |
| :material-printer-3d-nozzle: EVA shroud                | 1 | Your choice of printed shroud. Optional. |
| Axial Fan, 40mm x 10mm    | 1 | May substitute 20mm thickness. |
| Screw, M3-0.5 x 12mm      | 2 | |
| Screw, M3-0.5 x 16mm      | 2 | |
| Heat Set Insert, M3x5x4   | 2 | |

</div>
<div markdown class="jh-grid-img">
![intake_illustration](img/parts/intake_duct.png){ width=256px }
</div>
</div>

### Toolhead PCB Mount

Mounts for both NEMA14 ("36") and NEMA17 ("42") PCBs are available. Examples of '36 PCBs are the BIGTREETECH EBB36 and Piggyback36, as well as the Mellow Fly SHT36. An example of a '42 PCB is the BIGTREETECH EBB42.

Variants of each mount are available for both cable guides and cable chains.

!!! caution
    These mounts are only currently tested on NEMA17 steppers.

=== "'36 PCB, Cable Guide"
    <div markdown class="jh-grid-container jh-grid-2">
    <div markdown class="jh-grid-para">

    | Parts     | Qty | Notes |
    |-----------|-----|-------|
    | [:material-printer-3d-nozzle: `pcb36_mount.stl`][pcb36_mount] | 1 | |
    | [:material-printer-3d-nozzle: `cable_guide.stl`][cable_guide] | 1 | |
    | Toolhead PCB      | 1 | |
    | Screw, M3-0.5 x 25mm | 2 | |
    | Screw, M3-0.5 x 6mm  | 4 | May substitute two (2) 8mm screws, if desired. |
    | Heat Set Insert, M3x5x4 | 6 | |

    </div>
    <div markdown class="jh-grid-img">
    ![pcb36_illustration](img/parts/pcb36.png){ width=200px }
    </div>
    </div>
=== "'36 PCB, Cable Chain"
    <div markdown class="jh-grid-container jh-grid-2">
    <div markdown class="jh-grid-para">

    | Parts     | Qty | Notes |
    |-----------|-----|-------|
    | [:material-printer-3d-nozzle: `pcb36_mount_cable_chain.stl`][pcb36_mount_cable_chain] | 1 | |
    | Toolhead PCB      | 1 | |
    | Screw, M3-0.5 x 25mm | 2 | |
    | Screw, M3-0.5 x 6mm  | 5 | May substitute 8mm screws, if desired. |
    | Heat Set Insert, M3x5x4 | 7 | |

    </div>
    <div markdown class="jh-grid-img">
    ![pcb36_illustration](img/parts/pcb36_cable_chain.png){ width=200px }
    </div>
    </div>
=== "'42 PCB, Cable Guide"
    <div markdown class="jh-grid-container jh-grid-2">
    <div markdown class="jh-grid-para">

    | Parts     | Qty | Notes |
    |-----------|-----|-------|
    | [:material-printer-3d-nozzle: `pcb42_mount.stl`][pcb42_mount] | 1 | |
    | [:material-printer-3d-nozzle: `cable_guide.stl`][cable_guide] | 1 | |
    | Toolhead PCB      | 1 | |
    | Screw, M3-0.5 x 25mm | 2 | |
    | Screw, M3-0.5 x 6mm  | 4 | May substitute two (2) 8mm screws, if desired. |
    | Heat Set Insert, M3x5x4 | 6 | |

    </div>
    <div markdown class="jh-grid-img">
    ![pcb42_illustration](img/parts/pcb42.png){ width=200px }
    </div>
    </div>
=== "'42 PCB, Cable Chain"
    <div markdown class="jh-grid-container jh-grid-2">
    <div markdown class="jh-grid-para">

    | Parts     | Qty | Notes |
    |-----------|-----|-------|
    | [:material-printer-3d-nozzle: `pcb42_mount_cable_chain.stl`][pcb42_mount_cable_chain] | 1 | |
    | Toolhead PCB      | 1 | |
    | Screw, M3-0.5 x 25mm | 2 | |
    | Screw, M3-0.5 x 6mm  | 5 | May substitute 8mm screws, if desired. |
    | Heat Set Insert, M3x5x4 | 7 | |

    </div>
    <div markdown class="jh-grid-img">
    ![pcb42_illustration](img/parts/pcb42_cable_chain.png){ width=200px }
    </div>
    </div>

### Toolhead PCB Shroud

These shrouds cover the PCB and wiring for a PCB mount.

These come in three styles:

- Stock
- Cat face
- 30mm Fan

The cat face shroud is purely cosmetic and uses the same materials as the stock shroud.

=== "Stock"
    <div markdown class="jh-grid-container jh-grid-2">
    <div markdown class="jh-grid-para">

    | Parts     | Qty | Notes |
    |-----------|-----|-------|
    | [:material-printer-3d-nozzle: `pcb_shroud.stl`][pcb_shroud] | 1 | |
    | [:material-printer-3d-nozzle: `pcb_shroud_cat.stl`][pcb_shroud_cat] | 1 | Alternative to the above.|
    | Screw, M3-0.5 x 35mm | 2 | |
    
    </div>
    <div markdown class="jh-grid-img">
    ![pcb42_illustration](img/parts/pcb_shrouds.png){ width=400px }
    </div>
    </div>
=== "30mm Fan"
    <div markdown class="jh-grid-container jh-grid-2">
    <div markdown class="jh-grid-para">

    | Parts     | Qty | Notes |
    |-----------|-----|-------|
    | [:material-printer-3d-nozzle: `pcb_shroud.stl`][pcb_shroud_30mm] | 1 | |
    | Screw, M3-0.5 x 35mm | 2 | |
    | Axial Fan, 30mm x 10mm | 1 | |
    | Screw, M3-0.5 x 14mm | 2 | May use 15mm or 16mm. |
    | Heat Set Insert, M3x5x4 | 4 | |
    
    </div>
    <div markdown class="jh-grid-img">
    ![pcb42_illustration](img/parts/pcb_shroud_30mm.png){ width=200px }
    </div>
    </div>

### X Axis Stop Block

This is an adaptation of the M1 stop block for EVA 3.

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

| Parts     | Qty | Notes |
|-----------|-----|-------|
| [:material-printer-3d-nozzle: `x_axis_stop_block.stl`][x_stop_block] | 1 | |
| Screw, M3-0.5 x 8mm | 2 | |
| Tee Nut, Drop In, M3 | 2 | Roll in tee nuts may be used for easier installation. |

</div>
<div markdown class="jh-grid-img">
![x_stop_block_illustration](img/parts/x_stop_block.png){ width=200px }
</div>
</div>

### Z End Stop Mount

This part is necessary for Ender 5 Pros with stock (non-Hydra) Z kinematics. This part mounts the limit switch higher than normal.

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

| Parts     | Qty | Notes |
|-----------|-----|-------|
| [:material-printer-3d-nozzle: `z_limit_switch_cover.stl`][z_limit_cover] | 1 | |
| [:material-printer-3d-nozzle: `z_limit_switch_mount.stl`][z_limit_cover] | 1 | |
| Screw, M3-0.5 x 16mm | 2 | |
| Screw, M5-0.8 x 8mm  | 1 | |
| Tee Nut, Drop In, M5 | 1 | |
| Heat Set Insert, M3x5x4 | 2 |

</div>
<div markdown class="jh-grid-img">
![z_endstop_illustration](img/parts/z_limit_switch.png){ width=256px }
</div>
</div>
