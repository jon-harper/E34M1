---
title: Rear Inlet
summary: Components for the Rear Module
authors: Jon Harper
date: 2023-4-5
prefix: '../'
---

{% import 'format.md' as format with context %}
{% set comp_type='Rear Inlet' -%}
{% set values = product.sortEntries(product.filterComponents(comp_type).values()) -%}

The rear module acts as a part cooling fan inlet.

Several options are available:

- [Single 5015 Fan](#single-5015-fan): Use this if you aren't sure what's best.
- [Single 5015 Fan (Beacon)](#single-5015-fan-beacon): The above, modified for Beacon ABL probes.
- [Single 5015 Fan (EVA-style)](#single-5015-fan-eva-style): Modified stock 5015 inlet with lower height.
- [Single Papst RLF35-8](#single-papst-rlf35-8): Fits a Papst [RLF35-8][bom_papst_rlf35] blower.
- [Single Papst RLF35-8](#single-papst-rlf35-8-beacon): The above, modified for Beacon ABL probes.
- [Dual 5015 Fans](#dual-5015-fan): Redesigned from EVA stock for a lower profile.
- [Dual 5015 Fans (Owl Eyes)](#dual-5015-fan-owl-eyes): Alternative fan layout for smaller footprint.
- [15mm CPAP](#15mm-cpap): For remote cooling.
- [15mm CPAP (Beacon)](#15mm-cpap-beacon): The above, modified for Beacon ABL probes.
- [Stock Rear Inlet Adapter](#eva-rear-inlet-adapter): Lightweight adapter for stock EVA rear inlets.

{% for comp in values -%}
{{ format.comp_entry(comp, prefix) }}
{% endfor -%}