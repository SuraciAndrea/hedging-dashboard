
import pandas as pd
import datetime

def get_latest_pun_price():
    try:
        today = datetime.datetime.now().strftime("%Y%m%d")
        url = f"https://www.mercatoelettrico.org/Download/Dati/202401_PUN_{today}.csv"
        df = pd.read_csv(url, sep=";", decimal=",", encoding="latin1", skiprows=1)
        media = df["Prezzo"].astype(float).mean()
        return f"{media:.2f} €/MWh"
    except Exception as e:
        return f"Errore PUN: {e}"
