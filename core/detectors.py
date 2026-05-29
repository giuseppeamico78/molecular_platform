# detectors.py
# Riconoscimento tipo molecola: proteina, ligando, DNA, RNA, complesso

import re

def detect_molecule_type(pdb_block: str):
    """
    Analizza un PDB e determina se è:
    - protein
    - ligand
    - dna
    - rna
    - complex (protein + ligand)
    """

    if pdb_block is None or len(pdb_block.strip()) < 20:
        return "unknown"

    lines = pdb_block.splitlines()

    has_protein = False
    has_ligand = False
    has_dna = False
    has_rna = False

    for line in lines:
        if line.startswith("ATOM"):
            resn = line[17:20].strip()

            # Proteine: 20 amminoacidi standard
            if resn in ["ALA","VAL","LEU","ILE","MET","PHE","TRP","PRO",
                        "SER","THR","TYR","CYS","ASN","GLN","LYS","ARG",
                        "HIS","ASP","GLU","GLY"]:
                has_protein = True

            # DNA
            if resn in ["DA","DT","DG","DC"]:
                has_dna = True

            # RNA
            if resn in ["A","U","G","C"]:
                has_rna = True

        if line.startswith("HETATM"):
            resn = line[17:20].strip()

            # Escludiamo acqua
            if resn not in ["HOH","WAT"]:
                has_ligand = True

    # Logica decisionale
    if has_protein and has_ligand:
        return "complex"

    if has_protein:
        return "protein"

    if has_dna:
        return "dna"

    if has_rna:
        return "rna"

    if has_ligand:
        return "ligand"

    return "unknown"
