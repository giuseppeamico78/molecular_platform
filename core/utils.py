# utils.py
# Funzioni di utilità generali per parsing e analisi strutturale

def clean_pdb(pdb_block: str):
    """
    Rimuove righe vuote, spazi inutili e normalizza il testo.
    """
    if not pdb_block:
        return ""
    lines = pdb_block.splitlines()
    cleaned = [line.rstrip() for line in lines if line.strip()]
    return "\n"+ "\n".join(cleaned) + "\n"


def extract_chains(pdb_block: str):
    """
    Estrae le catene presenti nel PDB.
    """
    chains = set()
    for line in pdb_block.splitlines():
        if line.startswith(("ATOM", "HETATM")):
            chain = line[21].strip()
            if chain:
                chains.add(chain)
    return sorted(list(chains))


def extract_residues(pdb_block: str):
    """
    Estrae i residui unici (resn, resi, chain).
    """
    residues = set()
    for line in pdb_block.splitlines():
        if line.startswith("ATOM"):
            resn = line[17:20].strip()
            resi = line[22:26].strip()
            chain = line[21].strip()
            residues.add((resn, resi, chain))
    return sorted(list(residues), key=lambda x: (x[2], int(x[1])))


def extract_ligands(pdb_block: str):
    """
    Estrae ligandi (HETATM esclusa acqua).
    """
    ligands = set()
    for line in pdb_block.splitlines():
        if line.startswith("HETATM"):
            resn = line[17:20].strip()
            if resn not in ["HOH", "WAT"]:
                ligands.add(resn)
    return sorted(list(ligands))


def is_small_molecule(pdb_block: str):
    """
    Ritorna True se il PDB contiene solo HETATM (no ATOM).
    """
    has_atom = False
    has_het = False

    for line in pdb_block.splitlines():
        if line.startswith("ATOM"):
            has_atom = True
        if line.startswith("HETATM"):
            resn = line[17:20].strip()
            if resn not in ["HOH", "WAT"]:
                has_het = True

    return (not has_atom) and has_het
