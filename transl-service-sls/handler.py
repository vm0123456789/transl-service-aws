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
    pass


def handler(event, context):
    body = json.loads(event["body"])
    msg = body["message"]
    target_lang = body["target_language"]

    source_lang = detect_language(msg)
    tranlated_msg = translate_message(msg, source_lang, target_lang)

    body = {
        "translated_message": tranlated_msg
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
