import speech_recognition as sr
import datetime
import os
import pyttsx3
import webbrowser
import psutil
import pyjokes
import wikipedia
import time
import requests, json
from time import ctime
from googlesearch import search
from ecapture import ecapture as ec

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
webbrowser.register('chrome',
	            None,
	            webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source)
        data = ""
        try:
            data = r.recognize_google(audio,language='en-in')
            print("You said: " + data)
        except sr.UnknownValueError:
            respond("Pardon me,please say that again")
            return "None"
        except sr.RequestError as e:
            respond("Request Failed due to network issues")
            return "None"
        return data

def respond(audioString):
    print(audioString)
    engine.say(audioString)
    engine.runAndWait()

def wishme():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        respond("Good Morning")
    elif hour>=12 and hour<18:
        respond("Good Afternoon")
    else:
        respond("Good Evening")

def digital_assistant(data):
    try:
        if "how are you" in data:
            respond("I am well")
            return

        elif "time" in data:
            respond(ctime())
            return

        elif "who are you" in data or "what can you do" in data or "define yourself" in data:
            engine.say("I am viswanadh's personal assistant, I am programmed to do minor tasks like system monitoring, profiling,"
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
                os.system("shutdown /s /t 1")
                return
        
        elif "restart" in data:
            respond("want to restart your computer")
            data=listen()
            if data=="yes":
                os.system("shutdown /r /t 1")
                return
        
        elif "battery" in data or "cpu" in data:
            battery=psutil.sensors_battery()
            respond("Battery is at " + str(battery.percent) + " percent")
            return

        elif "cpu" in data:
            respond("CPU is at "+ str(psutil.cpu_percent()))
            return

        elif "music" in data:
            os.system("D:\\music\\RaceGurram\\Down_Down.mp3")
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
            respond(data[1] + "is open now")
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
            city_name = "kurupam"
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
            respond("According to wikipedia")
            respond(wikipedia.summary(data, sentences=4))
            return

        elif "capture the photo" in data or "take a photo" in data:
            ec.capture(0,False,"img.jpg")
            respond("photo captured successfully")
            return

        elif "video" in data or "capture the video" in data:
            ec.auto_vidcapture(0,False,"video.mkv",10)
            respond("video recorded successfully")
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

    
if __name__=="__main__":
    respond("checking remote servers!")
    respond("importing preferences and loading all the system drivers!")
    respond("establish secure connection!")
    os.startfile("c:\\Program files\\Rainmeter\\Rainmeter.exe")
    respond("secure connection established!")
    respond("we are online!")
    respond("welcome back sir!")
    wishme()
    respond("Jarvis is at your service")
    while True:
        respond("Please tell me how can i help you?")
        data = listen().lower()
        if data == 0:
            continue
        if "stop listening" in data or "ok bye" in data or "stop" in data or "exit" in data:
            os.system("taskkill /f /im Rainmeter.exe")
            break
        digital_assistant(data)
        time.sleep(2)