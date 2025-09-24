from openai import AsyncOpenAI

from app.settings import kb
from app.ai_prompts import service_assistant

class LLMService:
    def __init__(self, api_key: str, base_url: str | None, model: str = 'mistral-small-2501'):
        self.client = AsyncOpenAI(api_key=api_key, base_url=base_url)
        self.model = model

    async def ask(self, prompt: str, max_tokens: int = 150) -> str:
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {'role': 'system', 'content': service_assistant + kb},
                    {'role': 'user', 'content': prompt}]
                ,
                temperature=0.7,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f'Error calling OpenAI API: {e}'
