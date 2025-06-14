
import numpy as np
import pandas as pd

def compute_rsi(prices, period=14):
    delta = np.diff(prices)
    gain = np.maximum(delta, 0)
    loss = np.abs(np.minimum(delta, 0))
    avg_gain = pd.Series(gain).rolling(window=period).mean()
    avg_loss = pd.Series(loss).rolling(window=period).mean()
    rs = avg_gain / (avg_loss + 1e-6)
    rsi = 100 - (100 / (1 + rs))
    rsi = rsi.fillna(50)
    return rsi.tolist()[-1]

def compute_ma(prices, period):
    return pd.Series(prices).rolling(window=period).mean().iloc[-1]

def decide_signal(power_price, ttf_price, prices_history):
    support = 90
    resistance = 110
    coal_switching_threshold = 38

    rsi = compute_rsi(prices_history)
    ma200 = compute_ma(prices_history, 200)
    ma50 = compute_ma(prices_history, 50)

    motivazione = []
    score = 0

    if power_price < support:
        score += 1
        motivazione.append("Prezzo power sotto supporto tecnico → rischio rimbalzo")
    if ttf_price > coal_switching_threshold:
        score += 1
        motivazione.append("TTF sopra soglia switching gas-carbone → prezzi power sostenuti")
    if rsi < 35:
        score += 1
        motivazione.append(f"RSI {rsi:.1f} → ipervenduto")
    if power_price < ma200:
        score += 1
        motivazione.append(f"Prezzo < MA200 ({ma200:.1f}) → trend debole")
    if power_price > ma50:
        score -= 1
        motivazione.append(f"Prezzo > MA50 ({ma50:.1f}) → breve termine positivo")

    segnale = "HEDGIARE" if score >= 3 else "NON HEDGIARE"
    return segnale, motivazione, power_price

def generate_real_report():
    report = {}
    history = np.random.normal(loc=95, scale=5, size=200)
    ttf_price = 41.5
    power_prices = {
        "Italia": {"Cal-26": 92, "Q4-25": 98, "Lug-25": 88},
        "Francia": {"Cal-26": 105, "Q4-25": 107, "Lug-25": 101},
        "Germania": {"Cal-26": 100, "Q4-25": 102, "Lug-25": 95}
    }

    for paese in power_prices:
        report[paese] = {}
        for prodotto in power_prices[paese]:
            prezzo = power_prices[paese][prodotto]
            segnale, motivo, price = decide_signal(prezzo, ttf_price, history)
            report[paese][prodotto] = {
                "segnale": segnale,
                "motivazione": " | ".join(motivo),
                "prezzo": round(price, 2)
            }

    return report
