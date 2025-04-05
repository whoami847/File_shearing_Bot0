from pyrogram import filters
from pyrogram.types import Message
from config import config
from utils.messages import start_message
from utils.buttons import start_markup

async def start_handler(_, message: Message):
    await message.reply(
        start_message,
        reply_markup=start_markup
    )
