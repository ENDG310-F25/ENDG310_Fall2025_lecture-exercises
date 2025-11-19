from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import json
import sys
import time

MAX_RETRIES = 3

app = Flask(__name__)
CORS(app)

with open('config.json') as config_file:
    config = json.load(config_file)

openai.api_key = config["open_ai_key"]
client = openai.OpenAI(
    api_key=config["open_ai_key"],
)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"reply": "Please provide a message"}), 400

    for attempt in range(MAX_RETRIES):
        try:
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message},
                ]
            )
            bot_reply = completion.choices[0].message.content
            return jsonify({"reply": bot_reply})
        except openai.RateLimitError:
            time.sleep(2)  # Wait before retrying
        except Exception as e:
            print("Error:", e, file=sys.stderr)
            return jsonify({"reply": "There was an error processing your request"}), 500

    return jsonify({"reply": "Rate limit exceeded. Please try again later."}), 429

if __name__ == "__main__":
    app.run(port=5000)