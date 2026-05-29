import requests
from .crossref_client import crossref_article

API_KEY = ""  # puoi lasciarlo vuoto se non hai API key Elsevier


# ---------------------------------------------------------
# 1) SEARCH — FUNZIONA ANCHE SENZA API KEY
# ---------------------------------------------------------
def sciencedirect_search(query: str):
    url = "https://api.elsevier.com/content/search/sciencedirect"
    params = {
        "query": query,
        "apiKey": API_KEY
    }

    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None


# ---------------------------------------------------------
# 2) ARTICLE — FALLBACK AUTOMATICO A CROSSREF
# ---------------------------------------------------------
def sciencedirect_article(doi: str):
    """
    Recupera articolo da ScienceDirect.
    Se fallisce → fallback CrossRef.
    """

    url = f"https://api.elsevier.com/content/article/doi/{doi}"
    params = {
        "apiKey": API_KEY,
        "view": "FULL"
    }

    try:
        r = requests.get(url, params=params, timeout=10)

        # Se Elsevier risponde con contenuto valido
        if r.status_code == 200:
            data = r.json()
            if "full-text-retrieval-response" in data:
                return data

        # Fallback CrossRef
        return crossref_article(doi)

    except:
        # Fallback CrossRef
        return crossref_article(doi)
