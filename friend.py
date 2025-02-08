import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Generative AI model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Initialize Flask app
app = Flask("friend.py")

# Function to get Gemini AI's response
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return [chunk.text for chunk in response]

# Route for homepage
@app.route("/")
def index():
    return render_template("friend.html")

# Route for handling questions
@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question")
    if not question:
        return jsonify({"error": "Question cannot be empty"}), 400
    try:
        response = get_gemini_response(question)
        return jsonify({"response": "".join(response)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8000)
