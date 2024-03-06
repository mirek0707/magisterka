import os
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])

db = client.college

book_collection = db.get_collection("books")
user_collection = db.get_collection("users")
