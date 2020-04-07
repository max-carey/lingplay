from google.cloud import translate_v2
#instantiate objects of Client for each language 
spanish = translate_v2.Client(target_language='es')
thai = translate_v2.Client(target_language='th')
german = translate_v2.Client(target_language='de')
turkish = translate_v2.Client(target_language='tr')
chinese = translate_v2.Client(target_language='zh')
japanese = translate_v2.Client(target_language='ja')
korean = translate_v2.Client(target_language='ko')
arabic = translate_v2.Client(target_language='ar')

#get text and target langusge from user
text = input("What word would you like to translate?\n")
language = input("What language would you like to translate into?\nspanish\nthai\ngerman\nturkish\nchinese\njapanese\nkorean\narabic\n")

#print translations
if language == 'spanish':
	print(spanish.translate(text))

if language == 'thai':
	print(thai.translate(text))

if language == 'german':
	print(german.translate(text))

if language == 'turkish':
	print(turkish.translate(text))

if language == 'chinese':
	print(chinese.translate(text))

if language == 'japanese':
	print(japanese.translate(text))

if language == 'korean':
	print(korean.translate(text))

if language == 'arabic':
	print(arabic.translate(text))

