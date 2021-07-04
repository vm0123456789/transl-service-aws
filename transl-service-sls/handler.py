import json
import boto3


def detect_language(msg):
    """`detect_language` detects dominant language of the message

    Args:
        msg (str): text message

    Returns:
        str : dominant language code (e.g. 'en', 'ru' etc.)
    """
    comprehend = boto3.client(service_name='comprehend')
    return max(comprehend.detect_dominant_language(Text=msg)['Languages'], key=lambda x: x['Score'])['LanguageCode']


def translate_message(msg, source_lang, target_lang):
    transl = boto3.client('translate')
    res = transl.translate_text(
        Text=msg, SourceLanguageCode=source_lang, TargetLanguageCode=target_lang)
    return res['TranslatedText']


def handler(event, context):
    body = json.loads(event["body"])
    msg = body["message"]
    target_lang = body["target_language"]

    # use Amazon Comprehend to detect dominant language of the message
    source_lang = detect_language(msg)

    # use Amazon Translate to translate the message into target language
    tranlated_msg = translate_message(msg, source_lang, target_lang)

    body = {
        "translated_message": tranlated_msg
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
