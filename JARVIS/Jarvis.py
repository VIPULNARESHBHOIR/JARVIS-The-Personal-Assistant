import pyttsx3                    #user defined module(downloaded)
import speech_recognition as sr   #user defined module(downloaded)
import wikipedia                  #user defined module(downloaded)
import pywhatkit                  #user defined module(downloaded)
import datetime                   #in-Built module
import time                       #in-Built module
import webbrowser                 #in-Built module
import os                         #in-Built module(operating system)
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from jarvisGUI import Ui_jarvisUI

                       

#setting of engine to taking voice 
eng=pyttsx3.init('sapi5')
voices=eng.getProperty('voices')
eng.setProperty('voices',voices[0].id)
eng.setProperty('rate',190)

#Speak function (given name as Robo)
def Robo(audio):
    print("  ")
    eng.say(audio)
    print("   ")
    eng.runAndWait() 

#introducing itself
def myself():
    print("i'm JARVIS, built in 2022 by vipul,soham and abhinav. i can look up for answers for you or \nhelp you with find the quickest via home. \nif you need anything just ask, your wish is my command.")
    Robo("i'm JARVIS, built in 2022. i can look up for answers for you or help you with find the quickest via home. if you need anything just ask, your wish is my command.")
    
#wishing to user
def Wishes():
    time=datetime.datetime.now().hour
    if (time>=20 and time<24):
        Robo("Good night sir")
    elif(time<12):
        Robo("good morning sir")
    elif(time>=12 and time <=15):
        Robo("Good afternoon sir")
    else:
        Robo("good evening sir")
    Robo("How may i help you ?")

#function to returning the current date
def date():
    dt=time.strftime("%m-%d-%Y")
    print(" -------------------")
    print("|   "+dt+"      |")
    print(" -------------------")
    Robo(dt)

#function to returning the current time  
def clock():
    print(" -------------------")
    print(time.strftime("|   %I:%M:%S %p     |"))
    print(" -------------------")
    Robo(time.strftime("%I:%M"))

#function to returning the today's day
def day():
    de=time.strftime("%A")
    print(de)
    Robo("today is"+de)

def openApp(self):
    Robo("tell me the name")
    name=self.takecommand().lower()
    if (name=='none'):
        Robo("Sorry! tell me again")
    else:
        Robo("ok sir, just a second")
        if 'code' in name:
            os.startfile("C:\\Users\\bhoir\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif 'notepad' in name:
            os.startfile("C:\\Users\\bhoir\\OneDrive\\Desktop\\Notepad.txt")    
        elif 'word' in name:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
        elif 'exel' in name:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
        elif 'powerpoint' in name:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
        elif 'netbeans' in name:
            os.startfile("C:\\Program Files\\NetBeans-15\\netbeans\bin\\netbeans64.exe")
        elif 'crome' in name:
            os.start("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        else :
            Robo("Sorry !, app is not installed yet. you can download by chrome.")

def playMusic(self):
    Robo("tell me the song name")
    musicName=self.takecommand().lower()

    if 'bappa' in self.query:
        os.startfile("C:\\Users\\bhoir\\Music\\bappa_song.mp3")
    elif 'arjit' in self.query:
        os.startfile("C:\\Users\\bhoir\\Music\\best_song_arjit_singh(128kbps).m4a")
    elif 'that should be me' in self.query:
        os.startfile("C:\\Users\\bhoir\\Music\\that_should.mp3")
    elif 'alan wallkar' in self.query:
        os.startfile("C:\\Users\\bhoir\\Music\\alan_wallker.mp3")
    elif 'motivational' in self.query:
        os.startfile("C:\\Users\\bhoir\\Music\\motivational_songs.mp3")
    elif 'julun yeti' in self.query:
        os.startfile("C:\\Users\\bhoir\\Music\\reshimgathi.mp3")
    elif 'kesari' in self.query:
        os.startfile("C:\\Users\\bhoir\\Music\\kesari.mp3")
    elif 'desh mere' in self.query:
        os.startfile("C:\\Users\\bhoir\\Music\\O_desh_mere.mp3")
    elif 'muzafir' in self.query:
        os.startfile("C:\\Users\\bhoir\\Music\\muzafir_song.mp3")
    else:
        pywhatkit.playonyt(musicName)
    Robo("Enjoy Sir...")

#::::::::::: to play movies :::::::::::
def playMovie(self):
    Robo("tell me the movie name")
    movieName=self.takecommand().lower()
    pywhatkit.playonyt(movieName)
    Robo("Enjoy Sir...")

#showing search history in text file
def SearchHistory():
    Robo("This is your search history.")
    """print("_________________________________________________________")
    print("---------------------------------------------------------")  """    
    os.startfile("C:\\Jarvis\\JarvisSearchHistory.txt")
    """print("_________________________________________________________")
    print("---------------------------------------------------------")"""
    time.sleep(5)

def SaveHis(query):
    file=open("JarvisSearchHistory.txt","a")
    file.write( query + "       \t\t" + time.strftime("TIME:[ %I:%M %p ]") + "\t" + time.strftime("DATE:[ %m-%d-%Y ]") + "\n\n" ) 
    file.close()

#===============================MAIN FUNCTION======================================================================================================
#Function to listening voice command (returning the heared audio in the form of String(text))
class MainThread(QThread):
    
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.TaskExecution()

    def takecommand(self):
        com=sr.Recognizer()                     
        with sr.Microphone() as source:  #Creates a new "Microphone" instance, which represents a physical microphone on the computer.
            print("       ")
            print("Listening...")
            com.pause_threshold=1.15
            audio=com.listen(source)

        try:
            print("Recognizing...")
            query=com.recognize_google(audio,language='en-in')     #here we have used google engine AND have set the language english-india
            print(query)
        except Exception as ex:
            return "none"
        return query


    def TaskExecution(self):                 
        try:
            Wishes()
            while True:
                self.query=self.takecommand().lower()  #we have converted the query in lowecase to case-sensation
                SaveHis(self.query)
                #command to asking about itself
                if 'yourself' in self.query:
                    myself()
            
                #command to asking about current timing 
                if 'timing' in self.query:
                    clock()
                
                #command to asking about today's day
                elif 'day' in self.query:
                    day()

                #command to asking about today's date
                elif 'date' in self.query:
                    date()

                #reply to thanks
                elif 'thank' in self.query:
                    Robo("you'r most welcome sir")
                
                #Jarvis wait , up till the given timing
                elif 'wait' in self.query:
                    Robo("For how many time !")
                    min=self.takecommand().lower()
                    if 'second' in min:
                        min=min.replace("second","")
                        min=min.replace("seconds","")
                        Robo(f"waiting for {min} second")
                        time.sleep((int)(min))
                    elif 'minute' in min:
                        min=min.replace("minutes","")
                        min=min.replace("minute","")
                        print(min)
                        Robo(f"waiting for {min} minute")
                        time.sleep((int)(min)*60)
                    elif 'none' in min:
                        Robo("sorry ! unable to hear you")
                    Robo("Time out !")

                elif 'stop' in self.query:
                    Robo("For how many time !")
                    min=self.takecommand().lower()
                    if 'second' in min:
                        min=min.replace("second","")
                        min=min.replace("seconds","")
                        Robo(f"waiting for {min} second")
                        time.sleep((int)(min))
                    elif 'minute' in min:
                        min=min.replace("minutes","")
                        min=min.replace("minute","")
                        Robo(f"waiting for {min} minute")
                        time.sleep((int)(min)*60)
                    elif 'none' in min:
                        Robo("sorry ! unable to hear you")
                    Robo("Time out !")
                
        
                #command to open youtube from web
                elif 'open youtube' in self.query:
                    Robo("ok sir")
                    webbrowser.open("https://www.youtube.com")
                
                #command to open google from web
                elif 'open google' in self.query:
                    Robo("ok sir")
                    webbrowser.open("https://www.google.com")
                
                #command to open facebokk from web
                elif 'open facebook' in self.query:
                    Robo("ok sir")
                    webbrowser.open("https://www.facebook.com")
                    
                #command to open watsapp from web
                elif  'open whatsapp' in self.query:
                    Robo("ok sir")
                    webbrowser.open("https://www.whatsapp.com")

                #command to open insta from web
                elif 'open instagram' in self.query:
                    Robo("ok sir")
                    webbrowser.open('https://www.instagram.com')
                    
                #command to open telegram from web
                elif 'open telegram' in self.query:
                    Robo("ok sir")
                    webbrowser.open("https://www.telegram.com")

                #command to open stackoverflow from web
                elif 'open telegram' in self.query:
                    Robo("ok sir")
                    webbrowser.open("https://www.stackoverflow.com")

                elif 'open canva' in self.query:
                    Robo("ok sir")
                    webbrowser.open('https://www.canva.com')

                elif 'open chrome' in self.query :
                    Robo("ok sir")
                    webbrowser.open('https://www.chrome.com')


                #to Search perticuler thing on you tube
                elif 'youtube search' in self.query:
                    Robo('ok sir, This is , i found on search')
                    self.query=self.query.replace("jarvis","")
                    self.query=self.query.replace("youtube search","")
                    website='https://www.youtube.com/results?search_query='+self.query
                    webbrowser.open(website)
                    Robo("Done sir")
                
                

                #to open the website of given name
                elif 'website' in self.query:
                    if 'in' in self.query:
                        Robo("Launching...")
                        self.query=self.query.replace("jarvis","")
                        self.query=self.query.replace("open","")
                        self.query=self.query.replace("the","")
                        self.query=self.query.replace(".in","")
                        self.query=self.query.replace("launch","")
                        self.query=self.query.replace("website","")
                        web1=self.query.replace(" ","")
                        web2='https://www.' + web1 + '.in'
                        webbrowser.open(web2)
                        Robo("Launched!")

                    else:
                        Robo("Launching...")
                        self.query=self.query.replace("jarvis","")
                        self.query=self.query.replace("open","")
                        self.query=self.query.replace("the","")
                        self.query=self.query.replace(".com","")
                        self.query=self.query.replace("launch","")
                        self.query=self.query.replace("website","")
                        web1=self.query.replace(" ","")
                        web2='https://www.' + web1 + '.com'
                        webbrowser.open(web2)
                        Robo("Launched!")
                
                #to extracting information from Browser
                elif 'wikipedia' in self.query:
                    print("searching wikipedia...")
                    self.query=self.query.replace("wikipedia","")
                    text=wikipedia.summary(self.query,3)
                    print("according to wikipedia,"+text)
                    Robo("according to wikipedia.."+text)
                
                #to Searching perticuler thing on google
                elif 'google search' in self.query:
                    Robo("Yes Sir, This is what i found on search")
                    self.query=self.query.replace("jarvis","")
                    self.query=self.query.replace("google search","")
                    pywhatkit.search(self.query)
                    Robo("done sir")
                
                elif 'app' in self.query:
                    openApp()
                
                elif 'play music' in self.query:
                    playMusic(self)
                
                elif 'play movie' in self.query:
                    playMovie(self)

                elif 'search history' in self.query:
                    SearchHistory()

                elif 'none' in self.query:
                    Robo("please say that again, i couldn't hear the words.")

                #QUIT The JARVIS
                elif 'quit' in self.query:
                    exit()
                elif 'exit' in self.query:
                    exit()

                
                else :
                    Robo("Searching...")
                    self.query=self.query.replace("jarvis","")
                    pywhatkit.search(self.query)
                    Robo("this is the result on google.")
        except Exception as ex:
            print("CONNECTION ERROR")

startex=MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_jarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.close)
        self.ui.pushButton_2.clicked.connect(self.startTask)

    def startTask(self):
        self.ui.movie=QtGui.QMovie("../../Documents/Pictures/Black_Template.jpg")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("../../Documents/Pictures/speaker.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startex.start()
        
    
    def showTime(self):
        realtime=QTime.currentTime()
        realdate=QDate.currentDate()
        time=realtime.toString('hh:mm:ss')
        date=realdate.toString(Qt.ISODate)
        self.ui.textBrowser_2.setText(date)
        self.ui.textBrowser.setText(time)
    

app=QApplication(sys.argv)
jarvis=Main()
jarvis.show()
exit(app.exec_())


