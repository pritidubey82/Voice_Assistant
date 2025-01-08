import pyttsx3
import speech_recognition as sr
import eel
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    engine.setProperty('volume',250)
    print(voices)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        eel.DisplayMessage("listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source,10,6)
    try:
        print('Recognizing..')
        eel.DisplayMessage("listening...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")
        eel.DisplayMessage(query)
        speak(query)
        eel.ShowHood()
    except Exception as e:
        return ""
    return query.lower()






  
