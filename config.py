import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


try:
    GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]

except:

    GOOGLE_API_KEY = os.getenv(
        "GEMINI_API_KEY"
    )

MODEL_NAME = "gemini-3.5-flash"

TEMPERATURE = 0.7

VOICE_NAME = "ar-EG-SalmaNeural"

APP_TITLE = "🤖 AI Voice Assistant"
