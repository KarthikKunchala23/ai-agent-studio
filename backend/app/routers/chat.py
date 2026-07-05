from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models.chat import ChatRequest
from app.services.chat_service import ask_question

router = APIRouter()


@router.post("/chat")
async def chat(request: ChatRequest):

    generator = ask_question(
        request.question,
        request.model
    )

    return StreamingResponse(
        generator,
        media_type="text/plain"
    )