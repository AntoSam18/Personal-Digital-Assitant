# 🤖 Carpediem – Your Smart Personal Digital Assistant

Carpediem is a voice-activated personal assistant built with Python and PyQt5 that helps you perform a variety of tasks — from launching apps and searching files to controlling system settings and reading jokes. Think of it as your own desktop AI companion, always ready to assist with your day-to-day digital needs.

---

## 🚀 Features

### 🎙️ Voice Commands
- **Open Applications:** Just say "Open Chrome", "Launch Notepad", etc.
- **File Search & Open:** Ask “Find my resume” or “Open project report” and Carpediem1 will locate and open it.
- **Wikipedia Search:** “Tell me about Alan Turing” – get quick facts instantly.
- **Play Music:** Start a random track from your music directory.
- **Jokes & Fun:** “Tell me a joke” for a laugh.
- **IP & Location Info:** Ask for your public IP or where you are.
- **Browser Shortcuts:** Open YouTube or Google hands-free.

### ⚙️ Smart System Utilities
- **Take Notes / Set Reminders:** “Remind me in 15 minutes” or “Take a note.”
- **Scheduled Shutdowns / Screenshots:** “Shutdown in 30 minutes”, “Take a screenshot.”
- **Control Brightness, Volume, Wi-Fi:** (Future ready via PowerShell or Windows APIs)
- **ChatGPT API Integration:** Get intelligent responses to complex questions (optional).
- **Desktop Notification Reader:** Reads active system notifications (experimental).

### 🧠 AI-Powered File Search
Uses fuzzy matching to locate files even if the spoken name isn’t exact.

### 📊 Dynamic GUI
Built with PyQt5:
- Displays real-time date and time.
- Shows live logs of your commands and system responses.
- Animated feedback using GIFs.

---

## 🛠️ Technologies Used

- Python 3.9+
- PyQt5 (GUI)
- pyttsx3 (Text-to-Speech)
- speech_recognition (Voice Input)
- wikipedia, pyjokes, requests, webbrowser
- difflib (Fuzzy Matching)
- OS & sys for app/file control

---

## 🖥️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Carpediem1.git
cd Carpediem1
