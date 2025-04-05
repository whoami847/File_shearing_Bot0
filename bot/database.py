from motor.motor_asyncio import AsyncIOMotorClient
from config import config

class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(config.DATABASE_URL)
        self.db = self.client[config.DATABASE_NAME]
    
    async def get_collection(self, name: str):
        return self.db[name]

db = Database()
