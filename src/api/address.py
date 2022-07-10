from fastapi import APIRouter
import logging

from src.schema.address import Address
router = APIRouter()


logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


@router.post('/register')
async def register(address: Address):
    return {"response": f"testeee"}
