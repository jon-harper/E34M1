---
title: Changelog
summary: Materials for each E34M1 part
authors: Jon Harper
date: 2023-1-26
hide: navigation
---


## January 2023

### 23/01/26

- Deployed new doc site.
- Updated STEP files.

### 23/01/24

- `front_universal_pis_fi.stl`: Added FYSETC PIS (portable input shaper) support
- `pcb36_mount.stl`, `pcb42_mount.stl`: Added two files for, e.g., EBB36 and EBB42 stepper-mounted PCBS.
- These should support *all* stepper mounted PCBs, not just CANBUS (e.g., BTT Piggyback36).
- `pcb_shroud.stl`, `pcb_shroud_cat.stl` two shrouds to cover up the PCB wiring added (one is whimsical).

### 23/01/23

- Alternate top piece removes the cable support mount entirely now.
- Started work on rear PCB mount with integrated cable support instead.

### 23/01/20

- `bltouch_mount.stl`: Strengthened BLTouch bracket.

### 23/01/19

- Fixed missing screw holes in the alternate top piece.
- Shortened the front intake duct by 1mm.
- Updated all outdated STEP files.

### 23/01/18

- `5015_sidways_inlet_fi.stl`: Added some walls for the 5015 fan to sit in and a notch for the bit around the exhaust.
- Added a Z limit switch mount to raise the limit switch height. Comes with a cover.
- Added a front intake duct that lets you remove the fan with two screws instead of four.
- Note: the intake duct is not compatible with 4020 fans (or you lose Y space).

### 23/01/16

- Belt fit test is good.
- Added a bumper for the X axis limit switch.

### 23/01/13

- Fit test appears ready for testing on a working Merc.
- Added cutout in belt grabber for divider between belts.
- Added a version of the cable guide post with the guide to the side.

### 23/01/12

- Tweaked post again for cable guide.
- Spent most of the day fixing a printer.

### 23/01/11

- Tagged all parts in the Fusion model with part numbers to scrape BOM data.
- Tweaked BLTouch mount to add a little more material.
- Added a readme with BOM info.
- Added a chamfer to the top piece insert holes and an overhang for the endstop mount.
- Test fitting went well:
    - Found & fixed missing BLTouch holes in the front piece.
    - Made cable guide tower thinner to avoid blocking drive piece.
    - Rotated cable guide around to face completely backwards.
- Added CAD files for Volcano duct.
    - The duct source file has broken geometry that I am unable to fix.
    - I have made the changes otherwise needed to make the duct compatible.

### 23/01/10

- Started changelog
- Switched M3 inserts to Mercury One-style to simplify BOM.
    - All parts now use M3x5x4mm inserts.
    - Added Dragon BMO part with resized insert holes.
- Refactored Fusion 360 files;
    - Split out small Core parts into individual files
    - Removed a lot of quick hacks
- Added divider to belt grabber between belts.
- Re-oriented parts to export in the correct orientation for print.
- Endstop is now EVA-style horizontal and mounted on the right.
    - Ditched rear-mounted endstop design.
    - Still need to design a bumper for the endstop.
- Cable guide improvements:
    - Rotated guide mount 45 degrees to stay out of the way of endstop.
    - Closer to rear toolhead and takes less X axis space.
    - Raised cable guide 15mm.
    - Rear of cable guide allows for larger zip ties.
- BLTouch mount:
    - Moved mount points over belt clamp
    - Design a new BLTouch mount
    - Uses a simple cutaway support structure

### 23/01/07

- Started work
