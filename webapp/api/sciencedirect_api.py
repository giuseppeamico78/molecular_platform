from fastapi import APIRouter
from data_sources.sciencedirect_client import (
    sciencedirect_search,
    sciencedirect_article
)

router = APIRouter()

@router.get("/search")
def search_sciencedirect(query: str):
    """
    Ricerca articoli su ScienceDirect.
    """
    results = sciencedirect_search(query)
    return {
        "type": "sciencedirect_search",
        "content": results
    }

@router.get("/article")
def get_sciencedirect_article(id: str):
    """
    Recupera un articolo tramite DOI.
    Se ScienceDirect non risponde → fallback CrossRef.
    """
    article = sciencedirect_article(id)
    return {
        "type": "sciencedirect_article",
        "content": article
    }
