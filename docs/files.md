---
title: Files
summary: Summary of the repository file list
authors: Jon Harper
date: 2023-1-28
hide: navigation
---

## Printable Files

- Status: Indicates progress of the file towards completion. A check mark indicates a file has no known issues and is fit tested.
- HSI: The file requires [heat set inserts (HSI)](inserts.md).

| Filename                      | Purpose | Status | HSI |
|-------------------------------|---------|--------|---------|
| [`5015_inlet_fi.stl`][5015_inlet] | Lowered version of the stock inlet.   | :material-check-bold: | Y |
| [`5015_sideways_inlet_fi.stl`][5015_sideways_inlet]  | Improved Y axis profile 5015 inlet.   | :material-check-bold: | Y |
| [`belt_grabber.stl`][belt_grabber] | Larger belt grabber for the front.    | :material-check-bold: | N |
| [`bl_touch_mount.stl`][bltouch_mount] | ABL mount for BL Touch (non-Volcano). | :material-check-bold: | N |
| [`bottom_horns_fi.stl`][bottom_horns] | Longer bottom cooling duct.           | :material-check-bold: | Y |
| [`bottom_horns_klicky_fi.stl`][bottom_klicky]  | Bottom duct compatible with Klicky.   | :material-check-bold: | Y |
| [`cable_guide.stl`][cable_guide]             | Stock cable guide with larger zip tie cutouts. | :material-check-bold: | N |
| [`front_intake_duct.stl`][front_intake] | Duct for easier front fan/shroud removal. | :material-check-bold: | Y |
| [`front_universal_fi.stl`][front] | Replaces stock universal front.       | :material-check-bold: | Y |
| [`front_universal_pis_fi.stl`][front_pis] | Same as above; adds FYSETC portable input shaper support. | :material-check-bold: | Y |
| [`hotend_bmo_fi.stl`][dragon_bmo] | Dragon BMO hotend with M1-compatible inserts. | :material-check-bold: | Y |
| [`pcb36_mount.stl`][pcb36_mount] | Stepper mount for NEMA14 ('36) toolhead PCBs. | :material-check-bold: | Y |
| [`pcb42_mount.stl`][pcb42_mount] | Stepper mount for NEMA17 ('42) toolhead PCBs. | :material-check-bold: | Y |
| [`top_endstop_mgn12h.stl`][top] | Top piece compatible with MGN12H and M1 X endstop. | :material-check-bold: | Y |
| [`top_endstop_mgn12h_pcb.stl`][top_pcb] | Same as above; removes cable guide attachment. | :material-check-bold: | Y |
| [`x_axis_stop_block.stl`][x_stop_block] | Bumper for the X axis endstop. | :material-check-bold: | N |
| [`z_limit_switch_cover.stl`][z_limit_cover] | Covers the Z endstop PCB. | :material-check-bold: | N |
| [`z_limit_switch_mount.stl`][z_limit_mount] | Raises the Z endstop. | :material-check-bold: | Y |

## Related and Contributed Mods

These are user mods that add compatibility or new features to EVA 3.

| Mod Name | Author | Purpose |
|----------|--------|---------|
| [Klicky Probe Dock for Mercury 1 Zero G](https://www.printables.com/model/386819-klicky-probe-dock-for-mercury-1-zero-g) | [Sir_Wash](https://www.printables.com/social/415185-sir_wash) | Adds a dock for Klicky; works with `bottom_horns_klicky_fi.stl`. |

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