from fastapi import APIRouter
from app.rag.providers.factory import get_provider

router = APIRouter(prefix="/api/provider")

@router.get("/health")
def provider_health():
    provider = get_provider()
    return provider.health()