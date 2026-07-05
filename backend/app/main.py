from fastapi import FastAPI

from app.routers.chat import router as chat_router
from app.routers.health import router as health_router

app = FastAPI(
    title="AI Agent Studio",
    version="1.0.0"
)

app.include_router(chat_router)
app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Agent Studio 🚀"
    }