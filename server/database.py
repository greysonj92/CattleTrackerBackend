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
async def retrieve_animals():
    cattle = []
    async for animal in cattle_collection.find():
        cattle.append(cattle_helper(animal))
    return cattle

# Add a new animal
async def add_animal(animal_data: dict) -> dict:
    animal = await cattle_collection.insert_one(animal_data)
    new_animal = await cattle_collection.find_one({"_id": animal.inserted_id})
    return cattle_helper(new_animal)

# Retrieve an animal with a matching ID
async def retrieve_animal(id: str) -> dict:
    animal = await cattle_collection.find_one({"_id": ObjectId(id)})
    if animal:
        return cattle_helper(animal)

# Update an animal with a matching ID
async def update_animal(id: str, data: dict):
    # Return false if we got an empty request body
    if len(data) < 1:
        return False
    animal = await cattle_collection.find_one({"_id": ObjectId(id)})
    if animal:
        updated_animal = await cattle_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_animal:
            return True
        return False
# Delete an animal from the database
async def delete_animal(id: str):
    animal = await cattle_collection.find_one({"_id": ObjectId(id)})
    if animal:
        await cattle_collection.delete_one({"_id": ObjectId(id)})
        return True