from EmotionDetection import emotion_detector


def test_emotion_detector():
    test_cases = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for statement, expected_emotion in test_cases.items():
        response = emotion_detector(statement)
        dominant_emotion = response["dominant_emotion"]

        print(
            f"For the statement '{statement}' "
            f"the system response is '{dominant_emotion}'"
        )

        assert dominant_emotion == expected_emotion

    print("All tests passed!")


test_emotion_detector()