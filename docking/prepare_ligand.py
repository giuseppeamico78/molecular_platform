# prepare_ligand.py
# Preparazione del ligando per il docking

from ..core.utils import clean_pdb

def clean_ligand_block(block: str):
    """
    Rimuove righe vuote e normalizza il testo del ligando.
    Funziona per PDB, MOL e SDF semplici.
    """
    return clean_pdb(block)


def remove_water_from_ligand(block: str):
    """
    Rimuove eventuali molecole d'acqua dal ligando (raro ma possibile).
    """
    lines = block.splitlines()
    filtered = [
        line for line in lines
        if not (line.startswith("HETATM") and line[17:20].strip() in ["HOH", "WAT"])
    ]
    return "\n".join(filtered) + "\n"


def prepare_ligand(block: str):
    """
    Pipeline base:
    1. pulizia
    2. rimozione acqua
    """
    block = clean_ligand_block(block)
    block = remove_water_from_ligand(block)

    return block
