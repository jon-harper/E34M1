---
title: Sourcing Guide
summary: List of parts and known sources.
authors: Jon Harper
date: 2023-11-30
prefix: ''
---

Need help sourcing parts?

!!! note
    - This page is not an endorsement for any product or reseller.
    - Not all parts are verified.
    - Amazon and AliExpress links use manufacturer stores, where possible.
    - No affiliate links are included.

{% import 'format.md' as fmt with context %}

{% for part_type in product.part_types | sort -%}

{% if part_type != 'Printed' -%}

### {{ part_type }}

{% for part_id, part in product.sortKeyEntries(product.filterParts(part_type).items()) -%}

#### {{ fmt.part_header(part_id, part.name) }}

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
{% if part.note -%}
!!! note 
    {{ part.note }}

{% endif -%}
{{ fmt.source_table(part) }}
</div>
{% if part.img_url -%}
<div markdown class="jh-grid-img">
[![{{part.name}}]({{prefix + part.img_url}}){ width="240px" }]({{prefix + part.img_url}})
</div>
{% endif -%}
</div>
{% endfor %}

{% endif -%}

{% endfor %}