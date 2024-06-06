# Set up speech recognition
r = str.Recognizer()
with str.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)
# Initialize text-to-speech engine
engine = pyttsx3.init()
# Set up wake-up keyword
wake_word = "Jarvis"
# Define function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()
# Define function for opening a website
def open_website(url):
      webbrowser.open(url)
    speak("Opening website.")
    # Define function for telling the time
def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}.")
# Check if wake-up keyword is detected
if wake_word in r.recognize_google(audio):
    speak("Yes sir?")
    
    # Listen for command
    with str.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        # Convert speech to text
        command = r.recognize_google(audio)
        print("You said: " + command)
        
        # Execute command
        if "open" in command:
            if "website" in command:
                url = command.split()[-1]
                open_website(url)
            else:
                speak("I'm not sure what you want me to open.")
        elif "time" in command:
            tell_time()
        else:
            speak("I'm sorry, I didn't understand that.")
            
    except str.UnknownValueError:
        speak("I'm sorry, I didn't understand that.")
    except str.RequestError as e:
        speak("Sorry, I couldn't reach the Google servers. Check your internet # Define function for telling the time")
def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}.")
# Check if wake-up keyword is detected
if wake_word in r.recognize_google(audio):
    speak("Yes sir?")
    
    # Listen for command
    with str.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        # Convert speech to text
        command = r.recognize_google(audio)
        print("You said: " + command)
        
        # Execute command
        if "open" in command:
            if "website" in command:
                url = command.split()[-1]
                open_website(url)
            else:
                speak("I'm not sure what you want me to open.")
        elif "time" in command:
            tell_time()
        else:
            speak("I'm sorry, I didn't understand that.")
            
    except str.UnknownValueError:
        speak("I'm sorry, I didn't understand that.")
    except str.RequestError as e:
        speak("Sorry, I couldn't reach the Google servers. Check your internet # Define function for telling the time")
def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}.")
# Check if wake-up keyword is detected
if wake_word in r.recognize_google(audio):
    speak("Yes sir?")
    
    # Listen for command
    with str.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        # Convert speech to text
        command = r.recognize_google(audio)
        print("You said: " + command)
        
        # Execute command
        if "open" in command:
            if "website" in command:
                url = command.split()[-1]
                open_website(url)
            else:
                speak("I'm not sure what you want me to open.")
        elif "time" in command:
            tell_time()
        else:
            speak("I'm sorry, I didn't understand that.")
            
    except str.UnknownValueError:
        speak("I'm sorry, I didn't understand that.")
    except str.RequestError as e:
        speak("Sorry, I couldn't reach the Google servers. Check your internet # Define function for telling the time")
def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}.")
# Check if wake-up keyword is detected
if wake_word in r.recognize_google(audio):
    speak("Yes sir?")
    
    # Listen for command
    with str.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        # Convert speech to text
        command = r.recognize_google(audio)
        print("You said: " + command)
        
        # Execute command
        if "open" in command:
            if "website" in command:
                url = command.split()[-1]
                open_website(url)
            else:
                speak("I'm not sure what you want me to open.")
        elif "time" in command:
            tell_time()
        else:
            speak("I'm sorry, I didn't understand that.")
            
    except str.UnknownValueError:
        speak("I'm sorry, I didn't understand that.")
    except str.RequestError as e:
        speak("Sorry, I couldn't reach the Google servers. Check your internet # Define function for telling the time")
def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}.")
# Check if wake-up keyword is detected
if wake_word in r.recognize_google(audio):
    speak("Yes sir?")
    
    # Listen for command
    with str.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        # Convert speech to text
        command = r.recognize_google(audio)
        print("You said: " + command)
        
        # Execute command
        if "open" in command:
            if "website" in command:
                url = command.split()[-1]
                open_website(url)
            else:
                speak("I'm not sure what you want me to open.")
        elif "time" in command:
            tell_time()
        else:
            speak("I'm sorry, I didn't understand that.")
            
    except str.UnknownValueError:
        speak("I'm sorry, I didn't understand that.")
    except str.RequestError as e:
        speak("Sorry, I couldn't reach the Google servers. Check your internet# Define function for telling the time")
def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}.")
# Check if wake-up keyword is detected
if wake_word in r.recognize_google(audio):
    speak("Yes sir?")
    
    # Listen for command
    with str.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        # Convert speech to text
        command = r.recognize_google(audio)
        print("You said: " + command)
        
        # Execute command
        if "open" in command:
            if "website" in command:
                url = command.split()[-1]
                open_website(url)
            else:
                speak("I'm not sure what you want me to open.")
        elif "time" in command:
            tell_time()
        else:
            speak("I'm sorry, I didn't understand that.")
            
    except str.UnknownValueError:
        speak("I'm sorry, I didn't understand that.")
    except str.RequestError as e:
        speak("Sorry, I couldn't reach the Google servers. Check your internet connection.") 
        