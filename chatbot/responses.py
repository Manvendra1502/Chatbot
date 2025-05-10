# chatbot/responses.py

def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hello! How can I help you?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing fine!"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."
