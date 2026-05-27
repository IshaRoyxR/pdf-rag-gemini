import os
from langchain_community.llms import Ollama
from .base import BaseLLMProvider


class OllamaProvider(BaseLLMProvider):

    def __init__(self):
        self.model = "llama3"
        self.base_url = "http://127.0.0.1:11434"

        print(f"🚀 Using Ollama at {self.base_url}")

        self.llm = Ollama(
            model=self.model,
            base_url=self.base_url
        )

    def generate(self, prompt: str) -> str:
        try:
            print("📤 Prompt length:", len(prompt))

            # ✅ CORRECT METHOD
            response = self.llm.invoke(prompt)

            print("📥 Response received")

            return str(response)

        except Exception as e:
            print("🔥 OLLAMA ERROR:", str(e))
            return f"Ollama Error: {str(e)}"

    def health(self):
        try:
            self.llm.invoke("hello")
            return True
        except Exception as e:
            print("Health error:", e)
            return False