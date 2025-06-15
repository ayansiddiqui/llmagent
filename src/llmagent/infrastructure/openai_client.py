import os
from openai import AsyncOpenAI

class OpenAIClient:
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.model = model
        self.client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    async def generate_response(self, text: str) -> str:
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": text}],
        )
        return response.choices[0].message.content
