from fastapi import APIRouter
from data_sources.alphafold_client import fetch_alphafold_pdb

router = APIRouter()

@router.get("/load")
def load_alphafold(id: str):
    """
    Carica il modello AlphaFold dato un UniProt ID.
    Esempio: P38398, Q9Y2Z4, P0DTC2, ecc.
    """
    pdb_content = fetch_alphafold_pdb(id)
    return {
        "type": "pdb",
        "content": pdb_content
    }
