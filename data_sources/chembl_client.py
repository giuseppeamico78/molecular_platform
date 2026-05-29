import requests
import xml.etree.ElementTree as ET

def fetch_chembl_molecule(chembl_id: str):
    """
    Client ChEMBL robusto e veloce:
    - timeout breve
    - fallback immediato
    - mai più loading infinito
    """

    # 1) API JSON moderna (veloce)
    json_url = f"https://www.ebi.ac.uk/chembl/api/data/molecule/{chembl_id}.json"

    try:
        r = requests.get(json_url, timeout=5)
        if r.status_code == 200:
            data = r.json()
            if "molecule" in data:
                return data["molecule"]
    except:
        pass

    # 2) Fallback XML (con timeout breve)
    xml_url = f"https://www.ebi.ac.uk/chembl/api/data/molecule/{chembl_id}"

    try:
        r = requests.get(xml_url, timeout=5)
        if r.status_code != 200:
            return {"error": "ChEMBL non ha risposto"}

        root = ET.fromstring(r.text)
        molecule = {child.tag: child.text for child in root}
        return molecule

    except:
        return {"error": "Timeout ChEMBL"}
