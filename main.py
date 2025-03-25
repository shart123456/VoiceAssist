import os
import speech_recognition as sr
import webbrowser

recognizer = sr.Recognizer()
MIC_INDEX = 5  # USB Audio MIC

def listen_and_execute():
    with sr.Microphone(device_index=MIC_INDEX) as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized: {command}")

        if "open chrome" in command:
            os.system("google-chrome &")
        elif "open firefox" in command:
            os.system("firefox &")
        elif "open terminal" in command:
            os.system("gnome-terminal &")
        elif "exit" in command or "quit" in command:
            print("Exiting...")
            return False  # Stop listening
        elif "open cherry notes" in command or "open the tree" in command:
            os.system("cherrytree &")
        elif "search google for" in command:
            search_query = command.replace("search google for", "").strip()
            if search_query:
                print(f"Searching Google for: {search_query}")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            else:
                print("No search query detected.")

    except sr.UnknownValueError:
        print("Could not understand the command.")
    except sr.RequestError:
        print("Could not request results from Google API.")
    
    return True  # Continue listening

# Loop to keep listening until 'exit' is spoken
while True:
    if not listen_and_execute():
        break
