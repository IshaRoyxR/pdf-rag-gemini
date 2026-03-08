import os
from langchain_google_genai import ChatGoogleGenerativeAI
from .base import BaseLLMProvider


class GeminiProvider(BaseLLMProvider):

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=os.getenv("GEMINI_MODEL", "gemini-flash-latest"),
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0
        )

    def generate(self, prompt: str) -> str:

        response = self.llm.invoke(prompt)

        # Gemini sometimes returns list of dicts
        content = response.content

        if isinstance(content, list):
            return content[0].get("text", "")

        return content

    def health(self):
        return True