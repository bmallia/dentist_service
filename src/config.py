import logging
import logging.config
import os

from pydantic import BaseSettings
from decouple import config
from functools import lru_cache

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    # BASE CONFIG
    BASE_DIR: str = os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))
    ENVIRONMENT: str = config('ENVIRONMENT', 'PRD')
    API_KEY: str = config('API_KEY', '')

    # DB CONFIG
    DB_HOST: str = config('DATABASE_HOST')
    DB_PORT: str = config('DATABASE_PORT')
    DB_PASSWORD: str = config('DATABASE_PASSWORD')
    DB_NAME: str = config('DATABASE_NAME')
    DB_USERNAME: str = config('DATABASE_USERNAME')

    # AWS CONFIG
    AWS_ACCESS_KEY: str = config('AWS_ACCESS_KEY')
    AWS_ACCESS_SECRET: str = config('AWS_ACCESS_SECRET')
    AWS_REGION: str = config('AWS_REGION')

    AWS_ACCESS_KEY: str = config('AWS_ACCESS_KEY')
    AWS_ACCESS_SECRET: str = config('AWS_ACCESS_SECRET')
    AWS_REGION: str = config('AWS_REGION')


@lru_cache()
def get_settings() -> BaseSettings:
    logger.info("Loading environment variables...")
    return Settings()
