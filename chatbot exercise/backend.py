from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import asyncio  # For asynchronous support
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


with open('config.json') as config_file:
    config = json.load(config_file)

# Access the API key
openai.api_key = config["open_ai_key"]
client = openai.OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=config["open_ai_key"],
)
@app.route("/chat", methods=["POST"])
async def chat():
    user_message = request.json.get("message", "")

    # Handle invalid or missing message
    if not user_message:
        return jsonify({"reply": "Please provide a message"}), 400

    try:
        completion = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"},
                        ] 
        )   
        bot_reply = completion["choices"][0]["message"]["content"]
        return jsonify({"reply": bot_reply})

    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": "There was an error processing your request"}), 500

if __name__ == "__main__":
    app.run(port=5000)
