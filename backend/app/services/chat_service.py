from app.llm.openai_client import stream_chat


def ask_question(question: str, model: str):
    return stream_chat(question, model)