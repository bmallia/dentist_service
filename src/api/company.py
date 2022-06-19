
from fastapi import Depends, APIRouter
import logging

router = APIRouter()


logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


@router.post('/register')
async def register():
    return {"Hello": "World"}
