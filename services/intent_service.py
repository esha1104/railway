import pickle

with open("nlp/intent_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("nlp/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


def detect_intent(message):

    X = vectorizer.transform([message])

    prediction = model.predict(X)

    return prediction[0]