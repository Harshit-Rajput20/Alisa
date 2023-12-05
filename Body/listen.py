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
        query = r.recognize_google(audio,language="hi")
        
    except:
        return ""
    
    query = str(query).lower()
    return query


# print(listen())


def translation(Text):
    line =str(Text)
    translate = Translator()
    result = translate.translate(line)
    data=result.text
    print(f"you: {data}.")
    return data




def connection():
    query = listen()
    data = translation(query)
    return data


# connection()

# translation("kaisi ho")

# listen()
