import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import pywhatkit
import pyautogui
import pyjokes
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Hirithik Raj Singh")
        speak("Good Morning Hirithik Raj Singh")
    elif hour>=12 and hour<17:
        print("Good Afternoon Hirithik Raj Singh")
        speak("Good Afternoon Hirithik Raj Singh")
    elif hour>=17 and hour<21:
        print("Good Evening Hirithik Raj Singh")
        speak("Good Evening Hirithik Raj Singh")
    else:
        print("Good Night Hirithik Raj Singh")
        speak("Good Night Hirithik Raj Singh")

def commands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Wait for Few Moments...")
        query=r.recognize_google(audio,language='en-in')
        print(f"You just said: {query}\n")
        
    except Exception as e:
        print(e)
        speak("Please Tell me again")
        query="none"
    return query

def wakeupCommands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis is sleeping...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
    try:
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        query="none"
    return query        

if __name__ == "__main__":
    while True:
        query=wakeupCommands().lower()
        if 'wake up' in query:
            wishings()
            speak("Yes sir what can I do for you!")
            while True:

                query=commands().lower()                 
                if 'ms word' in query:
                    speak("opening ms word Application sir...")
                    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

                elif 'youtube' in query:
                    speak("opening youtube Application sir...")
                    os.startfile("https://www.youtube.com//")
                    pywhatkit.playonyt('arabic kuthu')

                elif 'python' in query:
                    speak("opening python IDLE Application sir ...")
                    os.startfile()

                elif 'whatsapp' in query:
                    speak("opening whatsapp Application sir...")
                    os.startfile("https://web.whatsapp.com//")

                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(strTime)
                    speak(f"Sir,the time is {strTime}")

                elif "mute" in query:
                    speak("I'm muting Sir...")
                    break
                elif 'exit' in query or 'exit program' in query:
                    speak("I,m Leaving Sir, Byeee...")
                    quit()

                elif 'wikipedia' in query:
                    speak("searching in wikipedia...")
                    try:
                        query=query.replace("Wikipedia",'')
                        results = wikipedia.summary(query,sentences=1)
                        speak("According to Wikipedia,")
                        print(results)
                        speak(results)
                    except:
                        speak("NO results found...")
                        print("No results found...")

                elif 'play' in query:
                    playQuery=query.replace('play','')
                    speak('Playing '+ playQuery)
                    pywhatkit.playonyt(playQuery)

                elif 'type'in query:
                    speak("please tell me what should I write")
                    while True:
                        typeQuery = commands()
                        if typeQuery =='exit typing':
                            speak("Done sir")
                            break
                        else:
                            pyautogui.write(typeQuery)

                elif 'minimize' in query or 'minimise' in query:
                    pyautogui.moveTo(1901,17)
                    pyautogui.leftClick()

                elif 'joke' in query:
                    joke=pyjokes.get_joke()
                    print(joke)
                    speak(joke)

                elif 'good' in query:
                    print('thank you sir')
                    speak('thank you sir')

                elif 'exit' in query:
                    speak("I'm leaving sir...")
                    quit()
            



