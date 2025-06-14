
import streamlit as st
from report_generator import generate_real_report
from ttf_scraper import get_ttf_prices
from power_scraper import get_power_prices
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def generate_dummy_chart():
    x = pd.date_range("2025-01-01", periods=60)
    y = np.random.normal(loc=95, scale=5, size=60)

    plt.figure(figsize=(10, 4))
    plt.plot(x, y, label="Prezzo Cal-26")
    plt.axhline(y=100, color='red', linestyle='--', label='Resistenza')
    plt.axhline(y=90, color='green', linestyle='--', label='Supporto')
    plt.title("Italia Cal-26 - Prezzo Simulato")
    plt.legend()
    plt.tight_layout()

    chart_path = "charts/chart_italia_cal26.png"
    os.makedirs("charts", exist_ok=True)
    plt.savefig(chart_path)
    plt.close()
    return chart_path

st.set_page_config(page_title="Hedging Dashboard", layout="wide")
st.title("📊 Dashboard Hedging Energia")

if st.button("🔁 Genera Report"):
    with st.spinner("Analisi in corso..."):
        report = generate_real_report()
        chart_path = generate_dummy_chart()
        ttf_data = get_ttf_prices()
        power_data = get_power_prices()

        st.success("Report generato con logica reale")

        st.subheader("💨 Prezzi TTF (Investing.com)")
        for k, v in ttf_data.items():
            st.write(f"{k}: {v}")

        st.subheader("⚡ Prezzi Energia (Investing.com)")
        for k, v in power_data.items():
            st.write(f"{k}: {v}")

        for paese in ["Italia", "Francia", "Germania"]:
            st.subheader(f"📍 {paese}")
            col1, col2, col3 = st.columns(3)
            for i, prodotto in enumerate(report[paese]):
                col = [col1, col2, col3][i]
                segnale = report[paese][prodotto]["segnale"]
                motivo = report[paese][prodotto]["motivazione"]
                colore = "🟢" if segnale == "HEDGIARE" else "🔴"
                col.metric(prodotto, f"{colore} {segnale}", motivo)

        st.image(chart_path, caption="Grafico tecnico simulato")
