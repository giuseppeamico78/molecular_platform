from fastapi import APIRouter
from data_sources.nature_client import nature_search, nature_article

router = APIRouter()

@router.get("/search")
def search_nature(query: str):
    results = nature_search(query)
    return {
        "type": "nature_search",
        "content": results
    }

@router.get("/article")
def get_nature_article(id: str):
    article = nature_article(id)
    return {
        "type": "nature_article",
        "content": article
    }
