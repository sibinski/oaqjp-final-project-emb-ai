import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyse }}
    response = requests.post(url, json = myobj, headers=headers)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    else:
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        result = emotions.copy()
        result['dominant_emotion'] = dominant_emotion
        return result

if __name__ == "__main__":
    text = input("Please enter a phrase...\n")
    answer = emotion_detector(text)
    print(json.dumps(answer, indent = 2))
    print(f"\nDominant Emotion: {answer['dominant_emotion'].capitalize()} ({answer[answer['dominant_emotion']]})")
