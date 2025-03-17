---
title: Assembly Overview
summary: Introduction to assembling E34M1.
authors: Jon Harper
date: 2023-4-8
---

This guide covers assembly of a basic E34M1 build with a Rapido hotend, Sherpa Mini extruder, and BLTouch probe.

You should have your Mercury One build's X axis extrusion and linear rail assembled before following this guide. It is recommended that you include routing and securing the belts as part of the E34M1 build process, and will be prompted to do so.

!!! note "Beacon and Cartographer Users"
    These ABL types are not directly covered in this guide. Install your Beacon or Cartographer Low Profile probes according to the
    developer's documentation before starting E34M1 assembly.

## :material-printer-3d-nozzle: Print Checklist

Before continuing, check that you have all the printed parts necessary.

| Module | Example Part | Revision | Qty |
|---|---|---|---|
| [Front](../modules/front.md)          | FYSETC Portable Input Shaper Front| v0.5 | 1 |
| Front                                 | Belt Grabbers                     | v0.5 | 2 |
| [Top](../modules/top.md)              | Left-Handed Top with Cable Guide  | v0.5 | 1 |
| [Bottom Horns](../modules/bottom.md)  | Dual Horns                        | v0.3 | 1 |
| [Rear Inlet](../modules/rear.md)      | Single 5015 Fan                   | v0.2 | 1 |
| [Hotend Mount](../modules/hotend.md)  | Dragon BMO Mount                  | n/a | 1 |
| [Drive Mount](../modules/drive.md)    | Sherpa Mini Drive Mount           | n/a | 1 |
| [ABL Mount](../modules/abl.md)        | BLTouch Mount                     | v0.3 | 1 |
| [Other](../modules/other.md)          | Cable Guide                       | n/a | 1 |

Not all parts for E34M1 are covered in this guide. Other parts you may need or want for your build:

| Part | Purpose |
|------|---------|
| [X Axis Stop Block](../modules/stop_block.md) | Adjustable bumper for the X axis limit switch. |
| [Z Endstop Mount](../modules/other.md#z-endstop-mount) | For Ender 5 Pros with stock Z axis; raises the Z limit switch. |
| [PCB Mount](../modules/pcb_mounts.md#pcb-mounts) | Mounts for toolhead PCBs. |
| [PCB Shrouds](../modules/pcb_mounts.md#pcb-shrouds) | Covers toolhead PCB wiring. |
| Rear Cable Arm | Raises and supports cable umbilical. |

## Considerations

### Time

Assembly time depends on your experience level and build configuration. Wiring and connecting the belts are not part of this guide, but some guidence is given on these topics.

Excluding wiring and belt routing, assembly time is approximately 30-45 minutes.

### Heat Set Inserts

All heat set inserts should be installed before beginning this guide. The [Modules & BOM](../modules/index.md) section includes locations for every heat set insert included with E34M1.

!!! warning "Warning: Heat Set Inserts"
    Stock EVA 3 uses M3 x 4.6mm OD x 4mm L heat set inserts. E34M1 maintains consistency with ZeroG and uses M3 x 5mm OD x 4mm L inserts (often called "Voron inserts"). Double-check which insert you should be using for third-party components to avoid damaging or ruining a printed part.

### Lock Washers

M3 lock washers are used extensively in this guide. Lock washers are not required but are strongly recommended to prevent loosening screws.

To emphasize that they are optional, lock washers are *italicized* in the guide's Parts lists.
