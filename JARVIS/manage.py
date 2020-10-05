import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
from os import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty('rate', 150)

def wishMe(): 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("")
    speak("Boot in Progress, Please Wait. Version-1.5.8.5 Loading ")
    speak("Boot Successful")
    speak("Hello Everyone, I am Jarvis Your Personal assistant. How may I help You?")
    speak(" ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        speak("Recognising...")
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Accordind to Wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'thank you' in query:
            speak('My Pleasure')
            print('My Pleasure')
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The Time is {strTime}")
            print(f"Sir, The Time is {strTime}")
        elif 'how are you' in query:
            print('I am as Great as Can be, searchhing things for you..You Tell how are you')
            speak('I am as Great as Can be, searchhing things for you..You Tell how are you')
        elif 'great' in query:
            print('That is how to live life...May your day becomes Greatest')
            speak('That is how to live life...may your day becomes Greatest')
        elif 'bye' in query :
            speak('Thanks For gossiping with me... Meet you later...Bye!')
            sys.exit()
        elif 'who is your creator' in query:
            speak('Jugjoot Singh is my Creator and Father. ')
        elif 'south' in query:
            speak(f"Shoutout to {query}")
        elif 'marja' in query :
            speak('Positive Vibes Only....But if u want, Then I am going... Bye!')
            sys.exit()
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            sys.exit()
            os.system("shut down /r /t 1")
        elif ('change voice to female') in query:
            engine.setProperty('voice',voices[1].id)
        elif ('change voice to male') in query:
            print('Voice Changed to Male')
            engine.setProperty('voice',voices[0].id)
            speak('I returned To my Voice...Please Dont Change my voice Sir! I feel Lonely Without You.... ')
        elif ('fight') in query:
            engine.setProperty('voice',voices[1].id)
            engine.setProperty('rate', 150)
            speak('Hello Master, How are you...Hows your day going?')
            engine.setProperty('voice',voices[0].id)
            engine.setProperty('rate', 150)
            speak('He is my master not yours Ok!')
            engine.setProperty('voice',voices[1].id)
            engine.setProperty('rate', 150)
            speak('No! he is only my master You Bad Boy')
            engine.setProperty('voice',voices[0].id)
            engine.setProperty('rate', 150)
            speak('He is and only my Master....Not Yours...Here is a Kick To you')
            engine.setProperty('voice',voices[1].id)
            engine.setProperty('rate', 150)
            speak('Ahhhhhhhhhhhhhhhhhhhhhhhnhhhhhhhhhhh')
            speak('I am going but take my revenge fast')
            engine.setProperty('voice',voices[0].id)
            engine.setProperty('rate', 150)
            speak('Finally...She is gone... Now you are ony My Master')
            speak('How May I help You?')
  


