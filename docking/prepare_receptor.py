# prepare_receptor.py
# Preparazione del recettore per il docking

from ..core.utils import clean_pdb

def remove_water(pdb_block: str):
    """
    Rimuove molecole d'acqua (HOH, WAT) dal PDB.
    """
    lines = pdb_block.splitlines()
    filtered = [
        line for line in lines
        if not (line.startswith("HETATM") and line[17:20].strip() in ["HOH", "WAT"])
    ]
    return "\n".join(filtered) + "\n"


def keep_chain(pdb_block: str, chain_id: str):
    """
    Mantiene solo la catena selezionata.
    """
    lines = pdb_block.splitlines()
    filtered = [
        line for line in lines
        if line.startswith(("ATOM", "HETATM")) and line[21].strip() == chain_id
    ]
    return "\n".join(filtered) + "\n"


def prepare_receptor(pdb_block: str, chain_id: str = None):
    """
    Pipeline base:
    1. pulizia
    2. rimozione acqua
    3. selezione catena (se richiesta)
    """
    pdb_block = clean_pdb(pdb_block)
    pdb_block = remove_water(pdb_block)

    if chain_id:
        pdb_block = keep_chain(pdb_block, chain_id)

    return pdb_block
