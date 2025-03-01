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

    # Initializing default values
    anger_score = None
    disgust_score = None
    fear_score = None
    joy_score = None
    sadness_score = None
    dominant_emotion = None

    try:
        #POST request to the API
        response = requests.post(url, json=myobj, headers=header, timeout=10)

        #Parsed JSON response
        formatted_response= json.loads(response.text)

        #Extracting emotions
        if response.status_code == 200:
            emotions = formatted_response['emotionPredictions'][0]['emotion']
            dominant_emotion = max(emotions, key=emotions.get)
            anger_score = emotions['anger']
            disgust_score = emotions['disgust']
            fear_score = emotions['fear']
            joy_score = emotions['joy']
            sadness_score = emotions['sadness']

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}") # Error log

    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': f'{dominant_emotion}'
    }
