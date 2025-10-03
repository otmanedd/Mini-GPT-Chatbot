import subprocess
import os

# -------------------------
# 1️⃣ Lade statische Antworten aus chatbot.txt
# Format: frage: antwort
responses = {}
txt_file = "chatbot.txt"
if os.path.exists(txt_file):
    with open(txt_file, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                key, value = line.strip().split(":", 1)
                responses[key.lower()] = value.strip()
else:
    print(f"⚠️ {txt_file} nicht gefunden. Statische Antworten werden ignoriert.")

# -------------------------
# 2️⃣ Funktion, um Mistral über Ollama zu fragen
def ask_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()

# -------------------------
# 3️⃣ Chat-Loop
print("🤖 Chatbot gestartet! Tippe 'exit' zum Beenden.\n")

while True:
    user_input = input("You: ").strip().lower()
    if user_input in ["exit", "quit"]:
        print("Bot: Bye! 👋")
        break

    # 4️⃣ Prüfe zuerst die statischen Antworten
    found = False
    for key in responses:
        if key in user_input:
            print("Bot:", responses[key])
            found = True
            break

    # 5️⃣ Wenn kein Treffer, KI fragen
    if not found:
        reply = ask_ollama(user_input)
        print("Bot:", reply)
