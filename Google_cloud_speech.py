# Import the speech recognition library
import speech_recognition as sr
#import os


#read environment variables
#GOOGLE_CLOUD_SPEECH_CREDENTIALS = os.environ['GOOGLE_CLOUD_SPEECH_CREDENTIALS']
#print(GOOGLE_CLOUD_SPEECH_CREDENTIALS)
# Create a recognizer
r = sr.Recognizer()

# Create a microphone objec that gets system default
mic = sr.Microphone()

# Listen for audio and save it
with mic as source:
    audio = r.listen(source)


try:
    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
