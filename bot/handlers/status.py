from pyrogram import filters
from pyrogram.types import Message
from database import db

async def status_handler(_, message: Message):
    files_col = await db.get_collection("files")
    users_col = await db.get_collection("users")
    
    stats = f"""
    📊 Bot Status:
    Files: {await files_col.count_documents({})}
    Users: {await users_col.count_documents({})}
    """
    await message.reply(stats)
