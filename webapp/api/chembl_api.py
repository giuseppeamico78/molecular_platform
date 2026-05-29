from fastapi import APIRouter
from data_sources.chembl_client import fetch_chembl_molecule

router = APIRouter()

@router.get("/load")
def load_chembl(id: str):
    """
    Carica una molecola ChEMBL dato un ChEMBL ID.
    Esempio: CHEMBL25, CHEMBL1906, CHEMBL203
    """
    molecule = fetch_chembl_molecule(id)
    return {
        "type": "chembl",
        "content": molecule
    }
