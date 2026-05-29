import requests

def fetch_pdbe(pdb_id: str):
    url = f"https://www.ebi.ac.uk/pdbe/api/pdb/entry/files/{pdb_id.lower()}"
    r = requests.get(url)

    if r.status_code != 200:
        return None

    return r.json()
