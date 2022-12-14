from motor.motor_asyncio import AsyncIOMotorClient
import os

session = AsyncIOMotorClient(os.getenv("MONGO"))
economy = session.economy
users = economy.users
