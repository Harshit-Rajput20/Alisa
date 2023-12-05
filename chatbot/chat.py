import random
import json
import webbrowser
import pyautogui
import gtts
import pygame
import os
from bardapi import BardCookies
import speech_recognition as sr

import torch
# from Body.speak import speak
from chatbot.model import NeuralNet
from chatbot.nltk_utils import bag_of_words, tokenize
 

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

    # Clean up the generated audio file
    os.remove("output.mp3")

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('chatbot/intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


try:

    bot_name = "Alisa"
    cookie_dict = { 
                "__Secure-1PSID": "dwitsQtw-GHKZbmdJWekEcNGxShi0PVp-4SKsiEVvj_SYkojdq373VSggQphWTnSyLJZvQ.",
                "__Secure-1PSIDTS": "sidts-CjIBPVxjSt6rY41spsM8bgJWv2hcaLC2lp3pbkB9r2KnOZQAVOJ9WmyCGqQDsB07FRi4gxAA",
                "__Secure-1PSIDCC": "ACA-OxOVhpVl9Ss5OP4Ts6McZICITo_VXfjGhAfKwx-HzWgIt_1k0yq2EDZXh9-BbcCW2aAO7g"
                }
    bard = BardCookies(cookie_dict=cookie_dict)
except:
    pass


def ReplyBrain(question , chat_log = None):
    Reply = bard.get_answer(question)['content']
    return Reply

def answer(question):
    
        # sentence = "do you use credit cards?"
        sentence = question
         

        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    speak(f"{random.choice(intent['responses'])}")
        else:
            speak("wait a second")
            # speak("recognizing")     
             
            
            # chat_log = None  
            question =  question.replace('alisha','')
            # FileLog = open("chatbot/chat_log.txt", "r")
            # chat_log_template = FileLog.read()
            # FileLog.close()
            # if chat_log is None:
            #     chat_log = chat_log_template
            # prompt = f'{chat_log}You : {question}\n alisa : '
                
             
            try:
            
                if(len(question)<5):
                    speak("invalid question") 
                else:  
                    reply = bard.get_answer(question)['content']
                    print("Orognal reply :"+reply)
                    speak(reply.split(".")[0])
            except:
                pass
                # chat_log_template_update =  chat_log_template + f"\nYou : {question}\n Friday : {reply}"
                # FileLog = open("chatbot/chat_log.txt","w")
                # FileLog.write(chat_log_template_update)
                # FileLog.close()  
                      
            
            
            
            
            
# answer("cricket match between india and aus")

            

            
 