"""
badge_gen.py

Provides 'make_badge' to generate text and icon badges.
"""

# Utility methods
def __text_gen(txt : str, txt_url : str = None) -> str:
    """
    Generate a badge's text block.
    """
    if txt_url:
        return '<a href="{txt_url}" class="jh-text-badge" markdown>{txt}</a>'.format(
            txt_url=txt_url, txt=txt)
    else:
        return '<span class="jh-text-badge" markdown>{txt}</span>'.format(txt=txt)
    

def __icon_gen(icon: str, tooltip: str, url: str = None) -> str:
    """
    Generate a badge's icon block.
    """
    if url:
        return '<a href="{url}" title="{tooltip}" class="jh-icon-badge" markdown>{icon}</a>'.format(
            icon=icon, url=url, tooltip=tooltip)
    else:
        return '<span title="{tooltip}" class="jh-icon-badge" markdown>{icon}</span>'.format(
            icon=icon, tooltip=tooltip)

def make_badge(icon: str,
          tooltip: str,
          icon_url: str = None,
          txt : str = None,
          txt_url : str = None) -> str:
    """
    Creates a badge element from an icon, text, urls, and a tooltip.

    Badges can be used to concisely display information with optional links.
    Badges should always have an icon and tooltip. Text should be kept short,
    preferably one word.
    """
    icon_html = __icon_gen(icon, tooltip, icon_url)
    if txt:
        txt_html = __text_gen(txt, txt_url)
        return '<p class="jh-badge" markdown>{} {}</p>'.format(icon_html, txt_html)
    else:
        return '<p class="jh-badge" markdown>{}</p>'.format(icon_html)

