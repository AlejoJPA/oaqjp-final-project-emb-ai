'''This app performs emotion detection from text
    using the Watson NLP library
'''
import json
import requests

def emotion_detector(text_to_analyze):
    '''emotion_detector function
    '''
    #URL of the emotion-detection analysis service
    url = ("https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    #Dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze} }

    #Headers required for the API request
    header = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }

    try:
        #POST request to the API
        response = requests.post(url, json=myobj, headers=header, timeout=10)

        #Parsed JSON response
        formatted_response= json.loads(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}") # Error log

    return formatted_response
