# Portfolio-Tracker

Ein Kommandozeilen-Programm zum Verwalten eines Aktiendepots. Die Daten werden in einer Textdatei gespeichert und beim nächsten Start automatisch geladen.

## Warum ich es gebaut habe

Ich verfolge mein eigenes Depot und wollte ein Werkzeug, das mir Gesamtwert und Positionen auf einen Blick zeigt. Die erste Version verlor beim Schließen alles — das war der Anlass, Speichern und Laden zu ergänzen.

## Was es kann

- Depot anzeigen, Gesamtwert berechnen, teuerste Position finden
- Aktien hinzufügen und löschen
- Automatisches Speichern beim Beenden, automatisches Laden beim Start
- Fängt Fehleingaben ab: leere Namen, Buchstaben statt Zahlen, ungültige Menüwahl, fehlende Datei

## Starten

```bash
python3 portfolio_tracker.py
```

Beim ersten Start wird `mein_depot.txt` automatisch angelegt.

## Wie ich getestet habe

Statt zu raten, welche Eingaben Probleme machen, habe ich das Programm gezielt mit Falscheingaben beschossen und notiert, was passiert:

| Test | Ergebnis vorher | Fix |
|---|---|---|
| Menüwahl `9` oder Enter | nichts passierte, keine Rückmeldung | `else`-Zweig am Menü-Ende |
| Leerer Aktienname | **wurde gespeichert (Bug)** | `if name.strip() == ""` |
| Kurs `abc` | bereits abgefangen | — |
| Nicht vorhandene Aktie löschen | Meldung erschien | — |
| Datei fehlt beim Start | **Absturz** | `except FileNotFoundError` |

## Was ich dabei gelernt habe

**Dateimodi:** `"w"` löscht die Datei sofort beim Öffnen — auch wenn danach nichts geschrieben wird. Das ist mir beim Testen passiert und hat die Depot-Datei geleert. Seitdem prüfe ich bei jedem `open`, ob ich lese oder schreibe.

**Rückgabewerte bei Fehlern:** Stand das `return` innerhalb des `try`-Blocks, gab die Funktion bei fehlender Datei `None` zurück. Das stürzt nicht sofort ab, sondern erst später bei `None.items()` — die Fehlermeldung zeigte auf Code, der in Ordnung war. Lösung: Startwert vor den `try`, `return` nach dem `except`. So kommt in jedem Fall ein gültiges Dictionary zurück.

**Konkrete Fehlertypen:** `except FileNotFoundError` statt eines nackten `except` — sonst werden auch eigene Tippfehler stillschweigend verschluckt, und man sucht stundenlang nach einer Datei, die längst existiert.

**`try` oder `if`:** Zwei verschiedene Probleme. Ein leerer Name ist falsch, aber harmlos — das prüft man vorher mit `if`. `float("abc")` beendet das Programm — das kann man nur mit `try` auffangen.

## Was ich heute anders machen würde

Den Dateinamen als Parameter übergeben statt ihn fest in die Funktion zu schreiben. Dann wäre das Speichern mit jeder Datei nutzbar — so wie ich es im Ausgaben-Manager danach gemacht habe.