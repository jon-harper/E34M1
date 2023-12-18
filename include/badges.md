{%- macro template(template, prefix='') -%}
{%- if template -%}
{{ make_badge(':material-puzzle:', 'Part template', txt=template) }}
{%- endif -%}
{%- endmacro -%}

{%- macro author(name, url, prefix='') -%}
{{ make_badge(':octicons-person-fill-24:', 'Contributed by', '', name, url) }}
{%- endmacro -%}

{%- macro hsi() -%}
{{ make_badge(':material-cog:', 'Uses heat set inserts', None) }}
{%- endmacro -%}

{%- macro length(txt) -%}
{{ make_badge(':fontawesome-solid-up-down:', 'Hotend length. This affects bottom ducts and some ABL types.', txt=txt) }}
{%- endmacro -%}

{%- macro ptfe(value) -%}
{{ make_badge(':fontawesome-solid-ruler-vertical:', 'PTFE tube length needed for this part', txt=value) }}
{%- endmacro -%}

{%- macro origin(txt, txt_url) -%}
{{ make_badge(':material-source-branch:', 'Based on work by', txt=txt, txt_url=txt_url) }}
{%- endmacro -%}

{%- macro version(txt) -%}
{{ make_badge(':material-tag:', 'Version', txt=txt) }}
{%- endmacro -%}

{%- macro render(comp, variant, prefix='') -%}
{%- set ckeys = comp.attributes.keys() -%}
{%- set vkeys = variant.attributes.keys() -%}
{%- if variant.author -%}
{{ author(variant.author.name, variant.author.url, prefix) }}
{%- endif -%}
{%- if 'origin' in ckeys -%}
{%- set o_auth = authorForId(comp.attributes['origin']) -%}
{%- elif 'origin' in vkeys -%}
{%- set o_auth = authorForId(variant.attributes['origin']) -%}
{%- endif -%}
{%- if o_auth -%}
{{ origin(o_auth.name, o_auth.url) }}
{%- endif -%}
{%- if 'version' in ckeys -%}
{{ version(comp.attributes['version']) }}
{%- elif 'version' in vkeys -%}
{{ version(variant.attributes['version']) }}
{%- endif -%}
{%- if 'ptfe' in ckeys -%}
{{ ptfe(comp.attributes['ptfe']) }}
{%- elif 'ptfe' in vkeys -%}
{{ ptfe(variant.attributes['ptfe']) }}
{%- endif -%}
{%- if 'length' in ckeys -%}
{{ length(comp.attributes['length']) }}
{%- elif 'length' in vkeys -%}
{{ length(variant.attributes['length']) }}
{%- endif -%}
{%- if 'hsi' in ckeys or 'hsi' in vkeys -%}
{{ hsi() }}
{%- endif -%}
{%- endmacro -%}
