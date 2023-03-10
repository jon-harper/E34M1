---
title: Compatibility
summary: Summary of changes and compatibility.
authors: Jon Harper
date: 2023-1-27
hide: navigation
---

!!! note
    If you want to make a mod and check compatibility, see the [`/CAD`][folder_cad] folder for a sample assembly in `STEP` format.

## Mecury One Compatibility

E34M1 is compatible with Mercury One without limitations, i.e. no print area is lost by converting to EVA 3 from a different toolhead.

Minor modifications may be necessary to your Mercury One build (e.g., adjusting the Z end stop height). See [Other Changes and Additions](#other-changes-and-additions) for examples.

This mod is not yet tested on an Ender 5 Plus or with Hydra. Feedback is welcome if you have tried E34M1 with either.

## EVA 3 Compatibility

### Linear Rail/Top Piece

Support for MGN12C carriages was dropped in favor of the more common MGN12H that is used with Mercury One.

- [x] MGN12H
- [ ] MGN12C

### Hotends

Volcano hotends are not currently supported due to the lack of a working Volcano duct. Once a Volcano duct is available, this mod will support all hotends normally supported by EVA 3.

- [x] Standard hotends
- [ ] Volcano hotends (pending compatible bottom horns)

### Extruders

All stock extruders are compatible.

!!! note
    Mounting the Drive (extruder and stepper assembly) normally uses seven (7) M3-0.5 x 8mm SHCS. You will need to substitute three (3) of these screws for M3-0.5 x 12mm SHCS.

### Part Fan Inlets

Inlets may be made compatible fairly easily. The inlets included with E34M1 have a lower profile than stock EVA. This allows them to accomodate stepper-mounted breakout boards and should be considered when adapting ducts for E34M1.

- [x] Rear-facing 5015
- [x] Sideways 5015
- [ ] EVA stock

### Horns/Ducts

Existing duct mods may be made compatible by extending them.

The stock ducts contain geometry errors; the ones to the Volcano horns are beyond my ability to repair.

- [x] Dual horns
- [ ] Volcano horns (planned)

### ABL/Probes

Support for all probes listed are project goals. The ABL mount point is different than EVA 3 stock, so each ABL must be added individually.

- [x] BLTouch
- [x] BLTouch for Volcano hotends
- [x] Klicky\*
- [ ] Klicky for Volcano hotends (planned)
- [ ] 8mm probes (planned)
- [ ] 12mm probes (planned)

!!! note
    See the [Files](files.md) page for a compatible Klicky dock.

### Front Cooling Fans

No changes are made to hotend cooling fan mounting; mods are likely compatible.

### Shrouds

All stock shrouds are compatible.

### Cable Management

The top piece has an attachment point for a cable guide. There is a top piece available without this feature for toolhead PCB users; the toolhead PCB mounts all have cable guide attachment points.

The modified cable guide supports wider zip ties; the stock cable guide remains compatible.

## Other Changes and Additions

- The back tensioner and belt catch is removed entirely.
- All parts use Mercury One/Voron-style inserts (M3x5x4) instead of the normal EVA inserts.
- A new Z Limit Switch Mount allows the bed on Ender 5 Pros to reach the EVA 3 gantry.
- A X axis end stop bumper, modified from Mercury One Classic.
- Mounts are available for both '36- and '42-style toolhead PCBs.
- Shrouds to cover the PCB and mount wiring are available.
- There is an adapter that allows the shroud and cooling fan to be attached and removed with two (2) screws instead of four (4).