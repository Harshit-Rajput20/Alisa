from Body.speak import speak
import threading
import speech_recognition as sr
import os
import pyautogui
import webbrowser
from time import sleep
import subprocess
import datetime
import cv2
from Social_Media.youtube import searchYoutube
from Social_Media.search import searchGoogle
from Social_Media.whatsapp import whatsapp
from Features.temperature import answerTemp
from Features.Calculatenumbers import WolfRamAlpha
from Features.Calculatenumbers import Calc
from pynput.keyboard import Key,Controller
from time import sleep
from Features.call import call

keyboard = Controller()

 


def alarm(query):
    try:
        timehere = open("Alarmtext.txt", "a")
        timehere.write(query)
        timehere.close()
        
        subprocess.Popen(["python3", "alarm.py"])
        
    except Exception as e:
        print(f"Error in alarm function: {e}")

def listen():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio =r.listen(source,0,8)
        
    try:
        print("Recognition...")
        query = r.recognize_google(audio,language="en")
        
    except:
        return "" 
    
    query = str(query).lower()
    print(query)
    return query



import random
import json
from plyer import notification
import torch
import speedtest
from chatbot.model import NeuralNet
from chatbot.nltk_utils import bag_of_words, tokenize
from chatbot.chat import answer
import pygame





 
 
            
def mainExe():
     
    speak("On your service sir")
   
    
    while True:
        
        query = listen().lower()
        if "alisa" in query or "alisha" in query:
                print("AI:-" ,query )
                question =  query.replace('alisha','')
                print(question)
                answer(question)
        
        elif "youtube" in query :
            searchYoutube(query)  
            
        elif "pause" in query:
            pyautogui.press("k")
            speak("video paused")
        elif "play" in query:
            pyautogui.press("k")
            speak("video played")
        elif "mute" in query:
            pyautogui.press("m")
            speak("video muted")

        elif "remember that" in query:
            rememberMessage = query.replace("remember that","")
            rememberMessage = query.replace("alisa","")
            speak("You told me to remember that"+rememberMessage)
            remember = open("Remember.txt","a")
            remember.write(rememberMessage)
            remember.close()
        elif "what do you remember" in query:
            remember = open("Remember.txt","r")
            speak("You told me to remember that" + remember.read())
            remember = open("Remember.txt","w")
            rememberMessage = ' '
            remember.write(rememberMessage)
                    
        elif "calculate" in query:
            query = query.replace("calculate","")
            query = query.replace("alisa","")
            Calc(query)
            
        elif "call" in query:
            query= query.replace('call','')  
            call(query)
            
        elif "search" in query:
               searchGoogle(query)
            
        elif "temperature" in query:
            speak("searching the temperature")
            answerTemp(query)
            
        elif "weather" in query:
            speak("searching for the weather")
            answerTemp(query)
            
        elif "the current time" in query or "time now"in query or "whats the time" in query or "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")
             
        elif "set an alarm" in query:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("Done,sir")       
            
        elif "whatsapp" in query:
            whatsapp()
            
        elif "close one tab" in query or "1 tab" in query:
            speak("closing one tab")
            pyautogui.hotkey("ctrl","w")
            speak("tab closed")
        elif "close 2 tabs" in query or "close two tabs" in query or "close both tabs" in query:
            speak("closing both the tabs")
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            speak("All tabs closed")
        elif "3 tab" in query or "close all tabs" in query:
            speak("closing all the tabs")
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            speak("All tabs closed")
         
        elif "schedule my day" in query:
            tasks = [] #Empty list 
            speak("Do you want to clear old tasks (Plz speak YES or NO)")
            query = listen().lower()
            if "yes" in query:
                file = open("tasks.txt","w")
                file.write(f"")
                file.close()
                no_tasks = int(input("Enter the no. of tasks :- "))
                i = 0
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()
            elif "no" in query:
                i = 0
                no_tasks = int(input("Enter the no. of tasks :- "))
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()
            elif "show my schedule" in query:
                file = open("tasks.txt","r")
                content = file.read()
                file.close()
                if not pygame.mixer.get_init():
                    pygame.mixer.init()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(80) 
                pygame.mixer.music.load('Notification - Notification.mp3')  
                pygame.mixer.music.play()
                pygame.time.wait(10000)   
                pygame.mixer.music.stop()
                notification.notify(
                    title = "My schedule :-",
                    message = content,
                    timeout = 15
                    )
         
        elif "terminal" in query:
            speak("opening terminal")
            os.system('gnome-terminal')
            continue
        
        # elif "internet speed" in query:
        #             wifi  = speedtest.Speedtest()
        #             upload_net = wifi.upload()/1048576 
        #             download_net = wifi.download()/1048576
        #             print("Wifi Upload Speed is", upload_net)
        #             print("Wifi download speed is ",download_net)
        #             speak(f"Wifi download speed is {download_net}")
        #             speak(f"Wifi Upload speed is {upload_net}")

        
        elif "calendar" in query:
            speak("opening calendar")
            os.system('gnome-calendar')
            continue
        
        elif "calculator" in query:
            speak("opening calculator")
            os.system('gnome-calculator')
            continue

        elif "libra office" in query:
            speak("opening libra office")
            os.system('libreoffice --writer')  
            
            continue
        elif "firefox" in query:
            speak("opening firefox")
            os.system('firefox')
            continue
            
        elif "settings" in query:
             speak("opening settings")
             os.system('gnome-control-center')
             continue
        
        elif "system monitor" in query:
             speak("opening system monitor")
             os.system('gnome-system-monitor')
             continue
        
        elif "camera" in query:
            speak("opening the camera")
            speak("press q for exiting the camera")
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()
                cv2.imshow('Webcam', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
            
        elif "are you here" in query:
            speak("yes sir")
            
        elif "text editor" in query:
            speak("opening text editor")
            stop_flag = threading.Event()
            def open_editor(stop_flag):
                stop_flag.is_set()
                os.system('gedit')
                return
            your_thread = threading.Thread(target=open_editor,args=(stop_flag,))
            your_thread.start()


            
            continue
            
        elif "chat gpt" in query:
            webbrowser.open("https://chat.openai.com/?model=text-davinci-002-render-sha")
            
            
        elif  "shutdown" in query or "shut down" in query:
            speak("shutting down the system ,Good by sir")
            password = "7775"
            command = f'echo {password} | sudo -S poweroff'
            os.system(command)
        
        elif "backlit" in query or "back lit" in query or "back light" in query or "backlight" in query:
             pyautogui.hotkey('fn', 'f4')
             
        elif "bye" in query:
            speak("Bye sir have a nice day")
            break
            
        elif "go to sleep" in query:
            speak("O k sir , You can  call me anytime")
            break 
                
            

 
            
                    
 

 
            
            
            
 

                
            
   
        
        
        
  