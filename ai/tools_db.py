# tools_db.py
# Wrapper unificato per i database (PDB, PubChem, ChEMBL, AlphaFold)

from ..data_sources.pdb_client import fetch_pdb
from ..data_sources.pubchem_client import fetch_sdf as pubchem_fetch_sdf, fetch_properties as pubchem_props
from ..data_sources.chembl_client import fetch_sdf as chembl_fetch_sdf, fetch_properties as chembl_props
from ..data_sources.alphafold_client import fetch_alphafold_pdb

def fetch_from_source(source: str, identifier: str):
    """
    source: 'pdb', 'pubchem', 'chembl', 'alphafold'
    """
    source = source.lower()

    if source == "pdb":
        return {"type": "pdb", "content": fetch_pdb(identifier)}

    if source == "pubchem":
        return {
            "type": "sdf",
            "content": pubchem_fetch_sdf(identifier),
            "properties": pubchem_props(identifier)
        }

    if source == "chembl":
        return {
            "type": "sdf",
            "content": chembl_fetch_sdf(identifier),
            "properties": chembl_props(identifier)
        }

    if source == "alphafold":
        return {"type": "pdb", "content": fetch_alphafold_pdb(identifier)}

    return None
