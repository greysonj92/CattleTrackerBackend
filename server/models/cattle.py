from datetime import date
from typing import Optional, Literal
from pydantic import BaseModel, EmailStr, Field

# Base class for the model
class CattleSchema(BaseModel):
    tag_number: int = Field(...)
    sheep_type: Literal["Ewe", "Ram", "Lamb"]
    active_status: Literal["Active", "Dead"]
    pregnant: Literal["Yes", "No"]
    due_date: date
    lactating: Literal["Yes", "No"]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "tag_number": 1234,
                "sheep_type": "Ewe",
                "active_status": "Active",
                "pregnant": "No",
                "lactating": "No",
            }
        }


# Class to update model -- hence all fields are optional
class UpdateCattleModel(BaseModel):
    tag_number: Optional[int]
    sheep_type: Optional[Literal["Ewe", "Ram", "Lamb"]]
    active_status: Optional[Literal["Active", "Dead"]]
    pregnant: Optional[Literal["Yes", "No"]]
    due_date: Optional[date]
    lactating: Optional[Literal["Yes", "No"]]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "tag_number": 1234,
                "sheep_type": "Ewe",
                "active_status": "Active",
                "pregnant": "No",
                "lactating": "No",
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error":error, "code":code, "message":message}
