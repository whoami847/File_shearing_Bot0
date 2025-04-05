import asyncio
from pyrogram import Client
from bot.config import config

# Initialize bot client
bot = Client(
    "file_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

async def main():
    await bot.start()
    print("🤖 Bot started successfully!")
    await asyncio.Event().wait()  # Keep running

if __name__ == "__main__":
    asyncio.run(main())
