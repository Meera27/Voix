import pyttsx3
import datetime
import webbrowser
import os
import smtplib
import imaplib
import email
import requests
import sys
from email.header import decode_header

e_mail=sys.argv[1]
passw=sys.argv[2]
    
def wishme():
   hour = datetime.datetime.now()
   x=int(hour.strftime("%H"))
   print(hour)
   if x>=0 and x<12:
        speak("Good Morning!")    
    
   elif x==12 and x<18:
        speak("Good Afternoon!")       
    
   else:
        speak("Good Evening!")
        
        #input('Press enter to exit.')
   speak("To send an email please say Sent")
   speak("to read an email say Read")
   speak("To exit please say stop")
   speak('Please tell me how may I help you')

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
        hour = datetime.datetime.now()
        x=hour.strftime("%H")
       # print(x)
       
    except:
        print('error')
        
if __name__=="__main__" :    
    speak('Welcome')
    speak('I am voiz')
    speak('Your Artificial Intelligence Assistant')
    speak('i will be telling you some commands that will make your journey with me more easier')
    speak('Send command will help you to send emails using me')
    speak('Read command will help you to read emails')
    speak('Search Command will help you to search for emails in the inbox')
    speak('Stop Command will help you to exit. please note that when stop command is used you will exit the assistant and will need to login again')    

import speech_recognition as sr

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(e_mail,passw)
    server.sendmail(e_mail, to, content)
    server.close()
    
def getGmailUnread():
    SMTP_PORT = 993
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com" )
        mail.login(e_mail,passw)
        mail.select('inbox')
        data = mail.search(None,'UNSEEN')
        mail_ids = data[1]
        id_list = mail_ids[0].split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,latest_email_id-3, -1):
            data = mail.fetch(str(i), '(RFC822)' )
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1],'utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from + '\n')
                    speak(email_from)
                    print('Subject : ' + email_subject + '\n')
                    speak(email_subject)

    except Exception as e:
           traceback.print_exc() 
           print(str(e))

    
def get_sendmail():
  SMTP_PORT = 993
  try:
      mail = imaplib.IMAP4_SSL("imap.gmail.com" )
      mail.login(e_mail,passw)
      mail.select('"[Gmail]/Sent Mail"',readonly=True)
      data = mail.search(None,'All')
      mail_ids = data[1]
      id_list = mail_ids[0].split()   
      first_email_id = int(id_list[0])
      latest_email_id = int(id_list[-1])

      for i in range(latest_email_id,latest_email_id-5, -1):
          data = mail.fetch(str(i), '(RFC822)' )
          for response_part in data:
              arr = response_part[0]
              if isinstance(arr, tuple):
                  msg = email.message_from_string(str(arr[1],'utf-8'))
                  email_subject = msg['subject']
                  email_from = msg['from']
                  email_to = msg['to']  
                  print('From : ' + email_from + '\n')
                  speak(email_from)
                  print('To : ' + email_to + '\n')
                  speak(email_to)
                  print('Subject : ' + email_subject + '\n')
                  speak(email_subject)

  except Exception as e:
         traceback.print_exc() 
         print(str(e))


def search():
    SMTP_PORT = 993
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com" )
        mail.login(e_mail,passw)
        mail.select('inbox')
        speak("Whose mail should I search")
        receiver=takeCommand()
        print(receiver)
        #b=receiver.replace(" ","")
        speak("What is the subject of the email")
        take=takeCommand()
        data = mail.search(None,'From','"{}"'.format(receiver), 'SUBJECT','"{}"'.format(take))
        mail_ids = data[1]
        id_list = mail_ids[0].split()   
        # first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,latest_email_id-1, -1):
            data = mail.fetch(str(i), '(RFC822)' )
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1],'utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from + '\n')
                    speak(email_from)
                    print('Subject : ' + email_subject + '\n')
                    speak(email_subject)

    except Exception as e:
           traceback.print_exc() 
           print(str(e))






                
def takeCommand():
    #It takes microphone input from the user and returns string output    
     r = sr.Recognizer()
     microphone=sr.Microphone()
     with sr.Microphone() as source:
         r.adjust_for_ambient_noise(source)
         print("Listening...")
         speak("Listening...")
         r.pause_threshold = 1.4
         audio = r.listen(source)
         
     try:
            print("Recognizing...")  
            speak("Recognizing...")  
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            print(f"User said: {query}\n")  #User query will be printed.    
     except Exception as e:
            # print(e)  use only if you want to print the error!
            print("Say that again please...")   #Say that again will be printed in case of improper voice 
            return "None" #None string will be returned
     return query

if __name__ == "__main__":
    # wishme()
    while True:
        query = takeCommand().lower()   
        if 'wikipedia' in query: 
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'sent' in query:
            try:
                speak("Say gmail for gmail accounts or college for College Accounts")
                ss=takeCommand()
                if ss=="Gmail" or ss=="gmail":
                    de="@gmail.com"
                    speak("Whom should I sent")
                    receiver=takeCommand()
                    b=receiver.replace(" ","")
                    print(b)
                    org=b+de
                    speak("What should I say?")
                    content = takeCommand()
                    sendEmail(org, content)
                    speak("Email has been sent!")
                if ss=="college" or ss=="College" :
                    re="@cs.ajce.in"
                    speak("Whom should I sent")
                    receiver=takeCommand()
                    b=receiver.replace(" ","")
                    print(b)
                    org=b+re
                    speak("What should I say?")
                    content = takeCommand()
                    sendEmail(org, content)
                    speak("Email has been sent!")         
            except Exception as e:
                    print(e)
                    speak("Sorry sir. I couldn't find the specified email")
        elif 'read' in query:
            try:
                speak("What would you like me to read?")
                speak("Say inbox for inbox and sent mails for sent mails")
                s=takeCommand()
                if s=="inbox":
                    getGmailUnread()
                elif s=="sent mails":
                    get_sendmail()
            except Exception as e:
                    print(e)
        elif 'stop' in query:
                speak("stopping the assistant")
                exit()
        elif 'search' in query:
                search()