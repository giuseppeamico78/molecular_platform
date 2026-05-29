import requests

def pubmed_search(query: str):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json"
    }
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def pubmed_fetch(pmid: str):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": pmid,
        "retmode": "xml"
    }
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.text
