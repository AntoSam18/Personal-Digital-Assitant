import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import sys
import pyjokes
import wikipedia
import webbrowser
import requests
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTimer, QTime, QDate, QThread
from gui import Ui_MainWindow


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Carpediem, your assistant. How can I help you?")

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.Tasks()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, phrase_time_limit=5)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
        except Exception as e:
            speak("Say that again please...")
            return "none"
        return query.lower()

    def Tasks(self):
        greet()
        while True:
            try:
                self.query = self.takeCommand()
                print(f"Current query: {self.query}")  

                if "open notepad" in self.query:
                    speak("Opening Notepad...")
                    os.startfile("C:\\Windows\\system32\\notepad.exe")

                elif "open youtube" in self.query:
                    speak("Opening YouTube...")
                    webbrowser.open("https://www.youtube.com")

                elif "play music" in self.query:
                    speak("Playing music...")
                    music_dir = "E:\\music"
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, random.choice(songs)))

                elif "ip address" in self.query:
                    ip = requests.get("https://api.ipify.org").text
                    speak(f"Your IP address is {ip}")

                elif "wikipedia" in self.query:
                    speak("Searching Wikipedia...")
                    self.query = self.query.replace("wikipedia", "")
                    results = wikipedia.summary(self.query, sentences=2)
                    speak("According to Wikipedia")
                    speak(results)

                elif "tell a joke" in self.query:
                    joke = pyjokes.get_joke()
                    speak(joke)

                elif "where am i" in self.query:
                    try:
                        ip = requests.get("https://api.ipify.org").text
                        url = f'https://get.geojs.io/v1/ip/geo/{ip}.json'
                        locdata = requests.get(url).json()
                        city = locdata['city']
                        country = locdata['country']
                        speak(f"Sir, I think we are in {city} city of {country}")
                    except:
                        speak("Sorry, I couldn't fetch the location right now.")
                elif "no thanks" in self.query or "exit" in self.query:
                    speak("Thank you sir, have a nice day!")
                    sys.exit()

            except Exception as e:
                print(f"Error occurred: {e}")
                speak("Sorry, something went wrong. Please try again.")

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.movie = QtGui.QMovie("./Downloads/7LP8.gif")
        self.ui.label.setMovie(self.movie)
        self.movie.start()

        self.movie2 = QtGui.QMovie("./Downloads/projhu.gif")
        self.ui.label_3.setMovie(self.movie2)
        self.movie2.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.thread = MainThread()
        self.thread.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        self.ui.textBrowser.setText(current_date.toString(QtCore.Qt.ISODate))
        self.ui.textBrowser_2.setText(current_time.toString('hh:mm:ss'))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    jarvis = Main()
    jarvis.show()
    sys.exit(app.exec_())
