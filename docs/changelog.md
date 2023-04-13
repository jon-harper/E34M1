---
title: Changelog
summary: Materials for each E34M1 part
authors: Jon Harper
date: 2023-1-26
---

## April 2023

### 23/04/13

- Began altering hotends and drives for Voron inserts.
- Lots of minor doc edits.
- Created the `testing` branch for parts not yet ready.

### 23/04/12

- Added E3D V6 and Revo V6 to the hotends page.
- Lots of minor edits.
- Reformatted the modules pages, added a description.

### 23/04/11

- Optimized the design of the sideways inlet.
- Worked with cuiviemen on an improved Beacon inlet and bottom.

### 23/04/09

- Finished assembly docs.
- Added notes to several modules.
- Updated git license to reflect EVA 3 license (CC BY-NC-SA 4.0).
- Downconverted video and delayed download.

### 23/04/08 

- Added assembly docs outline.

### 23/04/07

- Added license and credits.
- Added images to hotends and extruders pages.
- More formatting to the landing page.

### 23/04/06

- Updated graphics and added missing graphics.
- Finished inlining BOM and insert data.
- Added accreditation to parts that are mods (mostly bottom horns)
- Updated landing page.
- Expanded compatibility page with known hotends and drives.

### 23/04/05

- Visual refresh:
    - BOM and heat set insert pages are combined into a Modules category.
    - TOC is integrated into the left along with each section.
- Updated docs with Trihorn and Klicky Trihorn.
- Updated doc links.
- Renamed a number of files.

### 23/04/04

- Added Trihorn and Klicky Trihorn
- Began prepping STLs and CAD to move to the E34M1 repo.

## March 2023

### 23/03/30

- Added CR Touch and CR Touch Volcano entries.
- Cleaned up some wording in the docs.

### 23/03/28

- Cut down significantly on duplicate documentation.

### 23/03/27

- Added the Tour page.
- Significant rework of other sections began.

### 23/03/24

- Added several mods.
- Slightly clarified the compatibility page about PCB mounts.

### 23/03/23

- All PCB mounts: strengthened middle criss-cross for less flex.
- All PCB mounts: added 1mm clearance between PCB and screws behind.
- `pcb36_mount_cable_chain.stl`, `pcb42_mount_cable_chain.stl`: Moved mount for chain further to the edge.

### 23/03/20

- `pcb36_mount_cable_chain.stl`, `pcb42_mount_cable_chain.stl`: New PCB mounts that support 10x11 open cable chain.
- Lots of documentation edits and updates.

### 23/03/18

- `pcb_shroud_30mm_fan.stl`: added a new shroud that mounts a 30mm fan for CANBUS users.

### 23/03/11

- `top_endstop_mgn12h.stl` & `top_endstop_mgn12h_pcb.stl`: moved modifications from `/testing` folder.

### 23/03/10

- `belt_grabber.stl` Smaller to match changes to the front piece.
- `front_universal_fi.stl`, `front_universal_pis_fi.stl`: Narrowed belt loops and inserts for mounting belt catches.
- The above have been fit tested and aare committed.
- `top_endstop_mgn12h.stl`: significantly strengthented the cable guide mount.
- `top_endstop_mgn12h_pcb.stl`: cosmetic modifications.

## February 2023

### 23/02/01

- `bottom_horns_klicky_fi.stl`: Modified Klicky horns (still in testing!)
- `5015_sideways_inlet.stl`: Thickened hex grill; it broke off on the build plate. >:(
- Merged contents of `EVA3` branch into `main`. This should help avoid confusion to newcomers to the repo.
- Added EVA34M1 on Printables.
- `bl_touch_volcano_mount.stl`: New ABL mount for Volcano hotends.

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
