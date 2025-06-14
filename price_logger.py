
import pandas as pd
import os
from datetime import datetime

def log_price(market: str, product: str, price: float):
    os.makedirs("prices", exist_ok=True)
    file_path = f"prices/{market.lower()}_{product.lower().replace('-', '').replace(' ', '')}.csv"

    date = datetime.now().strftime("%Y-%m-%d")
    new_entry = pd.DataFrame([[date, price]], columns=["Date", "Price"])

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        if date not in df["Date"].values:
            df = pd.concat([df, new_entry], ignore_index=True)
            df.to_csv(file_path, index=False)
    else:
        new_entry.to_csv(file_path, index=False)

    return file_path
