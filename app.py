from flask import Flask, render_template, request, jsonify
from chatbot.responses import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response")
def chat():
    user_message = request.args.get("message")
    if not user_message:
        return jsonify({"response": "Please enter a message."})
    
    bot_response = get_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=False)
