"""
bom.py

Data types for BOM data.
"""

from dataclasses import dataclass
from typing import Optional, NamedTuple

class Supplier(NamedTuple):
    """
    Defines a provider of Parts.
    """
    name: str   # Provider name
    region: str # Region(s) shipping FROM
    ships: str  # Region(s) shipping TO
    icon: str   # Optional icon
    note: str   # Optional note

SupplierData = dict[str, Supplier]

class SourceUrl(NamedTuple):
    """
    Supplier data for a specific Part.
    """
    supplier : Supplier
    url: str            # location
    note: str           # notes about a given supplier's product

SourceList = list[SourceUrl]

class Author(NamedTuple):
    """
    Accreditation information for a printed Part.
    """
    # author_id: str
    name: str   # Author name
    url: str    # Preferred profile URL
    note: str   # Any notes

AuthorData = dict[str, Author]

class Part(NamedTuple):
    """
    Contains relevant information for both printed and sourced parts.
    """
    name: str                   # Formal part name
    units: str                  # unit of measure
    part_type: str              # category, e.g. fastener, MCU, fan
    icon: Optional[str]         # internal; Material icon key
    file_url: Optional[str]     # STL for printable files
    template: Optional[str]     # Release version (for Core files) or template version (for others)
    img_url: Optional[str]      # internal; display image for major parts
    note: Optional[str]         # internal
    sources: Optional[SourceList] # list of part links
    author: Optional[str]       # Contributor for printable files

PartData = dict[str, Part]

# Part id and quantity for return values
MaterialsData = dict[str, float] #part_id, qty

class Variant(NamedTuple):
    """
    Defines a variation of a component. Variants container their own MaterialsData.
    """
    name: str
    attributes : dict[str, str]
    parts : MaterialsData
    author: Author
    note : Optional[str]
    img_url: Optional [str]

class Component(NamedTuple):
    """
    A component contains a group of Variants, typically all based on a common design or design feature (if part of
    a larger set of similar Components based on a template).
    """
    name : str                  # Uniqe, descriptive name
    template : Optional[str]    # Template for printed part interface
    comp_type: str              # Category
    attributes: dict[str, str]  # name, value dict for attributes
    variants : list[Variant]    # List of variants of this component
    note : Optional[str]        # Note common to all variants, optional
    img_url : Optional[str]     # Example image

ComponentData = dict[str, Component]

class ComponentId (NamedTuple):
    """
    Named pair for component IDs.
    """
    name: str
    variant: int

# template version list
TemplateList = list[str]

class GlobalData(NamedTuple):
    """
    Global variable for the part database.
    """
    components : ComponentData
    parts : PartData
    authors : AuthorData
    suppliers : SupplierData
    assembly_types : list[str]
    templates: dict[str, TemplateList]