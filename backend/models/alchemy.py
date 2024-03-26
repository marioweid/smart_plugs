
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Device(Base):
    __tablename__ = "devices"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    device_id = Column(String, index=True, nullable=False)
    local_key = Column(String, nullable=False)
    ip4_address = Column(String, index=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
