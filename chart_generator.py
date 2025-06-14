
import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_price_chart(market: str, product: str):
    file_path = f"prices/{market.lower()}_{product.lower().replace('-', '').replace(' ', '')}.csv"
    if not os.path.exists(file_path):
        return None

    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"])
    df["MA50"] = df["Price"].rolling(window=5).mean()

    plt.figure(figsize=(10, 4))
    plt.plot(df["Date"], df["Price"], label="Prezzo")
    plt.plot(df["Date"], df["MA50"], label="Media Mobile", linestyle="--")
    plt.title(f"Andamento Storico - {market} {product}")
    plt.xlabel("Data")
    plt.ylabel("€/MWh")
    plt.legend()
    plt.tight_layout()

    os.makedirs("charts", exist_ok=True)
    chart_path = f"charts/chart_{market.lower()}_{product.lower().replace('-', '').replace(' ', '')}.png"
    plt.savefig(chart_path)
    plt.close()

    return chart_path
