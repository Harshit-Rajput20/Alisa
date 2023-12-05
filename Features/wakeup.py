
 

import speech_recognition as sr
import os

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


def wakeUp():
    queery = listen().lower()
    
    if "wake up" in queery:
        file_path = r"/home/harshit/harshit/python/main.py"
        os.system(f"xdg-open '{file_path}'")
    else:
        pass
    
while True:
    wakeUp()
    
    
    
