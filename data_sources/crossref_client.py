import requests

def crossref_article(doi: str):
    """
    Recupera metadati articolo da CrossRef.
    Funziona per QUALSIASI DOI.
    """
    url = f"https://api.crossref.org/works/{doi}"

    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return None

        data = r.json()

        if "message" not in data:
            return None

        msg = data["message"]

        return {
            "title": msg.get("title", [""])[0],
            "authors": [
                f"{a.get('given', '')} {a.get('family', '')}".strip()
                for a in msg.get("author", [])
            ] if "author" in msg else [],
            "journal": msg.get("container-title", [""])[0],
            "published": msg.get("published-print", msg.get("published-online", {})),
            "doi": msg.get("DOI", doi),
            "abstract": msg.get("abstract", None)
        }

    except Exception as e:
        print("CrossRef error:", e)
        return None
