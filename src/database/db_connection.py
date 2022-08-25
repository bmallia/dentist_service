
from functools import wraps

from playhouse.pool import PooledPostgresqlExtDatabase
from playhouse.shortcuts import ReconnectMixin

from src.config import get_settings

config = get_settings()


class RetryDatabase(ReconnectMixin, PooledPostgresqlExtDatabase):
    """Class responsible for connecting to the database"""
    _instance = None

    @staticmethod
    def get_db_instance():
        """
            Function that get conections from .env params to conect to database
        """
        if not RetryDatabase._instance:
            RetryDatabase._instance = RetryDatabase(
                config.DB_NAME,
                host=config.DB_HOST,
                user=config.DB_USERNAME,
                password=config.DB_PASSWORD,
                port=config.DB_PORT,
                max_connections=100,
                stale_timeout=300
            )

        return RetryDatabase._instance


##ext_db = RetryDatabase.get_db_instance()


def check_connection(func):
    """
        Decorator that create conection with the database if it is closed
    """
    @wraps(func)
    def wrapper(*args):
        if ext_db.is_closed():
            ext_db.connect()
        return func(*args)
    return wrapper
