from fastapi import FastAPI
from pydantic import BaseModel

from ..application.agent_service import AgentService
from ..infrastructure.openai_client import OpenAIClient
from ..domain.message import Message

app = FastAPI(title="LLM Agent")
service = AgentService(OpenAIClient())

class ChatRequest(BaseModel):
    user: str
    content: str

@app.post("/chat")
async def chat(req: ChatRequest):
    message = Message(user=req.user, content=req.content)
    answer = await service.ask([message])
    return {"response": answer}
