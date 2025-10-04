# Mini GPT-Chatbot 🐱‍💻

Ein interaktiver **Offline-Chatbot**, der das LLM **Mistral** über **Ollama** nutzt.  
Der Chatbot kann **statische Antworten aus `chatbot.txt`** geben oder auf andere Fragen intelligent mit Mistral antworten.

---

## 🚀 Features

- Interaktiver Terminal-Chat
- Offline GPT-ähnliche Antworten über Mistral
- Statische Antworten für vordefinierte Fragen (`chatbot.txt`)
- Einfach erweiterbar und anpassbar

---

## 📦 Installation

1. **Repository klonen**
```bash
git clone https://github.com/otmanedyaf/Mini-GPT-Chatbot.git
cd Mini-GPT-Chatbot
```
---


## Virtuelle Umgebung erstellen & aktivieren
```
python3 -m venv venv
source venv/bin/activate
```
---
##Abhängigkeiten installieren
```
pip install -r requirements.txt
```
Ollama Desktop App installieren
Download: https://ollama.com/download
Starte die App einmal, damit der lokale Server läuft.
Mistral-Modell herunterladen
ollama pull mistral
---
## Nutzung / Testen
Chatbot starten
```
python3 chatbot.py
```
Nachrichten eingeben
Tippe etwas ein und der Bot antwortet entweder aus chatbot.txt oder mit Mistral.
Beispiel-Schlüsselwörter in chatbot.txt (falls vorhanden) werden zuerst verwendet.
Chat beenden
Tippe exit oder quit.
---
Hinweise
Läuft vollständig offline über Ollama
Erweiterbar mit eigenen Intents oder Logik
Funktioniert auf Mac (mit Ollama Desktop App)
Statische Antworten in chatbot.txt sollten das Format frage: antwort haben
Beispiel:
hi: Hello! How can I help you?
bye: Goodbye! See you soon!


