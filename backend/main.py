from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from backend.models.alchemy import Base, Device
from sqlalchemy.engine.base import Engine
import os
import json

conn_url = os.environ.get("SQLALCHEMY_DATABASE_URL", "sqlite:///test.sqlite")

engine = create_engine(conn_url)
Base.metadata.create_all(bind=engine)

def read_config_file(file_path: str) -> list[Device]:
    with open(file_path, 'r') as file:
        devices_json = json.load(file)
        
    devices = [Device(**item) for item in devices_json]
    return devices
    

def init_db(engine: Engine, file_path: str):
    print(f"Initializing db from file {file_path}")
    devices = read_config_file(file_path=file_path)
    # new_device = Device(device_id="some_device_id", local_key="some_local_key", ip4_address="some_ip4_address", name="some_name")
            
    with Session(bind=engine, autocommit=False, autoflush=False) as session:
        session.add_all(devices)
        session.commit()
    
init_db(engine=engine, file_path="config.json")