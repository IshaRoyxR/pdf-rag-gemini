import os
from langchain_openai import ChatOpenAI
from .base import BaseLLMProvider


class OpenAIProvider(BaseLLMProvider):

    def __init__(self):
        self.llm = ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0
        )

    def generate(self, prompt: str) -> str:
        return self.llm.invoke(prompt).content

    def health(self):
        return True