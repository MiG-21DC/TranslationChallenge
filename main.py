import urllib3
import json
import scripts.translation as trans
from google.cloud import translate

translate_client = translate.Client()

text = u'Hello, world!'
target = 'ru'

res = trans.translation(translate_client, text, target)

print(res)


# http = urllib3.PoolManager()
#
# data = {'q': 'Address', 'target': 'de', }
# encoded_data = json.dumps(data).encode('utf-8')
# r = http.request('POST', 'https://translation.googleapis.com/language/translate/v2', body=encoded_data)
#
# print(json.loads(r.data.decode('utf-8')))