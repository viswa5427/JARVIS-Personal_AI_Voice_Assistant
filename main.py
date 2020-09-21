import os
import time
from camera import face_rec
from RespondListen import respond, listen
from digital_assistant import digital_assistant, intiate_jarvis, pre_init   
if __name__=="__main__":
    pre_init()
    if face_rec():
        intiate_jarvis()
        while True:
            respond("Please tell me how can i help you?")
            data = listen().lower()
            if data == 0:
                continue
            if "stop listening" in data or "ok bye" in data or "stop" in data or "exit" in data:
                os.system("taskkill /f /im Rainmeter.exe")
                respond("I am going to sleep sir")
                break
            digital_assistant(data)          
            time.sleep(2)