import pyautogui
import time
import webbrowser
# Open Google Meet website in a web browser

import speech_recognition as sr
from googletrans import Translator

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
    return query



    
    



def call(name):
    
    
    callBook = {' harshdeep': '08755373055', ' jatin': ' 08630099127',' himanshu':' 09927070196','garima joshi':' 06397432184'}

    

    webbrowser.open("https://meet.google.com/calling/") 
    
    time.sleep(8)  # Wait for the page to load
    
    pyautogui.click(x=970, y=170)   
    
    for contact, number in callBook.items():
        if contact == name:
            
            pyautogui.typewrite(number)

    # Type text into the textarea
   
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(2)
    
    pyautogui.click(x=900, y=791)   
    pyautogui.press('enter')

  
 
  
 

 
    

 
