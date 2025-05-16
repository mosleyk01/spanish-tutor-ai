from flask import Flask, request, jsonify, render_template
from ai_chat import spanish_tutor, reset_conversation

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# New endpoint for starting the conversation (AI sends first message)
@app.route("/start", methods=["GET"])
def start():
    reset_conversation()  # Reset conversation for a fresh start
    ai_response = spanish_tutor()  # Call without user input so AI sends greeting
    return jsonify({"response": ai_response})

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    ai_response = spanish_tutor(user_input)
    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(debug=True)
