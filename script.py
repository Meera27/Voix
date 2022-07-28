import smtplib

import speech_recognition as sr
import pyttsx3
import sys

email1=sys.argv[1]
passwo=sys.argv[2]
name = sys.argv[3]

def speak(audio):  
    try:
        tts_engine = pyttsx3.init()
        voices = tts_engine.getProperty('voices')
        for voice in voices:
            print(voice.name)
        print(voices)
        tts_engine.setProperty('voice', voices[0].id)
        tts_engine.say(audio)
        tts_engine.runAndWait()

    except:
        print('error')

def sendmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    try:
        server.login(email1, passwo)
    except:
        speak("Please login with existing credentials or try to sign up a with valid email")
    server.close()
    
if __name__=="__main__" :  
    sendmail()  
    
    