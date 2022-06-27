from webbrowser import get
from peewee import Model, CharField, IntegerField, BigAutoField, FixedCharField
from playhouse.postgres_ext import PostgresqlExtDatabase

##from src.database.db_connection import ext_db
from src.config import get_settings

config = get_settings()

ext_db = PostgresqlExtDatabase(
    config.DB_NAME,
    host=config.DB_HOST,
    port=config.DB_PORT,
    user=config.DB_USERNAME,
    password=config.DB_PASSWORD
)


class Base(Model):
    class Meta:
        database = ext_db


class Company(Base):
    id: BigAutoField
    name: CharField
    description: CharField
    address: CharField
    rating: IntegerField
    phonenumber: FixedCharField(max_length=11)
