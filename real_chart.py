
import pandas as pd
import matplotlib.pyplot as plt
import os
import requests
from bs4 import BeautifulSoup

def get_price_table():
    url = "https://www.investing.com/commodities/electricity-historical-data"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    tables = pd.read_html(r.text)
    for table in tables:
        if "Date" in table.columns and "Price" in table.columns:
            df = table.copy()
            df["Date"] = pd.to_datetime(df["Date"])
            df["Price"] = df["Price"].astype(str).str.replace(",", "").astype(float)
            df.sort_values("Date", inplace=True)
            return df
    return None

def generate_real_chart(product_name):
    df = get_price_table()
    if df is None:
        return None

    plt.figure(figsize=(10, 4))
    plt.plot(df["Date"], df["Price"], label=product_name)
    plt.axhline(y=100, color="red", linestyle="--", label="Resistenza")
    plt.axhline(y=90, color="green", linestyle="--", label="Supporto")
    plt.title(f"Prezzo Storico - {product_name}")
    plt.legend()
    plt.tight_layout()

    os.makedirs("charts", exist_ok=True)
    path = f"charts/chart_{product_name.replace(' ', '_').lower()}.png"
    plt.savefig(path)
    plt.close()
    return path
