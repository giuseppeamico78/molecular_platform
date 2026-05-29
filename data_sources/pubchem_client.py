import requests

def fetch_sdf(cid: str):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/{cid}/SDF"
    r = requests.get(url)

    if r.status_code != 200:
        return None

    return r.text

def fetch_properties(cid: str):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/{cid}/property/MolecularWeight,IsomericSMILES/JSON"
    r = requests.get(url)

    if r.status_code != 200:
        return None

    return r.json()
