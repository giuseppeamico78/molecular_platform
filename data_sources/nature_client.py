import requests

def nature_search(query: str):
    """
    Cerca articoli Nature usando CrossRef.
    Filtra solo quelli del gruppo Nature (prefix 10.1038).
    """
    url = "https://api.crossref.org/works"
    params = {
        "query": query,
        "filter": "prefix:10.1038",  # Nature Publishing Group
        "rows": 20
    }

    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code != 200:
            return None

        data = r.json()
        return data.get("message", {}).get("items", [])

    except:
        return None


def nature_article(doi: str):
    """
    Recupera articolo Nature tramite CrossRef.
    """
    url = f"https://api.crossref.org/works/{doi}"

    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return None
        return r.json().get("message", {})
    except:
        return None
