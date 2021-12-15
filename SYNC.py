import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon !!")
    else:
        speak("Good Evening!!")

        
    speak("I am SYNC. Please tell me how can i help you")


def takeCommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User Asked: {query}\n")
        speak(f"User Asked: {query}\n")
    
    except Exception as e:
        print(e)
        
        print("Couldn't Recognise it Please Say it again..")
        return "None"
    return query

def sendEmail(to,content):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('samplemail808080@gmail.com', '@SampleMail808080')
    server.sendmail('samplemail808080@gmail.com',to,content)
    server.close()





if __name__ == "__main__":
    
    wishMe()
    
    while True:
        g_path="C://Program Files//Google//Chrome//Application//chrome.exe %s"
        query=takeCommand().lower()
        if 'wikipedia'  in query or 'who is' in query:
            speak('Searching Wikipedia...')
            query= query.replace("wikipedia","")
            query= query.replace("who is","")
            results= wikipedia.summary(query,sentences=2)
            print(f"Search Results for {query}")
            speak(f"Search Results for {query}")
            print(f"According to Wikipedia {results}\n")
            speak(f"According to Wikipedia {results}\n")

        elif 'open youtube' in query:
           g_path="C://Program Files//Google//Chrome//Application//chrome.exe %s"
           webbrowser. get(g_path).open_new("youtube.com")
        elif 'open google' in query:
            webbrowser. get(g_path).open_new("google.com")
        elif 'open whatsapp' in query:
            webbrowser. get(g_path).open_new("https://web.whatsapp.com/")
        elif 'what is' in query or 'search' in query or 'google' in query:
            query= query.replace("search","") 
            query= query.replace("google","") 
            webbrowser. get(g_path).open_new(f"https://www.google.com/search?q={query}")
        elif 'search youtube for' in query or 'youtube' in query:
            query= query.replace("search","") 
            query= query.replace("youtube","") 
            webbrowser. get(g_path).open_new(f"https://www.youtube.com/results?search_query={query}")
        elif 'play music' in query:
            music_dir ='C:\\Users\\Soumen-Riya-Tuku\\Desktop\\music'
            m_length= len(music_dir)
            songs=os.listdir(music_dir)
            music_random=random.randint(0,m_length-1)
            os.startfile((os.path.join(music_dir,songs[music_random])))        
        elif 'time' in query:
            time_str=datetime.now().strftime("%H:%M:%S")
            print(f"The time is : {time_str}")
            speak(f"The time is : {time_str}")
        elif 'send email' in query or 'email' in query:
            try:
                speak("What should i write Sir?")
                content= takeCommand()
                to ="soumen0maji@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent successfully!!")
            except Exception as e:
                print(e)
                speak("can't send this email write now..Please try again later!")
        elif 'goodbye' in query or 'bye' in query or 'exit' in query:
            hour = int(datetime.now().hour)
            if hour>=0 and hour<12:
                speak("Good Bye Sir!!  Have a great day")
                exit()
            elif hour>=12 and hour<18:
                speak("Good Bye Sir!!  Have a great afternoon")
                exit()
            else:
                speak("Good Bye Sir!! , Have a great Evening , Good Night!!")
                exit()
        elif 'random number' in query:
            ran_no= random.randint(0,9999)
            print(f"Ummm a random number, let it be {ran_no}")
            speak(f"Ummm a random number, let it be {ran_no}")
        elif 'open code' in query  or 'open vs code' in query:
            vs_path="C:\\Users\\Soumen-Riya-Tuku\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_path) 