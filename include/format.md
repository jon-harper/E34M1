{% import 'badges.md'as badges -%}

{% macro part_header(part_id, name) -%}
<a name="{{part_id}}"></a> {{ name }}
{% endmacro -%}

{% macro add_image(obj, width="240px", prefix = '') -%}
{% if obj.img_url -%}
    {% set url = prefix + obj.img_url -%}
[![{{obj.name}}]({{url}}){ width="{{width}}" }]({{url}})
{% endif -%}
{% endmacro -%}

{% macro add_note(comp, indent='') -%}
{% if comp.note -%}
{{ comp.note }}
{% else -%}
{{indent}}*(None)*
{% endif -%}
{% endmacro -%}

{% macro comp_entry(comp, prefix='', img_width="240px") -%}
### {{ comp.name }}

<div markdown class="grid">
<div markdown>
{% if comp.attributes and comp.attributes['fit_test'] -%}

{{issue_tag(comp.attributes['fit_test'])}}
{% endif -%}

:octicons-paperclip-24: **General Notes**

{{ add_note(comp) }}

:octicons-versions-24: **Details**

{% if comp.variants | count > 1 -%}
{%- set indent='    ' -%}
{%- for v in comp.variants -%}
=== "{{ v.name }}"
    {{ badges.render(comp, v, prefix=prefix) }}
{% if v.note -%}
{{ make_indented(add_note(v), indent) }}
{% endif %}

{{ make_indented(bom_table(v, prefix=prefix), indent) }}
{%- endfor -%}
{%- else -%}
{%- set v = comp.variants[0] -%}
{{ badges.render(comp, v, prefix=prefix) }}

{%- if v.note -%}
{{ add_note(v) }}

{%- endif -%}
{{ bom_table(v, prefix=prefix) }}
{% endif -%} {# comp.variants | count > 1 #}
</div>
<div markdown>
{{ add_image(comp, width=img_width, prefix=prefix) }}
</div>
</div>
---------
{% endmacro -%}

{% macro variant_entry(comp, prefix='', img_width="240px") -%}
{% for v in comp.variants -%}

{% if comp.variants | count > 1 -%}
### {{ v.name }}
{% else -%}
### {{ comp.name }}
{% endif -%}

<div markdown class="grid">
<div markdown>
{% if comp.attributes and comp.attributes['fit_test'] -%}

{{issue_tag(comp.attributes['fit_test'])}}
{%- endif -%}
:octicons-paperclip-24: **General Notes**

{% if comp.variants | count > 1 -%}
{{ add_note(v) }}

:octicons-versions-24: **Details**

{{ badges.render(comp, v, prefix=prefix) }}

{{ bom_table(v, prefix=prefix)}}
</div>
<div markdown>

{{ add_image(v, width=img_width, prefix=prefix) }}
{% else -%}
{{ add_note(comp) }}

:octicons-versions-24: **Details**

{{ badges.render(comp, v, prefix=prefix) }}

{{ bom_table(v, prefix=prefix)}}
</div>
<div markdown>

{{ add_image(comp, width=img_width, prefix=prefix) }}
{% endif -%}

</div>
</div>

{% endfor -%}
---------
{% endmacro -%}

{% macro source_table(part) -%}
| Source | Ships To | Ships From | Note |
|--------|----------|------------|------|
{% if part.sources | count == 0 -%}
| | | |
{% else -%}
{% for source in part.sources -%}
| [{{source.supplier.name}}]({{source.url}} "{{source.supplier.name}}: {{part.name}}") | {{ source.supplier.ships }} | {{ source.supplier.region }} | {{ source.note }} |
{% endfor -%}
{% endif -%}
{% endmacro -%}

{% macro bom_table(variant, prefix='') -%}
| Type | Part | Qty |
|------|------|-----|
{% if variant.parts -%}
{% for part_id, qty in variant.parts.items()-%}
{% set part = product.partFromId(part_id) -%}
{% set link = part_link(part_id, part, prefix=prefix) -%}
{% if part.part_type == 'Printed' -%}
|:material-printer-3d-nozzle: {{part.part_type}}|{{link}}|{{qty}} {{part.units}}|
{% else -%}
|{{part.part_type}}|{{link}}|{{qty}} {{part.units}}|
{% endif -%}
{% endfor -%}
{% endif %}
{% endmacro -%}

{# I hate the way this macro is written, but a more concise version has newlines. #}
{% macro part_link(part_id, part = None, prefix = '', url_text=None) -%}
{% if not part -%}
{% set part = product.partFromId(part_id=part_id) -%}
{% endif -%}
{% if not url_text -%}
{% set url_text = part.name -%}
{% endif -%}
{% if not part.file_url and not part.sources -%}
{{url_text}}{% else -%}
{% if part.part_type == 'Printed' and part.file_url -%}
{% if part.file_url.startswith(product.local_url_prefix) -%}
{% set icon = ":material-git:" -%}
{% set url = part.file_url -%}
{% set tooltip = "E34M1 GitHub file download"-%}
{% else -%}
{% set icon = ':octicons-link-external-24:' -%}
{% set url = part.file_url -%}
{% set tooltip = 'External site file download'-%}
{% endif -%}
{% elif part.sources -%}
{% set icon = ':material-cart:' -%}
{% set url = prefix + 'sourcing.md#' + part_id -%}
{% set tooltip =  'Sourcing information' -%}
{% endif -%}
[{{icon}} {{url_text}}]({{url}} "{{tooltip}}"){% endif -%}
{% endmacro -%}