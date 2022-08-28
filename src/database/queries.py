
from sqlalchemy.future import select
from sqlalchemy import update
from src.database.database import session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException


def create_company(company):

    with session() as session_db:
        try:
            session_db.add(company)
            session_db.commit()
            session_db.refresh(company)
            return company
        except SQLAlchemyError as e:
            session_db.rollback()
            raise e
        except HTTPException as http_ex:
            session_db.rollback()
            raise http_ex
        finally:
            session_db.close()
