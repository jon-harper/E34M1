"""
product.py

Filtering, sorting, and versioning for BOM data.
"""

import bom

class Product:
    """
    Manages a set of loaded part and component data. Incompatible parts are filtered out.
    """
    local_url_prefix: str
    components : bom.ComponentData
    parts : bom.PartData
    part_types: list[str]
    assembly_types: list[str]

    def __init__(self, 
                 components : bom.ComponentData, 
                 parts: bom.PartData,
                 templates: bom.TemplateList, 
                 prefix : str = '',
                 filter_unused_parts : bool = False):
        """
        Constructs a new Product and filters the provided data.
        """
        self.local_url_prefix = prefix
        self.components = {}
        if filter_unused_parts:
            self.parts = bom.PartData()
        else:
            self.parts = parts
        self.part_types = []
        self.assembly_types = []

        for comp_id, comp in components.items():
            if not comp.template or comp.template in templates:
                self.components[comp_id] = comp
                if comp.comp_type not in self.assembly_types:
                    self.assembly_types.append(comp.comp_type)
            if filter_unused_parts:
                for v in comp.variants:
                    for part_id in v.parts.keys():
                        if part_id not in self.parts.keys():
                            self.parts[part_id] = parts[part_id]

        for part in parts.values():
            if part.part_type not in self.part_types:
                self.part_types.append(part.part_type)

    def filterComponents(self, type_filter : str = '', attribute_filter: str = '', attribute_value: str = '') -> bom.ComponentData:
        """
        Returns a dict of all assemblies whose types match `type_filter` and/or
        whose attributes match `attribute_filter`.

        Attributes can be further constrained by filtering the value with `attribute_value`.
        """
        ret = bom.ComponentData()
        if type_filter and type_filter not in self.assembly_types:
            return ret

        for comp_id, comp in self.components.items():
            if type_filter and type_filter == comp.comp_type:
                if comp.attributes and attribute_filter in comp.attributes.keys():
                    if not attribute_value or attribute_value == comp.attributes[attribute_filter]:
                        ret[comp_id] = comp
                ret[comp_id] = comp
            elif comp.attributes and attribute_filter in comp.attributes.keys():
                if not attribute_value or attribute_value == comp.attributes[attribute_filter]:
                    ret[comp_id] = comp
        return ret

    def partFromId(self, part_id : str) -> bom.Part:
        """
        Retrieves a bom.Part from the loaded parts for a given part_id.
        """
        return self.parts.get(part_id)
    
    def filterParts(self, part_type: str) -> bom.PartData:
        """
        Filters the loaded parts by type and returns the results as bom.PartData.
        """
        if part_type not in self.part_types:
            return {}
        ret : bom.PartData = {}
        for part_id, part in self.parts.items():
            if part.part_type == part_type:
                ret[part_id] = part
        return ret
    
    def has_hsi(self, v : bom.Variant) -> bool:
        """
        Returns True if a part has the HSI flag set.
        """
        if 'hsi' in v.attributes.keys():
            return True
        return False

    def sortEntries(self, values : any) -> any:
        """
        Sorts an iterable object by its 'name' field. Used for bom.PartData and bom.ComponentData.
        """
        return sorted(values, key=lambda v : v.name)
    
    def sortKeyEntries(self, values : list[tuple]) -> list[tuple]:
        """
        Sorts a key, value pair (tuple) by the value's name field.
        """
        return sorted(values, key=lambda v: v[1].name)
    
    def componentFromId(self, comp_id) -> bom.Component:
        """
        Find the matching component for a given ID.
        """
        return self.components.get(comp_id)
    
    def joinMaterials(self, comp_ids : list[bom.ComponentId]) -> bom.MaterialsData:
        """
        Takes a list of ComponentIds and returns a MaterialsData instance
        with the resulting, combined BOM.
        """
        ret = bom.MaterialsData()
        for comp_id in comp_ids:
            comp = self.componentFromId(comp_id.name)
            if not comp:
                continue
            for part_id, qty in comp.variants[comp_id.variant].parts.items():
                if part_id in ret:
                    ret[part_id] += qty
                else:
                    ret[part_id] = qty
        return ret