from typing import List
from fastapi import BackgroundTasks
from .messages import send_message

async def broadcast_message(users: List[int], message: str, bg_tasks: BackgroundTasks):
    for user_id in users:
        bg_tasks.add_task(send_message, user_id, message)
