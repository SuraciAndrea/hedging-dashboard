
import requests

def get_openmeteo_forecast(city="Milan"):
    url = f"https://api.open-meteo.com/v1/forecast?latitude=45.46&longitude=9.19&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        tmin = data["daily"]["temperature_2m_min"][0]
        tmax = data["daily"]["temperature_2m_max"][0]
        return f"{city}: {tmin}°C - {tmax}°C"
    else:
        return "Errore meteo"
