from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router as upload_router
from app.api.chat import router as chat_router
from app.api.provider import router as provider_router
from app.api.documents import router as documents_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "https://lovable.dev"
]


app.include_router(upload_router, prefix="/api")
app.include_router(chat_router, prefix="/api")
app.include_router(provider_router, prefix="/api")
app.include_router(documents_router, prefix="/api")