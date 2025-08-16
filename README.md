# 🤖 Carpediem – Your Smart Personal Digital Assistant

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![PyQt5](https://img.shields.io/badge/PyQt5-GUI-green?logo=qt)
![License](https://img.shields.io/badge/License-MIT-orange)

**Carpediem** is a voice-activated desktop assistant built with Python and PyQt5.  
It helps you perform tasks like launching apps, searching files, controlling system settings, taking notes, and even having fun with jokes — all through simple **voice commands**.  

Think of it as your own **AI-powered desktop companion**. 🚀

---

## ✨ Features

### 🎙️ Voice Commands
- **Open Applications:** “Open Chrome”, “Launch Notepad”, etc.
- **File Search & Open:** “Find my resume”, “Open project report” → Carpediem1 locates and opens files.
- **Wikipedia Search:** “Tell me about Alan Turing” → quick facts.
- **Play Music:** Plays a random song from your music folder.
- **Jokes & Fun:** “Tell me a joke” → get a laugh.
- **IP & Location Info:** Ask “What’s my IP?” or “Where am I?”
- **Browser Shortcuts:** Open YouTube, Google, etc.

### ⚙️ Smart System Utilities
- **Take Notes / Set Reminders:** “Remind me in 15 minutes”, “Take a note.”
- **System Tasks:** “Shutdown in 30 minutes”, “Take a screenshot.”
- **System Controls (Future-Ready):** Adjust brightness, volume, Wi-Fi.
- **ChatGPT Integration (Optional):** Intelligent Q&A responses.
- **Notification Reader (Experimental):** Reads desktop notifications.

### 🧠 AI-Powered File Search
- Uses **fuzzy matching** to find files even with imperfect spoken names.

### 📊 Interactive GUI
- Built with **PyQt5**
- Displays real-time **date & time**
- Shows live **command logs**
- Animated **GIF feedback**

---

## 🛠️ Tech Stack

- **Language:** Python 3.9+
- **GUI Framework:** PyQt5
- **Libraries:**  
  - `pyttsx3` → Text-to-Speech  
  - `speech_recognition` → Voice input  
  - `wikipedia`, `pyjokes`, `requests`, `webbrowser`  
  - `difflib` → AI-powered fuzzy matching  
- **System Tools:** OS, sys

---

## 🖥️ Installation

### 1. Clone Repository
```bash
git clone https://github.com/your-username/Carpediem1.git
cd Carpediem1
```
### 2. Install Depedencies

```
pip install -r requirements.txt
```
### 3.Run the Assistant
```
python main.py
```
🎤 Make sure your microphone is enabled. Carpediem1 will greet you and start listening.

## 📂 Project Structure

Project Structure:
 Carpediem1/
 ```
├── main.py # Main assistant logic
├── gui.py # PyQt5 auto-generated GUI code
├── Downloads/ # Animated GIFs used in GUI
├── assets/ # (Optional) Sounds, icons
├── requirements.txt # Python dependencies
└── README.md # Documentation
```

---

## 🔧 Customization

- **Add More Apps:** Update `app_paths` dictionary in `main.py`.
- **Edit Search Paths:** Modify `search_dirs` list for file search locations.
- **Add More Commands:** Extend the `Tasks()` function with custom voice actions.
- **Improve GUI:** Edit `.ui` file in Qt Designer and regenerate `gui.py` using `pyuic5`.

---

## 🧠 Roadmap

- ✅ Voice-based file search with AI-powered fuzzy matching  
- ⏳ Persistent notes & reminders using SQLite/JSON  
- ⏳ Smart home integration (IoT / MQTT / IFTTT)  
- ⏳ Personality upgrade: customizable wake words & voices  
- ⏳ GUI enhancements: microphone animation & notifications  

---

## 🤝 Contributing

Contributions are welcome!  

1. **Fork** the repository  
2. **Create** a new feature branch (`git checkout -b feature-name`)  
3. **Commit** your changes (`git commit -m "Added feature xyz"`)  
4. **Push** to your branch (`git push origin feature-name`)  
5. **Open a Pull Request** 🎉  

---

## 👨‍💻 Author

**Anto Sam Christ A – B.Tech CSE**  
🚀 Passionate developer exploring AI assistants, data science, and automation.  

- 📧 Email: *[antosamchrist18@gmail.com]*    




