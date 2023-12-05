 
from Body.speak import speak
import speech_recognition as sr
import pywhatkit
import pyautogui
import webbrowser
 
 
 


 


def searchYoutube(query):
    if "youtube" in query or "play" in query:
        speak("This is what I found on youtube") 
        query = query.replace("search","")
        query = query.replace("youtube","")
        query = query.replace("play","")
        query = query.replace("on","")

       
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")
            

    
    
    
 
  


