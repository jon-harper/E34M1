"""
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

    @env.macro
    def part_link(part_id : str, part : bom.Part = None, prefix : str = '',
                  url_text=None) -> str:
        if not part:
            part = product.partFromId(part_id=part_id)
        if not url_text:
            url_text = part.name
        ret : str = '[{} {}]({} "{}")'
        if part.part_type == 'Printed' and part.file_url:
            if part.file_url.startswith(product.local_url_prefix):
                return ret.format(':material-git:', url_text, part.file_url, "OmniBox GitHub file download")
            else:
                return ret.format(':octicons-link-external-24:', url_text, part.file_url, 'External site file download')
        elif part.sources:
            return ret.format(':material-cart:', url_text, prefix + 'sourcing/#' + part_id, "Sourcing information")
        else:
            return url_text

    env.macro(badge.badge)

    @env.macro
    def render_badges(comp : bom.Component, variant : bom.Variant, prefix='') -> str:
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