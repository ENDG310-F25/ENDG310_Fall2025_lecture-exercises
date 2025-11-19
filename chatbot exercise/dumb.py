from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def decision_tree_bot(user_message):
    msg = user_message.lower().strip()
    # Simple decision tree logic
    if any(greet in msg for greet in ["hello", "hi", "hey"]):
        return "Hello! How can I help you today?"
    elif "weather" in msg:
        return "I'm not connected to the internet, but I hope the weather is nice where you are!"
    elif "name" in msg:
        return "I'm a simple rule-based chatbot."
    elif "bye" in msg or "goodbye" in msg:
        return "Goodbye! Have a great day!"
    elif "help" in msg:
        return "I can answer simple questions about greetings, weather, my name, and farewells."
    elif "joke" in msg:
        return "Why did the computer show up at work late? It had a hard drive!"
    else:
        return "Sorry, I didn't understand that. Try asking about the weather, my name, or say hello!"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"reply": "Please provide a message"}), 400

    bot_reply = decision_tree_bot(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(port=5000)