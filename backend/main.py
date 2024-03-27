import uuid
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.alchemy import Device
from fastapi import FastAPI, Depends
from SmartDevice import SmartDevice

from models.responses import DeviceResponse
from database import get_db, init_db
import uvicorn
import os

# Start App, Init db
try:
    init_db(file_path="config.json")
except IntegrityError as e:
    print(f"Devies from config file allready present in database")
app = FastAPI()

@app.get("/devices/", response_model=list[DeviceResponse], tags=["Devices"])
def get_devices(db: Session = Depends(get_db)):
    devices = [SmartDevice(
                device_id=device.device_id,
                local_key=device.local_key,
                ip4_address=device.ip4_address,
                id=device.id,
                name=device.name
            ) for device in db.query(Device).all()]
    
    device_states = [{"id": device.id, "name": device.name, "is_on": device.is_on()} for device in devices]    
    return device_states

@app.get("/devices/{id}", response_model=DeviceResponse, tags=["Devices"])
def get_devices(id: uuid.UUID, db: Session = Depends(get_db)):
    db_device = db.query(Device).filter(Device.id == str(id)).first()
    device = SmartDevice(
                device_id=db_device.device_id,
                local_key=db_device.local_key,
                ip4_address=db_device.ip4_address,
                id=db_device.id,
                name=db_device.name)
    
    device_states = {"id": device.id, "name": device.name, "is_on": device.is_on()}    
    return device_states

@app.get("/devices/{id}/toggle", response_model=DeviceResponse, tags=["Devices"])
def toggle_device(id: str, db: Session = Depends(get_db)):
    db_device = db.query(Device).filter(Device.id == str(id)).first()
    device = SmartDevice(
                device_id=db_device.device_id,
                local_key=db_device.local_key,
                ip4_address=db_device.ip4_address,
                id=db_device.id,
                name=db_device.name)
    is_on = device.toggle_power()
    ret = {"id": device.id, "name": device.name, "is_on": is_on}
    return ret 

if __name__ == "__main__":
    uvicorn.run(app, port=5000, host="0.0.0.0")
