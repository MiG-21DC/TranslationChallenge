import urllib3
import json
import scripts.translation as trans
from google.cloud import translate
import json

translate_client = translate.Client()

with open('translations.json') as translation_file:
    translation_content = json.load(translation_file)

trans_res = {}
for target, content in translation_content.items():
    trans_res[target] = {}
    for text, trans_content in content.items():
        if trans_content != '':
            trans_res[target][text] = trans_content
            continue
        res = trans.translation(translate_client, text, target.split('-')[0])
        trans_res[target][text] = res['translatedText']

with open('translations_after.json', 'w') as outfile:
    json.dump(trans_res, outfile)

# http = urllib3.PoolManager()
#
# data = {'q': 'Address', 'target': 'de', }
# encoded_data = json.dumps(data).encode('utf-8')
# r = http.request('POST', 'https://translation.googleapis.com/language/translate/v2', body=encoded_data)
#
# print(json.loads(r.data.decode('utf-8')))