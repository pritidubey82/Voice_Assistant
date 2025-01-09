from playsound import playsound
import eel
import os
import re
from engine.confi import ASSISTANT_NAME
from engine.command import speak 
import pywhatkit  as kit # Import the speak function

@eel.expose
def playAssistantSound():
    music_dir = r"C:\Users\Priti\OneDrive\Desktop\jarvis\www\assets\audio\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, " ")
    query = query.replace("open", "").strip().lower()

    if query:
        speak("Opening " + query)
        os.system('start ' + query)
    else:
        speak("Command not recognized")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    pattern=r'play\s+(.*?)\s+on\s+youtube'
    match=re.search(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None

