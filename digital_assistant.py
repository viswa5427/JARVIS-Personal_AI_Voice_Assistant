#MIT License

#Copyright (c) 2020 Viswanadh Kothakota

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import speech_recognition as sr
import datetime
import os, random
import webbrowser
import psutil
import wikipedia
import time
import speedtest
import requests, json
from time import ctime
from RespondListen import respond, listen
from googlesearch import search
from ecapture import ecapture as ec
from camera import face_rec, New_access
from Calendar import calendar_events, create_event
import time
from tictactoe import tic_tac_toe
import smtplib


webbrowser.register('chrome',
	            None,
	            webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

# to use this first enable less secure app setting in your gmail
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email address', 'password')
    server.sendmail('your email address', to, content)
    server.close()

def init_check():
    if internet_availability():
        pre_init()
        if face_rec():
            return True 
        else:
            return False
    else:
        return False

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please...")
        return "None"  # None string will be returned
    return query

def pre_init():
    respond("hi sir! You are activated Jarvis, But In orded to activate all the functions of Jarvis I have to recognize you sir ")
    respond("So, A facial recognition is under process, please wait!")

def intiate_jarvis():
    respond("checking remote servers!")
    respond("importing preferences and loading all the system drivers!")
    respond("establish secure connection!")
    os.startfile("c:\\Program files\\Rainmeter\\Rainmeter.exe")
    respond("secure connection established!")
    respond("we are online!")
    respond("welcome back sir!")
    wishme()
    respond("Jarvis is at your service")
 
def wishme():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        respond("Good Morning")
    elif hour>=12 and hour<18:
        respond("Good Afternoon")
    else:
        respond("Good Evening")

def internet_availability():
    try:
        url = "http://google.com/"
        timeout = 2
        _ = requests.get(url, timeout = timeout)
        return True
    except:
        respond("No internet connection!")
        return False

def access():
    respond("Are you confirm in access control transfer!")
    data = listen()
    if data=="confirm":
        respond("could you please say the name of  the person of whom you are going to give access")
        name = listen()
        respond("okay")
        respond("new visual confirmation required!")
        New_access(name)
        respond("access control transferred successfully!")
        return
    else:
        respond("are you sure in cancelling access control transfer!")
        data = listen()
        if data == "yes":
            return
        else:
            access()

def execute_commands():
    try:
        respond("okay sir!")
        respond("please give me the list of instruction to execute")
        a=[]
        while True:
            data = listen()
            if "that's it" in data:
                break
            else:
                a.append(data)
                respond("okay")
        for instruct in a:
            speech="your instruction {} is going to execute sir!".format(instruct)
            respond(speech)
            digital_assistant(instruct)       
    except:
        respond("sorry sir, I think there is a error in your code")
    return

def digital_assistant(data):
    try:
        if "how are you" in data: 
            respond("I am well")
            return
            
        elif "time" in data:      
            respond(ctime())
            return

        elif "who are you" in data or "what can you do" in data or "define yourself" in data:
            respond("I am viswanadh's personal assistant, I am programmed to do minor tasks like system monitoring, profiling,"
            "predict time, take a photo, predict weather,"
            " opening applications like youtube, google chrome ,gmail etcetre, show the top headline news and you can ask me computational or geographical questions too!")
            return

        elif "who made you" in data or "who created you" in data:
            respond("I was built by viswa")
            return

        elif "shutdown" in data:
            respond("Are you sure! you want to shutdown your computer")
            data = listen()
            if data == "yes":
                respond("system is going to shutdown...")
                os.system("taskkill /f /im Rainmeter.exe")
                os.system("shutdown /s /t 1")
                return
        
        elif "restart" in data:
            respond("want to restart your computer")
            data=listen()
            if data=="yes":
                os.system("shutdown /r /t 1")
                return
        
        elif "battery" in data:
            battery=psutil.sensors_battery()
            respond("Your system is at " + str(battery.percent) + " percent")
            return

        elif "cpu" in data:
            respond("CPU is at "+ str(psutil.cpu_percent()))
            return

        elif "music" in data:
            respond("Here you go with music")
            music_dir = "C:\\Users\\VISWANADH\\Music"
            song = random.choice(os.listdir(music_dir))
            os.startfile(os.path.join(music_dir,song))
            time.sleep(5)
            return

        elif "movie" in data:
            os.system("D:\\movies\\Ala_Vaikunthapurramloo.mkv")
            time.sleep(5)
            return
        
        elif "notepad" in data:
            os.system("notepad")
            return

        elif "open" in data:
            data = data.split(" ")
            query = data[1]
            for j in search(query, tld='com', lang='en', num=1, start=0, stop=1, pause=2.0):
                url=j
            webbrowser.get('chrome').open_new(url)
            respond(data[1] + " is open now")
            time.sleep(7)
            return

        elif "news" in data:
            query = "news"
            url="https://timesofindia.indiatimes.com/home/headlines"
            webbrowser.get('chrome').open_new(url)
            respond("Here are some headlines from the Times of India,Happy reading")
            time.sleep(5)
            return
                
        elif "weather" in data:
            data=data.split(" ")
	    #create key: https://home.openweathermap.org/users/sign_in
            api_key = ####################
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            if "in" not in data:
                city_name = "kurupam"
            else:
                city_name = data[-1]
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                respond(" Temperature in kelvin unit at " + city_name + " is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                return
            else:
                respond(city_name + " weather details not found")
                return
        
        elif "something" in data:
            respond("Searching...")
            data=data[22:]
            data =  "According to wikipedia " + wikipedia.summary(data, sentences=4) 
            respond(data)
            return

        elif "capture the photo" in data or "take a photo" in data:
            ec.capture(0,False,"img.jpg")
            respond("photo captured successfully")
            return

        elif "video" in data or "capture the video" in data:
            ec.auto_vidcapture(0,False,"video.mkv",10)
            respond("video recorded successfully")
            return

        elif "access" in data:
            access()
            return
        
        elif "where is" in data:
            data = data.split(" ")
            name = data[-1]
            url = "https://www.google.com/maps/place/"+name
            webbrowser.get('chrome').open_new(url)
            time.sleep(5)
            return

        elif "write a note" in data:
            respond("What should i write, sir!")
            data = listen()
            file = open('note.txt', 'w')
            file.write(data)
            respond("noted successfully")
            return
        
        elif "execute" in data:
            execute_commands()
            return

        elif "upcoming events" in data or "scheduled events" in data or "events" in data:
            events = calendar_events()
            return

        elif "game" in data or "play" in data:
            try:
                tic_tac_toe()
                return
            except:
                return

        elif "create event" in data:
            create_event()
            return
            
        elif "speed test" in data:
            try:
                respond("sure! wait a second to measure")
                st = speedtest.Speedtest()
                server_names = []
                st.get_servers(server_names)
                ping = st.results.ping
                downlink_Mbps = round(st.download() / 1000000, 2)
                uplink_Mbps = round(st.upload() / 1000000, 2)
                respond('ping {} ms'.format(ping))
                respond("The uplink is {} Mbps".format(uplink_Mbps))
                respond("The downlink is {}Mbps".format(downlink_Mbps))
                return
            except:
                respond ("I couldn't run a speedtest")     
                return              
        
        elif "memory" in data:
            process_id = os.getpid()
            py = psutil.Process(process_id)
            memory_use = round(py.memory_info()[0]/2. **30, 2)
            respond("I use {} Gb of memory".format(memory_use))
            return
        
        elif "internet connection" in data or "internet" in data:
            if internet_availability():
                respond("Internet Connection is okay!")
            return
       elif 'email to' in data:
            try:
                respond("Sir, give me your message")
                print('Give message.......')
                content = takeCommand()
                to = "receiver email address"
                sendEmail(to, content)
                print('Sending mail........')
                respond("Email has been sent!")
            except Exception as e:
                print(e)
                respond("Sorry master . I am not able to send this email")

        else:
            respond("I can search the web for you,Do you want to continue?")
            opinion=listen()
            if opinion=="yes":
                url="https://www.google.com/search?q =" + '+'.join(data.split())
                webbrowser.get('chrome').open_new(url)
                time.sleep(5)
                return
            else:
                return
    except:
        respond("I don't understand, I can search the web for you,Do you want to continue?")
        opinion=listen()
        if opinion=="yes":
            url="https://www.google.com/search?q =" + '+'.join(data.split())
            webbrowser.get('chrome').open_new(url)
            time.sleep(5)
            return
        else:
            return

