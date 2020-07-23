import requests, json

subscription_key = 'mykey'

def moderate(text_input):
    url = 'https://westeurope.api.cognitive.microsoft.com/contentmoderator/moderate/v1.0/ProcessText/Screen?classify=True'


    headers = {
    # Request headers
    'Content-Type': 'text/plain',
    'Ocp-Apim-Subscription-Key': subscription_key
    }

    params = ({
        # Request parameters

        'classify': 'True'})

    body = [{'text' :text_input}]

    r = requests.post(url, json = body, params = params,headers= headers )
    return r.json()