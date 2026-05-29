from fastapi import APIRouter
from data_sources.swissmodel_client import fetch_swissmodel

router = APIRouter()

@router.get("/load")
def load_swissmodel(id: str):
    """
    Carica i modelli SwissModel per un UniProt ID.
    """
    models = fetch_swissmodel(id)
    return {
        "type": "swissmodel",
        "content": models
    }
