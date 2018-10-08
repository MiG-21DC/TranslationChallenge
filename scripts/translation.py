# Translation function with Google Translation API
def translation(client, text, target):
    res = client.translate(
        text,
        target_language=target, source_language='en')
    return res['translatedText']
