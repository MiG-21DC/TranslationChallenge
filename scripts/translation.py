# Translation object with Google Translation API
class Translations:
    def __init__(self, client, target, content):
        self.target = target
        self.source = 'en'
        self.content = content
        self.client = client
        self.translated_content = self.translation()

    def translation(self):
        trans_res = dict()
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
                print('Error occurs while attempting to translate: {}'.format(text))
                print(Exception)
                break
            trans_res[self.target][text] = res['translatedText']
        return trans_res
