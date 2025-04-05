from config import config
from database import db

async def check_fsub(user_id: int):
    for channel in config.FSUB_CHANNELS:
        try:
            member = await client.get_chat_member(channel, user_id)
            if member.status in ['left', 'kicked']:
                return False
        except:
            return False
    return True

def format_size(size: int):
    units = ["B", "KB", "MB", "GB"]
    for unit in units:
        if size < 1024:
            break
        size /= 1024
    return f"{size:.2f} {unit}"
