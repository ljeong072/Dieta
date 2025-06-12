from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
from flask_cors import CORS
import torch

app = Flask(__name__)
CORS(app)

# Load from local directory
model = AutoModelForCausalLM.from_pretrained("C:/Users/mahri/OneDrive/Desktop/TCSS456/my_model")
tokenizer = AutoTokenizer.from_pretrained("C:/Users/mahri/OneDrive/Desktop/TCSS456/my_model")
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100, do_sample=True)
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
