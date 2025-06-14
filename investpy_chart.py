
import investpy
import matplotlib.pyplot as plt
import pandas as pd
import os

def get_investpy_chart(product_name="Electricity", country="Italy", from_date="01/01/2024", to_date="13/06/2025"):
    try:
        df = investpy.get_commodity_historical_data(
            commodity=product_name,
            from_date=from_date,
            to_date=to_date,
            interval='Daily'
        )

        df = df.reset_index()
        df.columns = [col.capitalize() for col in df.columns]

        plt.figure(figsize=(10, 4))
        plt.plot(df["Date"], df["Close"], label=f"{product_name} ({country})")
        plt.axhline(y=df["Close"].mean(), color='orange', linestyle='--', label='Media')
        plt.title(f"Andamento storico - {product_name} ({country})")
        plt.xlabel("Data")
        plt.ylabel("Prezzo (€)")
        plt.legend()
        plt.tight_layout()

        os.makedirs("charts", exist_ok=True)
        path = f"charts/chart_{product_name.lower()}_{country.lower()}.png"
        plt.savefig(path)
        plt.close()
        return path

    except Exception as e:
        print("Errore investpy:", e)
        return None
