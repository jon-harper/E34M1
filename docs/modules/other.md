---
title: Optional/Build-Specific
summary: Parts for E34M1 not part of other modules.
authors: Jon Harper
date: 2023-4-5
---

These are miscellaneous parts that may be useful in some builds.

## Additional Mods

### Klicky Docks

These are related mods not linked elsewhere that may be useful for your build.

| Mod Name | Author | Purpose |
|----------|--------|---------|
| [Klicky Probe Dock for Mercury 1 Zero G](https://www.printables.com/model/386819-klicky-probe-dock-for-mercury-1-zero-g) | [Sir_Wash](https://www.printables.com/social/415185-sir_wash) | Adds a dock for Klicky; works with `klicky_bottom.stl`. |
| [Ender 5/Mercury One Klicky Probe Dock](https://www.printables.com/model/595738-ender-5mercury-one-klicky-probe-dock) | [jonspaceharper](https://www.printables.com/@jonspaceharper) | Uses M3 instead of M5 screws and provides enough adjustment for regular and UHF hotends. |

### Filament Sensors

Multi-material printing often requires a filament sensor at the toolhead. There are several third-party mods for this; note that these do not function as runout sensors (they are after the extruder).

- [Inductive Sensor](https://www.printables.com/model/239026-eva-3-toolhead-sensor) by [Dutchwoody](https://www.printables.com/@Dutchwoody)
- [Microswitch and Ball Bearing](https://www.printables.com/model/442650-eva-3-toolhead-sensor-mechanical-and-reliable) by [Guy](https://www.printables.com/@Guy_258839)
- [Microswitch and Ball Bearing](https://www.printables.com/model/1170113-eva-30-d2hw-filament-sensor-module/comments) by [cuiviemen](https://www.printables.com/@cuiviemen_127292)

### Z Endstop Mount

This part is necessary for Ender 5 Pros with stock (non-Hydra) Z kinematics. This part mounts the limit switch higher than normal.

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

| Parts     | Qty |
|-----------|-----|
| [:material-printer-3d-nozzle: `z_limit_switch_cover.stl`][z_limit_cover] | 1 |
| [:material-printer-3d-nozzle: `z_limit_switch_mount.stl`][z_limit_mount] | 1 |
| Stock Creality Endstop | 1 |
| Screw, M3-0.5 x 16mm | 2 |
| Screw, M5-0.8 x 8mm  | 1 |
| Tee Nut, Drop In, M5 | 1 |
| Heat Set Insert, M3x5x4 | 2 |

</div>
<div markdown class="jh-grid-img">
![z_endstop_illustration](../img/components/z_limit_switch.webp){ width=256px }

??? info "Heat Set Insert Locations"
    ![z_endstop_illustration](../img/inserts/z_mount.webp){ width=256px }
</div>
</div>
