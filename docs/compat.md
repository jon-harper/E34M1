---
title: Compatibility
summary: Summary of changes and compatibility.
authors: Jon Harper
date: 2023-1-27
hide: navigation
---

## Mecury One Compatibility

E34M1 is compatible with Mercury One without build area limitations, i.e. no print area is lost by converting to EVA 3 from a different toolhead.

Minor modifications may be necessary to your Z axis (e.g., adjusting the Z end stop height). See [Other Changes and Additions](#other-changes-and-additions) for examples.

See the [`/CAD`][folder_cad] folder for a sample assembly in `STEP` format.

!!! note
    Mercury One.1 with E34M1 has a theoretical build area of 275mm x 275mm using 330mm linear rails.

    Practical build area is affected by your build, e.g. the type of rear intake used or presence of a toolhead PCB.

## EVA 3 Compatibility

E34M1 is generally compatible with EVA 3 hotend mounts and drive modules. Stock EVA cooling inlets may be used with E34M1 with an adapter.

### Horns/Ducts

Existing bottom horn mods may be made compatible with E34M1 by extending them.

- [x] Dual horns
- [x] Volcano horns *(for some configurations)*

### ABL

!!! note
    The side ABL mount point is different than EVA 3 stock.

|          | Standard Hotends   | Volcano Hotends    | Mount Point |
|----------|:------------------:|:------------------:|:-----------:|
| BLTouch  | :white_check_mark: | :white_check_mark: | ABL         |
| Klicky   | :white_check_mark: | *Planned*          | Bottom      |
| Beacon   | *Planned*          | :white_check_mark: | Bottom      |
| CR Touch | *Planned*          | *Planned*          | ABL         |

Support for 8mm and 12mm probes is not currently planned.

### Cable Management

There are two methods of cable management and two attachment points. The table below shows how they are compatible.

| Part             | Cable Guide | Cable Chain |
|------------------|:-----------:|:-----------:|
| Top with Endstop | :white_check_mark: | *Planned* |
| PCB Mount        | :white_check_mark: | :white_check_mark: |

Currently only open cable chain hole patterns are supported.

## Other Changes and Additions

- All parts use Mercury One/Voron-style inserts (M3x5x4) instead of the normal EVA inserts.
- The back piece (belt tensioner/belt catch) is removed entirely.
- *New:* A new Z Limit Switch Mount allows the bed on Ender 5 Pros to reach the EVA 3 gantry.
- *New:* A X axis end stop bumper, modified from Mercury One Classic.
- *New:* Mounts are available for both '36- and '42-style toolhead PCBs for NEMA17 steppers.
- *New:* Shrouds to cover the PCB and mount wiring are available.
- *New:* There is an adapter that allows the shroud and cooling fan to be attached and removed with two (2) screws instead of four (4).