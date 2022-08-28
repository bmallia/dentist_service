from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from src.config import get_settings

config = get_settings()

engine = create_engine(config.DATABASE_URL,
                       pool_size=100, max_overflow=100)

session = sessionmaker(
    engine, expire_on_commit=False)

Base = declarative_base()
