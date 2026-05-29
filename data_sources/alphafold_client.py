import requests

def fetch_alphafold_pdb(uniprot_id: str):
    # Nuovo endpoint ufficiale AlphaFold
    api_url = f"https://alphafold.ebi.ac.uk/api/prediction/{uniprot_id}"

    try:
        r = requests.get(api_url)
        if r.status_code != 200:
            print("AlphaFold API error:", r.status_code)
            return None

        data = r.json()

        if not data:
            print("AlphaFold returned empty JSON")
            return None

        # Il JSON contiene il link al file PDB
        pdb_url = data[0].get("pdbUrl")
        if not pdb_url:
            print("No pdbUrl found in AlphaFold response")
            return None

        # Scarichiamo il file PDB
        pdb_response = requests.get(pdb_url)
        if pdb_response.status_code == 200:
            return pdb_response.text

        print("PDB download failed:", pdb_response.status_code)
        return None

    except Exception as e:
        print("Exception:", e)
        return None
