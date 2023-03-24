---
title: Files
summary: Summary of the repository file list
authors: Jon Harper
date: 2023-1-28
hide: navigation
---

## Printable Files

The HSI columns signifies whether or not the file requires [heat set inserts (HSI)](inserts.md).

| Filename                      | Purpose | HSI    |
|-------------------------------|---------|--------|
| [`5015_inlet_fi.stl`][5015_inlet] | Lowered version of the stock inlet.   | Y |
| [`5015_sideways_inlet_fi.stl`][5015_sideways_inlet]  | Improved Y axis profile 5015 inlet.   | Y |
| [`belt_grabber.stl`][belt_grabber] | Larger belt grabber for the front.    | N |
| [`bl_touch_mount.stl`][bltouch_mount] | ABL mount for BL Touch (non-Volcano). | N |
| [`bottom_horns_fi.stl`][bottom_horns] | Longer bottom cooling duct.           | Y |
| [`bottom_horns_klicky_fi.stl`][bottom_klicky]  | Bottom duct compatible with Klicky.   | Y |
| [`cable_guide.stl`][cable_guide]             | Stock cable guide with larger zip tie cutouts. | N |
| [`front_intake_duct.stl`][front_intake] | Duct for easier front fan/shroud removal. | Y |
| [`front_universal_fi.stl`][front] | Replaces stock universal front.       | Y |
| [`front_universal_pis_fi.stl`][front_pis] | Same as above; adds FYSETC portable input shaper support. | Y |
| [`hotend_bmo_fi.stl`][dragon_bmo] | Dragon BMO hotend with M1-compatible inserts. | Y |
| [`pcb36_mount.stl`][pcb36_mount] | Stepper mount for NEMA14 ('36) toolhead PCBs. Uses the cable guide. | Y |
| [`pcb42_mount.stl`][pcb42_mount] | Stepper mount for NEMA17 ('42) toolhead PCBs. Uses the cable guide. | Y |
| [`pcb36_mount_cable_chain.stl`][pcb36_mount_cable_chain] | Stepper mount for NEMA14 PCBs. Uses cable chains. | Y |
| [`pcb42_mount_cable_chain.stl`][pcb42_mount_cable_chain] | Stepper mount for NEMA17 PCBs. Uses cable chains. | Y |
| [`pcb_shroud.stl`][pcb_shroud] | Simple cover for toolhead PCBs. | N |
| [`pcb_shroud_cat.stl`][pcb_shroud_cat] | Whimsical shroud with a cat face. | N |
| [`pcb_shroud_30mm_fan.stl`][pcb_shroud_30mm] | Shroud that mounts a 30mm fan for CAN PCBs. | Y |
| [`top_endstop_mgn12h.stl`][top] | Top piece compatible with MGN12H and M1 X endstop. | Y |
| [`top_endstop_mgn12h_pcb.stl`][top_pcb] | Same as above; removes cable guide attachment. | Y |
| [`x_axis_stop_block.stl`][x_stop_block] | Bumper for the X axis endstop. | N |
| [`z_limit_switch_cover.stl`][z_limit_cover] | Covers the Z endstop PCB. | N |
| [`z_limit_switch_mount.stl`][z_limit_mount] | Raises the Z endstop. | Y |

## Related and Contributed Mods

These are user mods that add compatibility or new features to EVA 3.

| Mod Name | Author | Purpose |
|----------|--------|---------|
| [Klicky Probe Dock for Mercury 1 Zero G](https://www.printables.com/model/386819-klicky-probe-dock-for-mercury-1-zero-g) | [Sir_Wash](https://www.printables.com/social/415185-sir_wash) | Adds a dock for Klicky; works with `bottom_horns_klicky_fi.stl`. |
| [Beacon Volcano Duct](https://www.printables.com/model/428524-eva30-phaetus-rapido-uhfvolcano-beacon-for-mercury) | [Psych0h3ad](https://www.printables.com/social/168275-psych0h3ad/about) | Add support for Beacon ABL for Volcano-length hotends. |
| [EVA 3 Beltless backplate for dual 5015](https://www.printables.com/model/430281-eva-3-beltless-backplate-for-dual-5015) | [Psych0h3ad](https://www.printables.com/social/168275-psych0h3ad/about) | Allows any stock rear intake to be used with E34M1. |
| [E34M1/EVA 3 Lightweight Back Piece ](https://www.printables.com/model/431146-e34m1eva-3-lightweight-back-piece) | [jonspaceharper](https://www.printables.com/social/511131-jonspaceharper/about) | Allows any stock rear intake to be used with E34M1. Lightweight remix of the above. |

## STEP Files (`/CAD`)

This is a list of all parametric assemblies on the repository.

- [5015_inlet_fi.step][step_5015_inlet]
- [5015_sideways_inlet.step][step_5015_sideways]
- [BLTouch.step][step_bltouch]
- [Bottom Horns - Volcano v1.step][step_volcano_horns]
- [Bottom Horns - Volcano.f3d][fusion_volcano_horns]
- [Core.Insert.CoreXY.step][step_core]
- [Front Intake Duct.step][step_front_intake]
- [Test Assembly - Dragon BMO and BMG.step][step_test_assembly]
- [Z Limit Switch.step][step_z_endstop]