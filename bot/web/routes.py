from fastapi import APIRouter, UploadFile, HTTPException
from .file_sharing import handle_file_upload
from .status import router as status_router
from fastapi.responses import FileResponse

router = APIRouter()
router.include_router(status_router)

@router.post("/upload")
async def upload_file(file: UploadFile):
    try:
        return await handle_file_upload(file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/files/{filename}")
async def download_file(filename: str):
    file_path = os.path.join(Config.STORAGE_PATH, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, filename=filename)
