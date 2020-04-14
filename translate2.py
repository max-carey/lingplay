from google.cloud import translate_v2
# Import the speech recognition library
import speech_recognition as sr

print("Say a word:")

# Create a recognizer
r = sr.Recognizer()

# Create a microphone objec that gets system default
mic = sr.Microphone()

# Liste nfor audio and save it
with mic as source:
    audio = r.listen(source)

# Recognize the speech, turn it into text
text = r.recognize_google(audio)
print(" \n")
print(text)
print(" \n")

language = input("Pick a language \n\nspanish\nthai\ngerman\nturkish\nchinese\njapanese\nkorean\narabic\n")
print(" \n")

language_code_mapping = {'spanish': 'es',
                         'german': 'de',
                         'thai': 'th',
                         'turkish': 'tr',
                         'chinese': 'zh',
                         'japanese': 'ja',
                         'korean': 'ko',
                         'arabic': 'ar'}

languageISO = language_code_mapping[language]


def translate(target_string, target_language):

    # Instantiate a translation object
    translator = translate_v2.Client(target_language=target_language)

    translated_string = translator.translate(target_string)

    print("{0} in {1} is {2}".format(text, language, translated_string['translatedText']))

    return translated_string['translatedText']


translate(text, languageISO)
