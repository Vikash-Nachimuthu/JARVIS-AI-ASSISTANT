import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("INITIALIZING JARVIS...")

MASTER="VIKASH"

engine=pyttsx3.init('vicky')
voices=engine.getproperty('voices')
engine.setProperty('voice',voices[0].id)

#speak function to speak
def speak(audio):
    engine.say(audio)
    engine.run()

def wish():
    hour=int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour<12:
        print("Good morning " + MASTER)
    elif  hour>=12 and hour<18:
        print("Good afternoon " + MASTER)
    else:
        print("Good Evening " + MASTER)

def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
    try:
        print("Recoginizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said :{query}\n")
    except Exception as e:
        print("say that again please")
        query=None
    return query    

def email(to,content):
    server=smtplib.smtp('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('vikash34817@gmail.com','vikash056')
    server.sendmail('vikash.n2019it@sece.ac.in',to,content)
    server.close()

speak("INITIALIZING JARVIS...")

def main():
    wish()
    query=command()  
    if 'wikipedia' in query.lower():
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
    elif 'open youtube' in query.lower():
            webbrowser.open("youtube.com")
    elif 'open google' in query.lower():
            webbrowser.open("google.com")
    elif 'the time' in query.lower():
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{MASTER} the time is {strtime}")
    elif 'open code' in query.lower():
            codepath="C:\\Users\\kavi priyan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
    elif 'email to vikash'  in query.lower():
            try:
                speak("what should i send")
                content=command()
                to="abisheka409@gmail.com"
                email(to,content)
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)        

main()
    


