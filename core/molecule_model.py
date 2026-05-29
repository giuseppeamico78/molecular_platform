# molecule_model.py
# Modelli dati per rappresentare proteine, ligandi, acidi nucleici e complessi

class BaseMolecule:
    """Classe base per tutte le molecole."""
    def __init__(self, name="", pdb_block="", metadata=None):
        self.name = name
        self.pdb_block = pdb_block
        self.metadata = metadata or {}

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name}>"


class Protein(BaseMolecule):
    """Proteina: contiene catene, residui, domini, ligandi associati."""
    def __init__(self, name="", pdb_block="", chains=None, residues=None, ligands=None, metadata=None):
        super().__init__(name, pdb_block, metadata)
        self.chains = chains or []
        self.residues = residues or []
        self.ligands = ligands or []
        self.type = "protein"


class Ligand(BaseMolecule):
    """Piccola molecola: ligando, farmaco, metabolita."""
    def __init__(self, name="", pdb_block="", formula="", molecular_weight=None, metadata=None):
        super().__init__(name, pdb_block, metadata)
        self.formula = formula
        self.molecular_weight = molecular_weight
        self.type = "ligand"


class NucleicAcid(BaseMolecule):
    """DNA o RNA."""
    def __init__(self, name="", pdb_block="", sequence="", na_type="dna", metadata=None):
        super().__init__(name, pdb_block, metadata)
        self.sequence = sequence
        self.na_type = na_type  # "dna" o "rna"
        self.type = na_type


class Complex(BaseMolecule):
    """Complesso proteina-ligando."""
    def __init__(self, protein=None, ligand=None, pdb_block="", metadata=None):
        super().__init__(name="Protein-Ligand Complex", pdb_block=pdb_block, metadata=metadata)
        self.protein = protein
        self.ligand = ligand
        self.type = "complex"
