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

    env.macro(badge.make_badge)

    @env.macro
    def make_indented(txt : str, indent='') -> str:
        ret = ''
        for line in txt.splitlines(keepends=True):
            ret += indent + line
        return ret