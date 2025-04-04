from fastapi import APIRouter, UploadFile, Depends, BackgroundTasks
from .file_sharing import share_file
from .status import router as status_router

router = APIRouter()
router.include_router(status_router)

@router.post("/upload")
async def upload_file(file: UploadFile, bg_tasks: BackgroundTasks):
    return await share_file(file)
