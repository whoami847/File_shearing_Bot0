import asyncio
from pyrogram import Client
from bot.config import config
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

async def run_bot():
    bot = Client(
        "file_bot",
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        bot_token=config.BOT_TOKEN
    )
    await bot.start()
    print("🤖 Bot started successfully!")
    await asyncio.Event().wait()  # Keep running indefinitely

async def main():
    # Start both web server and bot
    server = uvicorn.Server(
        config=uvicorn.Config(
            app=app,
            host="0.0.0.0",
            port=8080,
            log_level="info"
        )
    )
    await asyncio.gather(
        server.serve(),
        run_bot()
    )

if __name__ == "__main__":
    asyncio.run(main())
