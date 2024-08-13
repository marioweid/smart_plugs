import enum
import uuid

from sqlalchemy import Column, String, ForeignKey, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import zoneinfo

Base = declarative_base()


class Device(Base):
    __tablename__ = "devices"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    device_id = Column(String, index=True, nullable=False)
    local_key = Column(String, nullable=False)
    ip4_address = Column(String, index=True, unique=True, nullable=False)
    name = Column(String, nullable=False)


# Enum for device event types
class DeviceEventType(enum.Enum):
    ON = "on"
    OFF = "off"


class DeviceEvent(Base):
    __tablename__ = "device_events"
    
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    device_id = Column(String, ForeignKey('devices.id'), nullable=False)
    event_type = Column(Enum(DeviceEventType), nullable=False)
    timestamp = Column(DateTime, default=datetime.now(tz=zoneinfo.ZoneInfo(key="Europe/Berlin")), nullable=False)

