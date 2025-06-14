
import streamlit as st
from report_generator import generate_fake_report, generate_dummy_chart
from ttf_scraper import get_ttf_prices

st.set_page_config(page_title="Hedging Dashboard", layout="wide")
st.title("📊 Dashboard Hedging Energia")

if st.button("🔁 Genera Report"):
    with st.spinner("Analisi in corso..."):
        report = generate_fake_report()
        chart_path = generate_dummy_chart()
        ttf_data = get_ttf_prices()

        st.success(f"Report generato per il {report['data']}")

        st.subheader("💨 Prezzi TTF (Investing.com)")
        for k, v in ttf_data.items():
            st.write(f"{k}: {v}")

        for paese in ["Italia", "Francia", "Germania"]:
            st.subheader(f"📍 {paese}")
            col1, col2, col3 = st.columns(3)
            for i, prodotto in enumerate(report[paese]):
                col = [col1, col2, col3][i]
                segnale = report[paese][prodotto]
                colore = "🟢" if segnale == "HEDGIARE" else "🔴"
                col.metric(prodotto, f"{colore} {segnale}")

        st.image("charts/chart_italia_cal26.png", caption="Grafico tecnico simulato")
