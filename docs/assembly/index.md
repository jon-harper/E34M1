---
title: Assembly Overview
summary: Introduction to assembling E34M1.
authors: Jon Harper
date: 2023-4-8
---

This guide covers assembly of a basic E34M1 build with a Dragon hotend, BMG extruder, and BLTouch probe. The first half of the assembly process—building the Core—is universal. The second half—adding the hotend, extruder, and ABL—may differ in details to your assembly.

You should have your Mercury One build's X axis extrusion and linear rail assembled before following this guide. It is recommended that you include routing and securing the belts as part of the E34M1 build process.

## Time

Assembly time depends on your experience level and build configuration. Wiring and connecting the belts are not part of this guide, but some guidence is given on these topics.

Excluding wiring and belt routing, assembly time is approximately 30 minutes.

## :material-printer-3d-nozzle: Print Checklist

Before continuing, check that you have all the printed parts necessary.

The table below lists parts that are universal to all builds:

| Module | Example Part | Qty |
|---|---|---|
| [Front](../modules/front.md)          | Stock Front                       | 1 |
| Front                                 | Belt Grabbers                     | 2 |
| [Top](../modules/top.md)              | Top with Endstop and Cable Guide  | 1 |
| [Bottom Horns](../modules/bottom.md)  | Dual Horns                        | 1 |
| [Rear Inlet](../modules/rear.md)      | Low-Profile Sideways Inlet        | 1 |
| [Hotend Mount](../compat/hotends.md)  | Dragon BMO Mount                  | 1 |
| [Drive Mount](../compat/drives.md)    | BMG Drive Mount           | 1 |


The following build-specific parts are used in this guide:

| Part | Example | Qty |
|---|---|---|
| [ABL Mount](../modules/abl.md)        | BLTouch Mount | 1 |
| [Cable Guide](../modules/other.md)    | Other         | 1 |

Not all parts for E34M1 are covered in this guide. Other parts you may need or want for your build:

| Part | Purpose |
|------|---------|
| [X Axis Stop Block](../modules/other.md#x-axis-stop-block) | Adjustable bumper for the X axis limit switch. |
| [Front Intake Duct](../modules/other.md#front-intake-duct) | Easier hotend access using two (2) screws instead of four (4). |
| [Z Endstop Mount](../modules/other.md#z-endstop-mount) | For Ender 5 Pros with stock Z axis; raises the Z limit switch. |
| [PCB Mount](../modules/pcb_mounts.md) | Mounts for toolhead PCBs. |
| [PCB Shrouds](../modules/pcb_shrouds.md) | Covers toolhead PCB wiring. |

## Considerations

### Heat Set Inserts

All heat set inserts should be installed before beginning this guide. The [Modules & BOM](../modules/index.md) section includes locations for every heat set insert included with E34M1.

!!! warning "Warning: Heat Set Inserts"
    Stock EVA 3 uses M3 x 4.6mm OD x 4mm L heat set inserts. E34M1 maintains consistency with ZeroG and uses M3 x 5mm OD x 4mm L inserts (often called "Voron inserts"). Double-check which insert you should be using for third-party components to avoid damaging or ruining a printed part.

### Lock Washers

M3 lock washers are used extensively in this guide. Lock washers are not required (and cannot be used for the Drive module) but are strongly recommended to prevent loosening screws.

To emphasize that they are optional, lock washers are *italicized* in the guide's Parts lists.