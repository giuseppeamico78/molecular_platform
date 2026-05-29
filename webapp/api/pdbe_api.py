from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/load")
def load_pdbe(id: str):
    url = f"https://www.ebi.ac.uk/pdbe/api/pdb/entry/files/{id.lower()}"
    r = requests.get(url)
    return r.json()
