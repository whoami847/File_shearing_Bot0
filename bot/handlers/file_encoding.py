import hashlib
import os

def encode_file(file_path: str) -> str:
    file_name = os.path.basename(file_path)
    encoded_name = hashlib.md5(file_name.encode()).hexdigest()
    encoded_path = f"encoded/{encoded_name}"
    os.rename(file_path, encoded_path)
    return encoded_path
