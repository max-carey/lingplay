# Import the speech recognition library
import speech_recognition as sr

# Create a recognizer
r = sr.Recognizer()

# Create a microphone objec that gets system default
mic = sr.Microphone()

# Listen for audio and save it
with mic as source:
    audio = r.listen(source)

GOOGLE_CLOUD_SPEECH_CREDENTIALS = /Users/grahamderry/praxis-road-272622-d0ad9ed1867c.json
try:
    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
