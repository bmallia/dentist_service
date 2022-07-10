
import logging
from fastapi import Depends, APIRouter
from src.database.models import Company as cp, Address
from src.schema.company import Company

router = APIRouter()


logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


@router.post('/register')
async def register(company: Company):
    c = cp.create(name=company.name, city=company.city,
                  phonenumber=company.phonenumber)
    return {"response": f"company {c.id} created!"}
