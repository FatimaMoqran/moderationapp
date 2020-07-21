import requests, json

subscription_key = 'be89ff386a1d485b89e585a8955f6f57'

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