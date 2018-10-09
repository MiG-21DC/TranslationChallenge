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

trans_res = {}
for target, content in translation_content.items():
    trans = Translations(translate_client, target, content)
    trans_res.update(trans.translated_content)
# # Implement translation function
# for target, content in translation_content.items():
#     trans_res[target] = {}
#     for text, trans_content in content.items():
#         if trans_content != '':
#             trans_res[target][text] = trans_content
#             continue
#         try:
#             res = trans.translation(translate_client, text, target.split('-')[0])
#         except Exception:
#             print('Error occurs while attempting to translate')
#             print(Exception)
#             break
#         trans_res[target][text] = res

# Implement translation function with Translation object


# Write translation result into new json file
with open('translations_after.json', 'w') as outfile:
    json.dump(trans_res, outfile, indent=4)

