import asyncio
import logging
from pyrogram import Client, filters
from bot.config import config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize client
app = Client(
    "my_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("🚀 Bot is running!")

async def run_bot():
    await app.start()
    logger.info("Bot started successfully")
    await app.send_message(config.OWNER_ID, "🤖 Bot deployed and online!")
    await asyncio.Event().wait()  # Keep running

if __name__ == "__main__":
    try:
        asyncio.run(run_bot())
    except Exception as e:
        logger.error(f"Bot crashed: {str(e)}")
        raise
