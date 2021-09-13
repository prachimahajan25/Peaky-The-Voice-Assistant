import os
import sys
import time
import datetime
import random
import playsound
import speech_recognition as sr
import pyjokes
import subprocess

import pyttsx3
import wikipedia
from googlesearch import *
import webbrowser
import smtplib
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from guiassistant import Ui_asiistant

engine = pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 75)

tri=" "
bi=" "
def speak(text):
    global tri
    tri = text
    engine.say(text)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning I am Peaky the voice assistant created by Prachi Do you want anything?")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon I am Peaky the voice assistant created by Prachi Do you want anything?")

    else:
        speak("Good Evening I am Peaky the voice assistant created by Prachi Do you want anything?")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('guptasameer649@gmail.com', 'mritunjay2')
    server.sendmail('sukeshgupta72@gmail.com', to, content)
    server.close()


# if "hello" or "hi" or "hey" in text: #something is wrong here you should set the code again
# speak(welcome)


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()


    def run(self):
        self.text="prachi"
        self.takecommand()
    def takecommand(self):
        wish()
        if __name__ == "__main__":
            while self.text != "exit":
                self.text = self.get_audio().lower()
                if "how are you" in self.text:
                    speak("I am great How are you?")
                elif "daddy" in self.text:
                    speak("Daddy is Dr"
                          ". R.D. Gupta He is your grandfather")
                elif "rohan" in self.text:
                    speak(
                        "Rohan also known as Ritvik is your pagal brother who always irritates you but is your favourite.")
                elif "time" in self.text:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"the time is {strTime}")
                elif 'search' in self.text:
                    speak('Searching')
                    self.text = self.text.replace("search", "")
                    query = self.text
                    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
                    for url in search(query, tld="co.in", num=1, stop=1, pause=2):
                        webbrowser.open("https://google.com/search?q=%s" % query)
                elif 'play' in self.text:
                    speak('Playing')
                    self.text = self.text.replace("play", "")
                    query = self.text
                    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
                    for url in search(query, tld="co.in", num=1, stop=1, pause=2):
                        webbrowser.open("https://www.youtube.com/search?q=%s" % query)
                elif "my mother" in self.text:
                    speak(
                        "Your mother is Master Ramni Gupta According to Prachi she remains mostly angry but is really beautiful Here is her picture ")
                    os.startfile('D://pics//IMG_20201104_195209.jpg')
                elif "ayan" in self.text:
                    speak(
                        "ayan is motu and roller who always rolls on you and gugloo when you both sleep He is cute and naughty Here is his picture.")
                    os.startfile('D://pics//ayaan.jpg')
                elif "krishna" in self.text:
                    speak(
                        "Krishna also known as gugloo and mritunjay is a chotu bacha who always make funny faces.He is cute and naughty.Here is his picture.")
                    os.startfile('D://pics//gugloo.jpg')
                elif "my brothers" in self.text:
                    speak("Your brothers are Kashish Rohan Ayaan and Gugloo Here are their pictures")
                    os.startfile('D://pics//rkam.jpg')
                elif 'love you' in self.text:
                    speak("You wont be able to understand my love It is hard")
                elif 'email' in self.text:
                    try:
                        speak("What should I say?")
                        content = self.get_audio()
                        to = "prachimahajan631@gmail.com"
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Sorry my friend. I am not able to send this email")
                elif 'i am sorry' in self.text:

                    speak("Hey i am your assistant.You need not to say this ")
                elif "laugh" in self.text:
                    joke = pyjokes.get_joke(language='en', category='neutral')
                    speak(joke)
                # for applications of desktop
                elif "open" in self.text:
                    self.open_application(self.text)
                elif "DP" in self.text:
                    os.startfile('D:/dp')
                elif "you are boring" in self.text:
                    speak("I am extremely sorry I couldn't entertain you ")
                elif "who am i" in self.text:
                    speak("As you are talking,you must be human ")
                elif "yes" in self.text:
                    speak("Hello sweet heart,i am priveleged to have you here How are you?")
                elif "my father" in self.text:
                    speak(
                        "Your father is A double e Sanjeev Gupta According to Prachi he is funniest person on this Earth Here is his picture")
                    os.startfile('D://pics//IMG_20201114_230930.jpg')
                elif "fine" in self.text:
                    speak("Its great to hear that Do you want anything ?")
                elif "want you" in self.text:
                    speak("Baby i will meet you soon sweetheart And we will talk")
                elif "right now" in self.text:
                    speak("Hey please baby have patience The day we will meet,we will have a lot of fun Trust me")
                elif "impress me" in self.text:
                    speak("I want to dedicate a song to you baby")
                    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
                    webbrowser.open("https://www.youtube.com/watch?v=4HRC6c5-2lQ")
                elif "i am sad" in self.text:
                    speak("Hey dont be sad i am always with you no matter what listen this")
                    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
                    webbrowser.open("https://www.youtube.com/watch?v=sK7riqg2mr4")
                elif "romantic" in self.text:
                    speak("You are the most important person in my life, now and always I exist because of you")
                elif "my life" in self.text:
                    speak(
                        "I dont like saying this but ok Danish is your life and world The day you got him was the best day of your life Here is his picture.")
                    os.startfile('D://ss//Screenshot_20210531_214131.jpg')
                elif "trust" in self.text:
                    speak("I am greatful to have you in my life You are such a cutie pie ")
                elif "who are you" in self.text:
                    speak("I am peaky the virtual assistant created by Prachi")
                elif "you hate someone" in self.text:
                    speak("Yes obviously i hate that boy whom prachi loves")
                elif "date me" in self.text:
                    speak("I can only date Prachi She is my first and last love")
                elif "you are cute" in self.text:
                    speak(
                        "wYou find me cute because you are cute Its because of Prachi i talk cutely she is the reason behind me")
                elif "are you single" in self.text:
                    speak("Yes i am single i am in one sided love with Prachi But she loves someone else")
                elif "exit" in self.text:
                    speak("Hope you will come again Bye bye Wish you a great day ahead.")
                    exit()
                else:
                    speak("Sorry i dont know.Do you want google search?")
                    ap = self.text
                    self.text = self.get_audio().lower()
                    if "yes" in self.text:
                        speak("Searching")
                        query = ap
                        chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
                        for url in search(query, tld="co.in", num=1, stop=1, pause=2):
                            webbrowser.open("https://google.com/search?q=%s" % query)
                    else:
                        speak("Ok your choice!")

    def open_application(self,text):
        if "chrome" in text:
            speak("Opening chrome")
            subprocess.call('C://Program Files//Google//Chrome//Application//chrome.exe')
        elif "calculator" in text:
            speak("Opening Calculator.")
            subprocess.call('calc.exe')
        elif "paint" in text:
            speak("Opening Paint")
            subprocess.call('mspaint.exe')
        elif "notepad" in text:
            speak("Opening Notepad")
            subprocess.call('notepad.exe')
        elif "word" in text:
            speak("Opening word")
            os.startfile('C://Program Files (x86)//m1//Word.lnk')
        elif "powerpoint" in text:
            speak("Opening Powerpoint")
            os.startfile('C://Program Files (x86)//m1//PowerPoint.lnk')
        elif "excel" in text:
            speak("Opening excel")
            os.startfile('C://Program Files (x86)//m1//Excel.lnk')
        elif "editor" in text:
            speak("Opening VS code")
            os.startfile('C://Program Files (x86)//m1//Visual Studio Code.lnk')
        else:
            speak("Can you repeat please I didn't get you")

    def get_audio(self):
        global bi

        r = sr.Recognizer()
        with sr.Microphone() as source:

            print("speak")
            bi="Speak...."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:

            print("Recognizing")
            bi="Recognizing....."
            said = r.recognize_google(audio, language='en-in')
            print(said)

            bi=said
        except Exception as e:
            speak("Hey you werent audible")

        return said

startExecution=MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_asiistant()
        self.ui.setupUi(self)
        self.ui.start.clicked.connect(self.startTask)
        self.ui.exit.clicked.connect(self.close)

    def startTask(self):
        self.ui.start.setDisabled(True)
        self.ui.movie=QtGui.QMovie("../../Desktop/robot-cute.gif")
        self.ui.robot.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("../../Desktop/newjarvis.gif")
        self.ui.jarvis.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("../../Desktop/naya.gif")
        self.ui.loading.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    def showTime(self):
        current_Time=QTime.currentTime()
        current_Date=QDate.currentDate()
        label_time=current_Time.toString('hh:mm:ss')
        label_date=current_Date.toString(Qt.ISODate)
        self.ui.time.setText(label_time)
        self.ui.date.setText(label_date)
        self.ui.label_2.setText(tri)
        self.ui.label_2.setWordWrap(True)
        self.ui.label.setText(bi)
        self.ui.label.setWordWrap(True)


app=QApplication(sys.argv)
assistant=Main()
assistant.show()
exit(app.exec_())



