---
title: Compatibility
summary: Summary of changes and compatibility.
authors: Jon Harper
date: 2023-1-27
---

## Mecury One Compatibility

E34M1 is compatible with Mercury One without build area limitations, i.e. no print area is lost by converting to EVA 3 from a different toolhead.

Minor modifications may be necessary to your Z axis (e.g., adjusting the Z end stop height). See [Other Changes and Additions](#other-changes-and-additions) for examples.

See the [`/CAD`][folder_cad] folder for a sample assembly in `STEP` format.

!!! note
    Mercury One.1 with E34M1 has a theoretical build area of 275mm x 275mm using 330mm linear rails.

    Practical build area is affected by your build, e.g. the type of rear intake used or presence of a toolhead PCB.

## EVA 3 Compatibility

E34M1 is generally compatible with EVA 3 hotend mounts and drive modules. See the [Hotends](hotends.md) and [Extruder](drive.md) pages for a list of known mounts (including non-stock mods).

### Heat Set Inserts

All E34M1 parts are designed for Mercury One/Voron-style inserts (M3x5x4) instead of the M3x4.6x4 inserts preferred by EVA. Every part has a bill of materials that reflects this.

### ABL

The side ABL mount points are different than EVA 3 stock, and not all ABL methods use them. The chart below shows which ABL methods are supported by E34M1.

|          | Standard Hotends   | Volcano/UHF Hotends | Mount Point |
|----------|:------------------:|:------------------:|:-----------:|
| BLTouch  | :white_check_mark: | :white_check_mark: | ABL         |
| CR Touch | :white_check_mark: | :white_check_mark: | ABL         |
| Klicky   | :white_check_mark: | *Planned*          | Bottom      |
| Beacon   | :white_check_mark: | :white_check_mark: | Bottom      |

Support for 8mm and 12mm inductive probes is not currently planned.

### Bottom Horns

| Duct Type             | Standard Hotends | Volcano/UHF Hotends  |
|-----------------------|:----------------:|:--------------------:|
| Dual Horns            | :white_check_mark: | *See note*         |
| Dual Horns for Klicky | :white_check_mark: | *See note*         |
| Dual Horns for Beacon | :white_check_mark: | :white_check_mark: |
| Trihorns              | :white_check_mark: | :x:                |
| Trihorns for Klicky   | :white_check_mark: | :x:                |
| Trihorns for Beacon   | :x:                | :x:                |

!!! note
    EVA 3's dual horn for Volcano hotends contains geometry errors. This limits support at present.

### Cooling Inlets

Stock EVA cooling inlets may be used with E34M1 with an [adapter](../modules/rear.md#stock-rear-inlet-adapter).


### Cable Management

There are two methods of cable management and two attachment points. The table below shows how they are compatible.

| Part             | Cable Guide | Cable Chain |
|------------------|:-----------:|:-----------:|
| Top with Endstop | :white_check_mark: | *Planned* |
| PCB Mount        | :white_check_mark: | :white_check_mark: |

Currently only open cable chain hole patterns are supported.