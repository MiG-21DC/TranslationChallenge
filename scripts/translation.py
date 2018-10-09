# Translation function with Google Translation API
# def translation(client, text, target):
#     res = client.translate(
#         text,
#         target_language=target, source_language='en')
#     return res['translatedText']


class Translations:
    def __init__(self, client, target, content):
        self.target = target
        self.source = 'en'
        self.content = content
        self.client = client
        self.translated_content = self.translation()

    def translation(self):
        trans_res = {}
        trans_res[self.target] = {}
        for text, trans_text in self.content.items():
            if trans_text != '':
                trans_res[self.target][text] = trans_text
                continue
            try:
                res = self.client.translate(
                    text,
                    target_language=self.target.split('-')[0], source_language='en')
            except Exception:
                print('Error occurs while attempting to translate: {}').format(text)
                print(Exception)
                break
            trans_res[self.target][text] = res['translatedText']
        return trans_res
