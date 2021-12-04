# library imports
from flair.models import TextClassifier
from flair.data import Sentence
from gibberish_detector import detector
from pathlib import Path
import re

# load the gibberish detection model
gibberish_detector_path = Path('./pretrained_models/gibberish-detector.model')
Detector = detector.create_from_model(gibberish_detector_path)

# load the sentiment classifier model
flair_model_path = Path('./pretrained_models/flair-sentiment-en-mix-distillbert_4.pt')
classifier = TextClassifier.load(flair_model_path)

def check_input(text):
    """
    Confirm that the user's text input is appropriate
    for sentiment prediction
    """
    validity_flag = True

    # input is too lengthy
    if len(text)>500:
        validity_flag = False

    # input has no letters at all
    if not re.search(r'[a-zA-z]', text):
        validity_flag = False

    # input is gibberish
    if Detector.is_gibberish(text) == True:
        validity_flag = False

    return validity_flag


def sentiment_prediction(user_input):
    """
    Predict "POSITIVE"/"NEGATIVE" labels for a given text
    """
    # tokenize and predict
    text = Sentence(user_input)
    classifier.predict(text)

    # get the predicted label
    sentiment = text.labels[0].to_dict()['value']

    # get the confidence score
    confidence = text.to_dict()['labels'][0]['confidence']
    confidence = str(round(confidence*100))+'%'

    return f"{sentiment} | {confidence} Confidence"
