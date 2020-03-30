# Import the speech recognition library
import speech_recognition as sr

# Create a recognizer
r = sr.Recognizer()

# Create a microphone objec that gets system default
mic = sr.Microphone()

# Liste nfor audio and save it
with mic as source:
    audio = r.listen(source)

# Recognize the speech
print(r.recognize_google(audio))
