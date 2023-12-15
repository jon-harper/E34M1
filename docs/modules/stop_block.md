---
title: X Axis Stop Blocks
summary: Options for triggering the X endstop.
authors: Jon Harper
date: 2023-5-3
---

Stop blocks are bumpers for the X endstop (or toolhead if using sensorless homing). Several options are available based on your needs.

### Adjustable X Axis Stop Block

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

**Description**

This is an adaptation of the M1 stop block for EVA 3. It acts as a bumper for the X endstop that can be moved to trigger at the edge of the bed.

Roll in tee nuts may be used instead of drop-in for easier installation.

[**Revision:**](#revision-history) v0.1

**Bill of Materials**

| Parts     | Qty |
|-----------|-----|
| [:material-printer-3d-nozzle: `x_axis_stop_block.stl`][x_stop_block] | 1 |
| M3-0.5 x 8mm SHCS | 2 |
| Drop In Tee Nut, 2020 Profile, M3 | 2 | 

</div>
<div markdown class="jh-grid-img">
![x_stop_block_illustration](../img/components/x_stop_block.png){ width=200px }
</div>
</div>

### Ender 5 Plus 377mm Stop Block

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

**Description**

The adjustable stop block does not *quite* fit for the edge of the 370x377mm bed. This stop block projects far enough out from the X Joint to trigger the endstop at *X = 377mm*.

The M5 x 16mm screw replaces the M5 x 12mm screw that normally attaches the X Joint to the X extrusion.

[**Revision:**](#revision-history) v0.1

**Bill of Materials**

| Parts     | Qty |
|-----------|-----|
| [:material-printer-3d-nozzle: `e5plus_x_axis_stop_block.stl`][e5plus_stop_block] | 1 |
| M5-0.8 x 16mm SHCS | 1 |
| *Lock washer, M5* | *1* | 

</div>
<div markdown class="jh-grid-img">
![x_stop_block_illustration](../img/components/e5plus_x_stop_block.png){ width=200px }
</div>
</div>

### Max X Axis Stop Block

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

**Description**

This block mounts on the top edge of the X joint, triggering at the maximum distance available on the X axis. Use this if you have a large bed or need room outside the bed (such as a nozzle brush).

The M5 x 16mm screw replaces the M5 x 12mm screw that normally attaches the X joint to the X extrusion.

[**Revision:**](#revision-history) v0.1

**Bill of Materials**

| Parts     | Qty |
|-----------|-----|
| [:material-printer-3d-nozzle: `x_axis_max_x_stop_block.stl`][x_max_stop_block] | 1 |
| M5-0.8 x 16mm SHCS | 1 |
| *Lock washer, M5* | *1* | 

</div>
<div markdown class="jh-grid-img">
![x_stop_block_illustration](../img/components/x_max_stop_block.png){ width=200px }
</div>
</div>

## Revision History

| Date | File | Version | Description |
|------|------|---------|-------------|
| 23/05/06 | `e5plus_x_axis_stop_block.stl` | v0.1 | Initial release. |
| 23/05/03 | `x_axis_max_x_stop_block.stl`  | v0.1 | Initial release. |
| 23/01/16 | `x_axis_stop_block.stl`        | v0.1 | Initial release. |