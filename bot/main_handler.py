import logging
import asyncio
from pyrogram import Client, filters

# লগিং সেটআপ
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Client(
    "my_bot",
    api_id=123456,       # আপনার API_ID দিয়ে রিপ্লেস করুন
    api_hash="abc123",   # আপনার API_HASH দিয়ে রিপ্লেস করুন
    bot_token="TOKEN"    # আপনার বট টোকেন দিয়ে রিপ্লেস করুন
)

@app.on_message(filters.command("start"))
async def start(client, message):
    logger.info(f"User {message.from_user.id} sent /start")
    await message.reply("🎉 বট এক্টিভ! /help লিখে কমান্ডগুলো দেখুন")

@app.on_message(filters.command("ping"))
async def ping(client, message):
    await message.reply("🏓 পং! বট লাইভ আছে")

async def main():
    await app.start()
    logger.info("বট সফলভাবে স্টার্ট হয়েছে!")
    await asyncio.Event().wait()  # বট চলতে থাকবে

if __name__ == "__main__":
    asyncio.run(main())
