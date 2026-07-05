import requests


def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, json=input_json, headers=headers)

        # Se a API retornar um erro (ex: 400, 500), isso vai gerar uma exceção
        response.raise_for_status()

        formatted_response = response.json()
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        # Encontra a emoção dominante
        dominant_emotion = max(emotions, key=emotions.get)

        # Cria o retorno aproveitando o dicionário original + a emoção dominante
        return {
            "anger": emotions.get("anger", 0),
            "disgust": emotions.get("disgust", 0),
            "fear": emotions.get("fear", 0),
            "joy": emotions.get("joy", 0),
            "sadness": emotions.get("sadness", 0),
            "dominant_emotion": dominant_emotion
        }

    except (requests.exceptions.RequestException, KeyError, IndexError) as error:
        # Retorna uma estrutura padrão em caso de falha para o seu código não parar
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "error": f"Falha ao processar as emoções: {str(error)}"
        }
