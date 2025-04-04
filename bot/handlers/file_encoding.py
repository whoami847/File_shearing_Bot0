import uuid
import os

def generate_unique_filename(original_name: str) -> str:
    ext = original_name.split('.')[-1]
    unique_name = f"{uuid.uuid4().hex}.{ext}"
    return unique_name
