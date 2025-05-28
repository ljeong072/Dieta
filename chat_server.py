from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

# Load from local directory
model = AutoModelForCausalLM.from_pretrained("my_model")
tokenizer = AutoTokenizer.from_pretrained("my_model")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100, do_sample=True)
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
