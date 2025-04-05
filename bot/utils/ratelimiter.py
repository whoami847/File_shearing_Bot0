from pyrogram import filters
from database import db
from datetime import datetime, timedelta

class RateLimiter:
    def __init__(self, limit: int, window: int):
        self.limit = limit
        self.window = window

    async def check(self, user_id: int):
        users_col = await db.get_collection("ratelimit")
        user = await users_col.find_one({"_id": user_id})
        
        if not user:
            await users_col.insert_one({
                "_id": user_id,
                "count": 1,
                "last_update": datetime.now()
            })
            return True
            
        if (datetime.now() - user["last_update"]) > timedelta(seconds=self.window):
            await users_col.update_one(
                {"_id": user_id},
                {"$set": {"count": 1, "last_update": datetime.now()}}
            )
            return True
            
        if user["count"] >= self.limit:
            return False
            
        await users_col.update_one(
            {"_id": user_id},
            {"$inc": {"count": 1}}
        )
        return True
