from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings
from typing import Optional, List, Any
from models.events import Event
from models.users import User

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)

        await init_beanie(
            database=client.get_default_database(),
            document_models=[Event, User]
        )

    class Config:
        env_file = ".env"


class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document):
        await document.create()

    async def get(self, id):
        return await self.model.get(id)

    async def get_all(self):
        return await self.model.find_all().to_list()

    async def update(self, id, body):
        doc = await self.get(id)
        if not doc:
            return False

        update_data = {k: v for k, v in body.dict().items() if v is not None}

        await doc.update({"$set": update_data})
        return doc

    async def delete(self, id):
        doc = await self.get(id)
        if not doc:
            return False

        await doc.delete()
        return True