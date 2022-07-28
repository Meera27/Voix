import smtplib
import speech_recognition as sr
import pyttsx3
import sys


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
    
if __name__=="__main__" :  
    speak("Account Already Exist. Please Login")
