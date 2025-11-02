# ...existing code...
from flask import Flask, request, jsonify, render_template
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

# Create Flask app
app = Flask(__name__)

# Load tokenizer and model explicitly and create pipeline with proper device
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

device = 0 if torch.cuda.is_available() else -1
chatbot = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=device,
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    # support JSON or form submissions
    data = request.get_json(silent=True) or {}
    user_input = data.get("text") or request.form.get("text", "")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        # Use eos_token_id as pad_token_id and return only the new generated portion
        results = chatbot(
            user_input,
            max_length=200,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            num_return_sequences=1,
            return_full_text=False,
        )
        bot_reply = results[0].get("generated_text", "") if isinstance(results, list) else str(results)
    except Exception as e:
        return jsonify({"error": "Generation failed", "details": str(e)}), 500

    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    # bind to 0.0.0.0 for accessibility on the local network if needed
    app.run(host="0.0.0.0", port=5000, debug=True)
# ...existing code...