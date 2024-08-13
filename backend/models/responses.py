from pydantic import BaseModel, Field
import uuid
import datetime

class DeviceResponse(BaseModel):
    id: uuid.UUID = Field(..., title="Database ID", description="The unique identifier of the device in the database")
    name: str = Field(..., title="Device Name", description="The name of the device")
    is_on: int = Field(..., title="Device State", description="The current state of the device (on[1]/off[0]/unknown[2])")
    latest_event_time: str = Field(..., title="Latest event timestamp", description="The timestamp from the latest event")
    model_config = {
        "json_schema_extra": {
            "example": {
                "db_id": "7e5521fc-df5c-42d4-82e0-1e8fecf2485e",
                "name": "Smart Plug",
                "is_on": 1
            }
        }
    }