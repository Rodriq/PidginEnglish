import requests
import uuid
import json

# Add your subscription key and endpoint
subscription_key = "8233c450462546009c5f76566e1028ae"


def translate_word(word):
    print(word)

def get_translation(text_input, language_output):
    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&to=' + language_output
    constructed_url = base_url + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': text_input
    }]
    response = requests.post(constructed_url, headers=headers, json=body).json()
    return response[0]['translations'][0]['text']
