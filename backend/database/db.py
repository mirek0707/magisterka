import os
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])

db = client.db

books_collection = db.get_collection("books")
users_collection = db.get_collection("users")
