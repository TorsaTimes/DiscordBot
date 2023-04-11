# Discord Bot

Dies ist ein einfacher Discord-Bot, der mit Hilfe der Discord.py-Bibliothek erstellt wurde. Der Bot kann verschiedene Zitate aus der TV-Show "Brooklyn Nine-Nine" und Geburtstagswünsche generieren.

## Vorraussetzungen

Um den Bot auszuführen, müssen Sie die folgenden Vorraussetzungen erfüllen:

- Python 3 installiert
- Discord.py-Bibliothek installiert
- Eine Discord-Bot-Token von Discord Developer Portal
- Eine `.env`-Datei mit den erforderlichen Umgebungsvariablen, wie `DISCORD_TOKEN` und `DISCORD_GUILD`, erstellt

## Installation

1. Klonen Sie das Repository auf Ihren lokalen Computer.
2. Stellen Sie sicher, dass Python 3 und pip installiert sind.
3. Installieren Sie die erforderlichen Python-Bibliotheken mit dem Befehl `pip install -r requirements.txt`.
4. Erstellen Sie eine `.env`-Datei im gleichen Verzeichnis wie die `bot.py`-Datei und füllen Sie sie mit den erforderlichen Umgebungsvariablen:

DISCORD_TOKEN=<Ihr Discord-Bot-Token>
DISCORD_GUILD=<Name des Discord-Servers>

5. Führen Sie den Bot mit dem Befehl `python bot.py` aus.

## Funktionen

Der Bot hat die folgenden Funktionen:

- Erkennt die Nachricht "99!" und antwortet mit einem Zitat aus "Brooklyn Nine-Nine".
- Erkennt die Nachricht "happy birthday" und antwortet mit einem zufälligen Geburtstagswunsch.

## Beitragende

- Autor: <Ihr Name>
- Email: <Ihre Email-Adresse>

Bitte fühlen Sie sich frei, den Bot nach Ihren Bedürfnissen anzupassen und zu erweitern.
