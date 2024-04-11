from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_animal,
    delete_animal,
    retrieve_animal,
    retrieve_animals,
    update_animal
)

from server.models.cattle import (
    ErrorResponseModel,
    ResponseModel,
    CattleSchema,
    UpdateCattleModel
)

router = APIRouter()

@router.post("/", response_description="Animal data added to database")
async def add_animal_data(animal: CattleSchema = Body(...)):
    animal = jsonable_encoder(animal)
    new_animal = await add_animal(animal)
    return ResponseModel(new_animal, "Animal added successfully.")

@router.get("/", response_description="All cattle data retrieved")
async def get_cattle():
    cattle = await retrieve_animals()
    if cattle:
        return ResponseModel(cattle, "Cattle data successfully retrieved")
    return ResponseModel(cattle, "Empty list returned")

@router.get("/{id}", response_description="Single animal data retrieved")
async def get_animal_data(id):
    animal = await retrieve_animal(id)
    if animal:
        return ResponseModel(animal, "Animal data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Animal doesn't exist")

@router.put("/{id}")
async def update_animal_data(id: str, req: UpdateCattleModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_animal = await update_animal(id, req)
    if update_animal:
        return ResponseModel(
            "Animal with ID: {} update is successful".format(id),
            "Animal updated successfully"
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )
@router.delete("/{id}", response_description="Animal data deleted from the database")
async def delete_animal_data(id: str):
    deleted_animal = await delete_animal(id)
    if deleted_animal:
        return ResponseModel("Animal with id: {} removed.".format(id),
                             "Animal deleted successfully")
    return ErrorResponseModel(
        "An error occurred", 404, "Animal with id {} doesn't exist".format(id)
    )