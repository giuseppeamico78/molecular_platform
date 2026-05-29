# tools_viewer.py
# Funzioni di supporto per il viewer (non JS, ma lato Python)

def get_view_style(mol_type: str):
    """
    Ritorna uno stile suggerito per il viewer in base al tipo:
    protein, ligand, dna, rna, complex.
    """
    styles = {
        "protein": "cartoon",
        "ligand": "ball+stick",
        "dna": "cartoon",
        "rna": "cartoon",
        "complex": "cartoon+ligand_ball+stick"
    }
    return styles.get(mol_type, "cartoon")
