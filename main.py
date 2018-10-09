'''
Tha main program that read local json file, and implement Google translation API to translate words into target language
'''

# import scripts.translation as trans
from scripts.translation import Translations
from google.cloud import translate
import json

# Instantiates a client
translate_client = translate.Client()
trans_res = {}


# Read local json file
with open('translations.json') as translation_file:
    translation_content = json.load(translation_file)

# Implement translation function with Translation object
for target, content in translation_content.items():
    trans = Translations(translate_client, target, content)
    trans_res.update(trans.translated_content)

# Write translation result into new json file
with open('translations_after.json', 'w') as outfile:
    json.dump(trans_res, outfile, indent=4)

