import asyncio
from pyrogram import Client
from bot.config import config
from bot.web.routes import router  # Correct import path
from fastapi import FastAPI

# Initialize Web App
web_app = FastAPI()
web_app.include_router(router)

async def run_bot():
    bot = Client(
        "file_bot",
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        bot_token=config.BOT_TOKEN
    )
    
    async with bot:
        print("🤖 Bot started successfully!")
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(run_bot())
