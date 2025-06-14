
import streamlit as st
from report_generator import generate_real_report
from ttf_scraper import get_ttf_prices
from power_scraper import get_power_prices
from price_logger import log_price
from chart_generator import generate_price_chart
import os

st.set_page_config(page_title="Hedging Dashboard", layout="wide")
st.title("📊 Dashboard Hedging Energia – Prezzi reali cmdty")

if st.button("🔁 Genera Report"):
    with st.spinner("Analisi in corso..."):
        report = generate_real_report()
        ttf_data = get_ttf_prices()
        power_data = get_power_prices()

        st.success("Report generato con logica reale e prezzi cmdty")

        st.subheader("💨 Prezzi TTF (Investing.com)")
        for k, v in ttf_data.items():
            st.write(f"{k}: {v}")

        st.subheader("⚡ Prezzi Future Energia (ICE cmdty)")
        for paese in power_data:
            st.write(f"📍 {paese}")
            for prodotto, prezzo in power_data[paese].items():
                st.write(f"{prodotto}: {prezzo} €/MWh")

        for paese in ["Italia", "Francia", "Germania"]:
            st.subheader(f"📍 {paese}")
            col1, col2, col3 = st.columns(3)
            for i, prodotto in enumerate(report[paese]):
                col = [col1, col2, col3][i]
                entry = report[paese][prodotto]
                segnale = entry["segnale"]
                motivo = entry["motivazione"]
                prezzo = entry["prezzo"]
                colore = "🟢" if segnale == "HEDGIARE" else "🔴"
                testo = f"{colore} {segnale} a {prezzo} €/MWh"
                col.metric(prodotto, testo, motivo)

                log_price(paese, prodotto, prezzo)
                chart_path = generate_price_chart(paese, prodotto)
                if chart_path and os.path.exists(chart_path):
                    col.image(chart_path, caption=f"{paese} {prodotto} - Andamento storico")
