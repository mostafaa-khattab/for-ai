import streamlit as st

from config import APP_TITLE
from llm import ask_gemini
from streamlit_mic_recorder import mic_recorder
from speech import speech_to_text
from tts import text_to_speech

from memory import (
    initialize_memory,
    add_message,
    get_messages,
    get_conversation,
    clear_chat,
)


# ==========================
# Page Config
# ==========================

st.set_page_config(
    page_title="AI Voice Assistant",
    page_icon="🤖",
    layout="centered",
)


st.title(APP_TITLE)


# ==========================
# Initialize Memory
# ==========================

initialize_memory()


# ==========================
# Sidebar
# ==========================

with st.sidebar:

    st.header("⚙️ Settings")

    if st.button("🗑️ Clear Chat"):

        clear_chat()

        st.rerun()



# ==========================
# Display Chat History
# ==========================

for message in get_messages():

    with st.chat_message(message["role"]):

        st.markdown(message["content"])



# ==========================
# Text Input
# ==========================

question = st.chat_input(
    "اكتب رسالتك..."
)



# ==========================
# Voice Input
# ==========================

st.write("أو تحدث 🎤")


audio = mic_recorder(

    start_prompt="🎤 Start Recording",

    stop_prompt="⏹ Stop Recording",

    just_once=True,

    key="voice"

)



if audio:

    question = speech_to_text(
        audio["bytes"]
    )



# ==========================
# Send Message
# ==========================

if question:


    # حفظ الـ history قبل السؤال الحالي
    history = get_conversation()



    # عرض رسالة المستخدم

    add_message(
        "user",
        question
    )


    with st.chat_message("user"):

        st.markdown(question)



    # ==========================
    # Gemini Response
    # ==========================

    with st.spinner(
        "Gemini is thinking..."
    ):


        answer = ask_gemini(

            question,

            history

        )



    # حفظ رد Gemini

    add_message(

        "assistant",

        answer

    )



    # عرض الرد

    with st.chat_message("assistant"):

        st.markdown(answer)



        # ==========================
        # Text To Speech
        # ==========================

        try:

            audio_path = text_to_speech(
                answer
            )


            st.audio(
                audio_path
            )


        except Exception as e:

            st.warning(
                "تعذر تشغيل الصوت."
            )