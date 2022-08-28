
import logging
from fastapi import Depends, APIRouter
from src.database.models import Company
from src.schema.company import Company as cp
from src.controller.company import update_registry


router = APIRouter()


logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


@router.post('/register')
async def register(company: cp):

    company = Company(**company.__dict__)
    update_registry(company)

    return company


@router.get('/list')
async def list_register():
    return {"id": 131, "name": "company"}
