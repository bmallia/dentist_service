
from peewee import Model,  IntegerField
from src.database.db_connection import ext_db
from src.config import get_settings
from playhouse.postgres_ext import *
from datetime import datetime

config = get_settings()


class Address(Model):
    id = PrimaryKeyField()
    cep = IntegerField()
    place = TextField()
    number: TextField()
    city = TextField()
    coutry = TextField()

    class Meta:
        database = ext_db
        db_table = 'Address'


class Company(Model):
    id = PrimaryKeyField()
    name = TextField()
    about = TextField()
    resume = TextField()
    phonenumber = TextField()
    createdatetime: DateTimeField(default=datetime.now())
    updatedatetime: DateTimeField()
    adress: ForeignKeyField(Address)

    class Meta:
        database = ext_db
        db_table = 'Company'
