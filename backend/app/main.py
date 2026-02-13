from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.documents import router as documents_router

from app.api.health import router as health_router
from app.api.upload import router as upload_router
from app.api.chat import router as chat_router

app = FastAPI(
    title="RAG Ollama Backend",
    version="1.0.0"
)

# =========================
# CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# Routers
# =========================
app.include_router(documents_router, prefix="/api")
app.include_router(health_router, prefix="/api")
app.include_router(upload_router, prefix="/api")
app.include_router(chat_router, prefix="/api")
