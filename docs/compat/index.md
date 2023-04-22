---
title: Overview
summary: Summary of changes and compatibility.
authors: Jon Harper
date: 2023-1-27
---

## Mercury One Compatibility

!!! note
    E34M1 is *not* compatible with Mercury One Classic.

E34M1 is compatible with Mercury One.1 without limiting the build area; no print area is lost by converting to EVA 3 from a different toolhead. Minor modifications may be necessary to your Z axis (e.g., adjusting the Z end stop height). See [Other Changes and Additions](#other-changes-and-additions) for examples.

!!! note
    Mercury One.1 with E34M1 has a theoretical build area of 275mm x 275mm using 330mm linear rails.

    Practical build area is affected by your build, e.g. the type of rear intake used or presence of a toolhead PCB.

!!! tip
    Making a mod? Want to see how it looks in CAD? See the [`/CAD`][folder_cad] folder for a `STEP` files.


## EVA 3 Compatibility

### Hotends and Extruders

E34M1 is compatible with other EVA 3 hotend mounts and drive modules. See the [Hotends](hotends.md) and [Extruder](drives.md) pages for a list of known mounts (including non-stock mods).

### Heat Set Inserts

Stock EVA 3 uses M3 x 4.6mm OD x 4mm L heat set inserts. E34M1 maintains consistency with ZeroG and uses [:material-cart: **M3 x 5mm OD x 4mm L inserts**][bom_inserts] (often called "Voron inserts"). Double-check which insert you should be using for third-party components to avoid damaging or ruining a printed part.

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

Files for these parts can be found in the [Bottom Horns Modules](../modules/bottom.md) page.

| Duct Type             | Standard Hotends | Volcano/UHF Hotends  |
|-----------------------|:----------------:|:--------------------:|
| Dual Horns            | :white_check_mark: | *See note*         |
| Dual Horns for Klicky | :white_check_mark: | *See note*         |
| Dual Horns for Beacon | :white_check_mark: | :white_check_mark: |
| Trihorns              | :white_check_mark: | :x:                |
| Trihorns for Klicky   | :white_check_mark: | :x:                |
| Trihorns for Beacon   | :white_check_mark: | :x:                |

!!! note
    EVA 3's dual horn for Volcano hotends contains geometry errors. This limits support for longer hotends at present.

### Cooling Inlets

Stock EVA cooling inlets may be used with E34M1 with an [rear inlet adapter](../modules/rear.md#stock-rear-inlet-adapter).

### Cable Management

There are two methods of cable management and two attachment points. The default attachment is the Top module for umbilical users. PCB mounts supporting both umbilical (cable guide) and drag chain are available.

| Part             | Cable Guide | Drag Chain |
|------------------|:-----------:|:-----------:|
| Top with Endstop | :white_check_mark: | *Planned* |
| PCB Mount        | :white_check_mark: | :white_check_mark: |

Currently only open cable chain hole patterns are supported.