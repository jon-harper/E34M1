"""
load_yaml.py

Loads a YAML bill of materials, parses it, and injects
the result into the provided environment variable.
"""

import bom

def load_yaml(env_variables, filepath : str) -> bom.GlobalData:
    """
    Imports YAML data, parses it, and injects the result into a provided (global) object.
    """

    import yaml

    f = open(filepath, 'r')
    raw_bom = yaml.safe_load(f.read())
    
    parser = BOMParser(raw_bom)
    env_variables['base_url'] = parser.base_url

    return bom.GlobalData(components=parser.components, 
                          parts=parser.parts, 
                          authors=parser.authors, 
                          suppliers=parser.suppliers,
                          assembly_types=parser.assembly_types,
                          templates=parser.templates)
    

class BOMParser():
    
    def __init__(self, yaml_data : dict) -> None:
        """
        Parses through raw YAML and builds BOM data structures from it.

        All other methods are internal.
        """

        config = yaml_data['config']
        self.base_url = config['baseUrl']

        self.suppliers = bom.SupplierData()
        if 'suppliers' in yaml_data:
            for key, entry in yaml_data['suppliers'].items():
                self.suppliers[key] = self.parseSupplier(entry)
        
        self.authors = bom.AuthorData()
        if 'authors' in yaml_data:
            for key, entry in yaml_data['authors'].items():
                self.authors[key] = self.parseAuthor(entry)

        # fail if no parts are provided
        assert('parts' in yaml_data)
        self.parts = bom.PartData()
        self.part_types : list[str] = []
        for part_type, entry in yaml_data['parts'].items():
            if part_type not in self.part_types:
                self.part_types.append(part_type)
            for part_id, part_entry in entry.items():
                part = self.parsePart(part_entry, part_type)
                self.parts[part_id] = part

        # parts parsed, build subassemblies
        self.subassemblies = yaml_data.get('subassemblies', None)

        # build components from subassemblies and parts
        self.components = self.parseComponents(yaml_data['components'])

        self.templates = yaml_data['templates']
        

    def parseSupplier(self, entry : dict) -> bom.Supplier:
        """
        Returns a newly-constructed Supplier from a YAML entry.
        """
        return bom.Supplier(
            name=entry['name'], 
            region=entry.get('region', 'n/a'), 
            ships=entry.get('ships', 'n/a'),
            icon=entry.get('icon', ''),
            note=entry.get('note', ''))

    def parsePart(self, entry : dict, part_type : str) -> bom.Part:
        """
        Returns a newly-constructed Part from a YAML entry. Relative URLs are converted to absolute by prepending the base_url value.

        parseSources() is called on each source to replace supplier ids with Suppliers.
        """
        author_id = entry.get('author', None)
        if author_id:
            author = self.authors[author_id]
        else:
            author = None
        fi : str = entry.get('file', None)
        if fi and not fi.startswith('https://'): #rough, but everything is https (for now)
            fi = self.base_url + fi
        return bom.Part(name=entry['name'],
                       units=entry.get('units', 'Ea'),
                       part_type=part_type,
                       icon=entry.get('icon', None),
                       file_url=fi,
                       template=entry.get('template', None),
                       author=author,
                       note=entry.get('note', None),
                       sources=self.parseSources(entry.get('sources', None)),
                       img_url=entry.get('img', None))
    
    def parseSources(self, entry : dict) -> bom.SourceList:
        """
        Builds a list of Sources, substituting the actual Source for its identifier.
        """
        ret = bom.SourceList()

        if not entry:
            return ret
        
        for supplier_id, source_data in entry.items():
            source = bom.SourceUrl(self.suppliers[supplier_id],
                                   url = source_data['url'],
                                   note=source_data.get('note', ''))
            ret.append(source)
        return ret
    
    def parseAuthor(self, entry: dict) -> bom.Author:
        """
        Constructs an Author from YAML data.
        """
        return bom.Author(name=entry['name'], 
                          url=entry['url'],
                          note=entry.get('note', ''))
    
    def breakSubassembly(self, parts: bom.MaterialsData) -> bom.MaterialsData:
        """
        Given a MaterialsData object, breaks down any subassemblies into their constituent Parts/qty pairs 
        and returns the merged results.
        """
        ret : bom.MaterialsData = {}
        if not parts:
            return ret
        for part_id, qty in parts.items():
            if part_id in self.subassemblies.keys():
                mult : int = round(qty)
                for sub_id, sub_qty in self.subassemblies[part_id].items():
                    if sub_id in ret:
                        ret[sub_id] += mult * sub_qty
                    else:
                        ret[sub_id] = mult * sub_qty
            elif part_id in ret:
                ret[part_id] += qty
            else:
                ret[part_id] = qty
        return ret
    
    def parseComponents(self, raw_entries : dict[str, dict]) -> bom.ComponentData:
        """
        Constructs components from raw entries. Any subassemblies found are broken down and merged.
        Parts listed with the component are merged into each variant's unique part list.
        """
        ret : bom.ComponentData = {}
        
        self.assembly_types = raw_entries.keys()
        for comp_type, comp_entries in raw_entries.items():
            # Process the entries and flag any that refer to subassemblies
            for comp_id, comp_data in comp_entries.items():
                comp = bom.Component(name=comp_data['name'],
                                     template=comp_data.get('template', ''),
                                     comp_type=comp_type,
                                     attributes=comp_data.get('attributes', {}),
                                     variants=[],
                                     note=comp_data.get('note', None),
                                     img_url=comp_data.get('img', None))
                # get the parts common to all variants and break up any subassemblies
                comp_parts = self.breakSubassembly(comp_data.get('parts', bom.MaterialsData()))
                
                # process the variants
                for v_name, v_data in comp_data['variants'].items():
                    v_parts = self.breakSubassembly(v_data['parts'])
                    # add in the common parts
                    for part_id, qty in comp_parts.items():
                        if part_id in v_parts.keys():
                            v_parts[part_id] += qty
                        else:
                            v_parts[part_id] = qty
                    author_id = v_data.get('author', None)
                    variant = bom.Variant(name=v_name,
                                          attributes=v_data.get('attributes', {}),
                                          parts=v_parts,
                                          author=self.authors.get(author_id, None),
                                          note=v_data.get('note', ''),
                                          img_url=v_data.get('img', None))
                    comp.variants.append(variant)
                #add the component to the list
                ret[comp_id] = comp
        return ret