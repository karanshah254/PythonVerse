import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis. How can I help you?")


def takeCommand():
    """
    It takes microphone input from the user and returns string output
    """

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "yourpassword-here")
    server.sendmail("youremail@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            speak("Opening Youtube...")
            webbrowser.open("youtube.com")
        elif "open google" in query:
            speak("Opening Google...")
            webbrowser.open("google.com")
        elif "open github" in query:
            speak("Opening Github...")
            webbrowser.open("github.com")
        elif "stackoverflow" in query:
            speak("Opening Stackoverflow...")
            webbrowser.open("stackoverflow.com")
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "open code" in query:
            speak("Opening VS Code...")
            path = "C:\\Users\\Karan Shah\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif "email to John" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "johnbanegadon@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email.")
        elif "I am done with you Jarvis" in query:
            speak("Thank you for using me!")
            exit()
        else:
            speak("I am sorry, I don't understand that.")
