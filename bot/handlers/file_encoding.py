import shutil
from fastapi import UploadFile
from .file_encoding import encode_file

async def share_file(file: UploadFile):
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    encoded_file = encode_file(file_path)
    return {"filename": file.filename, "encoded_path": encoded_file}
