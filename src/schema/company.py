from pydantic import BaseModel


class Company(BaseModel):
    name: str
    about: str
    resume: str
    phonenumber: int
    address_id: int
