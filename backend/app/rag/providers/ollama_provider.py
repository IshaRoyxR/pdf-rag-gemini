import os
from langchain_ollama import ChatOllama
from .base import BaseLLMProvider


class OllamaProvider(BaseLLMProvider):

    def __init__(self):
        self.llm = ChatOllama(
            model=os.getenv("OLLAMA_MODEL", "llama3"),
            base_url=os.getenv("OLLAMA_BASE_URL", "http://host.docker.internal:11434")
        )

    def generate(self, prompt: str) -> str:
        return self.llm.invoke(prompt).content

    def health(self):
        return True