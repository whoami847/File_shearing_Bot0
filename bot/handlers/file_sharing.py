from fastapi import UploadFile, HTTPException
import os
from .config import Config
from .file_encoding import generate_unique_filename

async def handle_file_upload(file: UploadFile):
    # Check file size
    max_size = Config.MAX_FILE_SIZE
    file.file.seek(0, 2)
    file_size = file.file.tell()
    file.file.seek(0)
    
    if file_size > max_size:
        raise HTTPException(status_code=413, detail="File too large")
    
    # Generate safe filename
    unique_name = generate_unique_filename(file.filename)
    file_path = os.path.join(Config.STORAGE_PATH, unique_name)
    
    # Save file
    with open(file_path, "wb") as buffer:
        while content := await file.read(1024 * 1024):  # 1MB chunks
            buffer.write(content)
    
    return {
        "original_name": file.filename,
        "stored_name": unique_name,
        "download_url": f"{Config.BASE_URL}/files/{unique_name}"
    }
