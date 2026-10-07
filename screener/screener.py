# Aktien-Screener
# Prueft eine Watchlist gegen eine selbst definierte Kaufregel.

def kaufwuerdig(kurs, ziel):
    return kurs < ziel

watchlist = [
    {"name": "NVDA", "kurs": 120, "ziel": 100},
    {"name": "ASML", "kurs": 900, "ziel": 950},
    {"name": "SAP",  "kurs": 200, "ziel": 250},
]

zahler = 0                               # Zaehler VOR der Schleife
print("Treffer:")
for aktie in watchlist:
    if kaufwuerdig(aktie["kurs"], aktie["ziel"]):
        print(f"  {aktie['name']}: {aktie['kurs']} (Ziel {aktie['ziel']})")
        zahler = zahler + 1

print(f"{zahler} von {len(watchlist)} Titeln erfuellen die Regel.")