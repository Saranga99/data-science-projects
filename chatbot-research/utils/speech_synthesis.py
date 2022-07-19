# importing libraries 
import os 
import speech_recognition as sr 
from gtts import gTTS
from pydub import AudioSegment
from pydub.silence import split_on_silence
import pyttsx3

def text_to_speech(text):
    synthesizer = pyttsx3.init()
    voices = synthesizer.getProperty('voices')
    synthesizer.setProperty('voice', voices[1].id) 
    synthesizer.setProperty('rate', 150)
    print("Speaking...")
    synthesizer.say(text) 
    synthesizer.runAndWait() 
    synthesizer.stop() 

r = sr.Recognizer()

def speech_to_text():
    with sr.Microphone() as source:
        print("Tell me something:")
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        # read the audio data from the default microphone
        audio_data = r.listen(source)
        # audio_data = r.record(source, duration=60)
        print("Recognizing...")
        # convert speech to text        
        text = r.recognize_google(audio_data, language = 'En', show_all=False)
        return text
