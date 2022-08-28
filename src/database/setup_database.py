""" Module that load database and tables necessary to run this project

    Raises:
        DatabaseError: Error related with the project database_

"""

from sqlalchemy_utils.functions import database_exists, create_database
from src.config import get_settings

from src.database import models
from src.exceptions import DatabaseError
from src.database.database import engine


config = get_settings()


def setup():
    try:
        create_db()
    except Exception as e:
        raise DatabaseError(e)


def create_db():
    """ create a new database with the current connection

    Args:
        cursor (_type_): the given cursor_
        dbname (str): the name of the given database
    """

    if not database_exists(config.DATABASE_URL):
        create_database(engine.url)

    create_tables()


def create_tables():
    models.Base.metadata.create_all(bind=engine)
