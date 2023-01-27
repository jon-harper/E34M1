---
title: Welcome
summary: E34M1 landing page
authors: Jon Harper
date: 2023-1-26
hide: navigation
---

Welcome! E34M1 is a project to adapt [EVA 3][eva3] for the [Mercury One][merc1] project. It includes support for stepper-mounted PCBs and other tools for a Mercury One build.

## Compatibility

**Linear Rail/Top Piece**

Support for MGN12C is dropped in favor of the more common MGN12H.

- [x] MGN12H
- [ ] MGN12C

**Hotends**

Volcano hotends are not currently supported due to the lack of a working Volcano duct.  Once a Volcano duct is available, this mod will support all hotends normally supported by EVA 3.

- [x] Standard hotends
- [ ] Volcano hotends (planned)

**Extruders**

All extruders are compatible.

**Part Fans Inlet**

Inlets may be made compatible fairly easily.

- [x] Single 5015 (stock)
- [x] Sideways 5015
- [ ] Dual 5015

**Horns/Ducts**

Non-stock ducts may be made compatible by extending them. The stock ducts contain geometry errors; the ones to the Volcano horns are beyond my ability to repair.

- [x] Dual horns
- [ ] Volcano horns (planned)

**Probes**

Support for all probes listed are project goals.

- [x] BLTouch
- [ ] BLTouch for Volcano (in progress)
- [ ] Klicky (in progress)
- [ ] 8mm probes (planned)

**Cooling Fans**

No changes are made to cooling fan mounting; mods are likely compatible.

**Shrouds**

All stock shrouds are compatible.

## New Parts

### Z Limit Switch Mount

This allows the bed to raise high enough to reach the elevated gantry.

### X Axis Stop Block

This is a bumper for the X axis limit switch that is compatible with Mercury One.

### Toolhead PCB Mounts

Mounts are available for both '36- and '42-style PCBs.

Shrouds to cover the PCB are also available.

### Quick Remove Front Face Adapter

This adapter is a shim that allows the shroud and cooling fan to be attached and removed with two (2) screws instead of four (4).

## Other Changes and Additions

- The back tensioner and belt catch is removed entirely.
- The top piece has an attachment point for a cable guide (in place of the back piece).
- There is a top piece available without a this feature for toolhead PCB users.
- The cable guide supports wider zip ties.
- All parts use Mercury One/Voron-style inserts (M3x5x4) instead of the normal EVA inserts.

[eva3]: https://main.eva-3d.page/
[merc1]: https://docs.zerog.one/