import os
import motor.motor_asyncio
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])

db = client.db

books_collection = db.get_collection("books")
users_collection = db.get_collection("users")
shelves_collection = db.get_collection("shelves")
