import pyttsx3
import time
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import playsound

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  ## You can print the voice too

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def cointoss():
    print("The coin is about to toss")
    playsound.playsound('toss.mpeg')
    rand = random.randint(0, 1)
    if rand == 1:
        print("HEADS!!!!")
        speak("Its Heads!!!")
    else:
        print("TAILS!!!")
        speak("Its Tails")

def jokes():
    jokes1=["Why do bees have sticky hair? ","What did one wall say to the other wall?","What animal needs to wear a wig?","What do you call an alligator in a vest?","Where do fish keep their money?","What has hands but can’t clap?","What kind of room doesn’t have doors?","What do you call the horse that lives next door?","What kind of shoes do ninjas wear?","Why did the picture go to jail?","Why did the banker quit his job?","What did the baby corn say to the mama corn?","Which programming language is the shortest?","What is a developer’s favorite country song?","Why was nobody given food at the developer conference?","Why was the computer freezing?"]
    
    jokes2=["Because, They use honey combs!","I'll meet you at the corner!","A bald eagle!","An investigator!","In the river bank!","A clock!","A mushroom!","Your neighbor!","Sneakers!","Because it was framed","Because, He lost interest!","Where is popcorn?","HTML. Because it doesn’t have a neck between its head and body.","Hello World — by Lady Antebellum","It was a serverless function!","It left its Windows open!"]
    jk=random.randint(0,16)
    first = jokes1[jk]
    print(first)
    speak(first)
    time.sleep(2)
    second = jokes2[jk]
    print(second)
    speak(second)
    playsound.playsound('laughcrowd2.mp3')

def calculation():
    speak("What you want to do")
    calci= listen().lower()
    speak("What is the first number?")
    fnum= listen().lower()
    speak("What is the second number?")
    snum= listen().lower()
    if calci == 'addition':
        result= int(fnum) + int(snum)
        print(f"The sum of {fnum} and {snum} is {result}")
        speak(f"The sum of {fnum} and {snum} is {result}")
    elif calci == 'subtraction':
        result= int(fnum) - int(snum)
        print(f"The difference of {fnum} and {snum} is {result}")
        speak(f"The difference of {fnum} and {snum} is {result}")
    elif calci == 'multiplication':
        result= int(fnum) * int(snum)
        print(f"The product of {fnum} and {snum} is {result}")
        speak(f"The product of {fnum} and {snum} is {result}")
    elif calci == 'division':
        if snum == '0':
            speak("Sorry! but you can't divide any thing by zero")
        else:
            result= int(fnum) / int(snum)
            print(f"The quotient of {fnum} and {snum} is {result}")
            speak(f"The quotient of {fnum} and {snum} is {result}")
    elif calci == 'quit':
        return 1
    else:
        speak("There is problem in input, Please try again")
        calculation()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening")
    speak("I am Max. How can I Help you?")

def listen():
    '''This will take input from microphone and give output as string'''
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening........")
        r.energy_threshold=40000
        r.pause_threshold = 1
        audio =r.listen(source)
        
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio)
        print("User said: ",query,"\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None123"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = listen().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences =2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            speak("opening facebook")
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.open("instagram.com")
        
        elif 'play music' in query or 'play a song' in query:
            music_list='D:\\My Folder\\tones'
            songs=os.listdir(music_list)
            length= len(songs)
            choice= random.randint(0,length-1)
            print("Songs")
            os.startfile(os.path.join(music_list,songs[choice]))
        elif 'the time' in query:
            timestr=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time right now is {timestr}")
        
        elif 'open code' in query:
            speak("opening V S Code")
            vspath = "C:\\Users\\AMAAN KHAN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vspath)
        elif 'send email' in query:
            speak("opening gmail")
            webbrowser.open("gmail.com")
        elif 'thank you' in query:
            speak("Quitting Max")
            speak("It was my pleasure to help you")
            exit()
        elif 'joke' in query:
            jokes()

        elif 'toss a coin' in query:
            cointoss()
        
        elif 'calculation' in query:
            calculation()       
     
        elif 'hi' in query:
            speak("Hi sir. How can I help you?")
        elif 'hello' in query:
            speak("Hello sir. How can I help you?")
        elif 'hey' in query:
            speak("Hey there. How can I help you?")
        
        elif 'who is your boss' in query:
            speak("Amaan sir made me. So he is my boss though")

        elif 'none123' in query:
            continue
        
        elif 'zero divided by zero' in query:
            print("Well no one have discovered it yet, maybe you will be the one who will find it out")
            speak("Well no one have discovered it yet, maybe you will be the one who will find it out")

        else:
            webbrowser.open(query)