import datetime
import os
import webbrowser
import speech_recognition as sr
import pyttsx3
print("Program Started")
assistant_name="Alla"
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
def greet():
 print(f"Hello! i am {assistant_name}")
greet()

def get_time():
       current_time=datetime.datetime.now()
       formatted_time=current_time.strftime("%H:%M:%S")
       return formatted_time
def get_date():
         current_date=datetime.datetime.now()
         formatted_date=current_date.strftime("%d:%m:%y")
         return formatted_date
print("The current time is:",get_time())
print("The current date is:",get_date())
def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except:
        speak("Sorry, I did not understand.")
        return ""
greet()
speak("Your voice assistant is ready")



while True:

    command = take_command()

    # ---- Greeting ----
    if "hello" in command:
        speak("How are you?")

    # ---- Time ----
    elif "time" in command:
        speak("The current time is " + get_time())

    # ---- Date ----
    elif "date" in command:
        speak("Today's date is " + get_date())

    # ---- Open Notepad ----
    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    # ---- Google Search ----
    elif "search" in command:
        keyword = command.replace("search", "").strip()

        if keyword == "":
            speak("What should I search?")
        else:
            url = "https://www.google.com/search?q=" + keyword
            webbrowser.open(url)
            speak("Searching " + keyword)

    # ---- Exit ----
    elif "stop" in command or "exit" in command:
        speak("Goodbye Laiba!")
        break

    # ---- Unknown ----
    else:
        speak("Sorry, I don't understand this command.")