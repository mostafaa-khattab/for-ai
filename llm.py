from langchain_google_genai import ChatGoogleGenerativeAI

from config import (
    GOOGLE_API_KEY,
    MODEL_NAME,
    TEMPERATURE
)

llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    google_api_key=GOOGLE_API_KEY,
    temperature=TEMPERATURE,
)


def ask_gemini(question, history=""):

    prompt = f"""
أنت مساعد ذكي.

هذه المحادثة السابقة:
{history}

سؤال المستخدم الحالي:
{question}

أجب بناءً على سياق المحادثة.
"""

    response = llm.invoke(prompt)

    return response.content