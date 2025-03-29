
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from urllib.parse import quote_plus
import os

app = FastAPI()

username = "prabhudhanabal"
password = "Omsivam@007"

escaped_username = quote_plus(username)
escaped_password = quote_plus(password)

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://" + escaped_username + ":" + escaped_password + "@healthcarecluster.qlmp9t1.mongodb.net/?retryWrites=true&w=majority&appName=HealthCareCluster")
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
