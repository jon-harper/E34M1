---
title: Getting Started
summary: Introduction to E34M1 and this documentation
authors: Jon Harper
date: 2023-1-27
---

{% import 'badges.md' as badges with context %}

This page covers general topics about E34M1 and this documentation site.

!!! note
    E34M1 is *not* compatible with Mercury One Classic.

!!! tip
    Making a mod? Want to see how it looks in CAD? See the [`/CAD`][folder_cad] folder for a `STEP` files.

## Reading the Documentation

We use icons to condense and abbreviate these docs; these conventions are explained below.

### Icons and Terminology

| Icon/Term | Explanation |
|---|---|
| :material-printer-3d-nozzle: | Emphasizes that a part is 3D printed. |
| :material-cart: | Used for example links. *There are no affiliate links on this site.* |
| Drive module | Refers to the extruder, stepper, and mount for both. |
| FHCS | Flat head cap screw (DIN 7991) |
| SHCS | Socket head scap screw (DIN 912) |
| Voron inserts | M3 x 5mm OD x 4mm L heat set inserts, used by Mercury One.1 and E34M1. |
| EVA-style inserts | M3 x 4.6mm OD x 4mm L heat set inserts, mostly used by EVA and RatRig. |

### Tips

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

### ABL Offsets

{{ badges.x_offset(8) }}{{ badges.y_offset(-15) }}

These badges are references for setting your ABL-to-nozzle offset in firmware. No badge
represents an offset of 0.

## Compatibility 

### Mercury One.1

E34M1 is compatible with Mercury One.1; in most configurations, no print area is lost by converting to EVA 3 from a different toolhead. In some configurations, adjustments are necessary to the Z axis (see the [Mercury One.1 Build Manual](https://docs.zerog.one/manual/build/mercury_eva/build_instruction) for details).

The chart below demonstrates build area for different Mercury One.1 builds.

| Base Printer/Rails | X Axis   | Y Axis |
|---|---|---|
| Ender 5 Pro, 330mm rails | >= 265mm | >= 250mm |
| Ender 5 Plus | > 370mm | > 377mm |

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

Most hotends are paired with Standard-length horns; longer hotends require the UHF bottom horns. The Mosquito has the Trihorns as a cooling workaround. Which see the [Hotend Modules](modules/hotend.md) for which bottom horns work with your hotend.

More about Bottom Horns can be found on the [Bottom Horns Modules](modules/bottom.md) page.

### Cable Management

There are two methods of cable management. The default attachment is the [Top](modules/top.md) module for umbilical users. Third parties offer PCB mounts supporting both umbilical (cable guide) and drag chains.

## Frequently Asked Questions

### How does this fit together?

Visit the [Tour](tour.md) to get an overview of how the modules are arranged. The [Assembly Guide](assembly/index.md) includes videos to assist during your build process.

### Is E34M1 supported by ZeroG or EVA?

No, this is a third-party project by [jonspaceharper](https://jon-harper.github.io) with community additions.

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