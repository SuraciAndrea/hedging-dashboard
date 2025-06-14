
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
    spread = power_price - ttf_price

    motivazione = []
    score = 0

    if power_price < support:
        score += 1
        motivazione.append("Prezzo sotto supporto tecnico")
    if ttf_price > coal_switching_threshold:
        score += 1
        motivazione.append("TTF sopra soglia switching gas-carbone")
    if rsi < 35:
        score += 1
        motivazione.append(f"RSI basso ({rsi:.1f}) → ipervenduto")
    if power_price < ma200:
        score += 1
        motivazione.append(f"Prezzo < MA200 ({ma200:.1f}) → trend debole")
    if power_price > ma50:
        score -= 1
        motivazione.append(f"Prezzo > MA50 ({ma50:.1f}) → segnale breve positivo")
    if spread < 50:
        score += 1
        motivazione.append(f"Spread Power-TTF basso ({spread:.1f}) → rischio salita power")

    segnale = "HEDGIARE" if score >= 3 else "NON HEDGIARE"
    return segnale, motivazione, power_price

def generate_real_report():
    report = {}
    history = np.random.normal(loc=95, scale=5, size=200)
    prezzi = {
        "Italia": {"Cal-26": 111.88, "Q4-25": 119.30, "Lug-25": 125.35},
        "Francia": {"Cal-26": 102.15, "Q4-25": 108.40, "Lug-25": 113.25},
        "Germania": {"Cal-26": 98.90, "Q4-25": 105.60, "Lug-25": 109.75},
        "TTF": {"Front-Month": 38.25, "Cal-26": 41.10}
    }

    ttf_price = prezzi["TTF"]["Cal-26"]

    for paese in ["Italia", "Francia", "Germania"]:
        report[paese] = {}
        for prodotto in prezzi[paese]:
            prezzo = prezzi[paese][prodotto]
            segnale, motivo, prezzo_corrente = decide_signal(prezzo, ttf_price, history)
            report[paese][prodotto] = {
                "segnale": segnale,
                "motivazione": " | ".join(motivo),
                "prezzo": round(prezzo_corrente, 2)
            }

    return report
