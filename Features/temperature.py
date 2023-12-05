import requests
from bs4 import BeautifulSoup
import gtts
import pygame
import os




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

def answerTemp(question):
    
    url = f"https://www.google.com/search?q={question}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")

    # The class name might change, so it's good to inspect the HTML source and adjust accordingly
    temp = data.find("div", class_="BNeawe iBp4i AP7Wnd").text
    speak("the temperature is " +temp)
