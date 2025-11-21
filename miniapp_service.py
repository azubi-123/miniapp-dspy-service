from flask import Flask, request, jsonify
import dspy
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health():
    return "DSPy Miniapp Service Running", 200

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    # Basic DSPy pipeline
    lm = dspy.OpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
    result = lm(prompt)

    return jsonify({"response": result}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
