from playsound import playsound
import eel
import os
import re
import sqlite3  # Import sqlite3
import webbrowser  # Import webbrowser
from engine.confi import ASSISTANT_NAME
from engine.command import speak
import pywhatkit as kit  # Import pywhatkit

# Connect to the SQLite database
con = sqlite3.connect('jarvis.db')
cursor = con.cursor()  # Create a cursor object

@eel.expose
def playAssistantSound():
    music_dir = r"C:\Users\Priti\OneDrive\Desktop\jarvis\www\assets\audio\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower()

    app_name = query.strip()

    if app_name != "":
        try:
            # Search in sys_command table
            cursor.execute(
                'SELECT path FROM sys_command WHERE name = ?', (app_name,)
            )
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening " + query)
                os.startfile(results[0][0])

            elif len(results) == 0:
                # Search in web_command table
                cursor.execute(
                    'SELECT url FROM web_command WHERE name = ?', (app_name,)
                )
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening " + query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening " + query)
                    try:
                        os.system('start ' + query)
                    except Exception as e:
                        speak("Not found. Error: " + str(e))
        except Exception as e:
            speak("Something went wrong. Error: " + str(e))

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speak("Playing " + search_term + " on YouTube")
        kit.playonyt(search_term)
    else:
        speak("Could not extract a valid search term for YouTube.")

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None

# Properly close the database connection when done (optional but recommended)
import atexit
@atexit.register
def close_db():
    con.close()
