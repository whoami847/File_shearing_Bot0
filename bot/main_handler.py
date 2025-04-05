import asyncio
from pyrogram import Client
from config import config
from database import db
from web.routes import router
from fastapi import FastAPI

# Initialize Web App
web_app = FastAPI()
web_app.include_router(router)

async def run_bot():
    # Connect to database
    await db.connect()
    
    # Start Telegram client
    bot = Client(
        "file_bot",
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        bot_token=config.BOT_TOKEN
    )
    
    async with bot:
        print("🤖 Bot started successfully!")
        await asyncio.Event().wait()  # Run indefinitely

if __name__ == "__main__":
    # Start both web server and bot
    asyncio.run(run_bot())
