kaufen_zaehler = 0
watchlist = []

for i in range(3):
    name = input("Aktienname: ")
    try:
        kurs = float(input("Aktueller Kurs: "))
        ziel = float(input("Zielkurs: "))
    except ValueError:
        print("Bitte eine Zahl eingeben!")
        continue
    watchlist.append({"name": name, "kurs": kurs, "ziel": ziel})

for aktie in watchlist:
    if aktie["kurs"] < aktie["ziel"]:
        kaufen_zaehler = kaufen_zaehler + 1
        print(f"{aktie['name']}: KAUFEN (unter Ziel)")
    else:
        print(f"{aktie['name']}: warten (ueber Ziel)")

print(f"von {len(watchlist)} sind kaufwuerdig: {kaufen_zaehler}")