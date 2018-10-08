'''
Tha main program that read local json file, and implement Google translation API to translate words into target language
'''

import scripts.translation as trans
from google.cloud import translate
import json

# Instantiates a client
translate_client = translate.Client()
trans_res = {}

# Read local json file
with open('translations.json') as translation_file:
    translation_content = json.load(translation_file)

# Implement translation function
for target, content in translation_content.items():
    trans_res[target] = {}
    for text, trans_content in content.items():
        if trans_content != '':
            trans_res[target][text] = trans_content
            continue
        try:
            res = trans.translation(translate_client, text, target.split('-')[0])
        except Exception:
            print('Error occurs while attempting to translate')
            print(Exception)
            break
        res = json.loads(res)
        trans_res[target][text] = res['translatedText']

# Write translation result into new json file
with open('translations_after.json', 'w') as outfile:
    json.dump(trans_res, outfile, index=4)

