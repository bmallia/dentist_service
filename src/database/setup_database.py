
from src.config import get_settings

import psycopg2
import psycopg2.extras

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from playhouse.postgres_ext import *

from src.exceptions import DatabaseError

from src.database.models import Company
config = get_settings()


class Database:

    @staticmethod
    def setup():
        try:
            inst = Database()
            inst.setup_db()
        except Exception as e:
            raise DatabaseError(data={'message': e})

    def setup_db(self):
        con = psycopg2.connect(
            f'user={config.DB_USERNAME} host={config.DB_HOST} port={config.DB_PORT} password={config.DB_PASSWORD} dbname={config.DB_NAME}')
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = con.cursor()
        self.create_db()
        self.create_tables()

    def create_db(self):
        self.cursor.execute(
            "SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (config.DB_NAME,))
        exists = self.cursor.fetchone()

        if not exists:
            self.cursor.execute(f'CREATE DATABASE {config.DB_NAME}')

    @staticmethod
    def create_tables():
        ext_db = PostgresqlExtDatabase(
            config.DB_NAME,
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USERNAME,
            password=config.DB_PASSWORD
        )
        ext_db.create_tables([Company])
