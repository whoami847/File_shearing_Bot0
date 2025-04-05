from pyrogram import filters
from pyrogram.types import Message, ChatJoinRequest
from config import config
from utils.helpers import check_fsub

async def join_request_handler(_, message: ChatJoinRequest):
    if not await check_fsub(message.from_user.id):
        await message.decline()
    else:
        await message.approve()
