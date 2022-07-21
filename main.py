import datetime

import pywhatkit
import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import pyjokes
import sys

listener = sr.Recognizer()

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()

engine = pyttsx3.init()
engine.say('Hello friend !')
engine.say("I am your bot   Blanco !")
engine.say("How can i assist you?")
engine.runAndWait()

def user_commands():
    try:
        with sr.Microphone() as source:
            print("Start Speaking!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'blanco' in command:
                command = command.replace('blanco', '')
                print(command)
    except:
        pass
    return command


def run_blanco():
    commands= user_commands()
    if 'play' in commands:
        song= commands.replace('play','')
        engine_talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in commands:
        time= datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current time is '+ time)
    elif 'who is' in commands:
        name= commands.replace('who is','')
        info= wikipedia.summary(name,1)
        print(info)
        engine_talk(info)
    elif 'joke' in commands:
        engine_talk(pyjokes.get_joke())
    elif 'stop' in commands:
        engine_talk('see ya!')
        engine_talk('Have a nice day !')
        sys.exit()
    else:
        engine_talk('I could not understand what you just said.')

while True:
    run_blanco()
