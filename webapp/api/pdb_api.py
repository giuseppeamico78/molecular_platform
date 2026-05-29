from fastapi import APIRouter
from molecular_platform.data_sources.pdb_client import fetch_pdb

router = APIRouter()

@router.get("/load")
def load_pdb(id: str):
    content = fetch_pdb(id)
    return {"type": "pdb", "content": content}
