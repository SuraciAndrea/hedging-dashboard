
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def generate_fake_report():
    today = datetime.now().strftime("%d %B %Y")

    report = {
        "data": today,
        "Italia": {
            "Cal-26": "HEDGIARE",
            "Q4-25": "NON HEDGIARE",
            "Lug-25": "HEDGIARE"
        },
        "Francia": {
            "Cal-26": "NON HEDGIARE",
            "Q4-25": "HEDGIARE",
            "Lug-25": "NON HEDGIARE"
        },
        "Germania": {
            "Cal-26": "HEDGIARE",
            "Q4-25": "HEDGIARE",
            "Lug-25": "HEDGIARE"
        }
    }

    return report

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
    plt.savefig(os.path.join(base_path, chart_path))
    plt.close()
    return chart_path
