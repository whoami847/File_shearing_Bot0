import asyncio
import logging
from pyrogram import Client
from bot.config import config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    async with Client(
        "my_bot",
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        bot_token=config.BOT_TOKEN,
        in_memory=True  # Disable session file
    ) as app:
        logger.info("✅ Bot started successfully!")
        await app.send_message("me", "Bot started successfully!")  # Test message
        await asyncio.Event().wait()  # Keep running

if __name__ == "__main__":
    asyncio.run(main())
