
import streamlit as st
from report_generator import generate_real_report
from ttf_scraper import get_ttf_prices
from power_scraper import get_power_prices
from real_chart import generate_real_chart
from gie_api import get_gie_storage_level
from gme_reader import get_latest_pun_price
from meteo_api import get_openmeteo_forecast
import os

st.set_page_config(page_title="Hedging Dashboard", layout="wide")
st.title("📊 Dashboard Hedging Energia")

if st.button("🔁 Genera Report"):
    with st.spinner("Analisi in corso..."):
        report = generate_real_report()
        ttf_data = get_ttf_prices()
        power_data = get_power_prices()

        st.success("Report generato con logica reale")

        st.subheader("💨 Prezzi TTF (Investing.com)")
        for k, v in ttf_data.items():
            st.write(f"{k}: {v}")

        st.subheader("⚡ Prezzi Energia (Investing.com)")
        for k, v in power_data.items():
            st.write(f"{k}: {v}")

        st.subheader("📦 Storage Gas UE")
        st.write(get_gie_storage_level())

        st.subheader("⚡ Prezzo medio PUN Italia")
        st.write(get_latest_pun_price())

        st.subheader("🌡️ Meteo Milano (oggi)")
        st.write(get_openmeteo_forecast())

        for paese in ["Italia", "Francia", "Germania"]:
            st.subheader(f"📍 {paese}")
            col1, col2, col3 = st.columns(3)
            for i, prodotto in enumerate(report[paese]):
                col = [col1, col2, col3][i]
                segnale = report[paese][prodotto]["segnale"]
                motivo = report[paese][prodotto]["motivazione"]
                colore = "🟢" if segnale == "HEDGIARE" else "🔴"
                col.metric(prodotto, f"{colore} {segnale}", motivo)

                chart_path = generate_real_chart(f"{paese} {prodotto}")
                if chart_path and os.path.exists(chart_path):
                    col.image(chart_path, caption=f"{paese} {prodotto} - Storico")
