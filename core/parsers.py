# parsers.py
# Parsing di PDB, MOL, SDF, FASTA, SEQ per costruire i modelli molecolari

from .molecule_model import Protein, Ligand, NucleicAcid, Complex
from .detectors import detect_molecule_type

def parse_pdb(pdb_block: str):
    """
    Analizza un PDB e restituisce un oggetto:
    - Protein
    - Ligand
    - NucleicAcid
    - Complex
    """

    mol_type = detect_molecule_type(pdb_block)

    if mol_type == "protein":
        return Protein(name="Protein", pdb_block=pdb_block)

    if mol_type == "ligand":
        return Ligand(name="Ligand", pdb_block=pdb_block)

    if mol_type == "dna":
        return NucleicAcid(name="DNA", pdb_block=pdb_block, na_type="dna")

    if mol_type == "rna":
        return NucleicAcid(name="RNA", pdb_block=pdb_block, na_type="rna")

    if mol_type == "complex":
        # Per ora ritorniamo un oggetto Complex semplice
        return Complex(pdb_block=pdb_block)

    return None


def parse_fasta(sequence: str):
    """
    Riconosce se la sequenza è proteica o nucleotidica.
    """

    seq = sequence.replace("\n", "").replace(" ", "").upper()

    dna_chars = set("ATGC")
    rna_chars = set("AUGC")
    protein_chars = set("ACDEFGHIKLMNPQRSTVWY")

    if set(seq).issubset(dna_chars):
        return NucleicAcid(name="DNA Sequence", sequence=seq, na_type="dna")

    if set(seq).issubset(rna_chars):
        return NucleicAcid(name="RNA Sequence", sequence=seq, na_type="rna")

    if set(seq).issubset(protein_chars):
        return Protein(name="Protein Sequence", pdb_block="", metadata={"sequence": seq})

    return None


def parse_molblock(molblock: str):
    """
    Per ora ritorna un Ligand semplice.
    In futuro: estrarre formula, peso molecolare, ecc.
    """
    return Ligand(name="Ligand", pdb_block=molblock)


def parse_sdf(sdf_block: str):
    """
    Per ora trattiamo SDF come MOL.
    """
    return parse_molblock(sdf_block)
