from google.cloud import translate_v2

##get text and target langusge from user
text = input("What word would you like to translate?\n")
language = input("What language would you like to translate into?\nspanish\nthai\ngerman\nturkish\nchinese\njapanese\nkorean\narabic\n")


language_code_mapping = {'spanish': 'es',
                         'german': 'de'}

language = language_code_mapping[language]


def translate(target_string, target_language):

    # Instantiate a translation object
    translator = translate_v2.Client(target_language=target_language)

    translated_string = translator.translate(target_string)

    print(translated_string['translatedText'])

    return translated_string['translatedText']


translate(text, language)
