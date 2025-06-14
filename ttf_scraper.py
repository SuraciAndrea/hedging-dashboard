
import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_ttf_prices():
    url = "https://www.investing.com/commodities/natural-gas-futures"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    tables = pd.read_html(response.text)
    prices = {}

    for table in tables:
        if "Contract" in table.columns and "Last" in table.columns:
            for _, row in table.iterrows():
                contract = row["Contract"]
                last_price = row["Last"]
                prices[contract] = last_price
            break

    return prices
