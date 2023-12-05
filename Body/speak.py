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

  
    os.remove("output.mp3")

# speak("Hello, sir!")

 


# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from time import sleep

# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from time import sleep

# chrome_options = Options()
# chrome_options.add_argument('--log-level=3')
# path = "/home/harshit/harshit/python/DataBase/chromedriver"
# chrome_options.headless = True
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--window-size=1920x1080')

# # Set the PATH environment variable to the Chrome WebDriver path
# os.environ['PATH'] = f'{os.environ["PATH"]}:{path}'

# # Create the Chrome WebDriver without specifying the executable_path
# driver = webdriver.Chrome(options=chrome_options)
# # driver.maximize_window()

# # Add a delay to keep the browser window open for a few seconds
# sleep(5)  # Adjust the sleep time as needed

# # Close the browser when done
# # driver.quit()


# # this is to open a perticular website and select the voice  


# website = r"https://ttsmp3.com/text-to-speech/British%20English/"
# driver.get(website)

# ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[2]/div[2]/form/select'))
# ButtonSelection.select_by_visible_text('British English / Brian')



# def speak(Text):
#     lengthofText =len(str(Text))
    
#     if(lengthofText==0):
#         pass
    
#     else:
        
#         print("")
#         print(f"AI: {Text}")
#         print("")
        
#         Data = str(Text)
       
#         textarea= driver.find_element(By.XPATH,value='/html/body/div[2]/div[2]/form/textarea').send_keys(Data)
#         driver.find_element(By.XPATH, value='//*[@id="vorlesenbutton"]').click()
#         driver.find_element(By.XPATH,value='/html/body/div[2]/div[2]/form/textarea').clear()
       
        
        
      
        
        
        
#         # textarea.clear()
#         # driver.quit()
        
#         if lengthofText>=30:
#             sleep(4)
            
#         elif lengthofText>=40:
#             sleep(6)
        
#         elif lengthofText>=55:
#             sleep(8)
            
#         elif lengthofText>=70:
#             sleep(10)    
        
#         elif lengthofText>=100:
#             sleep(13)
            
#         elif lengthofText>=120:
#             sleep(14)

#         else:
#             sleep(2)
            
            



# speak("Hello, sir!, I am Friday what can i do for you ")





