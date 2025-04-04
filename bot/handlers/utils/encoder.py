import base64

def encode_base64(data: str) -> str:
    return base64.b64encode(data.encode()).decode()

def decode_base64(data: str) -> str:
    return base64.b64decode(data).decode()
