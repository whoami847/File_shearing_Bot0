from pyrogram import Client
from config import config
from handlers import (
    start,
    commands,
    broadcast,
    file_sharing,
    fsub
)

bot = Client(
    "file_share_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# Register handlers
bot.add_handler(start.start_handler)
bot.add_handler(commands.commands_handler)
bot.add_handler(broadcast.broadcast_handler)
bot.add_handler(file_sharing.file_handler)
bot.add_handler(fsub.fsub_handler)

async def start_bot():
    await bot.start()
    print("Bot started!")
    await bot.idle()
