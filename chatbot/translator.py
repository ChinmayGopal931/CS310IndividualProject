import requests, uuid, json

# Add your subscription key and endpoint
subscription_key = "subkey"
endpoint = "https://api.cognitive.microsofttranslator.com"
location = "location"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.

def translateme(userinput):
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'to': ['en']
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': userinput
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    return(response[0])

def translator(userInput, language):
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': [language]
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': userInput
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = (request.json())[0]["translations"][0]["text"]

    response= (json.dumps(response,ensure_ascii=False))
    return(response.replace('"', ''))
