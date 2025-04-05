from fastapi import APIRouter
from config import config

router = APIRouter()

@router.get("/")
async def home():
    return {"status": "running", "port": config.PORT}

@router.get("/status")
async def status():
    return {"users": 0, "files": 0}
