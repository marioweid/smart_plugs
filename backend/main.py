from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.alchemy import Base, Device
from fastapi import FastAPI, Depends
from SmartDevice import SmartDevice

from database import get_db, init_db
import uvicorn

# Start App, Init db
try:
    init_db(file_path="config.json")
except IntegrityError as e:
    print(f"Devies from config file allready present in database")
app = FastAPI()

@app.get("/devices/")
def get_devices(db: Session = Depends(get_db)):
    devices = [SmartDevice(
                device_id=device.device_id,
                local_key=device.local_key,
                ip4_address=device.ip4_address,
                db_id=device.id,
                name=device.name
            ) for device in db.query(Device).all()]
    
    # Try getting the deive states
    device_states = [{"id": device.db_id, "name": device.name, "is_on": device.is_on()} for device in devices]
    
    return device_states


if __name__ == "__main__":
    uvicorn.run(app, port=5000, host="0.0.0.0")
