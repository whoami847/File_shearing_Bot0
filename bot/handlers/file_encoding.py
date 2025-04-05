from pyrogram import filters
from pyrogram.types import Message
from config import config
from database import db
from utils.encoder import generate_file_id
import ffmpeg

async def encode_video(file_path: str, quality: str):
    output_path = f"encoded/{generate_file_id()}_{quality}.mp4"
    (
        ffmpeg
        .input(file_path)
        .output(output_path, crf=config.QUALITY_PRESETS[quality])
        .run()
    )
    return output_path

async def encoding_handler(_, message: Message):
    if message.video:
        file_path = await message.download()
        encoded_files = {}
        for quality in ["360p", "480p", "720p"]:
            encoded_files[quality] = await encode_video(file_path, quality)
        await message.reply("Encoding completed!")
