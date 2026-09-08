# Zeigt alle Aktien mit Kursen im Depot an
def zeigt_depot(depot):
    for aktie, kurs in depot.items():
        print(f"{aktie}: {kurs} $")

# Fügt eine Aktie plus Kurs dem Depot hinzu
def aktie_hinzufuegen(depot, name, kurs):
    depot[name] = kurs

# Gibt die Summe aller Kurse im Depot zurück
def gesamtwert(depot):
    return sum(depot.values())

# Gibt den Namen der teuersten Aktie zurück
def teuerste_aktie(depot):
    hoechster = 0
    name = ""
    for aktie, kurs in depot.items():
        if kurs > hoechster:
            hoechster = kurs
            name = aktie
    return name

# Löscht eine Aktie aus dem Depot (prüft erst, ob sie existiert)
def aktie_loeschen(depot, name):
    if name in depot:
        del depot[name]
    else:
        print("Die Aktie ist nicht im Depot")

# Legt das Depot an und startet das Menü
mein_depot = {"NVDA": 120, "ASML": 900, "TSMC": 45}
while True:
    print("1 = Depot anzeigen")
    print("2 = Gesamtwert")
    print("3 = Teuerste Aktie")
    print("4 = Aktie hinzufügen")
    print("5 = Aktie löschen")
    print("6 = Beenden")
    wahl = input("Deine Wahl: ")
    if wahl == "1":
        zeigt_depot(mein_depot)
    elif wahl == "2":
        print(gesamtwert(mein_depot))
    elif wahl == "3":
        print(teuerste_aktie(mein_depot))
    elif wahl == "4":
        name = input("Aktienname: ")
        kurs = float(input("Kurs: "))
        aktie_hinzufuegen(mein_depot, name, kurs)
    elif wahl == "5":
        name = input("Welche Aktie löschen? ")
        aktie_loeschen(mein_depot, name)
    elif wahl == "6":
        break