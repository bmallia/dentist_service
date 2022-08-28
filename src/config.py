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

    DEFAULT_DBNAME: str = config('DEFAULT_DBNAME')

    DATABASE_URL: str = config('DATABASE_URL')


@lru_cache()
def get_settings() -> BaseSettings:
    logger.info("Loading environment variables...")
    return Settings()
