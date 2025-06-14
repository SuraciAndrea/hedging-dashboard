
import requests

def get_gie_storage_level():
    url = "https://agsi.gie.eu/api?country=EU&gas_day_start=latest&format=json"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        try:
            level = data["data"][0]["full"]
            return f"{level:.2f}%"
        except:
            return "Dati non disponibili"
    else:
        return "Errore nella richiesta GIE"
