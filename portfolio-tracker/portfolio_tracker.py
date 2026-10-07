# Portfolio-Tracker
# Verwaltet ein Aktiendepot. Daten werden in mein_depot.txt gespeichert
# und beim naechsten Start automatisch geladen.

def zeigt_depot(depot):
    for aktie, kurs in depot.items():
        print(f"{aktie}: {kurs} $")

def aktie_hinzufuegen(depot, name, kurs):
    depot[name] = kurs

def gesamtwert(depot):
    return sum(depot.values())

def teuerste_aktie(depot):
    hoechster = 0
    name = ""
    for aktie, kurs in depot.items():
        if kurs > hoechster:
            hoechster = kurs
            name = aktie
    return name

def aktie_loeschen(depot, name):
    if name in depot:
        del depot[name]
    else:
        print("Die Aktie ist nicht im Depot")

def depot_speichern(depot):
    datei = open("mein_depot.txt", "w")
    for aktien, kurs in depot.items():
        datei.write(f"{aktien},{kurs}\n")
    datei.close()

def depot_laden():
    depot = {}                           # Startwert VOR dem try
    try:
        datei = open("mein_depot.txt", "r")
        inhalt = datei.readlines()
        datei.close()
        for zeile in inhalt:
            teile = zeile.split(",")
            aktie = teile[0].strip()
            kurs = float(teile[1].strip())
            depot[aktie] = kurs
    except FileNotFoundError:
        print("Noch kein Depot vorhanden - starte mit leerem Depot.")
    return depot                         # NACH try/except -> immer ein Dict

mein_depot = depot_laden()

while True:
    print("1 = Depot anzeigen")
    print("2 = Gesamtwert")
    print("3 = Teuerste Aktie")
    print("4 = Aktie hinzufuegen")
    print("5 = Aktie loeschen")
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
        if name.strip() == "":
            print("Name darf nicht leer sein.")
        else:
            try:
                kurs = float(input("Kurs: "))
                aktie_hinzufuegen(mein_depot, name, kurs)
            except ValueError:
                print("Bitte eine Zahl eingeben!")
    elif wahl == "5":
        name = input("Welche Aktie loeschen? ")
        aktie_loeschen(mein_depot, name)
    elif wahl == "6":
        depot_speichern(mein_depot)
        break
    else:
        print("Ungueltige Wahl")

