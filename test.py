# import pyautogui

# try:
#     while True:
#         # Get the current mouse cursor position
#         current_position = pyautogui.position()
#         print(f"Mouse position: {current_position}")
# except KeyboardInterrupt:
#     print("Script terminated by user.")




# import cv2
# import face_recognition

# # Open a connection to the webcam (camera index 0 by default)
# cap = cv2.VideoCapture(0)

# # Set the resolution of the video capture
# cap.set(3, 640)
# cap.set(4, 480)

# while True:
#     # Read a frame from the webcam
#     ret, frame = cap.read()

#     # Convert the frame to RGB (face_recognition works with RGB images)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Detect faces in the frame
#     face_locations = face_recognition.face_locations(rgb_frame)

#     # Display the frame with face rectangles
#     for (top, right, bottom, left) in face_locations:
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

#     # Display the resulting frame
#     cv2.imshow('Webcam Capture', frame)

#     # Break the loop if the user presses the 'q' key
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Save the first captured frame as an image
# cv2.imwrite('unknown_peoples/captured_photo.jpg', frame)

# # Release the video capture object and close the window
# cap.release()
# cv2.destroyAllWindows()





 

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

 

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

         
        filename = "/home/harshit/harshit/Jarvis-Self-Trained-main/Features/123.png"  

 
        attachment = open(filename, 'rb')
        
        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(attachment_package)

       
        text = msg.as_string()
 
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Succesfully connected to server")
        print()


       
        print(f"Sending email to: {email_list}...")
        TIE_server.sendmail(email_from, email_list, text)
        print(f"Email sent to: {email_list}")
        print()

    
        TIE_server.quit()



send_emails(email_list)




        










