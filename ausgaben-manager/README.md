# Ausgaben-Manager

Ein Programm zum Erfassen und Auswerten monatlicher Ausgaben. Die Daten bleiben nach dem Beenden erhalten.

## Warum ich es gebaut habe

Als Selbsttest: Ich wollte prüfen, ob ich ein vollständiges Programm ohne Vorlage schreiben kann — vier Funktionen, Menü, Fehlerbehandlung, Datenspeicherung. Komplett aus dem Kopf, ohne in früheren Code zu schauen.

## Was es kann

- Ausgaben anzeigen und hinzufügen
- Teuerste Ausgabe ermitteln
- Speichert nach jedem Eintrag, nicht erst beim Beenden — so gehen auch bei einem harten Abbruch keine Daten verloren
- Fängt ab: leere Namen, ungültige Beträge, fehlende Datei, falsche Menüwahl

## Starten

```bash
python3 ausgaben_manager.py
```

Beim ersten Start wird `kosten.txt` automatisch angelegt.

## Getestet

| Fall | Erwartet | Ergebnis |
|---|---|---|
| Datei fehlt beim Start | leeres Dictionary, kein Absturz | ✓ |
| Ungültige Menüwahl | Meldung, Programm läuft weiter | ✓ |
| Leerer Name | abgefangen | ✓ |
| Betrag `abc` | abgefangen | ✓ |
| Anzeigen und Auswerten | korrekte Ausgabe | ✓ |
| Neustart | Daten noch vorhanden | ✓ |

## Was ich dabei gelernt habe

**Die Richtung bestimmt das Werkzeug.** Beim Schreiben braucht man `.items()`, f-string und `.write()`. Beim Lesen `.readlines()`, `.split()` und `float()`. Ich habe anfangs mehrfach Lese-Werkzeuge beim Schreiben benutzt — ein Denkfehler, der sich erst auflöste, als ich die beiden Richtungen bewusst getrennt habe.

**Zwei Ebenen beim Einlesen.** `.readlines()` liefert eine Liste *aller Zeilen*, `.split(",")` die *zwei Teile einer Zeile*. Greift man mit `[0]` auf die Zeile statt auf das Split-Ergebnis zu, bekommt man den ersten Buchstaben statt des Namens — und Python meldet nichts.

**Typumwandlung ist nicht optional.** Ohne `float()` werden Zahlen als Text verglichen, buchstabenweise. `"90" > "800"` ergibt dann `True`. Das stürzt nicht ab — es liefert still ein falsches Ergebnis, was schwerer zu finden ist als ein Absturz.

**Methoden geben zurück, statt zu verändern.** `zeile.split(",")` ohne Zuweisung macht nichts Sichtbares: Das Ergebnis wird erzeugt und sofort verworfen. Es muss in eine Variable.

## Was ich heute anders machen würde

Die Anzeige-Logik in eine eigene Funktion auslagern, statt sie direkt ins Menü zu schreiben. Dann wäre das Menü nur noch Steuerung und jede Aufgabe hätte ihre eigene Funktion.