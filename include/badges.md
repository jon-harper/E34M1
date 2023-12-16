{% macro template(template, prefix='') -%}
{% if template -%}
{{ badge(':material-puzzle:', 'Part template', txt=template) }}
{% endif -%}
{% endmacro -%}

{% macro author(name, url, prefix='') -%}
{{ badge(':octicons-person-fill-24:', 'Contributor', prefix + '/license/#contributing-to-omnibox', name, url) }}
{% endmacro -%}

{% macro hsi() -%}
{{ badge(':material-cog:', 'Uses heat set inserts', None) }}
{% endmacro -%}

{% macro length(txt) -%}
{{ badge(':fontawesome-solid-up-down:', 'Hotend length. This affects bottom ducts and some ABL types.', txt=txt) }}
{% endmacro -%}

{% macro ptfe(value) -%}
{{ badge(':fontawesome-solid-ruler-vertical:', 'PTFE tube length needed for this part', txt=value)}}
{% endmacro -%}

{% macro render(comp, variant, prefix='') -%}
{% set ckeys = comp.attributes.keys() -%}
{% set vkeys = variant.attributes.keys() -%}
{% if variant.author -%}
{{ author(variant.author.name, variant.author.url) }}
{% endif -%}
{% if 'ptfe' in ckeys -%}
{{ ptfe(comp.attributes['ptfe'])}}
{% elif 'ptfe' in vkeys -%}
{{ ptfe(variant.attributes['ptfe'])}}
{% endif -%}
{% if 'length' in ckeys -%}
{{ length(comp.attributes['length'])}}
{% elif 'length' in vkeys -%}
{{ length(variant.attributes['length'])}}
{% endif -%}
{% if 'hsi' in ckeys or 'hsi' in vkeys -%}
{{ hsi() }}
{% endif -%}
{% endmacro -%}