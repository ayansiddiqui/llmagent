from typing import List

from ..domain.message import Message
from ..infrastructure.openai_client import OpenAIClient

class AgentService:
    """Service to interact with the language model"""

    def __init__(self, client: OpenAIClient):
        self.client = client

    async def ask(self, messages: List[Message]) -> str:
        text = "\n".join(f"{m.user}: {m.content}" for m in messages)
        return await self.client.generate_response(text)
