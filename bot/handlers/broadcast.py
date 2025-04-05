from pyrogram import filters
from pyrogram.types import Message
from config import config
from database import db

async def broadcast_handler(_, message: Message):
    if message.from_user.id not in config.ADMINS:
        return
    
    users_col = await db.get_collection("users")
    users = await users_col.find().to_list(None)
    
    for user in users:
        try:
            await message.copy(user["_id"])
        except Exception as e:
            print(f"Broadcast error: {e}")
