from src.config import get_settings

import psycopg2
import psycopg2.extras

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from playhouse.postgres_ext import *
from src.database.models import Company
from src.exceptions import DatabaseError


config = get_settings()


CON_PARAMS = {
    'user': config.DB_USERNAME,
    'password': config.DB_PASSWORD,
    'host': config.DB_HOST,
    'port': config.DB_PORT,
    'dbname': config.DEFAULT_DBNAME,
}


def setup():
    """Setup database where create the database if there is none and the tables needed

    Raises:
        SaatiDatabaseError: handle database errors with the correct response format
    """
    conection = None

    try:
        connection = psycopg2.connect(**CON_PARAMS)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        create_db(cursor, config.DB_NAME)
        create_tables()
    except psycopg2.DatabaseError as e:
        raise DatabaseError(data={'message': e})
    finally:
        connection.close()


def create_db(cursor, dbname: str):
    """ create a new database with the current connection

    Args:
        cursor (_type_): the given cursor_
        dbname (str): the name of the given database
    """
    cursor.execute(
        "SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (dbname,))
    exists = cursor.fetchone()

    if not exists:
        print('não existe database...   ')
        cursor.execute(f'CREATE DATABASE {dbname}')


def create_tables():  # pragma: no cover
    """Create the necessary tables to the application"""
    ext_db = PostgresqlExtDatabase(
        config.DB_NAME,
        host=config.DB_HOST,
        port=config.DB_PORT,
        user=config.DB_USERNAME,
        password=config.DB_PASSWORD
    )

    ext_db.create_tables([Company])
    Company()
