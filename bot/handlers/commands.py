from pyrogram import filters
from pyrogram.types import Message
from config import config
from database import db

async def commands_handler(_, message: Message):
    if message.command[0] in ["help", "commands"]:
        commands = [
            "/start - Show welcome message",
            "/upload - Upload files",
            "/mysettings - User settings"
        ]
        await message.reply("\n".join(commands))
