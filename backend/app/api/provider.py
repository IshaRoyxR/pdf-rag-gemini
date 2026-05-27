from fastapi import APIRouter
from app.rag.providers.factory import get_provider

router = APIRouter(prefix="/api/provider")


@router.get("/health")
def provider_health():
    try:
        provider = get_provider()

        print(f"🔍 Active Provider: {provider.__class__.__name__}")

        health_status = provider.health()

        return {
            "status": "ok",
            "provider": provider.__class__.__name__,
            "healthy": health_status
        }

    except Exception as e:
        print("🔥 Provider Health Error:", str(e))

        return {
            "status": "error",
            "message": str(e)
        }