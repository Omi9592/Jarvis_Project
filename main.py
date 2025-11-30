import speech_recognition as sr
import webbrowser
import pyttsx3


# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()
    print("Command:", c)

    if "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open whatsapp" in c:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")

    elif "open gmail" in c:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    elif "open instagram" in c:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "open linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    
    elif "open github" in c:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
    

    elif "what is the time" in c:
        from datetime import datetime
        speak(f"The time is {datetime.now().strftime('%I:%M %p')}")

    else:
        speak("I did not understand that command.")

if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:

        #listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
         # recognize speech using google
        print("Recognizing ......")
        try:
            with sr.Microphone() as source:
                print("Listening ......")
                audio = r.listen(source , timeout=2 , phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("Yes Sir, I am listening")
                print("Listening for command ......")
                with sr.Microphone() as source:
                    audio = r.listen(source , timeout=5 , phrase_time_limit=5)
                command = r.recognize_google(audio)
                print("You said: " + command)

                # Process command
                processCommand(command)
                
        except Exception as e:
            print("error; {0}".format(e))
