 import tkinter as tk


# root.geometry("488x243")
def mk():
    print("manish kumawat")
    import pyttsx3
    import speech_recognition as sr
    import datetime
    import wikipedia
    import webbrowser

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[0].id)
    engine.setProperty('voice', voices[1].id)


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon!")
        else:
            speak("Good Evening!")

        speak("I am Jarvis Sir. Please tell me how may I help you")        

    def takeCommand():
        # it take microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            
            audio = r.listen(source)
            

        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n") 

        except Exception as e:
            print(e)

            print("Say that again please...")
            return "None"
        return query
        

    if __name__ == "__main__":
        wishMe()
        #  takeCommand()
        while True:
            query = takeCommand().lower()


        # logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences = 2)
                speak("According to Wikipedia")
                speak(results)
                print(results)
            elif "open youtube" in query:
                webbrowser.open("youtube.com")

            elif "open google" in query:
                webbrowser.open("google.com")

            elif "open youtube" in query:
                webbrowser.open("youtube.com")

            elif "open youtube" in query:
                webbrowser.open("youtube.com")   



 

def on_button_click():
    print("Button was clicked!")
    mk()

# Create the main application window
root = tk.Tk()
root.title("Tkinter Button Example")



# Create a Button widget
button = tk.Button(root, text="Click Me", command=on_button_click)

# Pack the button into the window
button.pack(pady=20)

# Run the application
root.mainloop()


 