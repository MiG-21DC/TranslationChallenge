import urllib3
import json
import scripts.translation as trans
from google.cloud import translate
import json

translate_client = translate.Client()

# text = u'Hello, world!'
# target = 'ru'

with open('translations.json') as translation_file:
    translation_content = json.load(translation_file)

# print(translation_content)
trans_res = {}
for target, content in translation_content.items():
    trans_res[target] = {}
    for text, trans_content in content.items():
        if trans_content != '':
            trans_res[target].update({text, trans_content})
            continue
        res = trans.translation(translate_client, text, target.split('-')[0])
        print(type(res['translatedText']))
        # trans_res[target].update({text, res['translatedText']})

print(trans_res)

# http = urllib3.PoolManager()
#
# data = {'q': 'Address', 'target': 'de', }
# encoded_data = json.dumps(data).encode('utf-8')
# r = http.request('POST', 'https://translation.googleapis.com/language/translate/v2', body=encoded_data)
#
# print(json.loads(r.data.decode('utf-8')))