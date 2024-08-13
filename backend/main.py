import logging
import uuid

import uvicorn
from database import get_db, init_db
from fastapi import Depends, FastAPI
from models.alchemy import Device, DeviceEvent, DeviceEventType
from models.responses import DeviceResponse
from SmartDevice import SmartDevice
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from datetime import datetime
import zoneinfo

# Start App, Init db
try:
    init_db(file_path="config.json")
except IntegrityError:
    logging.info("Devies from config file allready present in database")
app = FastAPI()


@app.get("/devices/", response_model=list[DeviceResponse], tags=["Devices"])
def get_devices(db: Session = Depends(get_db)):
    devices = [
        SmartDevice(
            device_id=device.device_id,
            local_key=device.local_key,
            ip4_address=device.ip4_address,
            id=device.id,
            name=device.name,
        )
        for device in db.query(Device).all()
    ]

    device_responses: list[DeviceResponse] = []
    for device in devices:
        latest_event: DeviceEvent = (
            db.query(DeviceEvent)
            .filter_by(device_id=device.id)
            .order_by(DeviceEvent.timestamp.desc())
            .first()
        )
        device_entry = DeviceResponse(
            id=device.id,
            name=device.name,
            is_on=device.status().is_on,
            latest_event_time=str(latest_event.timestamp) if latest_event else ""
        )
        device_responses.append(device_entry)
    return device_responses


@app.get("/devices/{id}", response_model=DeviceResponse, tags=["Devices"])
def get_device(id: uuid.UUID, db: Session = Depends(get_db)):
    db_device = db.query(Device).filter(Device.id == str(id)).first()
    device = SmartDevice(
        device_id=db_device.device_id,
        local_key=db_device.local_key,
        ip4_address=db_device.ip4_address,
        id=db_device.id,
        name=db_device.name,
    )
    latest_event: DeviceEvent = (
        db.query(DeviceEvent)
        .filter_by(device_id=device.id)
        .order_by(DeviceEvent.timestamp.desc())
        .first()
    )

    device_states = {
        "id": device.id,
        "name": device.name,
        "is_on": device.is_on(),
        "latest_event_time": str(latest_event.timestamp),
    }
    return device_states


@app.get("/devices/{id}/toggle", response_model=DeviceResponse, tags=["Devices"])
def toggle_device(id: str, db: Session = Depends(get_db)):
    db_device = db.query(Device).filter(Device.id == str(id)).first()
    device = SmartDevice(
        device_id=db_device.device_id,
        local_key=db_device.local_key,
        ip4_address=db_device.ip4_address,
        id=db_device.id,
        name=db_device.name,
    )
    is_on = device.toggle_power()

    device_event = DeviceEvent(
        device_id=db_device.id,
        event_type=DeviceEventType.ON if is_on else DeviceEventType.OFF,
        timestamp=datetime.now(tz=zoneinfo.ZoneInfo(key="Europe/Berlin")),
    )
    db.add(device_event)
    db.commit()
    ret: DeviceResponse = DeviceResponse(
        id=device.id, name=device.name, is_on=is_on, latest_event_time=str(device_event.timestamp)
    )
    return ret


if __name__ == "__main__":
    uvicorn.run(app, port=5000, host="0.0.0.0")
