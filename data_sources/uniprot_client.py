import requests

def fetch_uniprot_fasta(uniprot_id: str):
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
    r = requests.get(url)

    if r.status_code != 200:
        return None

    return r.text
