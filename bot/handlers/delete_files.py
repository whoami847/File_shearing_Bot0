import asyncio
from datetime import datetime, timedelta
from config import config
from database import db

async def auto_delete():
    while True:
        files_col = await db.get_collection("files")
        await files_col.delete_many({
            "expire_at": {"$lt": datetime.now()}
        })
        await asyncio.sleep(config.AUTO_DELETE_TIME * 60)

async def delete_file_handler(_, message: Message):
    if message.from_user.id in config.ADMINS:
        file_id = message.command[1]
        await db.files.delete_one({"_id": file_id})
        await message.reply("File deleted!")
