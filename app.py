
import streamlit as st
from report_generator import generate_real_report
from ttf_scraper import get_ttf_prices
from power_scraper import get_power_prices
from investpy_chart import get_investpy_chart
import os

st.set_page_config(page_title="Hedging Dashboard", layout="wide")
st.title("📊 Dashboard Hedging Energia - investpy")

if st.button("🔁 Genera Report"):
    with st.spinner("Analisi in corso..."):
        report = generate_real_report()
        ttf_data = get_ttf_prices()
        power_data = get_power_prices()

        st.success("Report generato con dati reali")

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

                # Prova generazione grafico da investpy
                product_name = "Electricity"
                country = paese
                chart_path = get_investpy_chart(product_name=product_name, country=country)
                if chart_path and os.path.exists(chart_path):
                    col.image(chart_path, caption=f"{product_name} {paese}")
                else:
                    col.warning(f"Nessun grafico disponibile per {paese}")
