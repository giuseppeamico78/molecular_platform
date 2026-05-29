# tools_analysis.py
# Analisi semplice di molecole

from ..core.utils import extract_chains, extract_ligands

def describe_molecule(mol_obj):
    """
    Ritorna una descrizione testuale semplice dell'oggetto molecolare.
    """
    desc = []

    desc.append(f"Tipo: {getattr(mol_obj, 'type', 'unknown')}")
    desc.append(f"Nome: {mol_obj.name}")

    if mol_obj.pdb_block:
        chains = extract_chains(mol_obj.pdb_block)
        ligs = extract_ligands(mol_obj.pdb_block)
        if chains:
            desc.append(f"Catene: {', '.join(chains)}")
        if ligs:
            desc.append(f"Ligandi: {', '.join(ligs)}")

    if isinstance(getattr(mol_obj, 'metadata', {}), dict) and mol_obj.metadata.get("sequence"):
        desc.append(f"Lunghezza sequenza: {len(mol_obj.metadata['sequence'])} aa/nt")

    return "\n".join(desc)
