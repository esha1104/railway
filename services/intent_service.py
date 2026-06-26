import pickle
import re

with open("nlp/intent_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("nlp/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


def preprocess(text):
    """
    Clean the user's message before prediction.
    """

    text = text.lower()

    # Remove punctuation
    text = re.sub(r"[^a-z0-9\s]", "", text)

    # Remove extra spaces
    text = " ".join(text.split())

    return text


def detect_intent(message):

    message = preprocess(message)

    X = vectorizer.transform([message])

    probabilities = model.predict_proba(X)[0]

    best_index = probabilities.argmax()

    confidence = probabilities[best_index]

    prediction = model.classes_[best_index]

    return prediction, confidence