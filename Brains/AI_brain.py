import gtts
import pygame
import os
from bardapi import BardCookies
import speech_recognition as sr




def speak(text):
    tts = gtts.gTTS(text,lang="en")
    tts.save("output.mp3")

    print(f"You: {text}.")

    pygame.mixer.init()

    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()

    # Clean up the generated audio file
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
    return query



cookie_dict = { 
               "__Secure-1PSID": "dQheJrZcQ2vx4gXEC1mMZmikJqQVT4TxjhP72GsKAlwRq_y4PEW9M23FHSMyb3BoksCHfQ.",
               "__Secure-1PSIDTS": "sidts-CjEBNiGH7lvRkQGTREJu3GmC7VnKqrO09btRDskOxMQEZvdAAYzoJAG6zlRY9em1RUCDEAA",
               "__Secure-1PSIDCC": "ACA-OxPMdzqts_2ZvO4YkDCslSWFsblS8v3FXxIt1BxmwLOlTXvdwF6mxRAuiGuvK5KfU2StVIY"
               }
bard = BardCookies(cookie_dict=cookie_dict)

def ReplyBrain(question , chat_log = None):
    FileLog = open("DataBase/chat_log.txt", "r")
    chat_log_template = FileLog.read()
    FileLog.close()
    
    
    if chat_log is None:
        chat_log = chat_log_template
        
    prompt = f'{chat_log}You : {question}\n Friday : '
    
    
    Reply = bard.get_answer(question)['content']
     
    chat_log_template_update =  chat_log_template + f"\nYou : {question}\n Friday : {Reply}"
    FileLog = open("DataBase/chat_log.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return Reply


def answers(question): 

    while True:
        input_text = question
        print(input_text)  
                
        reply = ReplyBrain(input_text)
        print(reply)
        speak(reply)
        # break
        
# answers()
                
       
       
       
       
 