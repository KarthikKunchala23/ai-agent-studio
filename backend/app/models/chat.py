from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str
    model: str = "gpt-4o-mini"