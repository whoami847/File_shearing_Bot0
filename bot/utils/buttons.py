from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import config

def start_markup():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Upload File", callback_data="upload")]
    ])

def fsub_markup():
    buttons = []
    for channel in config.FSUB_CHANNELS:
        buttons.append([InlineKeyboardButton(f"Channel {channel}", url=f"t.me/{channel}")])
    return InlineKeyboardMarkup(buttons)
