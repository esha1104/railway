from services.intent_service import detect_intent

while True:

    text = input("You: ")

    print(
        "Intent:",
        detect_intent(text)
    )