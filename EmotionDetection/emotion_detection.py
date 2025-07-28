import requests, json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    r=json.loads(response.text)
    anger_score = ("anger",r["emotionPredictions"][0]["emotion"]["anger"])
    disgust_score = ("disgust",r["emotionPredictions"][0]["emotion"]["disgust"])
    fear_score = ("fear",r["emotionPredictions"][0]["emotion"]["fear"])
    joy_score = ("joy",r["emotionPredictions"][0]["emotion"]["joy"])
    sadness_score = ("sadness",r["emotionPredictions"][0]["emotion"]["sadness"])
    
    L=[anger_score,disgust_score,fear_score,joy_score,sadness_score]
    L.sort(key=lambda tup: tup[1],reverse=True)

    dom_emo =L[0][0]
    d = {'anger': anger_score[1],'disgust': disgust_score[1],'fear': fear_score[1],'joy': joy_score[1],'sadness': sadness_score[1],
           'dominant_emotion': dom_emo}
    return d

