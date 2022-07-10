
from pydantic import BaseModel


class Address(BaseModel):
    id = int
    cep = int
    place = str
    number: int
    city = str
    country = str
