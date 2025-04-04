from fastapi import HTTPException
from .database import get_db

def handle_join_request(user_id: int, db = Depends(get_db)):
    # Implement your join request logic here
    return {"status": "approved"}
