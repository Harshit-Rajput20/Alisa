
 
 
import speech_recognition as sr
import os
import gtts
import pygame
import os
import pyautogui
import time
import webbrowser
 
 
 
def speak(text):
    tts = gtts.gTTS(text,lang="hi")
    tts.save("output.mp3")

    print(f"You: {text}.")

    pygame.mixer.init()

    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()
 
    os.remove("output.mp3")
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

def whatsapp():

    url = "https://web.whatsapp.com/"
    webbrowser.open(url)
    time.sleep(8)
    pyautogui.click(x=412, y=237)
    flag = True 
    speak('Search for a person ')
    while flag:
        out= listen().lower()
                    
        if (out != ''):
            print(out )
            time.sleep(1)
            pyautogui.typewrite(out)
            pyautogui.press('enter')
            flag = False
         
    time.sleep(2)
    pyautogui.click(x=1161, y=1031)  
    speak("what do you want to send")
    
    
    out= listen().lower()
                    
    if (out != ''):
        print(out )
        time.sleep(1)
        pyautogui.typewrite(out)
        pyautogui.press('enter')
    # elif "quit" in out or "quit chat" in out or "exit" in out :
    #     flag = False
        
        
     
    # pyautogui.press('enter')  
                
    
# whatsapp()