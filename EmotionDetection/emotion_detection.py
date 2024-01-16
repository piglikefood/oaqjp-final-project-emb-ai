import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)['emotionPredictions'][0]["emotion"]

    values = formatted_response.values()
    max_values = max(values) 

    for key, value in formatted_response.items():
        if value == max_values:
            dominant_emotion = key
            break

    formatted_response["dominant_emotion"] = dominant_emotion
    return formatted_response

#print(emotion_detector('I love this new technology.'))