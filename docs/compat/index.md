---
title: Overview
summary: Summary of changes and compatibility.
authors: Jon Harper
date: 2023-1-27
---

## Mercury One Compatibility

E34M1 is compatible with Mercury One.1 without limiting the build area; no print area is lost by converting to EVA 3 from a different toolhead. Minor modifications may be necessary to your Z axis (such as adjusting the Z end stop height). See [Other Changes and Additions](#other-changes-and-additions) for examples.

Mercury One.1 with E34M1 has a theoretical build area of 275mm x 275mm using 330mm linear rails. Practical build area is affected by your build, e.g. the type of rear intake used or presence of a toolhead PCB.

!!! note
    E34M1 is *not* compatible with Mercury One Classic.

!!! tip
    Making a mod? Want to see how it looks in CAD? See the [`/CAD`][folder_cad] folder for a `STEP` files.

## Icons and Terminology

These terms and icons are used throughout the site.

- The :material-printer-3d-nozzle: icon is used to emphasize that a part is 3D printed.
- The :material-cart: shopping cart icon is for example links. *There are no affiliate links on this site.*
- Drive: EVA 3 refers to the extruder, stepper, and mount as the *Drive* module.
- FHCS: flat head cap screw (DIN 7991)
- SHCS: socket head scap screw (DIN 912)
- Voron-style inserts: M3 x 5mm OD x 4mm L heat set inserts
- EVA-style inserts: M3 x 4.6mm OD x 4mm L heat set inserts

## Frequent Asked Questions

### How does it fit together?

Visit the [Tour](../tour.md) to get an overview of how the modules are arranged.

### What do I print?

See the Assembly guide's [Print Checklist](../assembly/#print-checklist) to ensure you have everything.

### What does an *italic* BOM entry mean?

These are optional parts that may be included or left out, at your discretion.

## Compatibility Charts

### ABL

The side ABL mount points are different than EVA 3 stock, and not all ABL methods use them. The chart below shows which ABL methods are supported by E34M1.

|          | Standard Hotends   | Volcano/UHF Hotends | Mount Point |
|----------|:------------------:|:------------------:|:-----------:|
| BLTouch  | :white_check_mark: | :white_check_mark: | ABL         |
| CR Touch | :white_check_mark: | :white_check_mark: | ABL         |
| Klicky   | :white_check_mark: | *Planned*          | Bottom      |
| Beacon   | :white_check_mark: | :white_check_mark: | Bottom and Rear     |

Support for 8mm and 12mm inductive probes is not planned but may be added in the future.

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

### Cable Management

There are two methods of cable management and two attachment points. The default attachment is the Top module for umbilical users. PCB mounts supporting both umbilical (cable guide) and drag chain are available.

| Part             | Cable Guide | Drag Chain |
|------------------|:-----------:|:-----------:|
| Top with Endstop | :white_check_mark: | *Planned* |
| PCB Mount        | :white_check_mark: | :white_check_mark: |

Currently only open cable chain hole patterns are supported.
