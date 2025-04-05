from pyrogram import filters
from pyrogram.types import Message
from config import config
from utils.buttons import fsub_markup

async def fsub_handler(_, message: Message):
    for channel in config.FSUB_CHANNELS:
        try:
            member = await bot.get_chat_member(channel, message.from_user.id)
            if member.status in ['left', 'kicked']:
                await message.reply(
                    "Please join our channels first!",
                    reply_markup=fsub_markup
                )
                return
        except Exception as e:
            print(f"FSUB Error: {e}")
