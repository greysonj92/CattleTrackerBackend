from bson.objectid import ObjectId
import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27018"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.cattle
cattle_collection = database.get_collection("cattle_collection")

# Helpers
def cattle_helper(cattle) -> dict:
    return {
        "id": str(cattle["_id"]),
        "tag_number": cattle["tag_number"],
        "sheep_type": cattle["sheep_type"],
        "active_status": cattle["active_status"],
        "pregnant": cattle["pregnant"],
        "due_date": cattle["due_date"],
        "lactating": cattle["lactating"],
    }

# CRUD Operations
# Retrieve all cattle in database
async def retrieve_cattle():
    cattle = []
    async for animal in cattle_collection.find():
        cattle.append(cattle_helper(animal))
    return cattle