import os

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")
OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "mxbai-embed-large")

CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "/app/data/chroma_db")
API_PREFIX = "/api"
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://host.docker.internal:11434")
