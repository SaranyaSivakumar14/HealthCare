
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
import os

app = FastAPI()

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client.Hospital  # Database name
collection = db.Doctors  # Collection name

# Pydantic model for request validation
class Item(BaseModel):
    id: int
    name: str
    specialty: str

@app.get("/doctors")
async def get_doctors():
    items = []
    for item in collection.find():       
        del item["_id"]
        items.append(item)
    return items
