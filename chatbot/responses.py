import random
import re
from googletrans import Translator

translator = Translator()

def get_response(user_input):
    user_input = user_input.lower().strip()

    # Handle informal translation requests like:
    # "translate i love you to spanish"
    # "how to say good night in french"
    match = re.search(r"(translate|say|how to say)?\s*(.*?)\s*(to|in)?\s*(\w+)?$", user_input)

    if match:
        _, text, _, target_lang = match.groups()

        if text and target_lang:
            # Normalize target language
            if target_lang == "american":
                target_lang = "english"

            try:
                translation = translator.translate(text.strip(), dest=target_lang.strip())
                return f"Translation: {translation.text}"
            except Exception:
                return "Sorry, I couldn't translate that. Please check your language name."

    # Chatbot default responses
    if 'hello' in user_input or 'hi' in user_input:
        return random.choice(["Hello!", "Hi there!", "Hey!"])

    elif 'how are you' in user_input:
        return "I'm a bot, but I'm doing great. Thanks for asking!"

    elif 'bye' in user_input or 'goodbye' in user_input:
        return "Goodbye! Have a great day!"

    elif 'name' in user_input:
        return "I'm your friendly chatbot."

    elif 'help' in user_input:
        return "Try: 'translate thank you to French' or 'how to say good morning in German'."

    else:
        return "I'm not sure how to respond to that yet. Try asking something else."
