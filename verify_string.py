#SUMMARY 
#Verify correct pronounciation by comparing transcription of audio in target language with target string 
#STEPS
# 1 Takes string from user in English 
# 2 Takes desired target language from user
# 3 Translates the string into target language
# 4 Takes audio from user 
# 5 Compares user audio with translation of target string 

from google.cloud import translate_v2
# Import the speech recognition library
import speech_recognition as sr

#promt user for a word
text = input("Write a word in English:\n")
#promt user to select a language
language = input("\nPick a language\n\nspanish\nthai\ngerman\nturkish\nchinese\njapanese\nkorean\narabic\n\n")


#transate function requires language in ISO code format 
language_code_mapping_ISO = {'spanish': 'es',
                         'german': 'de',
                         'thai': 'th',
                         'turkish': 'tr',
                         'chinese': 'zh',
                         'japanese': 'ja',
                         'korean': 'ko',
                         'arabic': 'ar'}

language_ISO = language_code_mapping_ISO[language]

#get_string function requires language in IETF format 
#IETF language codes allow for regional varients of languages
language_code_mapping_IETF = {'spanish': 'es-MX',
                         'german': 'de-DE',
                         'thai': 'th-TH',
                         'turkish': 'tr-TR',
                         'chinese': 'zh(cmn-hans-cn)',
                         'japanese': 'ja-JP',
                         'korean': 'ko-KR',
                         'arabic': 'ar-EG'}
language_IETF = language_code_mapping_IETF[language]

#take user input and translate into target language
def translate(target_string, target_language):

    # Instantiate a translation object
    translator = translate_v2.Client(target_language=target_language)

    translated_string = translator.translate(target_string)

    #print("{0} in {1} is {2}".format(text, language, translated_string['translatedText']))

    return translated_string['translatedText']

#transcribes audio from user in target langugage
def get_string(language_IETF):
	# Create a recognizer
    r = sr.Recognizer()

	# Create a microphone objec that gets system default
    mic = sr.Microphone()

	# Liste nfor audio and save it
    with mic as source:
	    audio = r.listen(source)

	# Recognize the speech
    transcribed_string = r.recognize_google(audio, language = language_IETF)
    #print(transcribed_string)
    return transcribed_string

translation = translate(text, language_ISO)
print("\n'{0}'' in {1} is '{2}'".format(text, language, translation))

print("\nSay '{0}':\n".format(translation))
target_string = get_string(language_IETF)

if translate(text, language_ISO) == target_string:
	print("Great job! You pronounced '{0}'' correctly in {1}\n".format(text, language))
else:
	print("You said '{0}'. We expected '{1}'\n".format(target_string, translation))


