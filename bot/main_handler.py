import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.errors import RPCError, ConnectionClosed  # Updated imports
from bot.config import config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize client
app = Client(
    name="my_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=False,
    workers=24,
    sleep_threshold=180
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("🚀 Bot is running!")

async def run_bot():
    while True:
        try:
            await app.start()
            logger.info("Bot started successfully")
            await app.send_message(config.OWNER_ID, "🤖 Bot deployed and online!")
            
            # Keep connection alive
            while True:
                await asyncio.sleep(300)
                await app.get_me()
                
        except (ConnectionClosed, RPCError) as e:  # Updated exception handling
            logger.error(f"Connection error: {e}, reconnecting in 5 seconds...")
            await app.stop()
            await asyncio.sleep(5)
        except Exception as e:
            logger.error(f"Critical error: {e}")
            await app.stop()
            break

if __name__ == "__main__":
    asyncio.run(run_bot())
