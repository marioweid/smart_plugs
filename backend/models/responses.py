from pydantic import BaseModel, Field

class DevicesResponse(BaseModel):
    db_id: int = Field(..., title="Database ID", description="The unique identifier of the device in the database")
    name: str = Field(..., title="Device Name", description="The name of the device")
    is_on: bool = Field(..., title="Device State", description="The current state of the device (on/off)")

    class Config:
        schema_extra = {
            "example": {
                "db_id": "7e5521fc-df5c-42d4-82e0-1e8fecf2485e",
                "name": "Smart Plug",
                "is_on": True
            }
        }