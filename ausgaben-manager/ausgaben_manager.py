# Ausgaben-Manager
# Erfasst und wertet Ausgaben aus. Speichert nach jedem Eintrag,
# damit auch bei einem harten Abbruch nichts verloren geht.

def ausgaben_speichern(ausgaben, dateiname):
    datei = open(dateiname, "w")
    for name, betrag in ausgaben.items():
        datei.write(f"{name},{betrag}\n")
    datei.close()

def ausgaben_laden(dateiname):
    ausgaben = {}                        # Startwert VOR dem try
    try:
        datei = open(dateiname, "r")
        inhalt = datei.readlines()
        datei.close()
        for zeile in inhalt:
            teile = zeile.split(",")
            name = teile[0].strip()
            betrag = float(teile[1].strip())
            ausgaben[name] = betrag
    except FileNotFoundError:
        print("Noch keine Ausgaben gespeichert.")
    return ausgaben                      # NACH try/except

def teuerste_ausgabe(ausgaben):
    hoechster_betrag = 0                 # zwei Zettel, beide VOR der Schleife
    name_zettel = ""
    for name, betrag in ausgaben.items():
        if betrag > hoechster_betrag:
            hoechster_betrag = betrag
            name_zettel = name
    return name_zettel

kosten = ausgaben_laden("kosten.txt")

while True:
    print("1 = Anzeigen")
    print("2 = Hinzufuegen")
    print("3 = Teuerste Ausgabe")
    print("4 = Beenden (speichert)")
    wahl = input("Eingabe: ")
    if wahl == "1":
        for name, betrag in kosten.items():
            print(f"{name}: {betrag} EUR")
    elif wahl == "2":
        name = input("Name der Ausgabe: ")
        if name.strip() == "":
            print("Name darf nicht leer sein.")
        else:
            try:
                betrag = float(input("Betrag: "))
                kosten[name] = betrag
                ausgaben_speichern(kosten, "kosten.txt")
            except ValueError:
                print("Bitte eine Zahl eingeben!")
    elif wahl == "3":
        print(teuerste_ausgabe(kosten))
    elif wahl == "4":
        ausgaben_speichern(kosten, "kosten.txt")
        break
    else:
        print("Ungueltige Eingabe")