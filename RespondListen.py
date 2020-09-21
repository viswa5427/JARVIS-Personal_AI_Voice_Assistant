import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def respond(audioString):
    print(audioString)
    engine.say(audioString)
    engine.runAndWait()

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
            data = listen()
        except sr.RequestError as e:
            respond("Request Failed due to network issues")
            data = listen()
        if data!="":
            return data
