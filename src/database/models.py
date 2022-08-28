from src.config import get_settings
from src.database.database import Base

from sqlalchemy import Column, PrimaryKeyConstraint, String, BigInteger, Integer, DateTime
from sqlalchemy.sql import func


config = get_settings()


class Address(Base):
    __tablename__ = 'address'

    id = Column(BigInteger, primary_key=True)
    cep = Column(Integer)
    place = Column(String)
    number: Column(Integer)
    city = Column(String, nullable=True)
    country = Column(String)


class Company(Base):
    __tablename__ = 'company'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    about = Column(String)
    resume = Column(String)
    phonenumber = Column(String)
    createdatetime: Column(DateTime(timezone=True), server_default=func.now())
    updatedatetime: Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self) -> str:
        return f"id: {self.id} name: {self.name} about: {self.about} resume: {self.resume} phonenumber: {self.phonenumber}"
