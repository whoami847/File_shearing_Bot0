import base64
from datetime import datetime

def generate_file_id():
    return base64.urlsafe_b64encode(
        datetime.now().isoformat().encode()
    ).decode().rstrip("=")
