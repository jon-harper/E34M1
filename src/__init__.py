"""
__init__.py

Initializes the Python environment. Methods tagged as macros can be called from within
Markdown.
"""

import load_yaml
import bom
import badge_gen as badge

from product import Product
def define_env(env):
    """
    Modifies the environment variable with new variables, macros, and filters.
    """
    from os.path import join

    file = env.variables.meta['bom']
    version = env.variables.meta['bom_template_str']
    
    global bom_data 
    bom_data = load_yaml.load_yaml(env.variables, join(env.conf.docs_dir, file))

    global product
    product = Product(components=bom_data.components,
                      parts=bom_data.parts,
                      templates=bom_data.templates[version])

    env.variables['product'] = product

    @env.macro
    def authorForId(auth_id :str ) -> bom.Author:
        return bom_data.authors.get(auth_id)

    @env.macro
    def issue_tag(issue_number : int) -> str:
        """
        Adds a caution annotation for a pending fit test.
        """
        return "!!! caution \"Fit Test Pending: See Issue [#{}](https://github.com/jon-harper/OmniBox/issues/{})\"".format(issue_number, issue_number)

    @env.macro
    def product_button(url : str) -> str:
        """
        Creates a link button
        """
        return "[{}]({})".format(":material-cart: Product Link", url) + "{ .md-button }"

    @env.macro
    def git_button(url : str) -> str:
        """
        Creates a GitHub file link button.
        """
        return '[{}][{}]'.format(":material-git: Files", url) + "{ .md-button }"

    #injects make_badge into the JINJA environment.
    env.macro(badge.make_badge)

    @env.macro
    def make_indented(txt : str, indent='') -> str:
        """
        Splits a block of text by lines and indents by the provided value.
        """
        ret = ''
        if indent != '':
            for line in txt.splitlines(keepends=True):
                ret += indent + line
        return ret

    def render_badges(comp : bom.Component, variant : bom.Variant, prefix='') -> str:
        """
        Generates badge HTML for a given component and variant.
        """
        ret : str = badge.template_badge(comp.template)
        ckeys = comp.attributes.keys()
        vkeys = variant.attributes.keys()
        if variant.author:
            ret += badge.author_badge(variant.author.name, variant.author.url)
        if 'half' in ckeys:
            ret += badge.half_badge(comp.attributes['half'])
        elif 'half' in vkeys:
            ret += badge.half_badge(variant.attributes['half'])
        if 'length' in ckeys:
            ret += badge.size_badge(comp.attributes['length'])
        elif 'length' in vkeys:
            ret += badge.size_badge(variant.attributes['length'])
        if 'base_depth' in ckeys:
            ret += badge.base_depth_badge(comp.attributes['base_depth'])
        elif 'base_depth' in vkeys:
            ret += badge.base_depth_badge(variant.attributes['base_depth'])
        if 'switch' in ckeys:
            ret += badge.switch_badge(comp.attributes['switch'])
        elif 'switch' in vkeys:
            ret += badge.switch_badge(variant.attributes['switch'])
        if 'display_type' in ckeys:
            ret += badge.display_badge(comp.attributes['display_type'])
        elif 'display_type' in vkeys:
            ret += badge.display_badge(variant.attributes['display_type'])
        if 'count' in ckeys:
            ret += badge.qty_badge(comp.attributes['count'])
        elif 'count' in vkeys:
            ret += badge.qty_badge(variant.attributes['count'])
        if 'mounts' in ckeys:
            ret += badge.extension_badge(comp.attributes['mounts'])
        elif 'mounts' in vkeys:
            ret += badge.extension_badge(variant.attributes['mounts'])
        if 'vent' in ckeys or 'vent' in vkeys:
            ret += badge.vent_badge()
        if 'fan' in ckeys or 'fan' in vkeys:
            ret += badge.fan_badge()
        if 'hsi' in ckeys or 'hsi' in vkeys:
            ret += badge.hsi_badge()
        return ret
    
    @env.macro
    def materialsFromYamlComponentList(raw : list[dict]) -> bom.MaterialsData:
        """
        Takes a simple YAML dictionary object, `raw` in the form:
          - comp_name: 0
          - comp2_name: 1
          - [...]
        where the key is a string (the component key) and the value 
        is an int (the index of the variant's definition, zero-based).

        The return value is a compiled MaterialsData.
        """
        
        components : list[bom.ComponentId] = []
        for line in raw:
            for key, value in line.items():
                components.append(bom.ComponentId(name=key, variant=value))
        return product.joinMaterials(components)
    
    @env.macro
    def splitPrintedMaterials(materials : bom.MaterialsData, 
                              printed_str : str = 'Printed') -> tuple[bom.MaterialsData, bom.MaterialsData]:
        """
        Splits a MaterialsData object into two lists of unprinted parts and printed parts, using
        `printed_str` as a key against the `Part.part_type` field.
        """
        printed : bom.MaterialsData = {}
        normal : bom.MaterialsData = {}
        for part_id, qty in materials.items():
            part = product.partFromId(part_id)
            if not part:
                continue
            elif part.part_type == printed_str:
                printed[part_id] = qty
            else:
                normal[part_id] = qty
        return (normal, printed)