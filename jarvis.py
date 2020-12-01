import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning manas sir")
    elif hour>=12 and hour<18:
        speak("Good afternoon manas sir")
    else:
        speak("Good evening manas sir")
    speak("i am jarvis sir. Please tell me how may i help you.")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == '__main__':
    wishme()
    while True:
       query = takecommand().lower()
       if 'wikipedia' in query:
           speak("searching wikipedia...")
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=3)
           speak("according to wikipedia")
           print(results)
           speak(results)
       elif 'open youtube' in query:
           speak("ok sir opening youtube")
           webbrowser.open("youtube.com")
       elif 'open google' in query:
           speak("opening google")
           webbrowser.open("https://www.google.com/")
       elif 'open github' in query:
           speak("opening github")
           webbrowser.open("https://github.com/ManasVerma1357?tab=repositories")
       elif 'open instagram' in query:
           speak("i think its your time for chill so as your wish i am opening instagram")
           webbrowser.open("https://www.instagram.com/")
       elif 'open whatsapp' in query:
           speak("yes sir, opening whatsapp for you")
           webbrowser.open("https://web.whatsapp.com/")
       elif 'the time' in query:
           strtime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"sir, the time is {strtime}")
       elif 'open pycharm' in query:
           pycharmpath = "C:\\pycharm\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe"
           os.startfile(pycharmpath)
       elif 'open spotify' in query:
           speak("ok sir opening spotify")
           spotifypath = "C:\\Users\\Admin\\AppData\\Roaming\\Spotify\\Spotify.exe"
           os.startfile(spotifypath)
       elif 'cortana' in query:
           speak("everyone was gangsta until i was not there")
       elif 'joke' in query:
           joke=pyjokes.get_joke(language='en', category='neutral')
           print(joke)
           speak(joke)
       elif 'open visual studio code' in query:
           speak("yes sir i am opening visual studio code")
           vspath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(vspath)
       elif 'how are you' in query:
           speak("i am fine sir.")
       elif 'times of india' in query:
           speak("opening times of india website")
           webbrowser.open("https://timesofindia.indiatimes.com/defaultinterstitial.cms")
       elif 'pranam' in query:
           speak("namashkar sir")
       elif 'exit' in query:
           speak("Bye sir i wish that i had helped you alot")
           quit()

