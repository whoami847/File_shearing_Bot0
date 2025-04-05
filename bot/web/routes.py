from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/healthz")
async def health_check():
    return JSONResponse(
        content={"status": "ok"},
        status_code=200
    )

@router.get("/status")
async def system_status():
    return {
        "service": "running",
        "bot_ready": True
    }
