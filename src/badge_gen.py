# badge_gen.py

# Utility methods
def __text_gen(txt : str, txt_url : str = None) -> str:
    if txt_url:
        return '<a href="{txt_url}" class="jh-text-badge" markdown>{txt}</a>'.format(
            txt_url=txt_url, txt=txt)
    else:
        return '<span class="jh-text-badge" markdown>{txt}</span>'.format(txt=txt)
    

def __icon_gen(icon: str, tooltip: str, url: str = None) -> str:
    if url:
        return '<a href="{url}" title="{tooltip}" class="jh-icon-badge" markdown>{icon}</a>'.format(
            icon=icon, url=url, tooltip=tooltip)
    else:
        return '<span title="{tooltip}" class="jh-icon-badge" markdown>{icon}</span>'.format(
            icon=icon, tooltip=tooltip)

def badge(icon: str,
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
    
def template_badge(template: str, prefix='') -> str:
        if not template:
            return ''
        return badge(':material-puzzle:', 'Part template', prefix + 'upgrade/templates', template)

def author_badge(name: str, url: str, prefix='') -> str:
    return badge(':octicons-person-fill-24:', 'Contributor', prefix + '/license/#contributing-to-omnibox', 
                 name, url)

def hsi_badge() -> str:
    return badge(':material-cog:', 'Uses heat set inserts', None)

def qty_badge(txt, indent : str ='') -> str:
    return badge(':material-chip:', 'Number of parts mounted per tray',
                icon_url=None, txt=txt)

def size_badge(txt : str) -> str:
    return badge(':material-relative-scale:', 'Printed component size',
                 icon_url=None, txt=txt.capitalize())

def base_depth_badge(txt: str) -> str:
    return badge(':material-format-vertical-align-bottom:', 'Required Base depth', 
                 'https://TODO', txt)

def switch_badge(txt: str, prefix : str = '') -> str:
    return badge(':material-power:', 'Power switch options with this PSU',
                 prefix + 'TODO', txt)

def no_iec_badge() -> str:
    return badge(':material-power-plug-off-outline:', 'This component does not provide an IEC power socket.')

def display_badge(txt : str) -> str:
    return badge(':material-monitor:', 'Display type (CPU or MCU)',
                 'https://TODO', txt)

def front_badge() -> str:
    return badge(':material-format-horizontal-align-left:', 'This is the front half of a larger component', 
                 txt='Front')

def rear_badge() -> str:
    return badge(':material-format-horizontal-align-right:', 'This is the rear half of a larger component',
                 txt='Rear')

def unified_badge() -> str:
    return badge(':material-vector-combine:', 'Unified parts replace front and rear halves',
                 txt='Unified')

def half_badge(txt : str) -> str:
    up = txt.upper()
    if up == 'FRONT':
        return front_badge()
    elif up == 'REAR':
        return rear_badge()
    elif up == 'UNIFIED':
        return unified_badge()

def vent_badge() -> str:
    return badge(':material-air-filter:', 'Provides ventilation')

def fan_badge() -> str:
    return badge(':material-fan:', 'Mounts at least one fan')

def extension_badge(txt : str, prefix : str='') -> str:
    return badge(':material-connection:', 'Panel mounts provided', 
                 prefix + 'TODO', txt=txt)

