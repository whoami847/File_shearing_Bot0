from fastapi import APIRouter
from .start import app

router = APIRouter()

@router.get("/status")
async def get_status():
    return {
        "status": "OK",
        "version": "1.0.0",
        "services": ["database", "storage"]
    }
