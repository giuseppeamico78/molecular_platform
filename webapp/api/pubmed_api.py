from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/search")
def pubmed_search(query: str):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {"db": "pubmed", "term": query, "retmode": "json"}
    r = requests.get(url, params=params)
    return r.json()

@router.get("/fetch")
def pubmed_fetch(pmid: str):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {"db": "pubmed", "id": pmid, "retmode": "xml"}
    r = requests.get(url, params=params)
    return r.text
