from fastapi import APIRouter
from data_sources.crossref_client import crossref_article

router = APIRouter()

@router.get("/article")
def get_crossref_article(id: str):
    """
    Recupera metadati articolo tramite DOI usando CrossRef.
    Funziona per QUALSIASI DOI.
    """
    article = crossref_article(id)
    return {
        "type": "crossref_article",
        "content": article
    }
