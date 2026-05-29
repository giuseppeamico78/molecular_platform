from fastapi import APIRouter
from molecular_platform.data_sources.uniprot_client import fetch_uniprot_fasta

router = APIRouter()

@router.get("/load")
def load_uniprot(id: str):
    fasta = fetch_uniprot_fasta(id)
    return {"type": "fasta", "content": fasta}
