import pygame
import time
pygame.init()
pygame.mixer.init()
emailFlag=time.time()
# print(emailFlag)

def listen():
    try:
        print("listening.....")
        r=sr.Recognizer()
        
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio =r.listen(source,0,8)
            
            
        try:
            print("Recognition...")
            try :    
                if not pygame.mixer.get_init():
                    pygame.mixer.init()                   
                pygame.mixer.music.load('recogniiton.mp3')  
                pygame.mixer.music.play()
                pygame.time.wait(2000)   
                   
                pygame.mixer.music.stop()
            except:
                    pass 
        
            query = r.recognize_google(audio,language="en")
             
        except:
            return "" 
        
        query = str(query).lower()
        
        print(query)
        
        return query
    except:
        return ""

 

waked = False


try:
    account_sid = 'AC68544509cd775ef557e9f521057a3c15'
    account_token = 'ee30dbacc56eadabf2ee9ebde965d4bb'
    twillow_number = '+15716205626'
    myphone='+918445167775'
except:
    pass


def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,sir")
    elif hour >12 and hour<=18:
        speak("Good Afternoon ,sir")

    else:
        speak("Good Evening,sir")
        


print("test -1")
while True:    
    try:
        
            
        
        import cv2
        import pyautogui
        import datetime
        import requests    
        import speech_recognition as sr
        import os
        from jarvis import mainExe
        from Body.speak import speak
        
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email import encoders

    except:
        continue
    try:
        
        

        print("Test0")
        response = requests.get("http://www.google.com", timeout=5)
        print("Test1")
        response.raise_for_status() 
        print("Test2")
        print("Internet connection is available.")
        
        if(response.ok):
            print("connnected")
        else:
            print("not connected")
            
        try :    
            if not pygame.mixer.get_init():
                pygame.mixer.init()                   
            pygame.mixer.music.load('alisaStarting.mp3')  
            pygame.mixer.music.play()
            pygame.time.wait(6000)   
                   
            pygame.mixer.music.stop()
        except:
                pass 
        greetMe()
            
        speak("initiating system security")
            


         
                
            

        import cv2
        import face_recognition
        import cv2 
        import numpy as np
        import os
        import pickle
        file = open('EncodeFile.p','rb')
        encodeListWithIds= pickle.load(file)
        file.close()
        encodeList, studentIds = encodeListWithIds
        print(studentIds)
        cap = cv2.VideoCapture(0)
        cap.set(3,640)
        cap.set(4,480)

        mainFlag = True
        while mainFlag:
                    
            flag = 0 
                    

            res, frame = cap.read()
    
            imgS = cv2.resize(frame,(0,0),None,0.25,.25)
            imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
            faceFrame = face_recognition.face_locations(imgS)
            encodeFaceFrame = face_recognition.face_encodings(imgS,faceFrame)
            x=0
            for encodeFace, faceloc in zip(encodeFaceFrame,faceFrame):
                matches = face_recognition.compare_faces(encodeList,encodeFace)
                faceDistance = face_recognition.face_distance(encodeList,encodeFace)
                print("match",matches[0])
                        
                        
                if(matches[0]==True):
                    print("111111")
                    x=1
                    flag=1
                           
                    break
            
                else:
                    print(0)
                    speak("you are not verified")
                           
                            
                    # try :
                    #     from twilio.rest import Client

                    #     client = Client(account_sid,account_token)

                    #     message = client.messages.create(
                    #         body = "Someone just access your pc",
                    #         from_= twillow_number,
                    #         to=myphone
                    #     )
                    #     print(message.body)
                    # except:
                    #     pass    
                            
                    try:
                                
                        if(time.time()-emailFlag>10):
                            face_locations = face_recognition.face_locations(imgS)
                            for (top, right, bottom, left) in face_locations:
                                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                            cv2.imwrite('unknown_peoples/captured_photo.jpg', frame)
                            smtp_port = 587 
                            smtp_server = "smtp.gmail.com"   

                                    
                            email_from = "hr6138705@gmail.com"
                            email_list = "harshitrajput778@gmail.com"

                                    
                            pswd = "suhr rlob snfj ldsn"  


                                    
                            subject = "here is a picture of intruder"



                                    
                            def send_emails(email_list):
                    
                                            
                                            body = f"""
                                            hello sir
                                            Alisa this side 
                                            this email is sent to inform you that your system is accessed by someone unknown 
                                            here i am attaching the picture of the intruder. 
                                            """

                                    
                                            msg = MIMEMultipart()
                                            msg['From'] = email_from
                                            msg['To'] = email_list
                                            msg['Subject'] = subject
                                    
                                            msg.attach(MIMEText(body, 'plain'))

                                            
                                            filename = "/home/harshit/harshit/Jarvis-Self-Trained-main (copy)2/unknown_peoples/captured_photo.jpg"  

                                    
                                            attachment = open(filename, 'rb')
                                            
                                            attachment_package = MIMEBase('application', 'octet-stream')
                                            attachment_package.set_payload((attachment).read())
                                            encoders.encode_base64(attachment_package)
                                            attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
                                            msg.attach(attachment_package)

                                        
                                            text = msg.as_string()
                                    
                                            # print("Connecting to server...")
                                            TIE_server = smtplib.SMTP(smtp_server, smtp_port)
                                            TIE_server.starttls()
                                            TIE_server.login(email_from, pswd)
                                            # print("Succesfully connected to server")
                                            # print()


                                        
                                            speak("sending your live picture to harshit sir")
                                            TIE_server.sendmail(email_from, email_list, text)
                                            speak("picture sent ")
                                            # print()

                                        
                                            TIE_server.quit()
                                    




                                    
                            send_emails(email_list)
                            emailFlag=time.time()
                    except:
                                pass

 
                            
 

                            
                            
                print("FACE distance",faceDistance)
                matchIndex = np.argmin(faceDistance)
                print("Match Index",matchIndex)
                if matches[matchIndex]:
            # print("Known face Detected")
            # print(studentIds[matchIndex
                            y1,x2,y2,x1 = faceloc
                            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                            bbox = 55+x1,162+y1,x2-x1,y2-y1
                 

            if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            if flag == 1:
                        
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                         
                cap.release()
                cv2.destroyAllWindows()
                speak("verification successful , you can wake me up if you want something")
                
                
                while not waked:
                    query = listen().lower()
                    # query = input("enter wake up") 
            
            
                    if "wake up" in query or "hello" in query:
                
                        try :    
                            if not pygame.mixer.get_init():
                                pygame.mixer.init()                   
                            pygame.mixer.music.load('openingTheme.mp3')  
                            pygame.mixer.music.play()
                            pygame.time.wait(5000)   
                   
                            pygame.mixer.music.stop()
                        except:
                               pass 
                        mainExe()
                        
                    else:
                        print("")
                        print("AI : Not started")
                        print("")
                        pass
                    
               
                print("After Main exe")
                        
                mainFlag=False
                waked= False
                    

        
        print("Thanks for using this program, have a good day.")
        print("MainFlag" , mainFlag)
                            

     
            
    except requests.RequestException as e:
        # speak("internetconnectio error")
        print("some error ")

        print("Internet connection error "+e) 
        
