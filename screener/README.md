# Aktien-Screener

Prüft eine Watchlist gegen eine selbst definierte Kaufregel und zeigt, welche Titel sie erfüllen.

## Warum ich es gebaut habe

Beim Durchsehen einer Watchlist mache ich immer dieselbe Prüfung von Hand: Liegt der Kurs unter meinem Zielkurs? Das Programm wendet die Regel auf alle Titel gleichzeitig an — und die Regel steht an genau einer Stelle, lässt sich also ändern, ohne den Rest anzufassen.

## Was es kann

- Prüft jeden Titel gegen die Kaufregel
- Gibt die Treffer mit Kurs und Zielkurs aus
- Zählt, wie viele Titel die Bedingung erfüllen

## Starten

```bash
python3 screener.py
```

Beispielausgabe:
```
Treffer:
  ASML: 900 (Ziel 950)
  SAP: 200 (Ziel 250)
2 von 3 Titeln erfuellen die Regel.
```

## Was ich dabei gelernt habe

**`return` statt `print`.** Eine Funktion, die nur `print` benutzt, zeigt etwas an — danach ist das Ergebnis weg. Mit `return` lässt sich die Funktion direkt als Bedingung verwenden: `if kaufwuerdig(kurs, ziel):`. Das war der Punkt, an dem aus einer Anzeige ein wiederverwendbares Werkzeug wurde.

**Regel und Daten trennen.** Die Prüfregel steht in einer eigenen Funktion, die Daten liegen außerhalb. Dadurch kann ich die Regel ändern, ohne die Schleife anzufassen — und dieselbe Funktion auf eine andere Watchlist anwenden.

**Das Werkzeug muss zur Domäne passen.** Für die Namensprüfung hatte ich zuerst `.isalpha()` erwogen. Das wäre falsch gewesen: Echte Ticker enthalten Punkte und Ziffern (BRK.B, 3M). Eine technisch korrekte Prüfung kann fachlich trotzdem unbrauchbar sein.

## Nächste Schritte

Statt fester Werte echte Kursdaten über eine API laden, die Ergebnisse validieren und in einer Datenbank speichern. Die Regel selbst bleibt dabei unverändert — das ist der Vorteil der Trennung.