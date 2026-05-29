import requests

def fetch_swissmodel(uniprot_id: str):
    url = f"https://swissmodel.expasy.org/repository/uniprot/{uniprot_id}.json"

    try:
        r = requests.get(url)
        if r.status_code != 200:
            print("SwissModel API error:", r.status_code)
            return None

        data = r.json()

        if "result" not in data:
            print("SwissModel returned no result")
            return None

        return data["result"]

    except Exception as e:
        print("Exception:", e)
        return None
