import datetime
import os, random
import webbrowser
import psutil
import pyjokes
import wikipedia
import time
import requests, json
from time import ctime
from RespondListen import respond, listen
from googlesearch import search
from ecapture import ecapture as ec
from camera import New_access
from api import calendar, create_event
import time
from tictactoe import tic_tac_toe


webbrowser.register('chrome',
	            None,
	            webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))




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
        
        elif "jarvis" in data:    
            respond("Yes Sir!")
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
        
        elif "joke" in data:
            respond(pyjokes.get_joke)
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
            api_key = "c046999b657d072a1dd2d413fd4dd156"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            respond("City name")
            city_name = listen()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                respond(" Temperature in kelvin unit is " +
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
            events = calendar()
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

