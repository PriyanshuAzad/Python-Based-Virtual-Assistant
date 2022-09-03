from ast import Lambda
from cProfile import run
from distutils.log import info
from pickle import TRUE
import webbrowser
from click import command
from django.template import engines
import regex
from soupsieve import match
import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import pyjokes
import re




listner = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate', 170)

def talk(text):
    engine.say(text)
    engine.runAndWait()




def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...') 
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass
    
    return command



def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)

    elif 'search' in command:
        person = command.replace('search', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'google search' in command:
        talk('This is what I found for your search sir!')
        person = command.replace('google search', '')
        google_search = pywhatkit.search(command)
        print(google_search)
        talk(google_search)

    elif 'website' in command:
        talk('Ok Sir, Launching....')
        replace = {"open": "", "website":"", " ": ""}
        regex = re.sub("|".join(replace.keys()), lambda match: replace[match.string[match.start():match.end()]], command)
        print(regex)
        site1 ='https://www.'
        site2 ='.com'
        web1 = site1+regex+site2
        web_search = webbrowser.open(web1)
        print(web1)
      
    elif 'alarm' in command:
        talk("Enter the time !")
        time = input(": Enter the time :")
        while True:
            Time_Ac = datetime.datetime.now()
            now = Time_Ac.strftime("%H:%M:%S")

            if now == time:
                talk("Time to wake up sir!")
                talk("Alarm Closed!")
            elif now>time:
                break


    else:
        talk('Please say the command again')

while TRUE:
    run_alexa()


