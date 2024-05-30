import json
import logging
import os
from contextlib import contextmanager

from models.alchemy import Base, Device
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create Alchemy Engine
conn_url = os.environ.get("SQLALCHEMY_DATABASE_URL", "sqlite:///devices.sqlite")
engine = create_engine(conn_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Session Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

def read_config_file(file_path: str) -> list[Device]:
    with open(file_path, "r") as file:
        devices_json = json.load(file)

    devices = [Device(**item) for item in devices_json]
    return devices

def init_db(file_path: str):
    # Drop all tables
    Base.metadata.drop_all(bind=engine)
    
    # Recreate all tables
    Base.metadata.create_all(bind=engine)
    
    # Read devices from config file
    logging.info(f"Initializing db from file {file_path}")
    devices = read_config_file(file_path=file_path)


    
    # Write SqLite
    db_context = contextmanager(get_db)
    with db_context() as session:
        session.add_all(devices)
        session.commit()

