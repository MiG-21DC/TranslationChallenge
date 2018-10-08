def translation(client, text, target):
    res = client.translate(
        text,
        target_language=target)
    return res
