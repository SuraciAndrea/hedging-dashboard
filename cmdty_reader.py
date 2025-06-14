
import pandas as pd

# Simulazione locale per assenza reale di API cmdty free
# In un contesto reale, qui importeremmo una libreria o caricheremmo da un file CSV aggiornato

def get_cmdty_prices():
    # Dati simulati ma realistici
    return {
        "Italia": {"Cal-26": 111.88, "Q4-25": 119.30, "Lug-25": 125.35},
        "Francia": {"Cal-26": 102.15, "Q4-25": 108.40, "Lug-25": 113.25},
        "Germania": {"Cal-26": 98.90, "Q4-25": 105.60, "Lug-25": 109.75}
    }
