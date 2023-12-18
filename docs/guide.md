---
title: Intro Guide
summary: Summary of changes and compatibility.
authors: Jon Harper
date: 2023-1-27
---

{% import 'badges.md' as badges with context %}

## Mercury One Compatibility

E34M1 is compatible with Mercury One.1 without limiting the build area; no print area is lost with stock beds by converting to EVA 3 from a different toolhead. In some configurations, minor adjustments to the Z axis are needed.

An Ender 5 Pro rebuilt as a Mercury One.1 with 330mm rails:

- Has a theoretical build area of 275mm x 275mm;
- Can expect at least 265mm of X axis travel;
- Can expect at least 250mm of Y axis travel (available Y axis depends on the rear intake).

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

## Frequently Asked Questions

### How does this fit together?

Visit the [Tour](tour.md) to get an overview of how the modules are arranged. The [Assembly Guide](assembly/index.md) includes videos to assist during your build process.

### Is E34M1 supported by ZeroG or EVA?

No, this is a third-party project started by [jonspaceharper](https://jon-harper.github.io).

### What do I print?

See the Assembly guide's [Print Checklist](assembly/index.md#print-checklist) to ensure you have everything.

### What print settings should I use?

E34M1 follows the [ZeroG Print Settings](https://docs.zerog.one/standard/print/settings) guidelines.

All STL files are exported in print orientation.

### How are Voron-style and EVA-style inserts different?

Voron-style inserts are slightly thicker than EVA inserts. Mercury One relies on Voron-style inserts exclusively,
so all E34M1 components use them, as well. Third-party and stock EVA components use EVA-style inserts instead.

Does it matter? Yes: the adjustments we made for the larger, Voron-style inserts make insertion easier and parts
fit together better. Users report that it is generally still possible to use Voron-style inserts with parts made
for thinner inserts, but post-processing is needed.

## Tips

The [Modules](modules/index.md) section contains entries for every component and variant in E34M1. These
are labeled with *badges*, like so:

{{ badges.author('jonspaceharper', 'https://jon-harper.github.io') }}{{ badges.hsi() }}

These badges are meant to speed up reading through many entries at once. 

Tap or hover over the icon for an explanation of what each badges means. Some badges use text to provide
additional information, such as an contributor's name and profile link.

### PTFE Values

{{ badges.ptfe(22.5) }}

Hotends and drives (extruders) have a PTFE length value, indicated with a badge
like the one above. Add the two values to determine how much PTFE tubing you need between your hotend
and extruder.

## Compatibility Charts

{{ badges.length('Standard') }}

A few components are only compatible in specific combinations. This generally relates to whether a part is for a standard-length or UHF-length hotend.

The Hotend Length badge identifies if a component or variant is affected by hotend length.

### ABL

The chart below shows which ABL methods are supported by E34M1. Note that the side ABL mount is than EVA 3 stock and that not all ABL methods use them.

|            | Standard Hotends   | UHF Hotends        | Mount Point |
|------------|:------------------:|:------------------:|:-----------:|
| 8mm Probes | :white_check_mark: | :white_check_mark: | ABL         |
| 12mm Probes | :x:               | :x:                | ABL         |
| Beacon     | :white_check_mark: | :white_check_mark: | Bottom/Rear |
| BL-Touch   | :white_check_mark: | :white_check_mark: | ABL         |
| CR-Touch   | :white_check_mark: | :white_check_mark: | ABL         |
| Klicky     | :white_check_mark: | :white_check_mark: | Bottom      |
| Klicky PCB | :x:                | :x:                | ABL         |

### Bottom Horns

Most hotends are paired with Standard-length horns. Very long hotends, such as the Rapido UHF, require the UHF bottom horns. The Mosquito has the Trihorns as a cooling workaround.

More about Bottom Horns can be found on the [Bottom Horns Modules](modules/bottom.md) page.

| Hotend                | Bottom Horns  |
|-----------------------|:-------------:|
| 3D Passion Nova       | Dual, Kraken  |
| E3D Revo Voron        | Dual, Kraken  |
| Phaetus Dragonfly BMO | Dual, Kraken  |
| Phaetus Dragonfly BMS | Dual, Kraken  |
| Phaetus Dragon BMO    | Dual, Kraken  |
| Phaetus Dragon UHF    | Dual, Kraken  |
| Phaetus Rapido        | Dual, Kraken  |
| Phaetus Rapido UHF    | UHF, Kraken UHF |
| Slice Engineering Mosquito | Trihorn |

### Cable Management

There are two methods of cable management. The default attachment is the [Top](modules/top.md) module for umbilical users. Third parties offer PCB mounts supporting both umbilical (cable guide) and drag chains.