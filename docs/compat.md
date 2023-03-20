---
title: Compatibility
summary: Summary of changes and compatibility.
authors: Jon Harper
date: 2023-1-27
hide: navigation
---



## Mecury One Compatibility

E34M1 is compatible with Mercury One without limitations, i.e. no print area is lost by converting to EVA 3 from a different toolhead.

Minor modifications may be necessary to your Z axis (e.g., adjusting the Z end stop height). See [Other Changes and Additions](#other-changes-and-additions) for examples.

See the [`/CAD`][folder_cad] folder for a sample assembly in `STEP` format.

!!! note
    Mercury One.1 with E34M1 has a theoretical build area of 275mm x 275mm using 330mm linear rails.

## EVA 3 Compatibility

### Linear Rail/Top Piece

E34M1 only supports the MGN12H carriages used with Mercury One.

### Hotends

Not all hotend and ABL combinations are currently available. Check [ABL]

- [x] Standard hotends
- [x] Volcano hotends

### Extruders

All stock extruders are compatible.

!!! note
    Mounting the Drive (extruder and stepper assembly) normally uses seven (7) M3-0.5 x 8mm SHCS. You will need to substitute three (3) of these screws for M3-0.5 x 12mm SHCS.

### Part Fan Inlets

Inlets may be made compatible fairly easily. The inlets included with E34M1 have a lower profile than stock EVA. This allows them to accomodate stepper-mounted breakout boards and should be considered when adapting ducts for E34M1.

- [x] Rear-facing 5015
- [x] Sideways 5015

### Horns/Ducts

Existing duct mods may be made compatible by extending them.

The stock ducts contain geometry errors; the ones to the Volcano horns are beyond my ability to repair.

- [x] Dual horns
- [ ] Volcano horns *(partial compatibility)*

### ABL

!!! note
    The side ABL mount point is different than EVA 3 stock.

|         | Standard Hotends | Volcano Hotends |
|---------|:------------------:|:------------------:|
| BLTouch | :white_check_mark: | :white_check_mark: |
| Klicky  | :white_check_mark: | *(Planned)*        |
| Beacon  | *(Planned)*        | :white_check_mark: |

Support for 8mm and 12mm probes is also planned.

### Front Cooling Fans

No changes; mods are likely compatible.

### Shrouds

All stock shrouds are compatible.

### Cable Management

There are two methods of cable management and two attachment points, depending on your use case. The table below shows how they are compatible.

| Part | Cable Guide | Cable Chain |
|------|:-----------:|:-----------:|
| Top Piece | :white_check_mark: | *Planned* |
| PCB Mount | :white_check_mark: | :white_check_mark: |

Currently only open cable chain hole patterns are supported.

## Other Changes and Additions

- All parts use Mercury One/Voron-style inserts (M3x5x4) instead of the normal EVA inserts.
- The back tensioner and belt catch is removed entirely.
- *New:* A new Z Limit Switch Mount allows the bed on Ender 5 Pros to reach the EVA 3 gantry.
- *New:* A X axis end stop bumper, modified from Mercury One Classic.
- *New:* Mounts are available for both '36- and '42-style toolhead PCBs.
- *New:* Shrouds to cover the PCB and mount wiring are available.
- *New:* There is an adapter that allows the shroud and cooling fan to be attached and removed with two (2) screws instead of four (4).