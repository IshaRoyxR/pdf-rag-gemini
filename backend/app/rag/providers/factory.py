from .gemini_provider import GeminiProvider
from .openai_provider import OpenAIProvider
from .ollama_provider import OllamaProvider


def get_provider(provider_name: str):

    if provider_name == "gemini":
        return GeminiProvider()

    elif provider_name == "openai":
        return OpenAIProvider()

    elif provider_name == "ollama":
        return OllamaProvider()

    else:
        raise ValueError("Invalid provider selected")