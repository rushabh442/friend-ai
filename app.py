from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to generate response
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Streamlit Page Configuration
st.set_page_config(page_title="Q&A Gemini App", layout="centered")

# Custom CSS for Styling & Animations
st.markdown("""
    <style>
        /* Gradient Background */
        body {
            background: linear-gradient(135deg, #2C3E50, #4CA1AF);
            color: white;
            font-family: 'Arial', sans-serif;
        }

        /* Centering Content */
        .stTextInput>div>div>input {
            border-radius: 10px;
            border: 2px solid #FFC107;
            background-color: rgba(255, 255, 255, 0.1);
            color: white;
            transition: 0.3s;
            box-shadow: none;
        }

        /* Input Field Hover */
        .stTextInput>div>div>input:hover {
            border-color: #FFA000;
            box-shadow: 0px 0px 12px #FFC107;
        }

        /* Input Text Color */
        .stTextInput>div>div>input::placeholder {
            color: #FFD54F;
        }

        /* Button Styling */
        .stButton>button {
            background: linear-gradient(90deg, #FFC107, #FF9800);
            color: black;
            padding: 12px 24px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            transition: 0.3s;
            border: none;
            box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.3);
        }

        /* Button Hover Effect */
        .stButton>button:hover {
            background: linear-gradient(90deg, #FF9800, #F57C00);
            transform: scale(1.07);
            box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.4);
        }

        /* Response Box Animation */
        .response-box {
            background: rgba(255, 255, 255, 0.1);
            color: white;
            padding: 20px;
            border-radius: 12px;
            border-left: 5px solid #FFC107;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.3);
            animation: fadeIn 1s ease-in-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0px); }
        }

        /* Centering Text */
        .center-text {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #FFD54F;
        }

    </style>
""", unsafe_allow_html=True)

# Header with Icon
st.markdown("<h1 class='center-text'>🤖 Gemini AI Chatbot</h1>", unsafe_allow_html=True)

# User Input Box
input_text = st.text_input("🚀 Ask a Question:", key="input")

# Button for Getting Response
if st.button("✨ Get Answer"):
    response = get_gemini_response(input_text)
    
    # Display Response Box
    st.markdown(f"<div class='response-box'><h4>💡 Answer:</h4><p>{response}</p></div>", unsafe_allow_html=True)
