from pyrogram import filters
from pyrogram.types import Message
from config import config

async def protect_content_handler(_, message: Message):
    if config.PROTECT_CONTENT:
        message.protect_content = True
    return message
