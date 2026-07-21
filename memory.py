import streamlit as st


# ==========================
# Initialize Memory
# ==========================

def initialize_memory():

    if "messages" not in st.session_state:

        st.session_state.messages = []



# ==========================
# Add Message
# ==========================

def add_message(role, content):

    st.session_state.messages.append(
        {
            "role": role,
            "content": content
        }
    )



# ==========================
# Get All Messages
# ==========================

def get_messages():

    return st.session_state.messages



# ==========================
# Get Conversation History
# ==========================

def get_conversation():

    conversation = ""

    for message in st.session_state.messages:

        role = message["role"]

        content = message["content"]

        conversation += f"""
{role}: {content}
"""


    return conversation



# ==========================
# Clear Memory
# ==========================

def clear_chat():

    st.session_state.messages = []