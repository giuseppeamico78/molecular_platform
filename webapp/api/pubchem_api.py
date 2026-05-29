from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/compound")
def pubchem_compound(cid: str):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/{cid}/SDF"
    sdf = requests.get(url).text
    return {"type": "sdf", "content": sdf}
