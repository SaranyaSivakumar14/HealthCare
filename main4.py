
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from urllib.parse import quote_plus
from bson import ObjectId
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
#  Properly configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

username = "prabhudhanabal"
password = "Omsivam@007"

escaped_username = quote_plus(username)
escaped_password = quote_plus(password)

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://" + escaped_username + ":" + escaped_password + "@healthcarecluster.qlmp9t1.mongodb.net/?retryWrites=true&w=majority&appName=HealthCareCluster")
print(MONGO_URI) 
client = MongoClient(MONGO_URI,  tls=True, tlsAllowInvalidCertificates=True)
db = client.Hospital  # Database name
collection = db.Doctors  # Collection name
print(db.list_collection_names())

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

@app.post("/doctors/")
async def create_item(item: Item):
    item_dict = item.dict()
    result = collection.insert_one(item_dict)
    return {"id": str(result.inserted_id), "message": "Item created successfully"}

#if __name__ == "__main__":
   # import uvicorn
   # uvicorn.run(app, host="0.0.0.0", port=8000)