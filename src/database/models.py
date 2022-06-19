from peewee import Model, TextField, IntegerField, BigAutoField, FixedCharField

from src.database.db_connection import ext_db


class Base(Model):
    class Meta:
        database = ext_db


class Company(Base):
    id: BigAutoField
    name: TextField
    description: TextField
    address: TextField
    rating: IntegerField
    phonenumber: FixedCharField(max_length=11)
