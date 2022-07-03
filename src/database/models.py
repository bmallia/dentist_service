from webbrowser import get
from peewee import Model, CharField, IntegerField, BigAutoField, FixedCharField
from playhouse.postgres_ext import PostgresqlExtDatabase

from src.database.db_connection import ext_db
from src.config import get_settings
from playhouse.postgres_ext import *

config = get_settings()


class Address(Model):
    id = PrimaryKeyField()
    cep = IntegerField()
    place = TextField()
    number: TextField()

    class Meta:
        database = ext_db
        db_table = 'Address'


class Company(Model):
    id = PrimaryKeyField()
    name = TextField()
    city = TextField(constraints=[SQL("DEFAULT 'Brasil'")])
    phonenumber = TextField()
    createdatetime: DateTimeField()
    updatedatetime: DateTimeField()
    adress: ForeignKeyField(Address)

    class Meta:
        database = ext_db
        db_table = 'Company'
