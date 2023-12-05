


from Body.speak import speak
import speech_recognition as sr
import pywhatkit
from time import sleep




def searchGoogle(query):
    if "search" in query:
        import wikipedia as googleScrap
       
        query = query.replace("search","")
        query = query.replace("google","")
        speak("This is what I found on google")
        print(query)

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")
    
   
    
                
    