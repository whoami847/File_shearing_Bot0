from pyrogram import filters
from pyrogram.types import Message
from config import config
from database import db
from datetime import datetime, timedelta

async def file_handler(_, message: Message):
    files_col = await db.get_collection("files")
    
    file_data = {
        "file_id": message.document.file_id,
        "user_id": message.from_user.id,
        "upload_time": datetime.now(),
        "delete_time": datetime.now() + timedelta(minutes=config.AUTO_DELETE_TIME)
    }
    
    await files_col.insert_one(file_data)
    await message.reply("File saved successfully!")
